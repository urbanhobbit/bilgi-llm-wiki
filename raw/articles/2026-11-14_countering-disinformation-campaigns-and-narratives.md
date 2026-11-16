---
type: raw_article
title: 'Countering Disinformation Campaigns and Narratives: An Innovative Graph-Based
  Solution for Malicious Content Analysis, Detection, and Visualization'
description: Kozik, Pawlicki ve Choraś (Bydgoszcz Teknik Üniversitesi + IDEAS Araştırma
  Enstitüsü), dezenformasyon kampanyalarına karşı **operatör odaklı, çizge (graph)
  tabanlı bir izleme ve görselleştirme** çözüm...
resource: https://dl.acm.org/doi/10.1145/3843205.3845624
tags:
- kurator
- akademik
- high
timestamp: '2026-11-16T05:26:42Z'
source_file: 2026-11-16_countering-disinformation-graph-based-solution.json
category: KURATOR; AKADEMİK ÖZEL
priority: high
roles:
- method
- result
published: '2026-11-14'
---

# Countering Disinformation Campaigns and Narratives: An Innovative Graph-Based Solution for Malicious Content Analysis, Detection, and Visualization

**Author(s):** Rafał Kozik, Marek Pawlicki, Michał Choraś (Bydgoszcz University of Science and Technology + IDEAS Research Institute, Polonya)

**Published:** 2026-11-14

**Source:** [https://dl.acm.org/doi/10.1145/3843205.3845624](https://dl.acm.org/doi/10.1145/3843205.3845624)

## Summary

Kozik, Pawlicki ve Choraś (Bydgoszcz Teknik Üniversitesi + IDEAS Araştırma Enstitüsü), dezenformasyon kampanyalarına karşı **operatör odaklı, çizge (graph) tabanlı bir izleme ve görselleştirme** çözümü öneriyor. Motivasyon: Romanya, Moldova ve ABD'de seçim öncesi/sırasında görülen iç ve dış kaynaklı dezenformasyon kampanyaları. Amaç, insan operatörlerin dijital uzaydaki **bilgi kümelerini (clusters)** anlayabilmesini sağlayacak, veriyi çizge biçiminde izleyip görselleştiren bir araç sunmak; odak siyasi dezenformasyon ve toplumsal güvenlik. Yani makale yeni bir doğruluk (fact-checking) modeli değil, **durumsal farkındalık arayüzü** öneriyor: dağınık içerikleri düğüm/kenar yapısına çevirip kampanya örüntülerini (aynı anlatının kümelenmesi, yayılım topolojisi) insan karar vericinin gözünde okunur kılmak. Yazarların önceki işleri (SemKGraph gibi hibrit anlamsal+sözlüksel çizge yaklaşımları) bu hattın parçası; bu bildiri onların 3D-Sec 2026 sürümü.

## Key Points

- Künye: 3D-Sec '26 (2nd ACM Workshop on Deepfake, Deception, and Disinformation Security), ACM SIGSAC CCS 2026 ile birlikte, The Hague, 15-19 Kasım 2026. Bildiri ss. 61-69, Crossref yayın tarihi 14 Kasım 2026 (Unpaywall OA tarihi 13 Ekim 2026 — ön baskı/online-first farkı). DOI 10.1145/3843205.3845624. CC BY 4.0. 14 kaynak. Üç yazar: Rafał Kozik (ORCID 0000-0001-7122-3306), Marek Pawlicki (ORCID 0000-0001-5881-6406), Michał Choraś.
- Özet (Semantic Scholar'dan birebir): toplumlar iç/dış dezenformasyon kampanyalarının örneklerini gördü (Romanya, Moldova, ABD seçimleri); yazarlar toplumu dezenformasyona karşı korumaya yardımcı **AI tabanlı** bir çözüm öneriyor; hedef, **çizge formunda** veri izleyip görselleştirerek insan operatörlerin dijital uzaydaki güncel bilgi kümelerini anlamasını sağlamak; odak siyasi ve toplumsal güvenlik dezenformasyonu.
- Katkı tipi: yeni bir sınıflandırma modeli değil, uçtan uca **araç + arayüz** (monitoring → graph construction → visualization). Değerlendirme iddiası özette NICEL olarak verilmiyor (F1, veri seti, karşılaştırma yok) — bu, bildirinin en zayıf halkası ve tam metin okunmadan doğrulanamaz.
- Bağlam: aynı ekibin SemKGraph çalışması (Springer, Eylül 2026) anlamsal + sözlüksel öznitelikleri çizge bilgisiyle birleştiriyor; bu bildiri o hattın operatör arayüzü/görselleştirme katmanı olarak okunabilir.
- Sınırlılık: TAM METİN OKUNAMADI. dl.acm.org tüm yollarda Cloudflare 'Just a moment' ile kapalı (doi, /pdf, /epdf → 403; r.jina.ai proxy de CAPTCHA sayfası döndü). Unpaywall/OpenAlex/Semantic Scholar tek OA konum olarak yayıncı sayfasını gösteriyor, repository kopyası yok; Google Scholar'da da açık PDF bulunamadı. Bu yüzden mimari detayları, kullanılan model, veri seti, ölçüm sonuçları ve ekran görüntüleri görülmedi — özet dışında iddia üretilmedi.

## Turkey Context

Bu bildiri Türkiye hattı için **araç/hat karşılaştırması** açısından değerli, bulgu açısından değil. Birincisi: KURATOR hattı zaten bir bilgi çizgesi üretiyor (OKF wiki: kavram-varlık-kaynak düğümleri, xref kenarları). Kozik vd.'nin önerisi bunun ters yönünden bakıyor — araştırmacı/akademisyen için değil, **nöbet tutan operatör** için: hangi anlatı kümeleniyor, hangi hesaplar aynı içeriği taşıyor, yayılım nerede yoğunlaşıyor. Türkiye'de dezenformasyon izleme (Teyit, Doğruluk Payı,EDMO Türkiye ayağı) ağırlıklı olarak **iddia bazlı doğrulama** yapıyor; kampanya/küme düzeyinde görselleştirme katmanı zayıf. Bu bildiri o boşluğun nasıl doldurulabileceğine dair mühendislik referansı. İkincisi: Türkiye'de seçim dönemlerinde (özellikle 2023 ve 2024 yerel seçimleri) koordineli anlatı yayılımı belgelenmiş bir olgu; çizge tabanlı küme tespiti, tek tek yalan haber doğrulamaktan daha verimli bir izleme ekseni olabilir. Üçüncüsü: eleştirel nokta — özet hiçbir nicel değerlendirme vermiyor ve tam metin erişilemedi; bu yüzden 'şu aracı kuralım' demek için erken. Ayrıca siyasi dezenformasyonu 'kötü niyetli içerik' olarak çerçeveleyen araçların en büyük riski, muhalif ama meşru konuşmayı kampanya olarak etiketlemek; Türkiye gibi hukuki güvencelerin zayıf olduğu bir ortamda bu risk daha yüksek. Araç seçilirse şeffaflık (küme kararının gerekçesi) ve itiraz mekanizması şart.

## 🏷 Retorik Roller

- 🧩 **Yöntem**
- 📊 **Bulgular**

---

## 🔗 İlgili Bağlantılar
### 🧠 İlgili Kavramlar
- [[concepts/dezenformasyon.md|Dezenformasyon]]
- [[concepts/media-literacy-fact-checking.md|Media Literacy and Fact-Checking (Medya Okuryazarlığı ve Doğrulama)]]
### 🏛 İlgili Kurum/Kişiler
- [[entities/dl-acm-org.md|Dl Acm Org]]
