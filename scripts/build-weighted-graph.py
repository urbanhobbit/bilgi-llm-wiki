#!/usr/bin/env python3
"""
build-weighted-graph.py
-----------------------
Kavram-kavram grafiğini normalize ağırlıklarla üretir.

HESAP KODU BURADA DEĞİL: tüm metrikler `scripts/graph_weights.py` içinde.
Bu betik yalnızca yükler, hesaplar ve yazar.

    PMI      : log2( N * cooc / (deg_a * deg_b) )
    Jaccard  : cooc / (deg_a + deg_b - cooc)
    score    : PMI * log2(1 + cooc) ^ alpha     (varsayılan alpha=0.5)

Kullanım:
    python3 scripts/build-weighted-graph.py
    python3 scripts/build-weighted-graph.py --min-cooc 5 --alpha 0.5

Çıktı: graph-weighted.json  (meta + edges[])
"""
import argparse
import datetime
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from graph_weights import (  # noqa: E402  (tek kaynak)
    DEFAULT_ALPHA,
    DEFAULT_MIN_COOC,
    METRIC_DOC,
    concept_graph,
    load_bundle,
)

WIKI = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def build(bundle, min_cooc=DEFAULT_MIN_COOC, alpha=DEFAULT_ALPHA, bundle_name="bundle.json"):
    """bundle -> graph-weighted.json sözlüğü. Metrikler graph_weights'ten."""
    cg = concept_graph(bundle, min_cooc=min_cooc, alpha=alpha)
    edges = cg.edges()
    meta = {
        "generated": datetime.datetime.now().isoformat(timespec="seconds"),
        "method": "kavram-kavram kenarlari, ortak raw_article uzerinden",
        "source_bundle": bundle_name,
        "metrics": METRIC_DOC,
        "thresholds": {"min_cooccurrence": min_cooc, "alpha": alpha},
        "stats": cg.stats(),
    }
    return {"meta": meta, "edges": edges}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--wiki", default=WIKI)
    ap.add_argument("--bundle", default="bundle.json", help="kaynak bundle dosyasi")
    ap.add_argument("--min-cooc", type=int, default=DEFAULT_MIN_COOC)
    ap.add_argument("--alpha", type=float, default=DEFAULT_ALPHA)
    ap.add_argument("--out", default=None)
    a = ap.parse_args()

    bundle = load_bundle(a.wiki, a.bundle)
    res = build(bundle, a.min_cooc, a.alpha, a.bundle)
    out = a.out or os.path.join(a.wiki, "graph-weighted.json")
    with open(out, "w", encoding="utf-8") as f:
        json.dump(res, f, ensure_ascii=False, indent=1)

    s = res["meta"]["stats"]
    print(f"yazildi: {out}")
    print(f"kaynak : {a.bundle}")
    print(f"kenar  : {s['kept_pairs']}/{s['raw_pairs']} (min_cooc={a.min_cooc})")
    print(f"kavram : {s['concept_nodes']} | kavramli makale: {s['corpus_articles_with_concepts']}")
    print("\nilk 10 kenar:")
    for e in res["edges"][:10]:
        print(f"  {e['score']:6.3f}  raw={e['cooccurrence']:4d}  "
              f"{e['source_label'][:38]} <-> {e['target_label'][:38]}")


if __name__ == "__main__":
    main()
