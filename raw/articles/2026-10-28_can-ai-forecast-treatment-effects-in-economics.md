---
type: raw_article
title: Can AI Forecast Treatment Effects in Economics?
description: 'Eva Vivalt, **LLM''lerin ekonomi alanındaki tedavi etkilerini ön-kayıt
  belgelerinden tahmin edip edemediğini** test ediyor. Tasarım titiz: AEA RCT Registry
  ve Open Science Framework''te ön-kayıtlı çalış...'
resource: https://arxiv.org/abs/2610.38883
tags:
- akademik
- genel
- high
timestamp: '2026-11-03T17:31:55Z'
source_file: 2026-11-03_prediction-league-and-vivalt-ai-forecasting.json
category: AKADEMİK ÖZEL; GENEL
priority: high
roles:
- result
- method
published: '2026-10-28'
---

# Can AI Forecast Treatment Effects in Economics?

**Author(s):** Eva Vivalt

**Published:** 2026-10-28

**Source:** [https://arxiv.org/abs/2610.38883](https://arxiv.org/abs/2610.38883)

## Summary

Eva Vivalt, **LLM'lerin ekonomi alanındaki tedavi etkilerini ön-kayıt belgelerinden tahmin edip edemediğini** test ediyor. Tasarım titiz: AEA RCT Registry ve Open Science Framework'te ön-kayıtlı çalışmalar arasından, sonuçları **ilk kez 2026'da** kamuya açıklanmış olanlar seçiliyor; tahmin istemleri ise eğitim/knowledge cut-off tarihi bu yayınlardan **önce** olan modellere yöneltiliyor — yani modelin cevabı 'görmüş olması' mümkün değil. İlk adımda LLM'ler ön-kayıt veya ön-analiz planlarından tahmin soruları çıkarıyor; bu sorular tahmin edilen tedavi etkilerini hedefliyor. Soruların hepsi sonraki makalede çözülmüyor, ama çözülenler tahmin doğruluğunu değerlendirmek için kullanılıyor: 39 makaleden **889 tedavi etkisi** (tarama sonrası 33 makaleden 673 etki) üzerinde tahmin alınıyor. Tahminler ham birimlerde isteniyor, ancak analizde standartlaştırılabilenler kullanılıyor (böylece makaleler arası karşılaştırma mümkün oluyor). Sonuçlar: en iyi model için **medyan mutlak tahmin hatası 0,054 SD**, ortalama mutlak hata 0,093 SD, MSE 0,0218. Yapay zekâ tahminleri, 'etki sıfırdır' ve 'etki o dönemdeki diğer makalelerin ortalama etkisidir' biçimindeki iki temel referans tahminden **belirgin biçimde daha iyi** performans gösteriyor. Vivalt'ın sonucu: tahminlerin politika ve araştırma kararlarını bilgilendirmede değerli olabileceği yönünde ciddi bir alan var — ve bu çalışma, The Agency Fund'ın açtığı prediction league'in bilimsel dayanağı olarak yarışma sayfasında doğrudan atıf alıyor.

## Key Points

- Künye: Eva Vivalt, 'Can Artificial Intelligence Forecast Treatment Effects in Economics?', arXiv:2610.38883 [econ.GN], 28 Ekim 2026, v1. Tek yazarlı. arXiv kaydında journal_ref ve dergi DOI'si yok; yayım DOI'si yalnızca arXiv DOI'si (10.48550/arXiv.2610.38883). Ön baskı, hakem değerlendirmesinden geçmemiş.
- Tasarım: veri kaynağı AEA RCT Registry + OSF ön-kayıtları; kapsam, sonuçları ilk kez 2026'da kamuya açıklanan çalışmalar. Sızıntıyı önlemek için modellerin training/knowledge cut-off tarihi ilgili yayın setinden ÖNCE olacak biçimde seçilmiş — bu, 'AI tahmini' literatüründe sık görülen veri sızıntısı eleştirisine doğrudan yanıt.
- Örneklem: 39 makaleden 889 tedavi etkisi; tarama sonrası 33 makaleden 673 etki. Tahminler ham birimlerde istenmiş, analizde standartlaştırılabilen alt kümeyle makaleler arası karşılaştırma yapılmış.
- Sonuçlar: en iyi modelde medyan mutlak hata 0,054 SD; ortalama mutlak hata 0,093 SD; MSE 0,0218. Referanslar: sıfır etki tahmini ve o dönemdeki diğer makalelerin ortalama etkisi — her ikisinden de belirgin biçimde iyi.
- Yöntemsel katkı: LLM'lerin ön-kayıt/ön-analiz planı metninden tahmin sorularını çıkarma adımı ayrı bir aşama olarak kurulmuş; yani 'soru üretimi' ile 'etki tahmini' birbirinden ayrılıyor. Bu ayrım, insan uzmanların soru yazmasına bağlı kalan önceki tahmin platformlarından (SSPP) farklı bir ölçekleme yolu açıyor.
- Yorum: Yazar, sonucu ihtiyatlı çerçeveliyor — 'tahminlerin politika ve araştırmayı bilgilendirmede değerli olabileceği yönünde ciddi bir alan var'. Metinde, yayımlanmış literatürle eğitilen modellerin yayın yanlılığını devraldığı ve doğruluk-interpretability ödünleşimi gibi sınırlılıklar da tartışılıyor (bu sınırlılıklar yarışma sayfasında da tekrarlanıyor).
- İlişki: Bu ön baskı, The Agency Fund'ın 3 Kasım 2026'da duyurduğu Prediction League'in dayanak çalışmalarından biri olarak yarışma sayfasında atıfla yer alıyor; Vivalt aynı zamanda duyuruyu yapan hesap. Yarışma, bu türden tahminleri 2027'de sonuçlanacak RCT'ler üzerinde takım yarışmasına dönüştürüyor.
- Sınırlılık: Ön baskı; hakem değerlendirmesi yok. Özet düzeyinde okundu (arXiv API), tam metin indirilmedi — tablo düzeyinde model karşılaştırmaları, hangi modellerin denendiği listesi ve standardizasyon yönteminin ayrıntısı bu kayıtta doğrulanmadı.

## Turkey Context

Türkiye açısından bu çalışma iki şeyi birden söylüyor. Birincisi, imkân: Türkiye'de politika değerlendirmesi pahalı ve seyrek — bir eğitim müfredatı reformunun, bir sosyal yardım kademelendirmesinin ya da bir mülteci entegrasyon programının etkisini ölçmek için RCT kurmak yıllar alıyor. Vivalt'ın gösterdiği şey, ön-kayıt metni varsa etkinin makul bir doğrulukla önceden tahmin edilebildiği (medyan 0,054 SD hata). Bu, Türkiye'de 'önce pilot, sonra ölçüm' döngüsünü hızlandırabilir: tasarım aşamasında tahmin alınır, sonuç açıklandığında tahmin puanlanır. İkincisi, uyarı ve asıl araştırma boşluğu: bu modeller ağırlıklı olarak İngilizce yayımlanmış literatürle eğitiliyor; Türkiye'deki programların etki büyüklükleri, kurumsal bağlam ve uygulama kalitesi farklı olduğu için tahminler sistematik olarak kayabilir. Türkiye'de yapılacak gerçek katkı, aynı yöntemi Türkiye'de sonuçlanmış bir dizi program üzerinde test etmek: 'ABD literatürüyle eğitilmiş model, Türkiye'deki etkileri ne kadar iyi tahmin ediyor?' Bu soru, uluslararası literatürde de henüz cevaplanmamış durumda ve Türkiye'deki araştırmacılar için düşük maliyetli, yüksek görünürlüklü bir çalışma. Üçüncüsü, yöntemsel ders: çalışmanın en değerli tarafı sonuç değil, **tasarım** — knowledge cut-off tarihini yayın tarihinden önceye sabitleyerek veri sızıntısını kapatması. Türkiye'de yapay zekâ ile ilgili ampirik çalışmalarda bu tür bir sızıntı kontrolü neredeyse hiç raporlanmıyor; basit ama belirleyici bir standart. Dördüncüsü, kurumsal: TÜBİTAK ve kalkınma ajansları destekli program değerlendirmelerinde ön-kayıt zorunlu değil; ön-kayıt olmadan bu tür bir tahmin altyapısı da kurulamıyor (tahmin edilecek sorular önceden yazılı olmalı). Yani teknik önce değil, kurumsal pratik önce geliyor: ön-kayıt zorunluluğu, tahmin temelli politika öğrenmesinin ön koşulu.

## 🏷 Retorik Roller

- 📊 **Bulgular**
- 🧩 **Yöntem**

---

## 🔗 İlgili Bağlantılar
### 🏛 İlgili Kurum/Kişiler
- [[entities/arxiv-org.md|Arxiv Org]]
