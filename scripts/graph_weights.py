#!/usr/bin/env python3
"""
graph_weights.py
----------------
Kavram-kavram ağırlıklandırma — TEK KAYNAK.

Bu modül hem `build-weighted-graph.py` (graph-weighted.json üreticisi) hem de
`mcp/wiki_server.py` (MCP araçları) tarafından import edilir. Kod kopyalanmaz.

Ölçütler
--------
  PMI      : log2( N * cooc / (deg_a * deg_b) )
  Jaccard  : cooc / (deg_a + deg_b - cooc)
  score    : PMI * log2(1 + cooc) ^ alpha        (varsayılan alpha=0.5)

Neden PMI: ham ortak-makale sayısı, her şeye bağlanan genel kavramları
("Siyaset Bilimi Metodolojisi" gibi) komşuluk listelerinin başına oturtur.
PMI bu hub etkisini normalize eder; min_cooc eşiği ise raw=1 nadir-çift
gürültüsünü keser.

Kullanım
--------
    from graph_weights import concept_graph, article_concepts

    cg = concept_graph(bundle)                 # ConceptGraph
    cg.score("concepts/a", "concepts/b")       # float
    cg.neighbors("concepts/a", k=10)           # [(other_id, score, pmi, jac, cooc)]
    cg.edges(min_cooc=5, alpha=0.5)            # graph-weighted.json girdisi

CLI (kendi kendini test eder):
    python3 scripts/graph_weights.py
"""
from __future__ import annotations

import collections
import itertools
import math
import os
import sys

# ---------------------------------------------------------------- sabitler
DEFAULT_MIN_COOC = 5
DEFAULT_ALPHA = 0.5

METRIC_DOC = {
    "pmi": "log2(N*cooc/(deg_a*deg_b))",
    "jaccard": "cooc/(deg_a+deg_b-cooc)",
    "score": "pmi * log2(1+cooc)^alpha",
}


def article_concepts(bundle):
    """bundle -> {article_id: {concept_id, ...}}  (bipartite izdüşümü)"""
    art2con = collections.defaultdict(set)
    for e in bundle.get("edges", []):
        d = e.get("data", e)
        tgt = d.get("target", "")
        if isinstance(tgt, str) and tgt.startswith("concepts/"):
            art2con[d["source"]].add(tgt)
    return art2con


class ConceptGraph:
    """Kavram-kavram ortak-makale grafiği + normalize ağırlıklar.

    Hesap bir kez yapılır (init), sorgular O(1)/O(deg).
    """

    def __init__(self, bundle, min_cooc: int = DEFAULT_MIN_COOC, alpha: float = DEFAULT_ALPHA):
        self.alpha = alpha
        self.min_cooc = min_cooc
        self.nodes = {n["data"]["id"]: n["data"] for n in bundle.get("nodes", [])}
        self.art2con = article_concepts(bundle)

        self.cdeg = collections.Counter()          # kavram -> makale sayısı
        self.pair = collections.Counter()          # (a,b) -> ortak makale
        for cs in self.art2con.values():
            for c in cs:
                self.cdeg[c] += 1
            for x, y in itertools.combinations(sorted(cs), 2):
                self.pair[(x, y)] += 1

        # N = en az bir kavramı olan makale sayısı
        self.N = sum(1 for cs in self.art2con.values() if cs)

        self._idx = collections.defaultdict(list)  # kavram -> [(other, pairkey)]
        for (a, b) in self.pair:
            self._idx[a].append((b, (a, b)))
            self._idx[b].append((a, (a, b)))

    # ------------------------------------------------------------ metrikler
    def pmi(self, pairkey) -> float:
        den = self.cdeg[pairkey[0]] * self.cdeg[pairkey[1]]
        cooc = self.pair.get(pairkey, 0)
        if not den or not cooc or not self.N:
            return 0.0
        return math.log2((cooc * self.N) / den)

    def jaccard(self, pairkey) -> float:
        cooc = self.pair.get(pairkey, 0)
        den = self.cdeg[pairkey[0]] + self.cdeg[pairkey[1]] - cooc
        return cooc / den if den else 0.0

    def score(self, pairkey) -> float:
        pm = self.pmi(pairkey)
        raw = self.pair.get(pairkey, 0)
        return pm * (math.log2(1 + raw) ** self.alpha)

    def metrics(self, pairkey) -> dict:
        return {
            "cooccurrence": self.pair.get(pairkey, 0),
            "pmi": round(self.pmi(pairkey), 4),
            "jaccard": round(self.jaccard(pairkey), 4),
            "score": round(self.score(pairkey), 4),
        }

    # -------------------------------------------------------------- sorgular
    def neighbors(self, node_id: str, k: int = 12, min_cooc: int | None = None):
        """En güçlü k komşu: [(other_id, other_label, score, pmi, jac, cooc)]"""
        mc = self.min_cooc if min_cooc is None else min_cooc
        rows = []
        for other, pk in self._idx.get(node_id, []):
            cooc = self.pair[pk]
            if cooc < mc:
                continue
            m = self.metrics(pk)
            if m["score"] <= 0:
                continue
            lbl = self.nodes.get(other, {}).get("label", other.split("/")[-1])
            rows.append((other, lbl, m["score"], m["pmi"], m["jaccard"], cooc))
        rows.sort(key=lambda r: -r[2])
        return rows[:k]

    def edges(self, min_cooc: int | None = None, alpha: float | None = None):
        """graph-weighted.json `edges` listesi."""
        if alpha is not None:
            self.alpha = alpha
        mc = self.min_cooc if min_cooc is None else min_cooc
        out = []
        for p, raw in self.pair.items():
            if raw < mc:
                continue
            m = self.metrics(p)
            out.append({
                "source": p[0],
                "target": p[1],
                "source_label": self.nodes.get(p[0], {}).get("label", p[0].split("/")[-1]),
                "target_label": self.nodes.get(p[1], {}).get("label", p[1].split("/")[-1]),
                "cooccurrence": raw,
                "pmi": m["pmi"],
                "jaccard": m["jaccard"],
                "score": m["score"],
                "degree_source": self.cdeg[p[0]],
                "degree_target": self.cdeg[p[1]],
            })
        out.sort(key=lambda x: -x["score"])
        return out

    def stats(self, min_cooc: int | None = None) -> dict:
        mc = self.min_cooc if min_cooc is None else min_cooc
        kept = sum(1 for v in self.pair.values() if v >= mc)
        return {
            "corpus_articles_with_concepts": self.N,
            "concept_nodes": len(self.cdeg),
            "raw_pairs": len(self.pair),
            "kept_pairs": kept,
            "total_concept_edges": sum(self.cdeg.values()),
            "min_cooccurrence": mc,
            "alpha": self.alpha,
        }


