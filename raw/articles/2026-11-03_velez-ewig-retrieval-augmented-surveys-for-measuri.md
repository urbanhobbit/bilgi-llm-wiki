---
type: raw_article
title: 'Velez Ewig: Retrieval-augmented surveys for measuring political representation'
description: 'Yamil Velez ve Alec Ewig''in (Columbia University) *Political Analysis*
  makalesi, klasik "temsil" ölçümünün en bilinen kısıtını hedefliyor: **anket maddeleri
  araştırmacının seçtiği sabit bir konu liste...'
resource: https://www.cambridge.org/core/journals/political-analysis/article/retrievalaugmented-surveys/2D43DFC0765382818BD8D402C905175B
tags:
- kurator
- high
timestamp: '2026-11-06T15:17:09Z'
source_file: 2026-11-06_velez-ewig-retrieval-augmented-surveys.json
category: KURATOR
priority: high
roles:
- result
- method
published: '2026-11-03'
---

# Velez Ewig: Retrieval-augmented surveys for measuring political representation

**Author(s):** Yamil Velez, Alec Ewig (Columbia University)

**Published:** 2026-11-03

**Source:** [https://www.cambridge.org/core/journals/political-analysis/article/retrievalaugmented-surveys/2D43DFC0765382818BD8D402C905175B](https://www.cambridge.org/core/journals/political-analysis/article/retrievalaugmented-surveys/2D43DFC0765382818BD8D402C905175B)

## Summary

Yamil Velez ve Alec Ewig'in (Columbia University) *Political Analysis* makalesi, klasik "temsil" ölçümünün en bilinen kısıtını hedefliyor: **anket maddeleri araştırmacının seçtiği sabit bir konu listesine bağlıdır**, yani seçmenin gerçekten önemsediği ama ankette sorulmamış bir konu "temsil edilmiş" sayılır ya da hiç görünmez.

**Önerilen yöntem — "retrieval-augmented survey" (dört adım):**
1. **Domain korpusu:** Kongre faturaları gibi kurumsal bir metin tabanı, anket maddesine dönüşecek kısa ve nötr özetlere çevriliyor.
2. **Açık uçlu öncelik beyanı:** Katılımcı kendi cümlesiyle en önemsediği tek konuyu yazıyor; ardından kısa bir netleştirme adımında (parafraz seçenekleri) kapsam ve yön onaylanıyor.
3. **Semantik geri getirme:** Gömme (embedding) modeliyle katılımcının önceliğine en yakın **üç "komşu" politika** seçiliyor — kişiye özel anket maddesi üretiliyor.
4. **Yanıt + doğrulama:** Bu kişiye özel maddelere destek ölçülüyor, LLM ile "bu politika kişinin derdini karşılıyor mu" kodlaması yapılıyor ve gündem aşaması (komisyon/Genel Kurul) izleniyor.

**Doğrulama (4 metrik, ABD Kongresi uygulaması):**

| Test | Sonuç |
|---|---|
| **1. Yüz geçerliliği** (n=2.000 ABD yetişkini, Verasight, 11-21 Ekim 2024) | En yakın komşu politika için **%69** "büyük ölçüde/tamamen karşılıyor"; %91 en azından "kısmen"; 2. ve 3. komşu %66 ve %64; **%81** en az bir maddeyi "büyük ölçüde/tamamen" buluyor |
| **2. El kodlaması denetimi** | 213 vaka / 71 katılımcı; Llama 4 Scout (109B) kodlaması insan kodlayıcılarla **%83,6** uyuşuyor (iki ayrı sette %82 ve %87); tek yönlü hata için DSL düzeltmesi |
| **3. Panel kararlılığı** (1.116 → 867, Haziran 2024) | Üç hafta sonra en yüksek destek düzeyini koruma: komşu politika **%82**, uyarlanabilir maddeler %68, CES maddeleri %68; orta nokta üstünde %93 / %84 / %87 |
| **4. Tailored conjoint** (10 ikili) | En büyük AMCE komşu politikada; en yüksek CES maddesinden **3 puan** (p=0,03), en yüksek uyarlanabilir maddeden **6 puan** (p<0,001) yüksek |

**Kongre uygulaması (118. Kongre):** Önceliği beyan edenlerin **%77**'sinin en az bir "karşılayan" faturası var (**gündem kapsanması**) — ama yalnız **%12**'si Genel Kurul'a ulaşmış (**gündem ilerlemesi**). Karşılayan eşleşmelerin **%84**'ü komisyonda duruyor, %1'den azı kanunlaşıyor. DSL ile hata düzeltmesi bu oranları %73 ve %10'a indiriyor.
**Yorum:** Dışlanma (Bachrach-Baratz'in "ikinci yüz") Kongre'de sanıldığı kadar "gündeme hiç girmeme" biçiminde değil — **komisyon aşamasında tıkanma** biçiminde işliyor.

**Alt grup farkları (keşifsel):** Kadınlar erkeklerden +5,8 puan kapsanma / +5,7 puan ilerleme; Cumhuriyetçiler Demokratlardan −5,1 / −3,5 puan; Asyalı Amerikalıların ilerleme oranı beyaz akranlarından **−8,5 puan** (SE 2,3). Yazarlar bunları hipotez olarak sunuyor, kesin sonuç değil.

⚠️ **Sınırlar:** Örneklem **%15'i hiçbir öncelik beyan etmiyor** ("üçüncü yüz" — sessizlik) ve bu grup düşük gelirli, düşük eğitimli, daha az oy kullanan; analiz bu kesim dışında yapılıyor. Alt grup tahminleri keşifsel ve küçük hücreli. Yöntem ABD Kongresi ve İngilizce ile sınırlı; uyarlanabilirlik iddiası (belediye bütçesi, kural koyma, parti programı) henüz test edilmedi.

## Key Points

- Sabit anket maddeleri yerine, her katılımcının kendi beyan ettiği önceliğe en yakın 3 politikayı semantik gömme ile getirip kişiye özel madde üreten yeni anket yöntemi.
- n=2.000 ulusal örneklem (Verasight, Ekim 2024): en yakın politika için %69 'büyük ölçüde/tamamen karşılıyor', %91 en az 'kısmen'; %81 en az birinde tatmin buluyor.
- LLM (Llama 4 Scout) tatmin kodlaması insan kodlamasıyla %83,6 uyuşuyor (213 vaka); DSL ile sistematik hata düzeltiliyor.
- Panel: en yüksek destek düzeyini 3 hafta sonra koruma komşu politikada %82 — CES ve uyarlanabilir maddelerde %68 (tutarlılık üstünlüğü).
- Conjoint: komşu politika, seçmen tercihinde en yüksek etkiye sahip; en iyi CES maddesinden +3 puan (p=0,03), en iyi uyarlanabilir maddeden +6 puan.
- Kongre (118.): gündem kapsanması %77, gündem ilerlemesi %12; DSL düzeltmesiyle %73 / %10.
- Karşılayan faturaların %84'ü komisyonda tıkanıyor, <1% kanunlaşıyor → temsil sorunu 'gündeme girmeme' değil 'komisyon kapısı'.
- Alt gruplar: kadınlar +5,8/+5,7 puan; Cumhuriyetçiler −5,1/−3,5; Asyalı Amerikalılar ilerlemede −8,5 puan (keşifsel).
- Kritik boşluk: katılımcıların %15'i hiçbir öncelik beyan etmiyor; bu grup düşük gelir/eğitim ve daha az oy kullanıyor — 'üçüncü yüz' sessizliği.
- Yöntem modüler: belediye bütçesi, kural koyma, parti programı gibi alanlara taşınabilir (henüz test edilmedi).
- Replikasyon: Harvard Dataverse doi 10.7910/DVN/V5TUYQ.

## Turkey Context

Türkiye'de temsil ölçümü neredeyse tamamen **sabit madde** mantığıyla yapılıyor: seçmen-milletvekili görüş uyumu, parti programı-seçmen önceliği karşılaştırması, ara sıra "hangi sorun önemli" anketleri. Bu makalenin açtığı kapı Türkiye için iki kat değerli:

(1) **TBMM verisiyle uygulanabilirlik:** Kanun teklifleri, komisyon gündemleri ve tutanaklar açık; yani "kapsanma" (seçmenin önceliğiyle örtüşen bir teklif var mı) ve "ilerleme" (komisyondan çıktı mı, Genel Kurul'a geldi mi) ölçülebilir. Türkiye'de bilinen ampirik boşluk tam burada: hangi seçmen önceliğinin gündeme girdiği, hangisinin komisyonda öldüğü sistematik olarak ölçülmüyor. Makalenin bulgusu (tıkanma komisyonda) Türkiye için güçlü bir test edilebilir hipotez — özellikle muhalefet partilerinin tekliflerinde.

(2) **Metodolojik uyarı:** Türkiye'de anketler "hangi parti" ekseninde kurulduğu için seçmenin *kendi* önceliği hiç sorulmuyor; sorulduğunda da (%15'lik "beyan etmeyen" grup gibi) sessizlik sınıfsal — düşük eğitimli, düşük gelirli seçmen dışarıda kalıyor. Türkiye'de bu oran muhtemelen daha yüksek; "siyasetten uzaklaşma" ölçüsü olarak okunmalı, veri kaybı olarak değil.

(3) **Uyarlama sınırı:** Yöntem LLM + gömme modeli gerektiriyor; Türkçe metin gömme kalitesi, kanun teklifi özetlerinin nötrlüğü ve komisyon verisinin dijitalleşme düzeyi kritik. Türkçe için "politika korpusu + gömme" hattı kurulmadan bu ölçüm tekrarlanamaz — ama kurulursa, Türkiye'de temsil literatüründe gerçek bir yenilik olur.

## 🏷 Retorik Roller

- 📊 **Bulgular**
- 🧩 **Yöntem**

---

## 🔗 İlgili Bağlantılar
### 🧠 İlgili Kavramlar
- [[concepts/siyasal-temsil.md|Siyasal Temsil ve Tepkisellik]] — makalenin ölçtüğü şey: gündem kapsanması ve gündem ilerlemesi olarak siyasal temsil.
- [[concepts/olcum-araclari.md|Ölçüm Araçları (Polarization Measurement)]] — kişiye özel madde üretimi ve LLM tabanlı tatmin kodlaması bir ölçüm tasarımı sorunu.
- [[concepts/siyaset-bilimi-metodolojisi.md|Siyaset Bilimi Metodolojisi]] — araştırma yöntemleri açısından sabit maddeli anket kısıtını aşan yeni bir saha tasarımı.
- [[concepts/yapay-zeka-demokrasi.md|Yapay Zeka ve Demokrasi]] — yapay zeka demokrasi ilişkisinde LLM'lerin ölçüm altyapısı olarak kullanımı.
### 🏛 İlgili Kurum/Kişiler
- [[entities/cambridge-university-press.md|Cambridge University Press]]
