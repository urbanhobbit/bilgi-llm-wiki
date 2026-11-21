#!/usr/bin/env python3
"""
triage.py — kavramsiz makaleler icin oneri uretici (SADECE DOSYA, DB'ye yazmaz).

Yontem (seffaf, denetlenebilir):
  1. Makale govdesinden + basligindan metin cikar.
  2. Her kavram icin anahtar terim listesi (KAVRAM_TERIMLERI) + kavram etiketinin
     kendisi ile eslesme ara.
  3. Skor = agirlikli terim isabeti (baslikta 3x, govdede 1x).
  4. En yuksek 1-3 kavram onerilir; skor 0 ise "elle inceleme" isaretlenir.
  5. Gerekce olarak eslesen TERIMLER yazilir — boylece oneri denetlenebilir.

Cikti: output/triage.csv  (makale, onerilen kavramlar, skorlar, gerekce, guven)
"""
import csv
import json
import pathlib
import re
import unicodedata

WIKI = pathlib.Path(__file__).resolve().parent.parent
BUNDLE = WIKI / "bundle2.json"
OUT = WIKI / "output" / "triage.csv"

# ---------------------------------------------------------------- terim sozlugu
# Kavram slug -> eslesme terimleri (Turkce + Ingilizce). Elle yazildi, denetlenebilir.
KAVRAM_TERIMLERI = {
    "dijital-haklar": ["dijital hak", "digital right", "çocuk hakları sözleşmesi", "uncrc", "hak temelli"],
    "sosyal-medya-yasagi-tartismasi": ["sosyal medya yasağı", "social media ban", "yasak", "minimum yaş", "age limit"],
    "dijital-okuryazarlik": ["dijital okuryazarlık", "digital literacy", "medya okuryazarlığı", "media literacy"],
    "yas-dogrulama": ["yaş doğrulama", "age verification", "age assurance", "yaş tespiti", "age estimation"],
    "dijital-vatandaslik": ["dijital vatandaşlık", "digital citizenship"],
    "ekran-suresi": ["ekran süresi", "screen time", "ekran başında"],
    "cocuk-veri-gizliligi": ["veri gizliliği", "data protection", "gdpr", "kişisel veri", "privacy"],
    "yapay-zeka-cocuklar": ["yapay zeka ve çocuk", "children and ai", "çocuklar ve yapay zeka", "ai for children"],
    "dezenformasyon": ["dezenformasyon", "disinformation", "misinformation", "yanlış bilgi"],
    "sosyal-medya-genclik": ["sosyal medya ve gençlik", "adolescent social media", "gençlerin sosyal medya"],
    "siber-zorbalik": ["siber zorbalık", "cyberbullying", "çevrimiçi zorbalık"],
    "sosyal-kutuplasma": ["kutuplaşma", "polarization", "polarisation", "kutuplaş"],
    "platform-seffaflik": ["platform şeffaflığı", "platform transparency", "şeffaflık yükümlülüğü"],
    "platform-economy-misinformation": ["platform ekonomisi", "platform economy", "reklam geliri", "ad revenue"],
    "olcum-araclari": ["ölçüm aracı", "measurement instrument", "ölçek geliştirme", "scale development", "ölçüm hatası"],
    "siyaset-bilimi-metodolojisi": ["metodoloji", "methodology", "nedensel çıkarım", "causal inference", "araştırma tasarımı"],
    "cocuk-dijital-kisitlamalar": ["kısıtlama", "restriction", "düzenleme", "regulation"],
    "duygusal-kutuplasma": ["duygusal kutuplaşma", "affective polarization", "affective polarisation"],
    "ai-generated-disinformation": ["ai ile üretilen", "ai-generated", "deepfake", "sentetik medya", "synthetic media"],
    "cocuk-dijital-katilim": ["katılım", "participation", "çocuk katılımı"],
    "demokratik-erozyon": ["demokratik erozyon", "democratic backsliding", "demokrasi"],
    "macaristan-secim-2026": ["macaristan", "hungary", "tisza", "orbán"],
    "populizm": ["popülizm", "populism", "popülist", "populist"],
    "turkiye-okul-saldirilari": ["okul saldırısı", "school attack", "okul güvenliği", "school shooting"],
    "filtre-baloncuklari": ["filtre balonu", "filter bubble"],
    "partizan-kimlik": ["partizan", "partisan", "partisanship"],
    "sentetik-populasyonlar": ["sentetik popülasyon", "synthetic population", "agent-based", "simülasyon"],
    "platform-is-modeli": ["iş modeli", "business model", "algoritmik"],
    "yapay-zeka-yonetisimi": ["yönetişim", "governance", "regulation of ai", "ai governance"],
    "ideolojik-kutuplasma": ["ideolojik kutuplaşma", "ideological polarization"],
    "cocuk-haklari": ["çocuk hakları", "children's rights", "uncrc", "çocuk hak"],
    "onvargi-ve-stereotipler": ["önyargı", "bias", "stereotip", "stereotype"],
    "komplo-inanclari": ["komplo", "conspiracy"],
    "yapay-zeka-cocuk-guvenlik": ["çocuk güvenliği", "child safety", "child safeguarding"],
    "fimi": ["fimi", "foreign information manipulation"],
    "geopolitical-disinformation": ["jeopolitik", "geopolitical", "bilgi savaşı", "information warfare"],
    "siyasal-katilim": ["siyasal katılım", "political participation", "oy verme", "voter turnout"],
    "metin-madenciligi": ["metin madenciliği", "text mining", "doğal dil işleme", "nlp", "topic model", "large language model", "llm", "büyük dil modeli", "qualitative coding", "nitel kodlama"],
    "yanlis-kutuplasma": ["yanlış kutuplaşma", "false polarization"],
    "yapay-zeka-demokrasi": ["ai and democracy", "yapay zeka ve demokrasi"],
    "kuram-operasyonellestirme-llm": ["operasyonelleştirme", "operationalization", "kuramsal kayma", "theory operationalization"],
    "bilim-ve-siyaset": ["bilim ve siyaset", "science and politics", "politicization of science"],
    "siyasal-etkileyiciler": ["etkileyici", "influencer"],
    "tavsan-deligi-etkisi": ["tavşan deliği", "rabbit hole"],
    "ahlaki-panik": ["ahlaki panik", "moral panic"],
    "akran-zorbaligi": ["akran zorbalığı", "peer victimization", "bullying"],
    "election-interference-disinformation": ["seçim müdahalesi", "election interference"],
    "negative-partisanship": ["negatif partizanlık", "negative partisanship"],
    "sentetik-odak-gruplari": ["sentetik odak grubu", "synthetic focus group", "silicon sampling"],
    "arastirma-sonucu-tahminleme": ["sonuç tahminleme", "forecasting", "tahmin"],
    "bilimsel-iletisim": ["bilimsel iletişim", "science communication"],
    "diploma-divide": ["diploma divide", "eğitim makası", "eğitim düzeyi"],
    "eko-odasi": ["yankı odası", "echo chamber"],
    "populist-oylama": ["popülist oy", "populist voting", "radical right voting"],
    "siyasal-siddet": ["siyasal şiddet", "political violence", "radikalleşme"],
    "dijital-ikizler": ["dijital ikiz", "digital twin"],
    "partizan-redistricting": ["gerrymandering", "redistricting", "seçim çevresi"],
    "synthetic-media-ai-content": ["sentetik medya", "synthetic media", "deepfake"],
    "kesifsel-dogrulayici-ayrimi": ["keşifsel", "doğrulayıcı", "exploratory", "confirmatory"],
    "kulturel-evrim": ["kültürel evrim", "cultural evolution"],
    "muzakereci-demokrasi": ["müzakereci demokrasi", "deliberative democracy", "deliberation"],
    "partizan-isaret-etkisi": ["partisan cue", "işaret etkisi"],
    "siyasal-temsil": ["siyasal temsil", "political representation", "responsiveness"],
    "surec-takibi-ve-nedensel-mekanizma": ["süreç takibi", "process tracing", "nedensel mekanizma", "causal mechanism"],
    "ahlaki-temeller-kurami": ["ahlaki temeller", "moral foundations"],
    "cycle-of-distrust": ["distrust", "güvensizlik döngüsü"],
    "harness-engineering": ["harness engineering", "agent harness", "harness mühendisliği"],
    "ideolojik-kamplar": ["ideolojik kamp", "ideological camp"],
}

