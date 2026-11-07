---
type: raw_article
title: 'Macke Gedon Wahl: Teaching AI to build scientific models'
description: 'Anthropic Science Blog''da **konuk yazı**: Jakob Macke, Daniel Gedon
  ve Stefan Wahl (ELLIS Institute Tübingen / Tübingen Üniversitesi; Anthropic "AI
  for Science" hibesi sahipleri), bilimsel modellemeni...'
resource: https://www.anthropic.com/research/teaching-ai-to-build-scientific-models
tags:
- kurator
- medium
timestamp: '2026-11-07T02:52:04Z'
source_file: 2026-11-06_macke-gedon-wahl-teaching-ai-scientific-models.json
category: KURATOR
priority: medium
published: '2026-11-06'
---

# Macke Gedon Wahl: Teaching AI to build scientific models

**Author(s):** Jakob Macke, Daniel Gedon, Stefan Wahl (ELLIS Institute Tübingen / University of Tübingen) — Anthropic Science Blog konuk yazısı

**Published:** 2026-11-06

**Source:** [https://www.anthropic.com/research/teaching-ai-to-build-scientific-models](https://www.anthropic.com/research/teaching-ai-to-build-scientific-models)

## Summary

Anthropic Science Blog'da **konuk yazı**: Jakob Macke, Daniel Gedon ve Stefan Wahl (ELLIS Institute Tübingen / Tübingen Üniversitesi; Anthropic "AI for Science" hibesi sahipleri), bilimsel modellemenin üç adımının (kurma, veriye oturtma, yorumlama) AI tarafından nasıl devralındığını anlatıyor.

**Anlatının omurgası — Hodgkin-Huxley (1951):** Cambridge'in bilgisayarı altı ay arızalı olduğu için Huxley denklemleri **el krankalı mekanik hesap makinesiyle üç haftada** çözdü. Denklemin bir parçası eğitimli bir tahmindi: eğriyi veriye oturtmak için bir değişkeni **dördüncü kuvvete** çıkarmaları gerekti, nedenini bilmiyorlardı. Yıllar sonra potasyum kanalının yapısı çözüldüğünde gerçekten **dört özdeş parça** olduğu görüldü — yani model, hiç uydurulmadığı bir şeyi de öngörmüştü. Yazının tezi burada: "dördüncü kuvvetin işe yaradığını bilmek yetmez; **daha basit modelin işe yaramadığını** bilmek gerekir."

**1) Sınırlama (constrain) — en olgun alan.** Klasik Bayesçi çıkarım her olası parametre kümesi için olasılık hesabı gerektirir; karmaşık modellerde hesaplanamaz. **Simülasyona dayalı çıkarım (SBI)** tersine çalışır: rastgele parametrelerle modeli çalıştır, çıktıyı kaydet, bunu **~100.000 kez** (Hodgkin-Huxley ölçeğinde) veya **milyonlarca kez** (büyük modellerde) tekrarla, sonra sinir ağını "çıktı → olası parametreler" eşlemesini öğrenecek şekilde eğit. Eğitimden sonra yeni veri için çıkarım **saniyeler** sürer.
*Uygulamalar:* nötron yıldızı çarpışmasının gökyüzündeki konumu (teleskopları sinyal hâlâ algılanabilirken yönlendirecek hızda), kozmoloji, yapısal biyoloji, jeofizik, nöron modelleri.

**2) Kurma (build) — LLM ajanı modeli yazıyor.** Veri + doğal dil tanımı verildiğinde ajan aday model kodunu yazar, çalıştırır, parametreleri oturtur, çıktıyı gerçek veriyle karşılaştırır ve revize eder (bazen denklemin biçimini değiştirerek); döngü veriye yeterince uyana kadar sürer. Son iki yılda böyle birkaç sistem çıktı.
**Kritik ilke:** tek "en iyi" model değil, **model dağılımı** üretilmeli. Ajan her adayı veri desteğine göre ağırlıklandırır, veriye uymak için çok esneklik isteyenlere daha az kredi verir, zayıflar elenir, kalanların varyasyonları denenir. Hayatta kalan tüm modeller **aynı özelliği** paylaşıyorsa veri onu destekliyor; **ayrışıyorlarsa** kanıtın ince olduğu yer orasıdır ve sonraki deney oraya yönelmeli.

**3) Yorumlama (interpret) — en zor adım.** Modelin veriye uyumu ölçülebilir, "anlayış" ölçülemez; bir AI'a "anlamayı" hedef vermek mümkün değil. İki öneri: (a) sistemi **bozduğunda** ne olacağını doğru tahmin ediyor mu; (b) çıktıları insan bilimcinin anlamasını gerçekten kolaylaştırıyor mu — örnek: kuantum deneyi tasarlayan sistem, tek bir düzenek değil, **bir deney ailesi üreten program** yazıyor; fizikçi tasarım ilkesini programdan okuyor.

**Ölçek:** AI işi devraldıkça "insanın yazabileceği kadar küçük model" sınırı kalkıyor. Meyve sineği beyni **100.000+ nöron** (tam bağlantı haritası çıkarıldı; figürde 124.635 hücre), insan beyni on milyarlarca. Bu ölçekte **tek doğru model yok** ("all models are wrong but some are useful" — Box); soru "hangi model doğru" değil, **"veriyle uyumlu tüm modellerin paylaştığı özellikler ne"**. Emsaller: iklim biliminin çoklu-model yayılımı, LHC'nin "hangi teori versiyonları elendi" haritası.

