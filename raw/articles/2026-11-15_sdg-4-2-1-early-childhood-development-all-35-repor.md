---
type: raw_article
title: 'SDG 4.2.1 early childhood development: all 35 reporting countries have data
  after 2020'
description: 'UNICEF''in baş istatistikçisi João Pedro Azevedo''nun **15 Kasım 2026**
  tarihli gönderisi, SDG 4.2.1 (erken çocukluk gelişimi) göstergesinde veri toplama
  takviminin kritik bir eşiği aştığını duyuruyor: ...'
resource: https://unstats.un.org/sdgapi/v1/sdg/Series/Data?seriesCode=SE_DEV_ONTRKWB
tags:
- kurator
- genel
- medium
timestamp: '2026-11-15T08:58:28Z'
source_file: 2026-11-15_unicef-ecdi2030-sdg-4-2-1-data-recency.json
category: KURATOR; GENEL
priority: medium
roles:
- result
- policy
published: '2026-11-15'
---

# SDG 4.2.1 early childhood development: all 35 reporting countries have data after 2020

**Author(s):** João Pedro Azevedo (UNICEF Baş İstatistikçi, Data & Analytics Section) — veri kaynağı: UNICEF / UN SDG Global Database

**Published:** 2026-11-15

**Source:** [https://unstats.un.org/sdgapi/v1/sdg/Series/Data?seriesCode=SE_DEV_ONTRKWB](https://unstats.un.org/sdgapi/v1/sdg/Series/Data?seriesCode=SE_DEV_ONTRKWB)

## Summary

UNICEF'in baş istatistikçisi João Pedro Azevedo'nun **15 Kasım 2026** tarihli gönderisi, SDG 4.2.1 (erken çocukluk gelişimi) göstergesinde veri toplama takviminin kritik bir eşiği aştığını duyuruyor: 'erken çocukluk gelişimi verisi olan **35 ülkenin tamamında** en güncel değer 2020 sonrasına ait; en güncel yıllar 2021-2025 aralığında, **medyan yıl 2023**.' Grafikte en güncel yılın ülke dağılımı 2021'den 2025'e beş çubukla gösteriliyor; kural açıkça tanımlanmış: 'ülke başına en güncel değer; 2020 veya öncesi güncel sayılmaz.' Gönderiye eklenen tanım, 4.2.1'in önerilen ölçütünün **ECDI2030** (Early Childhood Development Index 2030) olduğunu ve bunun 24-59 aylık çocuklarda nüfus temelli anketlerde 20 maddelik bir araçla ölçüldüğünü belirtiyor; veri ve kod GitHub'da (CC BY 4.0), tanım UNICEF Reference Data Manager'ın **ECD_CHLD_LMPSL** göstergesine dayanıyor. **Bağımsız doğrulama (bu kayıt için yapıldı):** UN SDG API'sinden `SE_DEV_ONTRKWB` serisi çekildiğinde 44 ülke ve 130 satır geliyor; ülke başına en güncel yıl dağılımı 2021:4, 2022:11, 2023:13, 2024:6, 2025:10 ve **medyan 2023** — yani 'hepsi 2020 sonrası, aralık 2021-2025, medyan 2023' iddiası birebir doğrulandı; ancak **ülke sayısı 44, gönderideki 35 değil** (muhtemelen yalnızca ECDI2030 modülüyle saha verisi üreten ülkelere daraltılmış bir alt küme). Karşılaştırma olarak eski MICS/DHS tabanlı `SE_DEV_ONTRK` serisi 61 ülke içeriyor ama medyan en güncel yıl **2018** ve 2020 sonrası verisi olan tek ülke El Salvador (2021). Yani iddia, eski seride **kesinlikle yanlış**, yeni ECDI2030 serisinde doğru — 4.2.1'in ölçüm rejimi değiştiği için 'güncellik' iddiası ancak yeni seri üzerinden anlamlı.

## Turkey Context

Türkiye bu veri setinde **var** ve ayrıntı, gönderinin ana mesajından daha ilginç: `SE_DEV_ONTRKWB` serisinde Türkiye 2022 turunda 'Türkiye Child Survey 2022' kaynağıyla yer alıyor — 24-59 aylık çocuklarda gelişimsel olarak yolda olma oranı **her iki cinsiyet için %71,1**, kızlarda %77,7, erkeklerde %64,8. Yani **12,9 puanlık bir cinsiyet farkı** var ve bu, 35-44 ülkelik havuzda karşılaştırmalı bir okuma yapmayı mümkün kılıyor. Üç sonuç çıkıyor. **Birincisi, ölçüm altyapısı.** Türkiye, ECDI2030'a geçen ülkeler arasında; bu, 2018 öncesi MICS/DHS tabanlı serilerle karşılaştırma yapmayı imkânsız kılıyor çünkü araç değişti (36-59 ay yerine 24-59 ay, 20 maddelik yeni endeks). TÜİK'in 2022 Çocuk Araştırması ile bu geçişi yapmış olması, erken çocukluk politikalarında (0-3 yaş bakım, okul öncesi erişim, 2024 Okul Öncesi Eğitim seferberliği) artık **uluslararası karşılaştırılabilir** bir taban çizgisi olduğu anlamına geliyor — ama bu taban çizgisi tek bir yıl, 2022. **İkincisi, cinsiyet açığı.** Kız-erkek farkının 13 puana varması, erken çocukluk gelişiminde toplumsal cinsiyetli ebeveynlik pratiklerinin (erkek çocuklarda dil ve öğrenme uyarımının daha az olması, kız çocukların erken sorumluluk alması) izini taşıyor olabilir; ancak ECDI2030 bir 'gelişimsel yolda olma' bileşik endeksi olduğu için hangi alanın (okuryazarlık-sayı, fiziksel, sosyal-duygusal, öğrenme) farkı sürüklediği bu veriden okunamıyor — alt alan kırılımı talep edilmeli. **Üçüncüsü, siyaset.** 'Tüm ülkelerde veri 2020 sonrası' türü bir cümle, SDG izleme rejiminde **göstergenin kendisinin yeniden tanımlandığını** gizleme riski taşıyor: aynı gösterge kodu (4.2.1) altında aracın değişmesi, zaman serisi karşılaştırmalarını kırar. Türkiye'de çocuk refahı raporlaması yapan kurumların (UNICEF Türkiye, TÜİK, SETA, Çocuk Hakları Platformu) '2022'yi baz yıl' olarak açıkça yazması, aksi halde 'iyileşme/kötüleşme' iddialarının ölçüm değişikliğinden kaynaklanan yapay bir eğri çizmesi riski var.

## 🏷 Retorik Roller

- 📊 **Bulgular**
- 🏛 **Politika Önerisi**

---

## 🔗 İlgili Bağlantılar
### 🧠 İlgili Kavramlar
- [[concepts/olcum-araclari.md|Ölçüm Araçları (Polarization Measurement)]]
- [[concepts/cocuk-haklari.md|Çocuk Hakları]]
### 🏛 İlgili Kurum/Kişiler
- [[entities/unicef.md|UNICEF]]
