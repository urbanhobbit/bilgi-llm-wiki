#!/usr/bin/env python3
"""
wiki_server.py — bilgi-llm-wiki icin MCP sunucusu (FastMCP, stdio).

Araclar:
  search(query, limit)          — kavram/varlik/makale ara
  get_concept(slug)             — kavram sayfasi + agirlikli komsulari
  recent(days, tag)             — son N gunde eklenen makaleler
  graph_neighbors(slug, k)      — normalize agirlikli komsuluk listesi
  data_health()                 — veri sagligi paneli
  list_concepts(min_articles)   — kavram envanteri
  bridges(gap_only)             — kumeler arasi kopru / bosluk raporu

Calistirma:
    python3 mcp/wiki_server.py            # stdio

Claude Desktop / MCP istemci yapilandirmasi:
    "bilgi-wiki": {
      "command": "/usr/bin/python3",
      "args": ["/home/E/bilgi-llm-wiki/mcp/wiki_server.py"]
    }

Kurulum:  pip install 'mcp==1.9.4' 'pydantic==2.9.2' --break-system-packages
"""
import collections
import datetime
import json
import os
import re
import sys

from mcp.server.fastmcp import FastMCP

WIKI = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# --- TEK KAYNAK: agirliklandirma hesabi scripts/graph_weights.py icinde -------
sys.path.insert(0, os.path.join(WIKI, "scripts"))
from graph_weights import ConceptGraph  # noqa: E402

mcp = FastMCP("bilgi-llm-wiki")

_cache = {}


def _bundle():
    if "b" not in _cache:
        with open(os.path.join(WIKI, "bundle.json"), encoding="utf-8") as f:
            _cache["b"] = json.load(f)
    return _cache["b"]


def _weighted():
    if "w" not in _cache:
        p = os.path.join(WIKI, "graph-weighted.json")
        _cache["w"] = json.load(open(p, encoding="utf-8")) if os.path.exists(p) else {"edges": [], "meta": {}}
    return _cache["w"]


def _graph() -> ConceptGraph:
    """PMI+Jaccard hesabi icin tek kaynak (scripts/graph_weights.py).

    graph-weighted.json eski hesapla uretilmis olsa bile skorlar ayni cikar;
    modul dogrudan bundle'dan hesaplar, dosya bayatligindan etkilenmez.
    """
    if "g" not in _cache:
        _cache["g"] = ConceptGraph(_bundle())
    return _cache["g"]


def _nodes():
    if "n" not in _cache:
        _cache["n"] = {n["data"]["id"]: n["data"] for n in _bundle()["nodes"]}
    return _cache["n"]


def _art2con():
    if "a" not in _cache:
        m = collections.defaultdict(set)
        for e in _bundle()["edges"]:
            t = e["data"].get("target", "")
            if t.startswith("concepts/"):
                m[e["data"]["source"]].add(t)
        _cache["a"] = m
    return _cache["a"]


def _read_page(slug):
    slug = slug.strip("/")
    cands = []
    if slug.startswith(("concepts/", "entities/", "raw/", "queries/", "synthesis/")):
        cands.append(slug)
    else:
        cands += [f"concepts/{slug}", f"entities/{slug}", f"queries/{slug}", slug]
    for c in cands:
        p = os.path.join(WIKI, c + ".md")
        if os.path.exists(p):
            return c, open(p, encoding="utf-8").read()
    return None, None


# ------------------------------------------------------------------ tools
@mcp.tool()
def search(query: str, limit: int = 15) -> str:
    """Wiki'de kavram, varlik ve makale basliklarinda arama yapar."""
    q = query.lower()
    hits = []
    for nid, n in _nodes().items():
        label = (n.get("label") or "").lower()
        desc = (n.get("description") or "").lower()
        score = 0
        if q in label:
            score = 100 - abs(len(label) - len(q))
        elif q in desc:
            score = 30
        if score:
            hits.append((score, nid, n.get("label"), n.get("type"), (n.get("description") or "")[:220]))
    hits.sort(reverse=True)
    if not hits:
        return f"'{query}' icin sonuc bulunamadi."
    return f"{len(hits)} sonuc (ilk {min(limit,len(hits))}):\n" + "\n".join(
        f"- [{t}] {nid} — {lbl}\n  {d}" for _, nid, lbl, t, d in hits[:limit])