BASLIK_AGIRLIK = 3
GOVDE_AGIRLIK = 1
MIN_SCORE = 4.5   # altinda kalan oneriler elenir (yanlis pozitif kontrolu)


def _norm(s: str) -> str:
    s = s.lower()
    s = s.replace("ı", "i").replace("İ", "i")
    s = unicodedata.normalize("NFKD", s)
    s = "".join(c for c in s if not unicodedata.combining(c))
    return re.sub(r"\s+", " ", s)


def parse_md(p: pathlib.Path):
    t = p.read_text(encoding="utf-8", errors="ignore")
    fm, body = {}, t
    if t.startswith("---"):
        parts = t.split("---", 2)
        if len(parts) >= 3:
            body = parts[2]
            for line in parts[1].splitlines():
                m = re.match(r"^(\w+):\s*(.*)$", line)
                if m:
                    fm[m.group(1)] = m.group(2).strip().strip("'\"")
    return fm, body


def score_article(title: str, body: str):
    """Skor > 0 olan kavramlari dondurur. Zayif/tek-isabet elenir.

    Kalite kurallari (ampirik olarak belirlendi):
      - Tek bir zayif isabet (skor < MIN_SCORE) oneri sayilmaz.
      - Kavram etiketinin kendisiyle eslesme daha agir basar (3x) cunku
        genel terimler (ai, platform, olcek) cok yanlis pozitif uretiyor.
    """
    tn, bn = _norm(title), _norm(body)
    rows = []
    for slug, terms in KAVRAM_TERIMLERI.items():
        hits, sc = [], 0
        for term in terms:
            t = _norm(term)
            in_t = tn.count(t)
            in_b = bn.count(t)
            if in_t or in_b:
                # kisa/genel terimler (<=3 harf) daha az agirlikli
                w = 1 if len(t) <= 3 else 1.5
                sc += (in_t * BASLIK_AGIRLIK + in_b * GOVDE_AGIRLIK) * w
                hits.append((term, in_t + in_b))
        if sc <= 0:
            continue
        # en az bir TERIM 2+ kez gecmeli ya da baslikta gorunmeli
        strong = any(n >= 2 for _, n in hits) or any(_norm(t_) in tn for t_, _ in hits)
        if not strong or sc < MIN_SCORE:
            continue
        rows.append((slug, round(sc, 1), [f"{a}×{b}" for a, b in hits]))
    rows.sort(key=lambda x: -x[1])
    return rows[:3]


