---
type: raw_article
title: Digital Twins Validated With 37 RCTs
description: Raj Chetty, Jamie Fogel, Lawrence Katz, Kadeem Noray, Sonya Porter ve
  James Reisinger'in çalışması, program değerlendirmesinin kurucu varsayımını büyük
  veri çağında yeniden test ediyor. Kurucu varsayı...
resource: https://opportunityinsights.org/wp-content/uploads/2026/09/DigitalTwins_FullPaper.pdf
tags:
- akademik
- genel
- high
timestamp: '2026-11-03T19:57:29Z'
source_file: 2026-11-03_chetty-digital-twins-and-jpal-qualitative.json
category: AKADEMİK ÖZEL; GENEL
priority: high
roles:
- result
- method
published: 2026-11
---

# Digital Twins Validated With 37 RCTs

**Author(s):** Raj Chetty; Jamie Fogel; Lawrence F. Katz; Kadeem Noray; Sonya Porter; James Reisinger

**Published:** 2026-11

**Source:** [https://opportunityinsights.org/wp-content/uploads/2026/09/DigitalTwins_FullPaper.pdf](https://opportunityinsights.org/wp-content/uploads/2026/09/DigitalTwins_FullPaper.pdf)

**Proje sayfası:** [opportunityinsights.org/paper/digital-twins/](https://opportunityinsights.org/paper/digital-twins/) — ek materyaller: [Non-technical Summary](https://opportunityinsights.org/wp-content/uploads/2026/09/DigitalTwins_NontechnicalSummary.pdf) (teknik olmayan özet) ve [Slides](https://opportunityinsights.org/wp-content/uploads/2026/09/DigitalTwins_Slides.pdf) (sunum). Her ikisi de 3 Kasım 2026'da 200 ile doğrulandı. Duyuru tweet'i: [@OppInsights, 3 Kasım 2026](https://x.com/OppInsights/status/2117623301400846483) — "Validated against 37 workforce-training RCTs / Closely matches experimental estimates / Faster, lower-cost evaluation across cohorts".

## Summary

Raj Chetty, Jamie Fogel, Lawrence Katz, Kadeem Noray, Sonya Porter ve James Reisinger'in çalışması, program değerlendirmesinin kurucu varsayımını büyük veri çağında yeniden test ediyor. Kurucu varsayım şuydu: gözlemsel tahminler (programa katılanlarla katılmayanların karşılaştırılması) deneysel sonuçlardan ciddi biçimde sapar; bu yüzden 'güvenilirlik devrimi' RCT'leri altın standart ilan etti. Ama RCT pahalı ve nadir — ABD'de faaliyet gösteren yaklaşık 5.000 iş gücü eğitim programının **%1'inden azı** randomize edilmiş. Yazarlar, 1999-2025 arasında 18 yaş ve üstü **327 milyon Amerikalının** anonim gelir vergisi kayıtlarını, **105.216 program katılımcısının** eğitim kayıtlarıyla birleştiriyor; katılımcıların program olmasaydı ne kazanacağını (counterfactual) önceki iş geçmişi, demografi ve ikamet yeri verisiyle makine öğrenmesi modelleyerek tahmin ediyor. Sonra iki farklı yola sapıyorlar: (1) tahminlerin yansız olup olmadığını test etmek yerine, **37 RCT** kullanarak yanlılığın dağılımını tahmin ediyorlar — çünkü tek bir RCT bile kendi içinde gürültülü, dolayısıyla 'tek deneme = gerçek' varsayımı yanlış. (2) Machine learning tahminleri RCT tahminlerine çok yakın çıkıyor; RMSE, RCT'lerin kendi RMSE'sine **eşdeğer** ve gerçek tedavi etkilerinin standart sapmasının **üçte biri** kadar. Yazarlar bu sonucu 'deneysel olarak doğrulanmış dijital ikiz' (experimentally validated digital twin) diye adlandırıyor: katılmayanlar arasından öyle karşılaştırma grupları buluyorlar ki, öngörülen sonuçları rastgele atamanınkine eşdeğer counterfactual sağlıyor. Yöntem, önceki çalışmalarda kullanılan parametrik tahmincilere göre RMSE'yi **%60 azaltıyor** — nedeni daha büyük örneklem ve daha zengin kovaryatların daha esnek, yüksek boyutlu counterfactual modellerine izin vermesi. Deneysel örneklemin dışına (daha fazla şehir ve kayıt yılı) uygulandığında tedavi etkilerinin mekân ve zaman içinde, aynı program içinde bile ciddi biçimde değiştiği görülüyor. En büyük kazançlar, katılımcıları **hedef sektörde işe yerleştiren** programlarda; bu etkiler katılımcılar ilk işlerinden ayrıldıktan sonra da sürüyor — yani etki bir işe değil, bir kariyer merdivenine yerleşmeye bağlı.

## Key Points

- Künye: Raj Chetty, Jamie Fogel, Lawrence F. Katz (Harvard & Opportunity Insights), Kadeem Noray (Harvard Business School), Sonya Porter (U.S. Census Bureau), James Reisinger (Meta; çalışma sırasında Opportunity Insights'ta). Başlık: 'Experimentally Validated Digital Twins: Evaluating Workforce Training Programs in the Age of Big Data', Kasım 2026, 55 sayfa PDF, opportunityinsights.org üzerinden açık erişim. DOI yok, hakem değerlendirmesinden geçmemiş çalışma raporu. Sayfa kısıtlaması notu: yalnızca yazarların görüşleri, Census Bureau görüşü değil; 14 ayrı CBDRB onay numarası listelenmiş.
- Veri: (1) iş gücü eğitim programı kayıtları — 105.216 katılımcı; (2) 1999-2025 arasında 18 yaşını aşmış 327 milyon kişiyi kapsayan anonim gelir vergisi (W-2) kayıtları. Karşılaştırma grubu, program katılımcısı olmayan tüm nüfustan, aynı program-şehir-kayıt yılı hücresi (cell) düzeyinde kuruluyor.
- Yöntem: double/debiased machine learning (DML, Chernozhukov ve ark. 2018). İki model — sonuç (earnings) modeli ve programa katılım propensity score modeli — aynı kovaryat vektörüyle (önceki kazanç geçmişi, sektör göstergeleri, demografi, ikamet Census tract özellikleri) tahmin ediliyor; 5 katlı çapraz uyum (cross-fitting) ile her gözlem kendi modelinde yer almıyor. Approach, LaLonde (1986) geleneğinden farklı: orada amaç unconfoundedness varsayımını test etmekti, burada amaç yanlılığın büyüklüğünü ve dağılımını kestirmek.
- Doğrulama: 37 randomize deneme (MDRC ve Economic Mobility Corporation verileri; Year Up United, Per Scholas, Project QUEST programları). Sonuç: ML tahminleri RCT tahminlerine yakın; RMSE RCT'lerin kendi RMSE'sine eşdeğer, gerçek tedavi etkilerinin standart sapmasının üçte biri. Parametrik tahmincilere göre RMSE'de %60 azalma. Yazarların tanımı: RMSE'si RCT'lerinkine eşit veya daha küçük olan gözlemsel tahminci = 'deneysel olarak doğrulanmış dijital ikiz'.
- Deneysel örneklem dışına genişletme: daha fazla şehir ve kayıt yılı eklendiğinde tedavi etkileri mekân ve zaman içinde — aynı program içinde bile — belirgin biçimde değişiyor. Bu, 'program etkisi tek bir sayıdır' varsayımını çürütüyor: aynı programın farklı şubelerinde farklı sonuçlar var.
- Mekanizma: en büyük kazançlar katılımcıları hedef sektörde işe yerleştiren programlarda. Year Up United'ın 271 program-şehir-kayıt yılı hücresinde, hedef işe yerleşme oranı ile DML kazanç etkisi arasındaki ilişki β̂Z = 121 (16) dolar/puan yüzdesi olarak raporlanıyor. Etkiler katılımcı ilk işinden ayrıldıktan sonra da sürüyor → sektörel programların etkisi 'iş garantisi' değil, kariyer merdivenine erişim.
- Politika çerçevesi: ABD'de ~5.000 iş gücü eğitim programının %1'inden azı randomize değerlendirilmiş; yazarlar dijital ikiz yaklaşımını 'ölçeklenebilir program değerlendirmesi' olarak sunuyor — her program için RCT kurmak yerine, idari veriyle counterfactual kurup mevcut RCT'lerle kalibre etmek.
- Şeffaflık ve çıkar ilişkisi: Raj Chetty, bu makalede geliştirilen yöntemlerle eğitim programlarına yatırım yapan **Opportunity Capital** kuruluşunu yönetiyor — yani yazar, yöntemin ticari uygulamasının başındaki kişi. Metin bunu dipnotta açıkça belirtiyor. Ayrıca metnin düzenlenmesinde ve düzeltmesinde yapay zekâ kullanıldığı beyan ediliyor. Fon: Carnegie, Chan Zuckerberg Initiative, Gates, Overdeck, Samvid, Walton aileleri vakıfları.
- Sınırlılık: hakem değerlendirmesi yok; ABD vergi idari verisine ve Census Bureau'nun özel erişim düzenine bağlı — yöntem başka ülkelerde ancak benzer idari veri altyapısı varsa tekrarlanabilir. Ayrıca doğrulama, iş gücü eğitimi programlarıyla sınırlı; başka politika alanlarına genellenebilirliği test edilmemiş.

## Turkey Context

Türkiye için bu makale hem bir yöntem transferi hem bir uyarı. Birincisi, altyapı sorusu: yöntemin çekirdeği, tüm nüfusu kapsayan idari kazanç verisi. Türkiye'de bu veri SGK hizmet dökümü + Gelir İdaresi kayıtları + TÜİK eşleştirmesiyle teorik olarak var, ama araştırmacı erişimi neredeyse imkânsız ve KVKK rejimi bu tür birleştirmeleri fiilen kapatıyor. Yani 'dijital ikiz' Türkiye'de bugün kurulamaz — kurulması için TÜİK/SGK içinde güvenli araştırma ortamı (secure research environment) ve akredite araştırmacı statüsü gerekiyor. Bu, tek bir makalenin değil, bir kurumsal yatırımın konusu. İkincisi, doğrudan uygulanabilir bulgu: hedef sektöre yerleştirme, kazanç artışının ana mekanizması (β̂Z = 121 dolar/puan). Türkiye'de İŞKUR'un kurs programları büyük ölçüde sertifika ve genel beceri odaklı; 'kursu bitiren kaç kişi hedef sektörde işe girdi' sorusu sistematik olarak izlenmiyor. Bu tek gösterge (target-sector placement rate) Türkiye'de kurs bazında toplanabilir ve İŞKUR'un program tasarımını değiştirebilir — idari veri eşleştirmesi gerektirmez, kurs sonrası 6. ay işe yerleşme takibi yeter. Üçüncüsü, yöntemsel ders: deneysel örneklemin dışına çıkıldığında etkilerin aynı program içinde bile mekâna ve yıla göre değişmesi, Türkiye'de 'program etkisi' tartışmaları için kritik. Türkiye'de bir programın 'etkili' olduğu genellikle tek bir ilde yapılan tek bir değerlendirmeyle ilan ediliyor; aynı programın Şanlıurfa ile İzmir'de farklı sonuç vermesi beklenmeli ve raporlanmalı. Dördüncüsü, etik/çıkar: Chetty'nin yöntemi ticarileştiren Opportunity Capital'in başında olması, 'bilimsel yöntem + yatırım fonu' birleşiminin şeffaflık sorusunu gündeme getiriyor; Türkiye'de benzer bir yapı (ör. bir üniversite merkezinin yöntemini özel sektöre satması) kurulursa, çıkar beyanı standardı en baştan tanımlanmalı. Beşincisi, fırsat: aynı mantığın Türkiye versiyonu için gereken asgari koşul, bir programın katılımcı listesi + benzer profilli katılmayanların idari kazanç verisi. Bu, milli eğitimde kurs/etüt merkezleri veya belediye meslek edindirme kursları düzeyinde pilot olarak mümkün olabilir — ama önce veri erişimi, sonra yöntem.

## 🏷 Retorik Roller

- 📊 **Bulgular**
- 🧩 **Yöntem**

---

## 🔗 İlgili Bağlantılar
### 🧠 İlgili Kavramlar
- [[concepts/dijital-ikizler.md|Dijital İkizler (Program Değerlendirmede)]] — bu çalışma, ikiz yaklaşımının RCT tabanlı (ampirik) doğrulama kanadını temsil ediyor.
- [[concepts/arastirma-sonucu-tahminleme.md|Araştırma Sonucu Tahminleme]] — counterfactual tahmini ve tahmin doğruluğunun puanlanması; dijital ikiz, tahminin program değerlendirmesine uygulanmış biçimi.
- [[concepts/siyaset-bilimi-metodolojisi.md|Siyaset Bilimi Metodolojisi]] — idari veri + DML temelli araştırma yöntemleri için ölçeklenebilir bir değerlendirme şablonu.
### 🏛 İlgili Kurum/Kişiler
- [[entities/opportunity-insights.md|Opportunity Insights]]
