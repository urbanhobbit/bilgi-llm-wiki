---
type: raw_article
title: A Practitioner's Guide to Using Large Language Models and Generative AI in
  Economic History
description: NBER Working Paper 35374, Haziran 2026 (JEL C55, C8, N0) - Andreas Ferrara
  (University of Pittsburgh, Department of Economics & NBER). LLM'lerin el yazmasi
  defterler, metin, gorsel ve ses kayitlari gi...
resource: https://x.com/i/status/2086887773894824432
tags:
- akademik
- genel
- high
timestamp: '2026-08-11T06:00:45Z'
source_file: 2026-08-10_categorized.json
category: AKADEMİK ÖZEL; GENEL
priority: high
---

# A Practitioner's Guide to Using Large Language Models and Generative AI in Economic History

**Source:** [https://x.com/i/status/2086887773894824432](https://x.com/i/status/2086887773894824432)

## Summary

NBER Working Paper 35374, Haziran 2026 (JEL C55, C8, N0) - Andreas Ferrara (University of Pittsburgh, Department of Economics & NBER). LLM'lerin el yazmasi defterler, metin, gorsel ve ses kayitlari gibi eskiden guclu veri bilimi becerisi gerektiren tarihsel veri kaynaklarina erisim engelini dusurdugu tezinden yola cikan kapsamli bir uygulayici rehberi. Calisma, arastirma fikrini calisan kod ve veriye donusturen adim-adim bir workflow sunuyor ve LLM ile etkilesimin dort ana yolunu tanimliyor: (1) tarayici sohbet penceresi, (2) editor-entegre asistanlar, (3) arastirmacinin bilgisayarinda dosyalarla calisabilen agentic coding araclari (Claude Code, OpenAI Codex, Gemini CLI), (4) API cagrilari. Rehber, uygulayicinin karsilastigi kararlari sirayla isliyor: LLM dogru arac mi, veri bir LLM'e gonderilebilir mi, model secimi, prompt yazma, context limitlerini yonetme, maliyet kontrolu ve son olarak LLM-uretimi olcumlerin regresyon ortamlarinda dogrulanmasi, yeniden uretilebilirligi, dokumantasyonu ve duzeltilmesi. Riskler vurgulaniyor: LLM'ler referans uydurabilir (hallucination), kulturel onyargilar uretebilir, cografya hakkinda zayif akil yurutur, gecerli nedensel tasarim uretemez (Kiciman et al. 2024); prompt veya model degisikligi bir regresyon katsayisinin boyutunu hatta ISARETINI degistirebilir (Ludwig et al. 2026; Yin et al. 2026) ve standart hatalar bu yanliligi isaretlemeyebilir (Battaglia et al. 2025). Ayrica entelektuel tembellik ve dusunce cesitliligi kaybi riski: arastirmacilar ayni sorulari ayni araclara sorup ayni cevaplari benimserse alan heterojenligini kaybeder. Dort calisilmis ornek replikasyon dosyalariyla sunuluyor: (1) tablolardaki duyguların sınıflandırılması, (2) isimsiz nüfus sayımı kayıtlarının eşleştirilmesi (1900-1910 arası 10.000 Connecticut erkeği; LLM'ler %43-62 eşleşme oranı vs basit join %4,3), (3) 1882 Çin Dışlama Yasası çevresinde gazete belirginliği ve duygu ölçümü (524.458 sayfa -> ön işleme ile 11.011 sayfa), (4) FDR'nin savaş konuşmalarında duygusal sunum puanlaması. Replikasyon dosyalari: https://doi.org/10.3886/E249897V2 (ICPSR). Ekonomi tarihinde LLM tabanli veri cikarma, harmonizasyon ve siniflandirma literaturunun genis bir incelemesi ile birlikte; GGT (Schmitt et al. 2026) GenAI metodoloji tartismasina tarihsel veri uygulamalariyla tamamlayici bir katki.

## Key Points

