---
type: raw_article
title: 'Deep Learning and Social-Context Approaches for Fake News Detection: A Review
  of Neural, Propagation-Based and Explainable Methods'
description: 'Pune''daki Jaihind College of Engineering''den dört yazarlı, **dört
  sayfalık** bir derleme: sahte haber tespitinde metin sınıflandırmasının ötesine
  geçen üç yaklaşım ailesini tarıyor — (1) **sosyal bağl...'
resource: https://ijsret.com/2026/11/14/deep-learning-and-social-context-approaches-for-fake-news-detection-a-review-of-neural-propagation-based-and-explainable-methods/
tags:
- kurator
- low
timestamp: '2026-11-16T18:19:28Z'
source_file: 2026-11-14_deep-learning-social-context-fake-news-detection-ijsret.json
category: KURATOR
priority: low
roles:
- gap
published: '2026-11-14'
---

# Deep Learning and Social-Context Approaches for Fake News Detection: A Review of Neural, Propagation-Based and Explainable Methods

**Author(s):** Durafe Sejal Dattatray, N. G. Rokade, M. C. Kolse, S. K. Said — Yapay Zekâ ve Veri Bilimi Bölümü, Jaihind College of Engineering, Pune (Hindistan)

**Published:** 2026-11-14

**Source:** [https://ijsret.com/2026/11/14/deep-learning-and-social-context-approaches-for-fake-news-detection-a-review-of-neural-propagation-based-and-explainable-methods/](https://ijsret.com/2026/11/14/deep-learning-and-social-context-approaches-for-fake-news-detection-a-review-of-neural-propagation-based-and-explainable-methods/)

## Summary

Pune'daki Jaihind College of Engineering'den dört yazarlı, **dört sayfalık** bir derleme: sahte haber tespitinde metin sınıflandırmasının ötesine geçen üç yaklaşım ailesini tarıyor — (1) **sosyal bağlam** (kaynak güvenilirliği, kullanıcı davranışı, yorumlar), (2) **yayılım (propagation) tabanlı** modeller (haberin nasıl yayıldığını çizge olarak modelleyen geometrik derin öğrenme), (3) **açıklanabilir** modeller (kullanıcı yorumlarını ve makale cümlelerini dikkat mekanizmasıyla eşleştirip 'neden sahte' sorusunu yanıtlayanlar). Taradığı literatür alanın kanonik referansları: Castillo (Twitter'da güvenilirlik), Ma (RNN ile söylenti yanıtı akışları), Ruchansky'nin **CSI** hibrit modeli, Shu'nun **dEFEND** dikkat modeli, Monti'nin yayılım çizgelerinde geometrik derin öğrenmesi, Rashkin'in dilbilimsel analizi, Zellers'ın **Grover**'ı (üretici modelin hem sahte haber üretip hem tespit edebilmesi) ve Nakamura'nın **Fakeddit** çok kipli veri seti. Ardından **beş katmanlı bir mimari** öneriyor: toplama → içerik kodlama (transformer + görüntü kodlayıcı + SVM/random forest taban çizgisi) → sosyal kodlama (kullanıcı güvenilirliği + yorum gömmeleri + paylaşım kaskadının GNN ile kodlanması) → birleştirme/sınıflandırma (dikkat ağırlıklı füzyon) → **açıklama ve eylem** (etkili cümle/yorumların vurgulanması, doğrulayıcıya bayrak, kullanıcıya uyarı etiketi). Füzyon basit bir ağırlıklı toplam olarak veriliyor: h = α_c·c + α_u·u + α_g·g, ŷ = σ(Wh+b). Tez: 'ne söyleniyor + kim söylüyor + nasıl yayılıyor' birlikte kullanıldığında tespit hem daha doğru hem daha güvenilir.

## Key Points

- Künye: IJSRET Cilt 12, Sayı 5 (Eyl-Oct 2026), ISSN 2395-566X, **4 sayfa**; Zenodo DOI 10.5281/zenodo.24220335 (CC BY 4.0, dosya: JCOEAIDSTS_ijsret_V12_issue5_131.pdf, 468 KB); yazarlar Jaihind College of Engineering (Pune) Yapay Zekâ ve Veri Bilimi Bölümü'nden.
- ⚠️ **Kalite uyarısı (kaydın en önemli kısmı):** IJSRET APC'li (yayın ücreti), çok geniş kapsamlı ve disiplin ayrımı yapmayan bir mühendislik dergisi; bu metin **hakemli araştırma makalesi değil, dört sayfalık bir öğrenci/öğretim üyesi derlemesi**. Deney, veri seti, ölçüm yok — hiçbir tablo kendi sonucunu raporlamıyor; Tablo I-II-III tamamen başka çalışmaların özeti ve kavramsal karşılaştırma. Bu kayıt **kanıt olarak değil, ancak kavram haritası olarak** kullanılmalı.
- Taradığı kanonik literatür (gerçek ve doğrulanabilir): Castillo vd. (Twitter güvenilirliği, mesaj+kullanıcı+yayılım özellikleri), Ma vd. (RNN ile söylenti yanıt akışları), Ruchansky vd. **CSI** (metin + etkileşim zaman serisi + kullanıcı karakteristikleri), Shu vd. **dEFEND** (makale cümleleri + yorumlar üzerinde ortak dikkat, açıklanabilirlik), Monti vd. (yayılım çizgelerinde geometrik derin öğrenme; sahte/gerçek haber yayılımının ayrıştığı ve yayından saatler içinde tespit edilebildiği iddiası), Rashkin vd. (güvenilmez haberin dilbilimsel işaretleri), Zellers vd. **Grover** (nöral üretici ikna edici sahte makale üretebiliyor ama aynı model iyi tespit ediyor), Nakamura vd. **Fakeddit** (metin+görüntü çok kipli veri seti); ayrıca Vosoughi vd. (yanlış haberin daha hızlı/yaygın yayılması) ve Potthast vd. (üslup, hiper-partizanı ana akımdan ayırıyor ama sahteyi gerçekten ayırmıyor).
- Önerilen mimari (5 katman): (1) toplama (izinli API'ler), (2) içerik kodlama (transformer + görüntü kodlayıcı; hızlı ön skor için SVM/random forest), (3) sosyal kodlama (kullanıcı güvenilirliği, yorum gömmeleri, paylaşım kaskadı → GNN), (4) füzyon/sınıflandırma (dikkat ağırlıklı; h = α_c·c + α_u·u + α_g·g, ŷ = σ(Wh+b); kayıp: cross-entropy; metrik: F1 + sabit zaman noktalarında erken tespit doğruluğu), (5) açıklama ve eylem (etkili cümle/yorum vurgulama, doğrulayıcıya bayrak, kullanıcıya uyarı etiketi + doğrulanmış kaynak bağlantısı).
- Belirlenen boşluklar (yazarların listesi): yayılım tabanlı yöntemler haberin yayılması için **zamana ihtiyaç duyduğu için tespiti geciktiriyor**; platform kısıtları nedeniyle **sosyal bağlam verisine erişim zorlaşıyor**; bir platform/dilde eğitilen modeller diğerlerinde çöküyor; **botlarla etkileşim manipüle edilerek** sosyal-bağlam dedektörleri yanıltılabiliyor; sıradan kullanıcının anlayacağı **açıklamalar hâlâ nadir**.
- Açık sorunlar tablosu (Tablo III) ve öneriler: geç tespit → içerik-önce yaklaşım + erken sinyallerle iyileştirme; veri erişimi → ortaklıklar, mahremiyet koruyan API'ler; platform kayması → alan uyarlaması, çok dilli modeller; bot manipülasyonu → bot tespiti, dayanıklı toplama; açıklanabilirlik → kanıt vurgulama + fact-check bağlantısı.
- Bildirilen 'gelecek işler': ilk birkaç paylaşımla erken tespit, **Hint dilleri için çok dilli modeller**, AI üretimi metin/görüntü tespiti, platformlar ile doğrulama kuruluşlarını bağlayan işbirlikçi sistemler.
- Sınırlılık: hakem süreci şeffaf değil, dergi kalitesi düşük; metin 4 sayfa olduğu için her yaklaşım 2-3 cümleyle geçiştirilmiş; önerilen mimari **hiç uygulanmamış ve test edilmemiş**; formülasyon (basit ağırlıklı toplam) literatürdeki füzyon yöntemlerine göre ilkel; kaynakça 13 madde ve güncel LLM tabanlı tespit literatürünü (2024-2026) kapsamıyor.

## Turkey Context

Bu metnin Türkiye için değeri, **kanıt değil yapı** düzeyinde: beş katmanlı mimarisi (içerik + kullanıcı + yayılım + açıklama) Türkiye'deki dezenformasyon izleme tartışmasına tercüme edilebilir bir şablon veriyor. Türkiye'de mevcut doğrulama pratiği ağırlıklı olarak **içerik katmanında** çalışıyor (Teyit, Doğruluk Payı, EDMO Türkiye ayağı): iddia → kaynak → karar. Kullanıcı katmanı (hesap güvenilirliği, koordinasyon tespiti) ve özellikle **yayılım katmanı** (kaskad çizgesi) sistematik olarak kullanılmıyor; oysa Türkiye'de koordineli kampanya örüntüleri (aynı metnin kısaltılmış varyantlarıyla onlarca hesaptan paylaşılması) tam olarak bu katmanın konusu. İkincisi: metnin 'platform verisine erişim giderek zorlaşıyor' tespiti Türkiye'de fazlasıyla geçerli — X API'nin ücretli hale gelmesi ve Meta'nın CrowdTangle'ı kapatması sonrası Türkiye'deki araştırmacılar için veri erişimi fiilen daraldı; yani mimarinin 1. katmanı (toplama) Türkiye'de en kırılgan halka. Üçüncüsü: 'açıklanabilirlik' katmanı Türkiye için hukuki bir zorunluluk haline gelebilir — bir içeriğin 'sahte' olarak işaretlenmesi idari yaptırıma bağlandığında, kararın gerekçesi (hangi cümle, hangi yorum, hangi kaskad) savunulabilir olmak zorunda. Uyarı: bu kaynak **düşük prestijli, APC'li bir dergide dört sayfalık derleme**; bir yazıda 'araştırmalar gösteriyor ki' diye atıf yapılmamalı, en fazla 'şu mimari şablonu öneriliyor' denebilir. Kanonik referanslar (Castillo, CSI, dEFEND, Grover, Fakeddit) doğrudan ve daha güvenilir kaynaklardan alınmalı.

## 🏷 Retorik Roller

- 🔍 **Araştırma Boşluğu**