@mcp.tool()
def get_concept(slug: str) -> str:
    """Bir kavram sayfasinin tam metnini ve normalize agirlikli komsularini getirir."""
    sid, body = _read_page(slug)
    if not body:
        return f"Sayfa bulunamadi: {slug}\nIpucu: search() ile dogru slug'i bulun."
    key = sid if sid.startswith(("concepts/", "entities/")) else "concepts/" + sid
    rows = _graph().neighbors(key, k=15) if key.startswith("concepts/") else []
    out = [body[:6000], "", "---", "## Komsular (normalize agirlikli)"]
    for oid, lbl, sc, pm, jc, co in rows:
        out.append(f"- {lbl}  (score={sc}, PMI={pm}, ortak makale={co})")
    if not rows:
        out.append("- (agirlik esigini gecen komsu yok — izole ya da seyrek kavram)")
    return "\n".join(out)


@mcp.tool()
def recent(days: int = 21, tag: str = "") -> str:
    """Son N gunde wiki'ye eklenen makaleleri listeler (istege bagli etiket filtresi)."""
    cutoff = (datetime.date.today() - datetime.timedelta(days=days)).isoformat()
    out = []
    for nid, n in _nodes().items():
        if n.get("type") != "raw_article":
            continue
        m = re.match(r"raw/articles/(\d{4}-\d{2}-\d{2})", nid)
        if not m or m.group(1) < cutoff:
            continue
        if tag and tag.lower() not in [t.lower() for t in (n.get("tags") or [])]:
            continue
        cs = [c.split("/")[-1] for c in _art2con().get(nid, [])]
        out.append((m.group(1), n.get("label", ""), nid, cs))
    out.sort(reverse=True)
    if not out:
        return f"Son {days} gunde makale yok."
    lines = [f"Son {days} gunde {len(out)} makale:"]
    for d, lbl, nid, cs in out[:40]:
        lines.append(f"- {d} | {lbl}\n  {nid}\n  kavramlar: {', '.join(cs) if cs else '(yok)'}")
    return "\n".join(lines)


@mcp.tool()
def graph_neighbors(slug: str, k: int = 12) -> str:
    """Bir kavramin normalize agirlikli (PMI+Jaccard) en guclu komsularini dondurur."""
    key = slug if slug.startswith("concepts/") else "concepts/" + slug
    rows = _graph().neighbors(key, k=k)
    if not rows:
        return f"{slug} icin agirlikli komsu yok (min_cooc=5 esigini gecen bag yok)."
    lines = [f"{key} — en guclu {len(rows)} komsu:"]
    for oid, lbl, sc, pm, jc, co in rows:
        lines.append(f"- {lbl}  score={sc} PMI={pm} JAC={jc} ortak={co}")
    return "\n".join(lines)


@mcp.tool()
def data_health() -> str:
    """Veri sagligi paneli: kavramsiz makale, izole kavram, bundle'a girmemis dosya."""
    nodes = _nodes()
    a2c = _art2con()
    cdeg = collections.Counter()
    for cs in a2c.values():
        for c in cs:
            cdeg[c] += 1
    raw = [n for n in nodes.values() if n.get("type") == "raw_article"]
    con = [n for n in nodes.values() if n.get("type") == "concept"]
    no_c = [n for n in raw if not a2c.get(n["id"])]
    iso = [n for n in con if cdeg[n["id"]] == 0]

    def norm(s):
        return s.rsplit(".md", 1)[0].strip("/")

    disk = []
    for root, _, files in os.walk(os.path.join(WIKI, "raw")):
        for f in files:
            if f.endswith(".md"):
                disk.append(os.path.relpath(os.path.join(root, f), WIKI))
    bn = {norm(n["id"]) for n in raw}
    missing = sorted(p for p in disk if norm(p) not in bn)
    st = _weighted().get("meta", {}).get("stats", {})

    return (
        f"# Veri Sagligi\n"
        f"- dugum: {len(nodes)} | makale: {len(raw)} | kavram: {len(con)}\n"
        f"- kavramsiz makale: {len(no_c)}\n"
        f"- izole kavram: {len(iso)}\n"
        f"- bundle'a girmemis dosya: {len(missing)}\n"
        f"- agirlikli kavram kenari: {st.get('kept_pairs','?')}/{st.get('raw_pairs','?')}\n\n"
        f"Kavramsiz ilk 10:\n" + "\n".join(f"- {n['id']}" for n in no_c[:10]) +
        f"\n\nIzole kavramlar:\n" + ("\n".join(f"- {n['id']}" for n in iso) or "- yok") +
        f"\n\nEksik dosyalar (ilk 20):\n" + ("\n".join(f"- {m}" for m in missing[:20]) or "- yok")
    )