# ------------------------------------------------------------------ yardımcı
def concept_graph(bundle, min_cooc: int = DEFAULT_MIN_COOC, alpha: float = DEFAULT_ALPHA) -> ConceptGraph:
    return ConceptGraph(bundle, min_cooc=min_cooc, alpha=alpha)


def load_bundle(wiki: str, name: str = "bundle.json") -> dict:
    import json
    path = os.path.join(wiki, name)
    if not os.path.exists(path):
        raise FileNotFoundError(f"bundle bulunamadi: {path}")
    with open(path, encoding="utf-8") as f:
        return json.load(f)


# ---------------------------------------------------------------------- test
if __name__ == "__main__":
    WIKI = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    b = load_bundle(WIKI, "bundle.json")
    cg = concept_graph(b)
    s = cg.stats()
    print("Corpus")
    print(f"  kavramli makale (N) : {s['corpus_articles_with_concepts']}")
    print(f"  kavram              : {s['concept_nodes']}")
    print(f"  ham cift            : {s['raw_pairs']}")
    print(f"  esigi gecen cift    : {s['kept_pairs']}  (min_cooc={s['min_cooccurrence']})")
    probe = "concepts/siyaset-bilimi-metodolojisi"
    if probe in cg.cdeg:
        print(f"\n{probe} komsulari (score, pmi, jac, cooc):")
        for oid, lbl, sc, pm, jc, co in cg.neighbors(probe, 8):
            print(f"  {sc:7.3f}  {pm:7.3f}  {jc:5.3f}  {co:4d}  {lbl[:50]}")
    else:
        print(f"\n(uyari: {probe} corpus'ta yok)")

    # eski graph-weighted.json ile tutarlilik kontrolu
    gw = os.path.join(WIKI, "graph-weighted.json")
    if os.path.exists(gw):
        import json
        old = json.load(open(gw, encoding="utf-8"))
        new = cg.edges()
        o = {(e["source"], e["target"]): e["score"] for e in old["edges"]}
        n = {(e["source"], e["target"]): e["score"] for e in new}
        common = set(o) & set(n)
        diff = [abs(o[k] - n[k]) for k in common]
        print(f"\ngraph-weighted.json ile karsilastirma:")
        print(f"  eski kenar {len(o)} | yeni kenar {len(n)} | ortak {len(common)}")
        print(f"  skor farki: maks {max(diff):.4f} | ort {sum(diff)/len(diff):.4f}" if diff else "  ortak kenar yok")
