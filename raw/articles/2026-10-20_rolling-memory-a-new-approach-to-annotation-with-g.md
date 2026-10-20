---
type: raw_article
title: 'Rolling Memory: A New Approach to Annotation with Generative LLMs in Social
  and Political Research'
description: Timoneda ve Vallejo Vera (Chinese Political Science Review, Springer,
  7 Ocak 2026, açık erişim) üretken büyük dil modelleriyle metin kodlama/annotasyon
  literatürüne doğrudan yöntemsel bir katkı sunuyo...
resource: https://link.springer.com/article/10.1007/s41111-025-00327-w
tags:
- akademik
- genel
- high
timestamp: '2026-10-20T12:00:43Z'
source_file: 2026-10-20_batch-user-links-3.json
category: AKADEMİK ÖZEL; GENEL
priority: high
published: 2026-1-7
---

# Rolling Memory: A New Approach to Annotation with Generative LLMs in Social and Political Research

**Author(s):** Joan C. Timoneda; Sebastián Vallejo Vera

**Published:** 2026-1-7

**Source:** [https://link.springer.com/article/10.1007/s41111-025-00327-w](https://link.springer.com/article/10.1007/s41111-025-00327-w)

## Summary

Timoneda ve Vallejo Vera (Chinese Political Science Review, Springer, 7 Ocak 2026, açık erişim) üretken büyük dil modelleriyle metin kodlama/annotasyon literatürüne doğrudan yöntemsel bir katkı sunuyor. Yazarlar, yaygın kullanılan zero-shot ve few-shot yaklaşımlarının modellerin in-context learning kapasitesini yeterince kullanmadığını; buna karşılık annotasyon görevi boyunca modelin hafızasını (memory) korumasına izin vermenin performansı belirgin biçimde artırdığını hatırlatıyor. Kendi önceki çalışmalarındaki (Timoneda vd., 'Memory Is All You Need', arXiv:2503.04874, 2025) hafıza yaklaşımını rafine ederek iki aşamalı (two-run) bir yöntem öneriyorlar: birinci koşuda model görev boyunca ilerledikçe kendi çıktılarından öğreniyor (in-context learning etkisi, performans kademeli olarak yükseliyor); ikinci koşunun başında ise birinci koşunun en bilgilendirici 100 örneği hafızada tutuluyor. Sonuç: ikinci koşuda performans hem yüksek hem de görev boyunca tutarlı hale geliyor; standart hafıza yaklaşımına göre %3,56, zero-shot/few-shot temel çizgisine göre ise %13,26'lık bir iyileşme raporlanıyor. Çalışma, siyaset bilimi ve sosyal bilimlerde LLM destekli kodlamanın (açık uçlu yanıtlar, parti/protesto metinleri, sosyal medya iletileri) maliyet-performans dengesini yeniden kuran, uygulaması kolay bir protokol sunuyor; kod ve etiket setlerinin açık erişimde olması nedeniyle Türkiye'deki araştırma ekipleri için de doğrudan tekrarlanabilir bir şablon niteliğinde.

## Turkey Context

Türkiye'de siyaset bilimi ve sosyal bilimlerde büyük ölçekli metin analizi hâlâ ağırlıklı olarak elle kodlamaya ya da kodlayıcılar arası güvenilirlik (Cohen's kappa, Krippendorff alfa) raporlamasına dayanıyor; TÜBİTAK SOBAG destekli projelerde ve doktora tezlerinde açık uçlu anket sorularının kodlanması araştırma bütçesinin en pahalı kalemlerinden biri. Rolling Memory protokolü, Türkçe metinlerde kodlayıcı-içi tutarlılığı artırırken insan kodlayıcı yükünü azaltmak için doğrudan kullanılabilir; özellikle yüksek hacimli veri setlerinde (TBMM tutanakları, yerel basın arşivleri, X/Twitter gönderileri, saha görüşmesi transkriptleri) iki aşamalı hafıza kurgusu, altın standart (gold standard) olarak elle kodlanmış 100-200 örneğin ardından ölçeklenebilir. Yöntemsel uyarı: hafıza örneklerinin etiket dağılımına göre seçilmesi, sınıf dengesizliği olan Türkiye veri setlerinde (ör. nefret söylemi, protesto katılımı, dindarlık ölçekleri) yanlılık üretebilir; bu nedenle ikinci koşuya aktarılacak 100 örneğin sınıf temsiliyeti açıkça raporlanmalı. KVKK (6698 sayılı Kanun) kapsamında kişisel veri içeren metinlerin bulut tabanlı LLM'lere gönderilmesi, açık rıza ve veri işleme sözleşmesi gerektirir; kurum içi (on-premise) açık ağırlıklı modellerle aynı protokolün uygulanması, Bilgi Üniversitesi gibi kurumlar için uyum açısından tercih edilmelidir. YÖK ve üniversite etik kurullarının, LLM destekli kodlamanın metodoloji bölümünde nasıl raporlanacağına dair ulusal bir rehber geliştirmesi, bu tür çalışmaların yaygınlaşmasıyla birlikte zorunlu hale gelecek; TÜİK mikro veri setleriyle birleştirilen kodlama protokolleri ise karşılaştırmalı araştırma kapasitesini güçlendirebilir.

---

## 🔗 İlgili Bağlantılar
### 🏛 İlgili Kurum/Kişiler
- [[entities/springer.md|Springer]]
