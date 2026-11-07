---
type: concept
title: 'Yapay Zeka ile Bilimsel Modelleme (AI for Scientific Modeling)'
description: 'Model kurma, veriye oturtma ve yorumlama işlerinin AI ajanlarına devri: simülasyona dayalı çıkarım (SBI), model uzayında arama, "tek model değil model dağılımı" ilkesi ve yorumlanabilirlik sınırı.'
tags:
- kavram
- yapay-zeka
- bilim
- metodoloji
- simulasyon
timestamp: '2026-11-06T19:35:00Z'
created: '2026-11-06'
updated: '2026-11-06'
sources:
- raw/articles/2026-11-06_macke-gedon-wahl-teaching-ai-to-build-scientific-models.md
related:
- concepts/siyaset-bilimi-metodolojisi.md
- concepts/yapay-zeka-yonetisimi.md
- concepts/bilim-ve-siyaset.md
confidence: medium
---

# Yapay Zeka ile Bilimsel Modelleme

## Üç adım

Bilimsel modelleme üç işten oluşur ve her biri artık kısmen AI'a devredilebiliyor:

| Adım | Ne yapılır | AI'ın durumu |
|---|---|---|
| **Kurma** (build) | Modelin parçalarına ve denklem biçimine karar vermek | LLM ajanı aday model kodunu yazıp çalıştırıyor, veriye uydurup revize ediyor |
| **Sınırlama** (constrain) | Serbest parametreleri veriye oturtmak | En olgun alan: Bayesçi çıkarım + **SBI** |
| **Yorumlama** (interpret) | Modelin gerçek sistem hakkında ne söylediğini çıkarmak | En zor adım; "anlama" ölçülemiyor |

## Simülasyona dayalı çıkarım (SBI)

Klasik Bayesçi çıkarım, her olası parametre kümesi için verinin olasılığını hesaplamayı gerektirir; karmaşık modellerde bu hesaplanamaz. **SBI** tersine çevirir: rastgele parametrelerle modeli çalıştır, çıktıyı kaydet, bunu **~100.000 kez** (Hodgkin-Huxley ölçeğinde), büyük modellerde **milyonlarca kez** tekrarla; sonra bir sinir ağını "çıktı → olası parametre aralığı" eşlemesini öğrenecek şekilde eğit. Eğitim bittikten sonra yeni veri için çıkarım **saniyeler** içinde yapılır.

Kullanım alanları: nötron yıldızı çarpışmalarının gökyüzündeki konumu (teleskopları sinyal hâlâ algılanabilirken yönlendirecek hızda), kozmoloji, yapısal biyoloji, jeofizik, nöron modelleri.

**Neden önemli:** tek bir "en iyi uyum" yerine **dağılım** verir → hangi parametrelerin veri tarafından gerçekten sınırlandığını, nerede birden çok açıklamanın eşit derecede geçerli olduğunu ve **bir sonraki deneyin nereye yapılması gerektiğini** gösterir.

## "Tek model değil, model dağılımı"

Aynı ilke bir üst düzeyde de geçerli: veriye uyan tek bir model yoktur. Bu yüzden AI ajanı tek bir "kazanan" model değil, **ağırlıklandırılmış bir model dağılımı** üretmeli:

- Tüm hayatta kalan modeller **aynı özelliği** paylaşıyorsa → veri o özelliği destekliyor.
- Modeller **ayrışıyorsa** → kanıtın ince olduğu yer orasıdır; sonraki deney oraya yönelmeli.
- Veriye uymak için çok esneklik gerektiren modeller daha az "kredi" almalı.

## Sınırlar ve uyarılar

- **Yeniden keşif etkisi:** bu sistemler çoğunlukla bilinen modelleri yeniden bulmakta test edildi; **cevabı bilinmeyen** problemlerde kanıt hâlâ seyrek.
- **Anlama ölçülemiyor:** modelin veriye uyumu ölçülebilir, "anlayış" ölçülemez. İki öneri: (a) sistemi bozduğunda ne olacağını doğru tahmin ediyor mu, (b) insan bilimcinin anlamasını gerçekten kolaylaştırıyor mu (ör. tek bir deney düzeneği değil, bir *deney ailesi* üreten program yazdırmak).
- **Ölçek arttıkça anlaşılırlık düşüyor:** insan beyni için "denklemleri okuyup anlamak" mümkün değil; soru "doğru model hangisi" değil, **"veriyle uyumlu tüm modellerin paylaştığı özellikler ne"** olur.

## Sosyal bilimlere aktarım

Aynı mantık sosyal bilimde de işliyor: bir anket modeli, bir oy tahmin modeli veya bir ajan tabanlı simülasyon, tek "en iyi" spesifikasyon yerine **spesifikasyon dağılımı** olarak sunulmalı. İklim biliminin çoklu-model yayılımı ve LHC'nin "hangi teoriler elendi" haritası bu yaklaşımın olgun örnekleri. Sosyal bilimde eksik olan, model dağılımını **sistematik** üretme pratiği — çoğu çalışma tek bir spesifikasyonu raporluyor.

Türkiye'de seçim modellemesi ve kamuoyu simülasyonu tam bu noktada: model belirsizliği (çoklu spesifikasyon) yerine tek nokta tahmini dolaşıma giriyor.

Kayıt: [[raw/articles/2026-11-06_macke-gedon-wahl-teaching-ai-to-build-scientific-models.md|Macke, Gedon & Wahl (2026, Anthropic Science Blog)]]
