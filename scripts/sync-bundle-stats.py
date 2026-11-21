#!/usr/bin/env python3
"""
bundle*.json icindeki `stats` blogunu nodes/edges'ten yeniden hesaplar.

Neden gerekli: dugum/kenar silindiginde `stats` blogu statik kaliyor ve
viz.html / viz2.html basligi `d.stats.nodes` okudugu icin eski sayiyi
gosteriyor (orn. 2086 dugum varken "2198 dugum" yaziyordu).

Kullanim:
    python3 scripts/sync-bundle-stats.py            # tum bundle*.json
    python3 scripts/sync-bundle-stats.py bundle2.json
"""
import json
import sys
import glob
import os
import collections

WIKI = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def recompute(d):
    nodes = d.get("nodes", [])
    edges = d.get("edges", [])
    byid = {n["data"]["id"]: n["data"] for n in nodes}

    types = collections.Counter(n["data"].get("type") for n in nodes)
    edge_kinds = collections.Counter(
        e["data"].get("kind") or e["data"].get("edgeKind") or "?"
        for e in edges
    )

    deg = collections.Counter()
    linked_concept = set()
    for e in edges:
        s, t = e["data"]["source"], e["data"]["target"]
        deg[s] += 1
        deg[t] += 1
        st, tt = byid.get(s, {}).get("type"), byid.get(t, {}).get("type")
        if st == "concept" and tt == "raw_article":
            linked_concept.add(t)
        if tt == "concept" and st == "raw_article":
            linked_concept.add(s)

    isolated = sum(1 for n in nodes if deg[n["data"]["id"]] == 0)

    label_counts = collections.Counter(
        str(n["data"].get("label", "")).strip().lower() for n in nodes
    )
    dupe_titles = sum(1 for c in label_counts.values() if c > 1)
    dupe_nodes = sum(c for c in label_counts.values() if c > 1)

    articles = [i for i, v in byid.items() if v.get("type") == "raw_article"]
    no_concept = len([a for a in articles if a not in linked_concept])

    hubs = [
        {"label": byid[i]["label"], "degree": c}
        for i, c in deg.most_common(8)
        if i in byid and byid[i].get("label")
    ][:5]

    stats = d.setdefault("stats", {})
    stats["nodes"] = len(nodes)
    stats["edges"] = len(edges)
    stats["types"] = dict(types)
    stats["edge_kinds"] = dict(edge_kinds)
    stats["isolated"] = isolated
    stats["dupe_titles"] = dupe_titles
    stats["dupe_nodes"] = dupe_nodes
    stats["no_concept"] = no_concept
    stats["hubs"] = hubs
    return stats


def check_ghosts(d):
    """okf-bundle/ onekli ve edgesiz hayalet dugumleri raporlar."""
    ghost = [n for n in d.get("nodes", []) if str(n["data"].get("id", "")).startswith("okf-bundle/")]
    kaynak = [n for n in d.get("nodes", []) if str(n["data"].get("label", "")).startswith("Kaynak:")]
    return ghost, kaynak


def main():
    targets = sys.argv[1:] or [
        os.path.basename(p) for p in glob.glob(os.path.join(WIKI, "bundle*.json"))
        if not p.endswith((".bak", ".pre-clean")) and "bak-" not in p
    ]
    for name in targets:
        p = name if os.path.isabs(name) else os.path.join(WIKI, name)
        if not os.path.isfile(p):
            print(f"  ! yok: {p}")
            continue
        d = json.load(open(p, encoding="utf-8"))
        old = (d.get("stats") or {}).get("nodes")
        st = recompute(d)
        ghost, kaynak = check_ghosts(d)
        json.dump(d, open(p, "w", encoding="utf-8"), ensure_ascii=False)
        print(f"{name}: stats.nodes {old} -> {st['nodes']} | edges {st['edges']}")
        print(f"  tipler: {st['types']}")
        print(f"  izole {st['isolated']} | kavramsiz makale {st['no_concept']}/{st['types'].get('raw_article', 0)}")
        if ghost or kaynak:
            print(f"  UYARI: {len(ghost)} okf-bundle hayalet dugum, {len(kaynak)} 'Kaynak:' etiketli dugum!")
        else:
            print("  temiz: hayalet dugum yok, 'Kaynak:' oneki yok")


if __name__ == "__main__":
    main()