def main():
    d = json.load(open(BUNDLE, encoding="utf-8"))
    nodes = {n["data"]["id"]: n["data"] for n in d["nodes"]}
    stats = json.load(open(WIKI / "graph-weighted.json", encoding="utf-8")).get("meta", {}) \
        if (WIKI / "graph-weighted.json").exists() else {}

    targets = [nid for nid, n in nodes.items()
               if n.get("type") == "raw_article" and not n.get("n_concepts")]

    rows = []
    for nid in sorted(targets):
        p = WIKI / (nid + ".md")
        if not p.exists():
            rows.append({"makale": nid, "baslik": "", "onerilen_kavramlar": "",
                         "skorlar": "", "gerekce": "DOSYA YOK", "guven": "yok"})
            continue
        fm, body = parse_md(p)
        title = fm.get("title") or nodes[nid].get("label", "")
        sugg = score_article(title, body)

        if not sugg:
            # neden oneri yok? metin cok kisa mi, yoksa kapsam disi mi?
            if len(body.strip()) < 400:
                why = "metin cok kisa (<400 karakter) — elle inceleme"
            else:
                why = "mevcut 127 kavramin kapsami disinda — YENI KAVRAM ADAYI"
            rows.append({"makale": nid, "baslik": title[:120],
                         "onerilen_kavramlar": "", "skorlar": "",
                         "gerekce": why, "guven": "kapsam-disi"})
            continue

        top = sugg[0][1]
        if top >= 10 and len(sugg) >= 2:
            conf = "yuksek"
        elif top >= 5:
            conf = "orta"
        else:
            conf = "dusuk"

        rows.append({
            "makale": nid,
            "baslik": title[:120],
            "onerilen_kavramlar": "; ".join(s for s, _, _ in sugg),
            "skorlar": "; ".join(str(s) for _, s, _ in sugg),
            "gerekce": " | ".join(f"{s}: {', '.join(h[:4])}" for s, _, h in sugg),
            "guven": conf,
        })

    OUT.parent.mkdir(parents=True, exist_ok=True)
    with open(OUT, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=["makale", "baslik", "onerilen_kavramlar",
                                          "skorlar", "gerekce", "guven"])
        w.writeheader()
        w.writerows(rows)

    from collections import Counter
    c = Counter(r["guven"] for r in rows)
    print(f"yazildi: {OUT}")
    print(f"toplam makale: {len(rows)}")
    for k in ("yuksek", "orta", "dusuk", "yok"):
        print(f"  {k}: {c.get(k,0)}")
    return rows


if __name__ == "__main__":
    main()