@mcp.tool()
def list_concepts(min_articles: int = 1) -> str:
    """Kavram envanterini makale sayisina gore siralar."""
    nodes = _nodes()
    cdeg = collections.Counter()
    for cs in _art2con().values():
        for c in cs:
            cdeg[c] += 1
    rows = [(cdeg[n["id"]], n["id"], n.get("label", "")) for n in nodes.values()
            if n.get("type") == "concept" and cdeg[n["id"]] >= min_articles]
    rows.sort(reverse=True)
    if not rows:
        return "Kavram yok."
    return f"{len(rows)} kavram (>= {min_articles} makale):\n" + "\n".join(
        f"- {c} makale | {nid} — {lbl}" for c, nid, lbl in rows)


@mcp.tool()
def bridges(min_score: float = 2.0) -> str:
    """Kumeler arasi kopruler ve bosluklar: guclu ama az makaleli baglar."""
    edges = [e for e in _graph().edges() if e["score"] >= min_score]
    if not edges:
        return "Esigi gecen bag yok."
    edges.sort(key=lambda e: -e["score"])
    weak = [e for e in edges if e["cooccurrence"] <= 6]
    strong = [e for e in edges if e["cooccurrence"] >= 15]
    out = ["# Kopru ve Bosluk Raporu", "", "## Zayif ama anlamli baglar (arastirma firsati)",
           "(az ortak makale, yuksek normalizasyon skoru — kesfedilmemis konular)"]
    for e in weak[:15]:
        out.append(f"- {e['source_label']} <-> {e['target_label']}  score={e['score']} ortak={e['cooccurrence']}")
    out += ["", "## Cok makaleli baglar (yerlesik kumeler)"]
    for e in strong[:10]:
        out.append(f"- {e['source_label']} <-> {e['target_label']}  score={e['score']} ortak={e['cooccurrence']}")
    return "\n".join(out)


if __name__ == "__main__":
    # ---------------------------------------------------------------- modlar
    #   (arguman yok)   -> stdio  (Claude Desktop / Hermes / yerel istemci)
    #   --http          -> streamable-http, 127.0.0.1:8765, gizli yol onekli
    #   --selftest      -> araclari dogrudan cagirip ciktisini basar
    argv = sys.argv[1:]

    if "--selftest" in argv:
        print(data_health()[:700])
        print("\n---", graph_neighbors("siyaset-bilimi-metodolojisi", 6))
        print("\n---", bridges()[:900])
        sys.exit(0)

    if "--http" in argv:
        # yol oneeki: WIKI_MCP_PATH env > varsayilan gizli onek
        path = os.environ.get("WIKI_MCP_PATH", "/mcp-w7k2q9zr4x")
        host = os.environ.get("WIKI_MCP_HOST", "127.0.0.1")
        port = int(os.environ.get("WIKI_MCP_PORT", "8765"))

        # FastMCP settings: yol oneki streamable_http_path ile verilir
        mcp.settings.host = host
        mcp.settings.port = port
        mcp.settings.streamable_http_path = path
        mcp.settings.stateless_http = True   # ters vekil arkasinda oturum sorunu cikmasin
        mcp.settings.json_response = True

        print(f"[wiki-mcp] streamable-http http://{host}:{port}{path}", flush=True)
        mcp.run(transport="streamable-http")
    else:
        mcp.run()  # stdio — varsayilan, degismedi
