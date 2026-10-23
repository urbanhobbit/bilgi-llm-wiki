---
type: raw_article
title: Mapping Economic Theory with AI
description: ETH Zurich AI & Economics Lab'tan Elliott Ash ve Andrea Ciccarone ile
  Sapienza Üniversitesi'nden Sergio Galletta'nın 22 Ekim 2026 tarihli çalışma makalesi
  (çalışma metni, dergi hakemliğinden geçmemiş;...
resource: https://andreaciccarone.github.io/claim_graphs_draft.pdf
tags:
- kurator
- high
timestamp: '2026-10-23T08:29:54Z'
source_file: 2026-10-23_mapping-economic-theory-with-ai.json
category: KURATOR
priority: high
roles:
- gap
- method
- result
- limitation
- policy
published: '2026-10-22'
---

# Mapping Economic Theory with AI

**Author(s):** Elliott Ash, Andrea Ciccarone, Sergio Galletta

**Published:** 2026-10-22

**Source:** [https://andreaciccarone.github.io/claim_graphs_draft.pdf](https://andreaciccarone.github.io/claim_graphs_draft.pdf)

## Summary

ETH Zurich AI & Economics Lab'tan Elliott Ash ve Andrea Ciccarone ile Sapienza Üniversitesi'nden Sergio Galletta'nın 22 Ekim 2026 tarihli çalışma makalesi (çalışma metni, dergi hakemliğinden geçmemiş; tam metin yazarların sitesinde). Soru: ekonomik teori makalelerindeki hataların hangisi gerçekten önemli? AI artık araştırmada hata bulmak için kullanılıyor, ama bulunan hatanın makalenin iktisadi sonuçlarını değiştirip değiştirmediği ayrı bir soru. Yazarlar bunun için 'claim graph' (iddia grafiği) yöntemini geliştiriyor: bir ajan tabanlı AI sistemi her teori makalesini varsayımlar (premises) → ara sonuçlar (lemmas) → teoremler → iktisadi sonuçlar zincirini gösteren bir grafiğe çeviriyor. Grafik, hangi varsayımların birlikte (joint) gerektiğini, hangi türetmelerin alternatif destek sunduğunu ve sonuçların hangi ortak girdilere dayandığını kaydediyor; her ifade kaynak pasaja bağlanıyor. Ağırlıklandırma yazarların kendi hiyerarşisine göre: başlık iddiaları (headline) ağırlık 1, ana sonuçlar 0,5. İki ayrı örneklem kullanılıyor: (a) 1995 sonrası dört önde gelen iktisat dergisinden rastgele 190 teori makalesi — argüman yapısını betimlemek ve merkezi varsayımların inandırıcılığını ölçmek için; (b) yayımlanmış düzeltmesi (corrigendum/erratum) olan 100 makale — hata bulmayı belgeliyor. Her iki örneklemde de grafikler orijinal makaleden üretiliyor ve yayımlanmış düzeltme ajanlardan saklanıyor. İki ölçüt tanımlanıyor: F (fragility/kırılganlık) = hatanın şüpheye düşürdüğü ana sonuçların ağırlıklı payı; Q (severity/ciddiyet) = en küçük geçerli onarımdan sonra kaybedilen iktisadi içeriğin ağırlıklı payı. Bulgular: rastgele örneklemde ortalama grafik 28,6 ifade ve 16,9 türetme içeriyor, başlık iddiasına giden en uzun zincir ortalama 5,3 türetme adımı. En etkili başlangıç girdisi (bir varsayım, tanım ya da ithal sonuç) kaldırıldığında ağırlıklı başlık ve ana iddiaların ortalama %91'i desteklenmez hale geliyor — yani tek bir hataya maruz kalma çok yüksek. Buna karşın 190 makalenin yalnızca 23'ü (%12) herhangi bir alternatif türetme kaydediyor. Yatıştırıcı bulgu: en çok yük taşıyan varsayımlar daha az inandırıcı değil, aksine biraz daha inandırıcı (ayrı bir GPT-5.6 geçişi her varsayımı makalenin sorusuna göre 1–10 inandırıcılık ölçeğinde puanlıyor). Hata keşfi benchmarkı: 100 makaledeki 168 belgelenmiş hatanın 79'u tam (%47), kısmi eşleşmelerle 115'i (%69) yakalanıyor; ancak sistem bu örneklemde toplam 473 hata buluyor ve çoğu yayımlanmış düzeltmedekinden daha önemsiz — eşleşmeyen bulguların 'yanlış' sayılamayacağı, dolayısıyla eşleşme oranının kesinlik (precision) göstergesi olmadığı yazarlarca açıkça belirtiliyor. Asıl sonuç onarım sonrası: düzeltmeyle eşleşen bulgularda medyan kırılganlık %28 iken onarım sonrası medyan ciddiyet yalnızca %4; rastgele 190 makalelik örneklemde medyan kırılganlık %14, medyan ciddiyet %2. Yani hatalar bir makalenin argümanının büyük kısmını çökertebiliyor ama en küçük geçerli onarımdan sonra başlık sonuçları nadiren değişiyor. İki bilinen örnek: Rothschild–Stiglitz (1970) F=45, Q=0 (kanıt onarılınca sonuçlar korunuyor, Leshno vd. 1997 düzeltmesine benzer); Brown (1983) F=100, Q=75 (tanımlama sonuçları onarımdan sağ çıkmıyor, Benkard–Berry 2006'daki dağılım-koruyucu rotasyon). Yapısal ilişkiler: tek bir varsayım üzerindeki azami yük arttıkça ciddi hata (onarım sonrası %10+ kayıp) olasılığı artıyor; 'sonuç verimi' (her maddi girdi başına biçimsel sonuç sayısı) arttıkça azalıyor; türetme derinliğinin net bir ilişkisi yok. Bu, hakemlerin kaynaklarını nereye ayıracağına dair doğrudan bir önceliklendirme ölçütü öneriyor: bir varsayımı kaldırınca makalenin büyük kısmı düşüyorsa orayı incele. Yazarlar ayrıca theorize.ink adlı etkileşimli platformu ve claim graph veri setini açıyor: okuyucu bir sonucu varsayımlara kadar geri izleyebiliyor, her ifade kaynak pasaja bağlı. Araştırma yöntemleri ve bilimsel iletişim açısından katkı şu: 'hata var mı' sorusunu 'hata iktisadi içeriği değiştiriyor mu' sorusundan ayırıyor ve hakemlik/dergi politikası tartışmasına denetlenebilir bir ara ölçüt veriyor.

## Key Points

- Yöntem: ajan tabanlı AI, her teori makalesini varsayım→lemma→teorem→iktisadi sonuç zincirini gösteren 'claim graph'a çeviriyor; ifadeler kaynak pasaja bağlı, ağırlıklar başlık=1 / ana sonuç=0,5.
- Ölçütler: F (kırılganlık) = hatanın şüpheye düşürdüğü ağırlıklı ana sonuç payı; Q (ciddiyet) = en küçük geçerli onarımdan sonra kaybedilen iktisadi içerik payı.
- Rastgele 190 teori makalesi (1995+, dört önde gelen dergi): en etkili başlangıç girdisi kaldırılınca ağırlıklı başlık+ana iddiaların ortalama %91'i desteklenmez kalıyor; yalnızca 23 makale alternatif türetme kaydediyor.
- Yapı: ortalama grafik 28,6 ifade / 16,9 türetme; başlık iddiasına en uzun zincir ortalama 5,3 adım. En yük taşıyan varsayımlar daha az değil, biraz daha inandırıcı.
- Benchmark: 100 düzeltme makalesindeki 168 hatanın 79'u tam (%47), 115'i kısmi eşleşmeyle (%69) yakalanıyor; sistem toplam 473 hata buluyor, çoğu daha önemsiz — eşleşmeyen bulgu 'yanlış' sayılamaz, eşleşme oranı kesinlik değildir.
- Asıl sonuç: eşleşen bulgularda medyan F %28 / Q %4; rastgele örneklemde medyan F %14 / Q %2 — hatalar argümanın büyük kısmını çökertiyor ama başlık sonuçları onarımdan sonra nadiren değişiyor.
- Örnekler: Rothschild–Stiglitz (1970) F=45 → Q=0; Brown (1983) F=100 → Q=75 (tanımlama sonuçları onarımdan sağ çıkmıyor).
- Yapısal korelasyonlar: azami yük ↑ → ciddi hata olasılığı ↑; sonuç verimi (biçimsel sonuç/maddi girdi) ↑ → ciddi hata olasılığı ↓; türetme derinliği ilişkisiz.
- Çıktı: theorize.ink etkileşimli platformu + claim graph veri seti; her iddia kaynak pasaja bağlı olarak incelenebilir.

## Turkey Context

Türkiye açısından en somut fayda hakemlik kapasitesi: TR Dizin kapsamındaki iktisat dergilerinde ve lisansüstü tezlerin teorik bölümlerinde hakem havuzu dar, teorik makalenin denetimi ise en pahalı iş — claim graph + kırılganlık ölçütü, hakemin 'nereden başlasın' sorusuna cevap veriyor ve tek bir varsayımın ne kadar yük taşıdığını gösteriyor. İkincisi uyarlama sınırı: korpus İngilizce ve dört Top-5 dergisi; Türkçe teorik literatür (kalkınma iktisadı, yapısalcı gelenek, Türkçe yazılmış modelleme metinleri) kapsam dışı ve bu metinlerde ajan performansı büyük olasılıkla daha düşük olacak — pilot uygulama Türkçe makalelerde ayrıca doğrulanmalı. Üçüncüsü ölçek: rapordaki 'tek varsayım kaldırılınca ağırlıklı iddiaların %91'i düşüyor' bulgusu, Türkiye'de sık görülen 'tek denklemli, tek varsayımlı' teorik katkıların denetim açısından ne kadar kırılgan olduğunu göstermesi bakımından da okunabilir; hakem raporlarında 'ana varsayımınızı gerekçelendirin' talebi veriye dayandırılabilir. Dördüncüsü yönetişim: araç 'AI hakem' değil 'AI denetçi' olarak konumlanıyor — Türkiye'de dergi/ULAKBİM düzeyinde AI kullanım beyanı olmadığı için bu ayrım politik olarak da kullanışlı: denetim çıktısı hakemin kararını değiştirmiyor, sadece nereye bakacağını gösteriyor. Beşincisi teşvik rejimi: akademik teşvik ve yükseltme yayın sayısına duyarlı olduğu için hata bulmayı ödüllendirmiyor; bu tür araçların kurumsal talep görmesi için dergi editörlerinin (TR Dizin kriterlerinde 'hata düzeltme politikası' başlığı altında) talebi gerekir. Asgari pilot: 20 Türkçe teorik makale, claim graph + kırılganlık, mevcut hakem raporlarıyla körlemesine karşılaştırma.

## 🏷 Retorik Roller

- 🔍 **Araştırma Boşluğu**
- 🧩 **Yöntem**
- 📊 **Bulgular**
- ⚠️ **Sınırlılıklar**
- 🏛 **Politika Önerisi**

---

## 🔗 İlgili Bağlantılar
### 🧠 İlgili Kavramlar
- [[concepts/bilimsel-iletisim.md|Bilimsel İletişim (Science Communication)]]
- [[concepts/siyaset-bilimi-metodolojisi.md|Siyaset Bilimi Metodolojisi]]