- NBER Working Paper 35374, Haziran 2026; DOI: 10.3386/w35374; yazar: Andreas Ferrara (Pittsburgh & NBER)
- LLM ile 4 etkilesim yolu: chat penceresi, IDE asistanlari, agentic coding araclari (Claude Code/Codex/Gemini CLI), API
- Adim-adim workflow: fikir -> calisan kod/veri; prompt yazma, context limitleri, maliyet kontrolu, dogrulama
- Riskler: hallucinated referanslar, kulturel onyargi, zayif cografya muhakemesi, gecersiz nedensel tasarim; prompt/model degisimi katsayi boyutunu/isaretini degistirebilir
- LLM-uretimi olcumlerde olcum hatasi sistematik olabilir; standart hatalar yanliligi isaretlemez (Battaglia et al. 2025)
- Entelektuel tembellik ve dusunce cesitliligi kaybi riski: yazma ve kritik dusunme arastirmacida kalmalI
- 4 calisilmis ornek: tablo duygu siniflandirma, isimsiz nufus baglama (%43-62), 1882 Cin Dislama Yasasi gazete duygu (524K->11K sayfa), FDR savas konusmalari duygu skoru
- Replikasyon: https://doi.org/10.3886/E249897V2 (ICPSR); JEL C55, C8, N0

## Turkey Context

Ferrara'nın ekonomik tarih araştırmalarında büyük dil modellerinin kullanımına yönelik uygulayıcı rehberi, Türkiye'deki dijital beşeri bilimler ve iktisat tarihi çalışmaları için zamanında bir katkıdır. Osmanlı arşivleri, nüfus kayıtları, vakıf defterleri ve gazete koleksiyonları gibi Türkiye'nin zengin tarihsel veri kaynakları, el yazısı tanıma ve büyük ölçekli metin işleme gerektirdiği için LLM'lerin sunduğu erişim kolaylığından doğrudan yararlanabilecek niteliktedir. Cumhurbaşkanlığı Devlet Arşivleri Başkanlığı'nın dijitalleştirme çalışmaları ile TÜBİTAK'ın yapay zekâ destekli araştırma projeleri, bu tür veri kaynaklarının LLM tabanlı analizini mümkün kılan altyapıyı sağlamaktadır. Bununla birlikte rehberin vurguladığı riskler Türkiye'de de dikkate alınmalıdır: halüsinasyon üreten referanslar, kültürel önyargılar ve geçersiz nedensel çıkarımlar, özellikle Osmanlı Türkçesi ve azınlık dillerindeki kaynaklarla çalışan araştırmacılar için kritik tehlikelerdir. Bu nedenle YÖK'ün ve üniversitelerin etik kurullarının, LLM kullanımını açıklayan veri yönetimi ve yöntem beyanı standartları geliştirmesi önerilir. KVKK (6698 sayılı Kanun), nüfus kayıtları gibi kişisel veri içeren tarihsel kaynakların işlenmesinde gizlilik sınırlarını belirleyen temel çerçeve olarak öne çıkar; araştırmacıların kişisel verileri LLM API'lerine göndermeden önce anonimleştirme ve veri minimizasyonu ilkelerini uygulaması gerekir. Türkiye'nin Ulusal Yapay Zekâ Stratejisi (2021-2025) kapsamında beşeri bilimlerde yapay zekâ kullanımını teşvik eden programların geliştirilmesi, bu rehberin yerel bağlama uyarlanmasını hızlandırabilir. Ayrıca TÜİK'in dijitalleştirilmiş tarihsel istatistikleri ve üniversitelerin iktisat tarihi kürsüleri, Ferrara'nın dört çalışılmış örneğine benzer Türkçe vaka analizleri geliştirerek uluslararası literatüre katkı sunabilir. Replikasyon kültürünün yerleşmesi, ICPSR benzeri ulusal bir veri deposunun kurulmasıyla desteklenmelidir. Sonuç olarak bu rehber, Türkiye'deki tarihsel veri araştırmalarının yapay zekâ çağında bilimsel titizlikten ödün vermeden dönüşümü için uygulanabilir bir yol haritası çizmektedir. Türkiye'deki üniversite kütüphanelerinin ve araştırma merkezlerinin (Atatürk Kültür, Dil ve Tarih Yüksek Kurumu bünyesindeki merkezler dahil) tarihsel koleksiyonlarının dijital altyapısı, LLM tabanlı analizlerin uygulanabilirliğini belirleyen temel unsurdur; bu altyapının güçlendirilmesi için kültürel mirasın dijitalleştirilmesine yönelik kamu yatırımlarının artırılması önerilir. Avrupa'da EHRI ve CLARIAH gibi beşeri bilimler veri altyapıları, uluslararası iş birliği için model oluştururken, Türkiye'nin benzer bir ulusal altyapı oluşturması hem arşiv erişimini hem de karşılaştırmalı araştırmayı kolaylaştıracaktır. Ayrıca üniversitelerde araştırma yöntemleri derslerine LLM kullanım etiketi ve raporlama standartlarının dahil edilmesi, genç araştırmacıların bu araçları bilimsel titizlikle kullanmasını sağlayacaktır.
