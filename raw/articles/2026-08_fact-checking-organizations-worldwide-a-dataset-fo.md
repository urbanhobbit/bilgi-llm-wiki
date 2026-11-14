---
type: raw_article
title: 'Fact-checking organizations worldwide: A dataset for structural and contextual
  analysis'
description: '**Veri makalesi (data descriptor) — Data in Brief 69:113385, Ağustos
  2026, CC BY-NC 4.0.** Sánchez-Mayordomo, García-Alcaraz ve Ruipérez-Valiente, dünya
  genelinde **doğrulama kuruluşlarının (fact-chec...'
resource: https://www.sciencedirect.com/science/article/pii/S2352340926009315
tags:
- kurator
- high
timestamp: '2026-11-14T00:41:00Z'
source_file: 2026-11-13_fact-checking-organizations-worldwide-dataset.json
category: KURATOR
priority: high
roles:
- method
- result
published: 2026-08
---

# Fact-checking organizations worldwide: A dataset for structural and contextual analysis

**Author(s):** Francisca Sánchez-Mayordomo; Teresa García-Alcaraz; José A. Ruipérez-Valiente

**Published:** 2026-08

**Source:** [https://www.sciencedirect.com/science/article/pii/S2352340926009315](https://www.sciencedirect.com/science/article/pii/S2352340926009315)

## Summary

**Veri makalesi (data descriptor) — Data in Brief 69:113385, Ağustos 2026, CC BY-NC 4.0.** Sánchez-Mayordomo, García-Alcaraz ve Ruipérez-Valiente, dünya genelinde **doğrulama kuruluşlarının (fact-checkers) yapısal ve bağlamsal analizi** için normalleştirilmiş bir veri seti yayımlıyor. Amaç: mevcut internet depolarının (Duke Reporters' Lab, IFCN listeleri vb.) yapısal sınırlamaları yüzünden yapılamayan **sistematik ve nicel** analizi mümkün kılmak.

**Yöntem (makale özetinden, birebir):** kuruluşların belirlenmesi ve seçimi **PRISMA** (Preferred Reporting Items for Systematic Reviews and Meta-Analyses) protokolüne göre yapılandırıldı; veri çıkarımı **16 Ekim 2025 – Şubat 2026** arasında zamanla sınırlandı; sektörün heterojenliğini yakalamak için **tümevarımsal kodlama** uygulandı. Veri seti **13 değişken** içeriyor: Entity, URL, Active, Country, Language, Year_Foundation, Scope, Type_Org, Type_Content, Methodological_Transparency, Affiliations_Memberships, Why, Financing.

**Veri setinin kendisi (OSF deposu `osf.io/ejzw9`, doğrulandı ve indirildi):** `Fact-Checking_Organizations_Worldwide.csv` (1,2 MB, 28 Temmuz 2026 sürümü) + veri sözlüğü + metodoloji notu + kaynak URL listesi + lisans. README'nin beyanı **750 kuruluş**; CSV'de ise **1.980 satır** var. Bu bir hata değil, **çok-değerli alanların satır açması**: (kuruluş, ülke) çifti bazında tekil sayı **750** ve tam satır tekrarı yok — Teyit'in 8 satırı yalnızca `LANGUAGE` (Turkish/English), `TYPE_CONTENT` (debunking/education) ve `AFFILIATIONS_MEMBERSHIPS` (EFCSN/IFCN) alanlarında farklılaşıyor. **Analiz öncesi dedupe zorunlu**, yoksa dil ve içerik türü dağılımları şişer.

**Hesapladığım yapısal tablo (750 tekil kuruluş üzerinden, CSV'den):** 575 **aktif** / 175 **kapalı**; **131 ülke**; 64 dil (ilk-kayıt bazında; en yaygın: İngilizce 291, İspanyolca 85, Fransızca 51, Arapça 47). Ölçek: Ulusal 530, Bölgesel 106, Uluslararası 39, Küresel 33, Yerel 33. Örgüt tipi: Bağımsız 253, Özel/ticari medya 164, STK/kâr amacı gütmeyen 137, Haber ajansı 62, İşbirliği projesi 52, Kamu/devlet medyası 49, Akademik/araştırma merkezi 29. İçerik türü: neredeyse tamamı **debunking** (736/750). Metodolojik şeffaflık: Yüksek 432, Çok yüksek 301, Düşük 9, N/A 8. Kuruluş yılı 1917–2025, **medyan 2018**; en büyük kuruluş dalgası **2017 (71) ve 2019 (108)** — 2023 sonrası sert düşüş (2024: 5, 2025: 3). Ülke yoğunlaşması: ABD 140, Hindistan 40, Fransa 26, Nijerya 17, Endonezya 17, Güney Kore 16, Almanya 15.

**Neden önemli:** veri seti, doğrulama sektörünün **hayatta kalma/kapanma**, **finansman bağımlılığı** (platform programları, IFCN/Google/YouTube Global Fact Check Fund, EDMO/AB projeleri, vakıf fonları) ve **şeffaflık iddiaları** ekseninde nicel analizine izin veriyor. `Financing` alanı serbest metin — yani fon kaynağı tipleri ancak yeniden kodlanarak sayılabilir; hazır kategori değil.

⚠️ **Erişim sınırı:** makalenin gövdesi (ScienceDirect) Cloudflare duvarı yüzünden okunamadı; özet **yayıncı sayfasından** alındı, veri seti ve istatistikler **OSF deposundan** doğrulandı. Gövdedeki tablo/şekil ve tartışma bölümü doğrulanmadı.

## Key Points

- Sánchez-Mayordomo, García-Alcaraz & Ruipérez-Valiente (2026), 'Fact-checking organizations worldwide: A dataset for structural and contextual analysis', Data in Brief 69:113385, DOI 10.1016/j.dib.2026.113385 — CC BY-NC 4.0, altın açık erişim.
- Veri seti OSF'te: osf.io/ejzw9 — 4 klasör (Data, Documentation, Sources, LICENSE); CSV 1.2 MB, sürüm 28.07.2026.
- 750 tekil doğrulama kuruluşu (575 aktif / 175 kapalı), 131 ülke, 13 değişken; kuruluş yılları 1917–2025, medyan 2018.
- CSV'de 1.980 satır var ama tekil kuruluş 750: çok-değerli alanlar (Language, Type_Content, Affiliations) satır açıyor → analiz öncesi dedupe şart.
- Kapsam dağılımı: Ulusal 530, Bölgesel 106, Uluslararası 39, Küresel 33, Yerel 33.
- Örgüt tipi: Bağımsız 253, Özel/ticari medya 164, STK 137, Haber ajansı 62, İşbirliği projesi 52, Kamu medyası 49, Akademik 29.
- İçerik türü: debunking 736/750 — sektör fiilen 'çürütme' işi yapıyor; pre-bunking ve eğitim marjinal.
- Metodolojik şeffaflık: Yüksek 432 + Çok yüksek 301 (≈%98); Düşük yalnızca 9 kuruluş.
- Kuruluş dalgası: 2017 (71) ve 2019 (108) zirve; 2023 sonrası çöküş (2024: 5, 2025: 3) — sektörün kurumsallaşma hızı düşüyor.
- Ülke yoğunlaşması: ABD 140, Hindistan 40, Fransa 26, Nijerya 17, Endonezya 17, Güney Kore 16, Almanya 15.
- Türkiye: 4 kuruluş — Doğrula (2021), Doğruluk Payı (2014), Teyit (2016), Malumatfuruş (2015); dördü de aktif, üçü STK, biri bağımsız.
- Yöntem (makale özeti): PRISMA protokolü + tümevarımsal kodlama; veri toplama 16.10.2025–Şubat 2026 aralığında kapatıldı.
- OSF dokümantasyonu (Temmuz 2026) makale özetinden daha sade: PRISMA ifadesi ve 13 değişkenli tümevarımsal kodlama çerçevesi makalede var, OSF metodoloji notunda yok — iki belge arasında sürüm farkı.
- Financing alanı serbest metin; fon kaynağı kategorileri (platform programları, IFCN/Google fonu, EDMO/AB fonları) ancak elle yeniden kodlanarak sayılabilir.
- Erişim: makale gövdesi okunamadı (ScienceDirect Cloudflare); özet yayıncı sayfasından, veri ve istatistikler OSF'ten doğrulandı.

## Turkey Context

**Türkiye'nin veri setindeki yeri zayıf ve bu bir bulgu:** 750 kuruluşun yalnızca **4'ü** Türkiye merkezli — Doğrula (2021), Doğruluk Payı (2014), Teyit (2016), Malumatfuruş (2015). Dördü de aktif; üçü STK/kâr amacı gütmeyen, biri bağımsız. Karşılaştırma: Gürcistan 34, Demokratik Kongo 33 kuruluşla listede — yani bu, Türkiye'de doğrulama kapasitesinin *yokluğu* değil, **kurumsal çeşitlenmenin ve görünürlüğün düşüklüğü** olarak okunmalı. Olası nedenler (doğrulanmamış): erişim kısıtları, platform ortaklık programlarına (Meta/ TikTok third-party fact-checking) kabul edilmeme, finansman bağımlılığı.

**Kullanım değeri:** bu veri seti Türkiye analizleri için üç somut imkân veriyor — (1) **hayatta kalma analizi**: 2015–2025 kuruluş dalgası içinde Türkiye'nin yeri ve kapanma riski; (2) **finansman haritası**: IFCN/Google fonu, EDMO/AB projeleri ve vakıf fonlarının ülke dağılımı — Türkiye'nin bu kaynaklardan ne kadar pay aldığı `Financing` alanından elle kodlanarak çıkarılabilir; (3) **şeffaflık karşılaştırması**: `Methodological_Transparency` alanı Türkiye'deki kuruluşların akranlarına göre nerede durduğunu gösterir.

**Uyarı:** veri seti **nicelik** ölçüyor, **etki** değil. "Türkiye'de 4 doğrulama kuruluşu var" cümlesi, dezenformasyonla mücadelenin kapasitesi hakkında tek başına bir şey söylemez; yayılma hızı/erişim verisiyle birleştirilmeden kullanılmamalı.

## 🏷 Retorik Roller

- 🧩 **Yöntem**
- 📊 **Bulgular**

---

## 🔗 İlgili Bağlantılar
### 🧠 İlgili Kavramlar
- [[concepts/media-literacy-fact-checking.md|Media Literacy and Fact-Checking (Medya Okuryazarlığı ve Doğrulama)]]
- [[concepts/platform-seffaflik.md|platform-seffaflik]]
- [[concepts/siyaset-bilimi-metodolojisi.md|Siyaset Bilimi Metodolojisi]]
### 🏛 İlgili Kurum/Kişiler
- [[entities/sciencedirect.md|Sciencedirect]]
