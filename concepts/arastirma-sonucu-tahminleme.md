---
type: concept
title: Araştırma Sonucu Tahminleme
description: 'Sonuçlanmamış deney ve RCT''lerin etkilerini önceden tahmin etme: ön-kayıt metinlerinden soru çıkarma, tahmin platformları (SSPP), LLM/ML tahmin modelleri ve tahmin doğruluğunun puanlanması.'
tags:
- akademik
- metodoloji
- tahmin
- nedensel-cikarim
- bilim-ustu-arastirma
timestamp: '2026-11-03T00:00:00Z'
created: 2026-11-03
updated: 2026-11-03
confidence: medium
---
# Araştırma Sonucu Tahminleme

Sosyal bilimde "ne biliyoruz" sorusunu tahmin performansı üzerinden yeniden kurma girişimi: henüz sonuçlanmamış bir deneyin (RCT) etkisini **önceden ve puanlanabilir biçimde** tahmin etmek.

**Neden:** RCT literatürü büyük ama kullanışsız — tekil çalışmalar gürültülü, genellenebilirliği zor; meta-analiz ve sistematik derleme yavaş, pahalı ve hızla eskiyor. Tahmin yaklaşımı şunu önerir: bir denemenin sonucunu ne kadar doğru öngörebildiğimiz, o alanda ne kadar şey bildiğimizin ölçüsüdür.

**Bileşenler:**
- **Tahmin soruları:** ön-analiz planı / ön-kayıt metninden çıkarılan, sonuç değişkeni + yön + büyüklük üzerine sorular.
- **Tahmin biçimi:** her sonuç için ortalama **ve** varyans (nokta tahmini + belirsizlik); puanlama hem doğruluk hem kalibrasyon üzerinden.
- **Platformlar:** Social Science Prediction Platform (SSPP) — araştırmacılar ön-kayıtlı çalışmalarını yükler, uzmanlar tahmin eder; DellaVigna & Vivalt (2025, NBER w34493) 100 proje / 1.482 soru / 53.298 tahmin üzerinde tahmincilerin sistematik iyimserlik ve sıfıra yakınlık yanlılığı gösterdiğini buldu.
- **LLM/ML modelleri:** ön-kayıt metninden soru çıkarma + etki büyüklüğü tahmini. Vivalt (2026, arXiv:2610.38883) 39 makaleden 889 tedavi etkisinde medyan mutlak hatayı 0,054 SD'ye indirdi; sıfır-etki ve ortalama-etki referanslarından belirgin biçimde iyi. Query2Effect (arXiv:2605.29631) ince ayarın hatayı %27-71 azalttığını gösterdi.
- **Yarışma biçimi:** Prediction League (The Agency Fund + 3ie + SSPP + Stanford/Northwestern/Toronto, 2026) — çok turlu, liderlik tablolu, açık ve yinelenebilir bölümlü ödüllü yarışma.

**Bilinen tuzaklar:**
- **Veri sızıntısı:** modelin eğitim kesme tarihi (knowledge cut-off) yayın tarihinden önce olmalı; aksi hâlde tahmin, hatırlamadır.
- **Yayın yanlılığı:** yayımlanmış literatürle eğitilen modeller yayın yanlılığını devralır; literatürde az temsil edilen bağlamlarda (Türkiye gibi) tahminler sistematik olarak kayar.
- **Doğruluk–yorumlanabilirlik ödünleşimi:** en isabetli model, nedenini en az açıklayan model olabilir.
- **Çözülmeyen sorular:** ön-kayıttaki tüm sorular makalede raporlanmaz; puanlama yalnızca çözülen alt kümede yapılabilir (seçim etkisi).
- **Karşıolgusal referans:** "sıfır etki" ve "literatür ortalaması" gibi naif referansları geçmek gerekir; tek başına düşük MSE bir başarı değildir.

**Bağlantılı kavramlar:** [[concepts/siyaset-bilimi-metodolojisi.md|Siyaset Bilimi Metodolojisi]], [[concepts/sentetik-populasyonlar.md|Sentetik Popülasyonlar]], [[concepts/katilimci-yapay-zeka-kullanimi.md|Katılımcıların Ankette Yapay Zekâ Kullanımı]]

## İlgili Makaleler
- [[raw/articles/2026-11-03_prediction-league-for-policy-relevant-rcts.md|Prediction League for Policy-Relevant RCTs]] — The Agency Fund (3 Kasım 2026): 500k+ USD pilot havuzu, açık/yinelenebilir bölümler, Kasım 2026–Ocak 2028 takvimi.
- [[raw/articles/2026-10-28_can-ai-forecast-treatment-effects-in-economics.md|Can AI Forecast Treatment Effects in Economics?]] — Vivalt (2026, arXiv:2610.38883): 889 tedavi etkisi, medyan mutlak hata 0,054 SD.
- [[raw/articles/2025-11-24_forecasting-social-science-evidence-from-100-proje.md|Forecasting Social Science: Evidence from 100 Projects]] — DellaVigna & Vivalt (2025, NBER w34493): SSPP'de 100 proje, 53.298 tahmin.
