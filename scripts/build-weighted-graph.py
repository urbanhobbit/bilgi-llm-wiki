#!/usr/bin/env python3
"""
build-weighted-graph.py
-----------------------
Kavram-kavram grafiğini normalize ağırlıklarla üretir.

Ham ortak makale sayısı (raw co-occurrence) yerine:
  - PMI      : log2( N * cooc / (deg_a * deg_b) )
  - Jaccard  : cooc / (deg_a + deg_b - cooc)
  - score    : PMI * log2(1 + cooc)^0.5      <- varsayılan sıralama ölçütü

Amaç: "Siyaset Bilimi Metodolojisi" gibi her şeye bağlanan genel kavramların
komşuluk listelerini doldurmasını engellemek, nadir-çift gürültüsünü (raw=1)
min_cooc eşiğiyle kesmek.

Kullanım:
    python3 scripts/build-weighted-graph.py
    python3 scripts/build-weighted-graph.py --min-cooc 5 --alpha 0.5

Çıktı: graph-weighted.json  (meta + edges[])
"""
import argparse
import collections
import datetime
import itertools
import json
import math
import os
import sys

WIKI = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def load(wiki):
    path = os.path.join(wiki, "bundle.json")
    if not os.path.exists(path):
        sys.exit(f"bundle.json bulunamadi: {path}")
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def build(d, min_cooc=5, alpha=0.5):
    edges = [e["data"] for e in d["edges"]]
    nodes = {n["data"]["id"]: n["data"] for n in d["nodes"]}

    # bipartite: article -> {concepts}
    art2con = collections.defaultdict(set)
    for e in edges:
        tgt = e.get("target", "")
        if tgt.startswith("concepts/"):
            art2con[e["source"]].add(tgt)

    cdeg = collections.Counter()
    pair = collections.Counter()
    for cs in art2con.values():
        for c in cs:
            cdeg[c] += 1
        for x, y in itertools.combinations(sorted(cs), 2):
            pair[(x, y)] += 1

    # N = kavramı olan makale sayısı
    N = sum(1 for cs in art2con.values() if cs)

    def pmi(p):
        den = cdeg[p[0]] * cdeg[p[1]]
        if not den or not pair[p]:
            return 0.0
        return math.log2((pair[p] * N) / den)

    def jaccard(p):
        den = cdeg[p[0]] + cdeg[p[1]] - pair[p]
        return pair[p] / den if den else 0.0

    out = []
    for p, raw in pair.items():
        if raw < min_cooc:
            continue
        pm = pmi(p)
        out.append({
            "source": p[0],
            "target": p[1],
            "source_label": nodes.get(p[0], {}).get("label", p[0].split("/")[-1]),
            "target_label": nodes.get(p[1], {}).get("label", p[1].split("/")[-1]),
            "cooccurrence": raw,
            "pmi": round(pm, 4),
            "jaccard": round(jaccard(p), 4),
            "score": round(pm * (math.log2(1 + raw) ** alpha), 4),
            "degree_source": cdeg[p[0]],
            "degree_target": cdeg[p[1]],
        })
    out.sort(key=lambda x: -x["score"])

    meta = {
        "generated": datetime.datetime.now().isoformat(timespec="seconds"),
        "method": "kavram-kavram kenarlari, ortak raw_article uzerinden",
        "metrics": {
            "pmi": "log2(N*cooc/(deg_a*deg_b))",
            "jaccard": "cooc/(deg_a+deg_b-cooc)",
            "score": f"pmi * log2(1+cooc)^{alpha}",
        },
        "thresholds": {"min_cooccurrence": min_cooc, "alpha": alpha},
        "stats": {
            "corpus_articles_with_concepts": N,
            "concept_nodes": len(cdeg),
            "raw_pairs": len(pair),
            "kept_pairs": len(out),
            "total_concept_edges": sum(cdeg.values()),
        },
    }
    return {"meta": meta, "edges": out}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--wiki", default=WIKI)
    ap.add_argument("--min-cooc", type=int, default=5)
    ap.add_argument("--alpha", type=float, default=0.5)
    ap.add_argument("--out", default=None)
    a = ap.parse_args()

    d = load(a.wiki)
    res = build(d, a.min_cooc, a.alpha)
    out = a.out or os.path.join(a.wiki, "graph-weighted.json")
    with open(out, "w", encoding="utf-8") as f:
        json.dump(res, f, ensure_ascii=False, indent=1)

    s = res["meta"]["stats"]
    print(f"yazildi: {out}")
    print(f"kenar: {s['kept_pairs']}/{s['raw_pairs']} (min_cooc={a.min_cooc})")
    print(f"kavram: {s['concept_nodes']} | kavramli makale: {s['corpus_articles_with_concepts']}")
    print("\nilk 10 kenar:")
    for e in res["edges"][:10]:
        print(f"  {e['score']:6.3f}  raw={e['cooccurrence']:4d}  "
              f"{e['source_label'][:38]} <-> {e['target_label'][:38]}")


if __name__ == "__main__":
    main()
