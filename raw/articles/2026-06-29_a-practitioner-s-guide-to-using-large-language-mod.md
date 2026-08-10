---
type: raw_article
title: A Practitioner's Guide to Using Large Language Models and Generative AI in
  Economic History
description: NBER Working Paper 35374, Haziran 2026 (JEL C55, C8, N0) - Andreas Ferrara
  (University of Pittsburgh, Department of Economics & NBER). LLM'lerin el yazmasi
  defterler, metin, gorsel ve ses kayitlari gi...
resource: https://doi.org/10.3386/w35374
tags:
- kurator
- high
timestamp: '2026-08-10T19:27:09Z'
source_file: 2026-08-10_ferrara-llm-genai-economic-history-guide.json
category: KURATOR
priority: high
roles:
- method
- result
published: '2026-06-29'
---

# A Practitioner's Guide to Using Large Language Models and Generative AI in Economic History

**Published:** 2026-06-29

**Source:** [https://doi.org/10.3386/w35374](https://doi.org/10.3386/w35374)

## Summary

NBER Working Paper 35374, Haziran 2026 (JEL C55, C8, N0) - Andreas Ferrara (University of Pittsburgh, Department of Economics & NBER). LLM'lerin el yazmasi defterler, metin, gorsel ve ses kayitlari gibi eskiden guclu veri bilimi becerisi gerektiren tarihsel veri kaynaklarina erisim engelini dusurdugu tezinden yola cikan kapsamli bir uygulayici rehberi. Calisma, arastirma fikrini calisan kod ve veriye donusturen adim-adim bir workflow sunuyor ve LLM ile etkilesimin dort ana yolunu tanimliyor: (1) tarayici sohbet penceresi, (2) editor-entegre asistanlar, (3) arastirmacinin bilgisayarinda dosyalarla calisabilen agentic coding araclari (Claude Code, OpenAI Codex, Gemini CLI), (4) API cagrilari. Rehber, uygulayicinin karsilastigi kararlari sirayla isliyor: LLM dogru arac mi, veri bir LLM'e gonderilebilir mi, model secimi, prompt yazma, context limitlerini yonetme, maliyet kontrolu ve son olarak LLM-uretimi olcumlerin regresyon ortamlarinda dogrulanmasi, yeniden uretilebilirligi, dokumantasyonu ve duzeltilmesi. Riskler vurgulaniyor: LLM'ler referans uydurabilir (hallucination), kulturel onyargilar uretebilir, cografya hakkinda zayif akil yurutur, gecerli nedensel tasarim uretemez (Kiciman et al. 2024); prompt veya model degisikligi bir regresyon katsayisinin boyutunu hatta ISARETINI degistirebilir (Ludwig et al. 2026; Yin et al. 2026) ve standart hatalar bu yanliligi isaretlemeyebilir (Battaglia et al. 2025). Ayrica entelektuel tembellik ve dusunce cesitliligi kaybi riski: arastirmacilar ayni sorulari ayni araclara sorup ayni cevaplari benimserse alan heterojenligini kaybeder. Dort calisilmis ornek replikasyon dosyalariyla sunuluyor: (1) tablolardaki duygularin siniflandirilmasi (Gorin et al. 2025'in CNN yaklasimina LLM alternatifi), (2) isimsiz nufus sayimi baglama (1900-1910 arasi 10.000 Connecticut erkegi; LLM'ler %43-62 eslesme orani vs basit join %4,3; Census Tree %93 anlasma; agentic ChatGPT-5.5 ve Claude Opus 4.8 en iyi sonuc), (3) 1882 Cin Dislama Yasasi cevresinde gazete belirginligi ve duygu olcumu (524.458 sayfa -> on isleme ile 11.011 sayfa, batch API), (4) FDR'nin savas konusmalarinda duygusal sunum puanlamasi (Day of Infamy en yogun). Replikasyon dosyalari: https://doi.org/10.3886/E249897V2 (ICPSR). Ekonomi tarihinde LLM tabanli veri cikarma, harmonizasyon ve siniflandirma literaturunun genis bir incelemesi ile birlikte; GGT (Schmitt et al. 2026) GenAI metodoloji tartismasina tarihsel veri uygulamalariyla tamamlayici bir katki.

## Key Points

- NBER Working Paper 35374, Haziran 2026; DOI: 10.3386/w35374; yazar: Andreas Ferrara (Pittsburgh & NBER)
- LLM ile 4 etkilesim yolu: chat penceresi, IDE asistanlari, agentic coding araclari (Claude Code/Codex/Gemini CLI), API
- Adim-adim workflow: fikir -> calisan kod/veri; prompt yazma, context limitleri, maliyet kontrolu, dogrulama
- Riskler: hallucinated referanslar, kulturel onyargi, zayif cografya muhakemesi, gecersiz nedensel tasarim; prompt/model degisimi katsayi boyutunu/isaretini degistirebilir
- LLM-uretimi olcumlerde olcum hatasi sistematik olabilir; standart hatalar yanliligi isaretlemez (Battaglia et al. 2025)
- Entelektuel tembellik ve dusunce cesitliligi kaybi riski: yazma ve kritik dusunme arastirmacida kalmalI
- 4 calisilmis ornek: tablo duygu siniflandirma, isimsiz nufus baglama (%43-62), 1882 Cin Dislama Yasasi gazete duygu (524K->11K sayfa), FDR savas konusmalari duygu skoru
- Replikasyon: https://doi.org/10.3886/E249897V2 (ICPSR); JEL C55, C8, N0

## 🏷 Retorik Roller

- 🧩 **Yöntem**
- 📊 **Bulgular**

---

## 🔗 İlgili Bağlantılar
### 🧠 İlgili Kavramlar
- [[concepts/siyaset-bilimi-metodolojisi.md|Siyaset Bilimi Metodolojisi]]
- [[concepts/olcum-araclari.md|Ölçüm Araçları (Polarization Measurement)]]