⚠️ **Yazarların kendi uyarısı:** bu sistemler çoğunlukla **bilinen modelleri yeniden keşfetmekte** test edildi; cevabı bilinmeyen problemlerde kanıt seyrek. Daha yeni LLM'ler araştırma görevlerinde daha iyi, ama bu bir eğilim iddiası.
⚠️ **Yayın türü:** şirket bloğunda **konuk yazı** — hakemsiz; yazarlar kendi araştırma gündemlerini tanıtıyor. Dipnotlardaki makaleler (Romera-Paredes vd. 2024; Shojaee vd. 2025; Wahl vd. 2026 vb.) okunmadı.

## Key Points

- Anthropic Science Blog konuk yazısı (06.11.2026): Macke, Gedon & Wahl — ELLIS Tübingen; 'AI for Science' hibesi.
- Modellemenin üç adımı: kurma (build), veriye oturtma (constrain), yorumlama (interpret) — AI üçünde de devrede.
- En olgun adım sınırlama: SBI rastgele parametrelerle ~100.000 (büyük modellerde milyonlarca) simülasyon çalıştırıp sinir ağı eğitiyor; çıkarım sonrası saniyeler.
- SBI uygulamaları: nötron yıldızı çarpışması konumlandırma (teleskop yönlendirecek hızda), kozmoloji, yapısal biyoloji, jeofizik, nöron modelleri.
- Kurma adımında LLM ajanı model kodunu yazıp çalıştırıp revize ediyor; tek model değil model dağılımı üretmeli.
- Dağılım ilkesi: ortak özellik = veri desteği; ayrışma = kanıtın ince olduğu yer; fazla esneklik isteyen model daha az kredi alır.
- Yorumlama en zor: 'anlayış' ölçülemiyor; öneriler — bozma testi ve insan bilimcinin anlamasını kolaylaştırma (deney ailesi üreten program).
- Ölçek: meyve sineği beyni 100.000+ nöron, insan beyni on milyarlarca; bu ölçekte tek doğru model yok, paylaşılan özellikler sorulur.
- Yazarların uyarısı: sistemler çoğunlukla bilinen modelleri yeniden keşfetmekte test edildi; bilinmeyen cevaplarda kanıt seyrek.
- Yayın türü: şirket blogunda konuk yazı, hakemsiz; dipnotlardaki makaleler doğrulanmadı.

## Turkey Context

Doğrudan Türkiye verisi yok; aktarım **yöntem ve kurumsal** düzeyde.

**1) Türkiye'de seçim/kamuoyu modellemesi tam bu ilkenin tersini yapıyor.** SBI'nin ve "model dağılımı" fikrinin sosyal bilim karşılığı şu: tek bir spesifikasyonun nokta tahmini yerine, **spesifikasyon dağılımı** raporlamak. Türkiye'de yayınlanan oy oranı tahminleri neredeyse her zaman tek model + tek sayı olarak dolaşıma giriyor; belirsizlik "±2 puan"a indirgeniyor, oysa asıl belirsizlik **model biçiminde**. Anket ağırlıklandırması, olası-seçmen tanımı, kararsızların dağıtımı ve sandık düzeyi eğilimler değiştiğinde aynı veriden çok farklı sonuçlar çıkıyor — bunlar "güven aralığı" değil, **model uzayı**.

**2) Bilim politikası açısından:** yazı, AI'ın bilimsel üretimdeki rolünü "hız" değil "**süreç**" üzerinden çerçeveliyor — anlayış, neyin işe yaramadığını bilmekten geliyor. Türkiye'de araştırma değerlendirme sistemi (akademik teşvik, dergi sayısı) tam tersini ödüllendiriyor: tek sonuç, tek makale, hızlı çıktı. AI araçlarının yaygınlaşması bu eğilimi hızlandırma riski taşıyor — üretilen model sayısı artar, **hangi alternatifin elendiği** kaydedilmezse anlayış artmaz.

**3) Kurumsal şeffaflık:** SBI'nin ürettiği dağılım, "hangi parametre veriyle gerçekten sabitlenmiş" sorusunu cevaplıyor. Türkiye'de kamu kurumlarının yayımladığı modeller (enflasyon tahminleri, seçim projeksiyonları, deprem senaryoları) için aynı standart uygulanabilir: tek tahmin değil, **kabul edilebilir model kümesi** yayımlamak. Bu, tahmin hatası tartışmasını "kurum yanıldı mı" düzeyinden "hangi varsayım tutmadı" düzeyine taşır.

---

## 🔗 İlgili Bağlantılar
### 🧠 İlgili Kavramlar
- [[concepts/yapay-zeka-ile-bilimsel-modelleme.md|Yapay Zeka ile Bilimsel Modelleme]] — yazının kurduğu çerçeve: kurma / sınırlama / yorumlama, SBI ve "tek model değil model dağılımı" ilkesi.
- [[concepts/siyaset-bilimi-metodolojisi.md|Siyaset Bilimi Metodolojisi]] — aynı mantığın sosyal bilim karşılığı: çoklu spesifikasyon ve model belirsizliği.
- [[concepts/yapay-zeka-yonetisimi.md|Yapay Zeka Yönetişimi]] — AI'ın bilimsel üretimdeki rolü, şirket bloklarının araştırma gündemini şekillendirmesi.
### 🏛 İlgili Kurum/Kişiler
- [[entities/anthropic.md|Anthropic]] — yayıncı; "AI for Science" hibesiyle dış araştırmacılara konuk yazı alanı açıyor (hakemsiz).
