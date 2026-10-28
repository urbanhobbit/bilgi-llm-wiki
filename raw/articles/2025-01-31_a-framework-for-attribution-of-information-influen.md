---
type: raw_article
title: A Framework for Attribution of Information Influence Operations (ADAC.io /
  Lund University PDR)
description: 'Bilgi etkisi operasyonlarının (IIO/FIMI) **faillerine atfedilmesi**
  için yapılandırılmış bir yöntem öneren teknik rapor. Temel argüman: atfetme, "kim
  yaptı" sorusuna verilen serbest bir yanıt değil; h...'
resource: https://adacio.eu/a-framework-for-attribution-of-information-influence-operations
tags:
- kurator
- akademik
- medium
timestamp: '2026-10-28T10:50:50Z'
source_file: 2026-10-28_batch-user-links-4.json
category: KURATOR; AKADEMİK ÖZEL
priority: medium
roles:
- method
- policy
published: '2025-01-31'
---

# A Framework for Attribution of Information Influence Operations (ADAC.io / Lund University PDR)

**Author(s):** Björn Palmertz; Elsa Isaksson; James Pamment (Lund University Psychological Defence Research Institute)

**Published:** 2025-01-31

**Source:** [https://adacio.eu/a-framework-for-attribution-of-information-influence-operations](https://adacio.eu/a-framework-for-attribution-of-information-influence-operations)

## Summary

Bilgi etkisi operasyonlarının (IIO/FIMI) **faillerine atfedilmesi** için yapılandırılmış bir yöntem öneren teknik rapor. Temel argüman: atfetme, "kim yaptı" sorusuna verilen serbest bir yanıt değil; hangi kanıtın sayıldığını, kanıtın hangi kaynaktan geldiğini ve araştırmacının sonucuna ne kadar güvendiğini açıkça beyan eden bir **usul** meselesi. Rapor, ilk kez NATO StratCom COE ve Hybrid CoE ile yayımlanan çerçevenin güncellenmiş sürümü; ADAC.io projesinin (Horizon Europe, Lund Üniversitesi Psikolojik Savunma Araştırma Enstitüsü koordinatörlüğünde, 7 ortak, Şubat 2024–Ocak 2027) atfetme iş akışının omurgası.

Çerçevenin yapısı üç kanıt kategorisi + bir değerlendirme katmanı: **teknik** kanıt (IP'ler, altyapı, dijital izler), **davranışsal** kanıt (TTP'ler, koordinasyon örüntüleri, hesap ağlarının işleyişi) ve **bağlamsal** kanıt (anlatılar, hedef kitleler, siyasal etki); bunların tamamı **hukuki ve etik** bir değerlendirmeyle birlikte okunuyor (orantılılık, mahremiyet, jeopolitik yansımalar). İkinci eksen **veriye erişim**: açık kaynak (herkese açık, OSINT), tescilli/proprietary (platform arka ucu, özel istihbarat firmaları) ve sınıflandırılmış (SIGINT/HUMINT). Yazarların vurgusu, hiçbir aktörün üçüne birden tam erişimi olmadığı; bu yüzden kamuya açık atfetmelerin çoğunlukla açık kaynak + tescilli veriye dayandığı ve bunun da iddiaların gücünü sınırladığı.

Siber atfetmeden farkı net: siber saldırıda teknik izler (IP, altyapı, kod) belirleyiciyken, IIO'da davranış ve bağlam öne çıkıyor; operasyon kamu alanında yürüdüğü için hukuki sınırlar müphem, anlatının kaynağı ile yayıcısı iç içe geçiyor ve çoğu zaman yalnızca **ülke düzeyinde** atfetme mümkün oluyor. Bu belirsizliği yönetmek için rapor güven düzeylerinin standart dilini öneriyor: Birleşik Krallık "Probability Yardstick" (ör. %25-35 "unlikely", %80-90 "highly likely"), STIX/OASIS ölçekleri, Admiralty ve DNI skalaları — hangi ölçek seçilirse seçilsin kategorilerin **tanımlı** olması şart. Kritik uyarı: aynı ağ içindeki hesapların atfetme güveni eşit değildir; resmî bir devlet hesabını hükümete atfetmek kolayken, kendini sıradan vatandaş gibi gösteren hesap için aynı güveni kurmak çoğu zaman mümkün değildir.

Rapor ayrıca Microsoft, Google, EUvsDisinfo/East StratCom, IISS, Debunk.org, DFRLab, Bellingcat, SCIII ve PGI gibi kurumların yöntemlerini karşılaştırıyor; Doppelgänger, LVU ve Paperwall vakalarıyla çerçeveyi uygulamalı olarak gösteriyor.

## Key Points

- Atfetme = usul: hangi kanıt sayılır, hangi kaynaktan gelir, güven düzeyi nedir
- Üç kanıt kategorisi (teknik/davranışsal/bağlamsal) + hukuki-etik katman
- Veri erişimi üç kademe: açık kaynak, tescilli, sınıflandırılmış — hiçbir aktörde tamamı yok
- IIO'da çoğu zaman yalnızca ülke düzeyinde atfetme mümkün; hesap düzeyinde güven değişir
- Güven dili standartları: UK Probability Yardstick, STIX/OASIS, Admiralty, DNI

## Turkey Context

Türkiye'de dezenformasyon ve bilgi operasyonları tartışmasının en zayıf halkası **atfetme usulü**. Kamu kurumlarının açıklamaları çoğu zaman "kim yaptı" iddiasını kanıt kategorisi, veri kaynağı ve güven düzeyi belirtmeden kuruyor; bağımsız araştırmacılar ise OSINT ile çalıştıkları için aynı iddiaları test edemiyor. Bu rapor, iki taraf arasındaki dili ortaklaştırmak için hazır bir şablon sunuyor: bir iddia yayımlandığında hangi kategoride kanıt sunduğu, kaynağın açık/tescilli/sınıflandırılmış olduğu ve güven düzeyinin ne olduğu yazılmalı. Türkiye'deki dezenformasyon izleme raporlaması için bu, "kaynak: güvenlik birimleri" türü atıfların yerine geçebilecek bir kalite ölçütü.

Üç pratik kullanım alanı var. Birincisi, **KURATOR hattındaki vaka kayıtları**: her dezenformasyon vakasında (ör. seçim dönemi koordineli hesaplar, deprem sonrası yanlış bilgi, göçmen karşıtı kampanyalar) atfetme iddiasının güven düzeyini işaretlemek, retrospektif olarak hangi iddiaların tuttuğunu ölçmeyi mümkün kılar. İkincisi, **kurumsal şeffaflık**: raporun üç kademeli veri erişimi şeması, RTÜK/İletişim Başkanlığı ile platformlar arasındaki veri paylaşımı tartışmasında "hangi veriye kim erişiyor" sorusunu yapılandırılmış biçimde sormayı sağlıyor. Üçüncüsü, **eğitim**: Lund Enstitüsü'nün çerçevesi, Türkiye'deki gazetecilik ve iletişim programlarında doğrulama/atfetme dersleri için kullanılabilir; DISARM çerçevesiyle birlikte okunduğunda taktik taksonomisi ile atfetme usulünü birleştiriyor.

Not: ADAC.io konsorsiyumunda Türkiye'den bir ortak yok (Alliance4Europe, Debunk EU, Dortmund, Cardiff, SWPS, Leiden, Lund). 5 Kasım 2026'daki FIMI Research Cluster kapanış konferansı (Brüksel + çevrimiçi) bu ağı görünür kılıyor; Türkiye'den katılım, hem vaka katkısı hem de yöntem transferi için düşük maliyetli bir giriş noktası.

## 🏷 Retorik Roller

- 🧩 **Yöntem**
- 🏛 **Politika Önerisi**

---

## 🔗 İlgili Bağlantılar
### 🧠 İlgili Kavramlar
- [[concepts/fimi.md|FIMI (Foreign Information Manipulation and Interference)]]
