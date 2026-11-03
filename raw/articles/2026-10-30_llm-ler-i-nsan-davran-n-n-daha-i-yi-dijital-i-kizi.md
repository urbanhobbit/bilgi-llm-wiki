---
type: raw_article
title: LLM'ler İnsan Davranışının Daha İyi Dijital İkizi Olabilir mi? HuMCal Kalibrasyonu
description: Yan Leng, Yunxin Sang ve Ashish Agarwal (University of Texas at Austin,
  McCombs), LLM'lerin insan davranışının dijital ikizi olarak kullanılmasındaki sistematik
  sapmayı azaltmak için **HuMCal** (Human...
resource: https://doi.org/10.1287/mksc.2024.0983
tags:
- kurator
- akademik
- high
timestamp: '2026-11-03T03:55:20Z'
source_file: 2026-10-30_humcal-llm-sample-calibration.json
category: KURATOR; AKADEMİK ÖZEL
priority: high
roles:
- method
published: '2026-10-30'
---

# LLM'ler İnsan Davranışının Daha İyi Dijital İkizi Olabilir mi? HuMCal Kalibrasyonu

**Author(s):** Yan Leng, Yunxin Sang, Ashish Agarwal

**Published:** 2026-10-30

**Source:** [https://doi.org/10.1287/mksc.2024.0983](https://doi.org/10.1287/mksc.2024.0983)

## Summary

Yan Leng, Yunxin Sang ve Ashish Agarwal (University of Texas at Austin, McCombs), LLM'lerin insan davranışının dijital ikizi olarak kullanılmasındaki sistematik sapmayı azaltmak için **HuMCal** (Human Mimicry Calibration) yöntemini öneriyor. Sorun tanımı net: analistler ya tek bir toplu prompt kullanıyor ya da birden fazla LLM çıktısını sezgisel kurallarla birleştiriyor — düz ortalama, nüfus ağırlıklı poststratifikasyon, ya da kalibrasyon verisinde en iyi tek alt-grubu seçmek. Bu yaklaşımlar insan referansından sapmaya devam ediyor. HuMCal, farklı prompt'lar, persona'lar ve model checkpoint'lerinden gelen LLM çıktılarını **ağırlıklı olarak birleştirmeyi öğrenen**, sonradan uygulanan (post hoc), modele bağımlı olmayan (model-agnostic) bir yöntem. İki önemli tasarım tercihi: (1) modelin içine erişim gerektirmiyor, (2) her alt-grup için ayrı insan referansı gerektirmiyor — yalnızca **toplulaştırılmış** insan referans verisi kullanıyor. Kalibrasyon verisi üzerinde HuMCal, insan referansına en iyi uyan ağırlıklı ortalamayı seçiyor; tam çözüldüğünde kalibrasyon kaybı, aynı çıktı kümesi üzerindeki **herhangi bir sabit ağırlıklı kuraldan zayıf biçimde daha düşük** oluyor. Yazarın tweet'ine göre ağırlıklar şehirler, zaman dönemleri, sektörler ve konu kümeleri arasında genellenebiliyor; uygulamalar tüketici işlem verisi ve kamuoyu anketlerini kapsıyor. ⚠️ Tam metin INFORMS ödeme duvarının arkasında (Cloudflare 403); aşağıdaki tüm ayrıntı yayıncı özeti, makalenin ilk sayfası ve yazarın tweet'i düzeyinde.

## Key Points

- Künye: Yan Leng, Yunxin Sang, Ashish Agarwal, 'Frontiers: Reducing Disparity Between LLMs and Humans: Optimal LLM Sample Calibration', *Marketing Science*, Articles in Advance, s. 1-13 (2026). DOI 10.1287/mksc.2024.0983. Üç yazar da UT Austin (McCombs School of Business); ORCID'ler 0000-0002-7084-2700 (Leng), 0000-0002-4521-5796 (Sang), 0000-0001-9259-0113 (Agarwal).
- Problem: LLM'ler tercih ve görüş ölçmek için giderek daha fazla kullanılıyor ama çıktıları temsil ettikleri insan popülasyonundan sapabiliyor. Mevcut pratik üç sezgisel kurala dayanıyor: tek toplu prompt, birden fazla çıktının düz ortalaması, nüfus ağırlıklı poststratifikasyon veya kalibrasyon bölmesinde en iyi tek alt-grubu seçmek.
- HuMCal'ın çözümü: farklı prompt'lar, persona'lar ve model checkpoint'lerinden gelen çıktıları birleştiren **ağırlıkları veriden öğrenmek**. Post hoc ve model-agnostik; model içine erişim (logit, ağırlık, aktivasyon) gerektirmiyor.
- Verimlilik iddiası: her alt-grup için ayrı insan referansı gerekmiyor; yalnızca toplulaştırılmış insan referansı yeterli. Bu, pratikte kritik — çünkü dijital ikiz üretiminde en pahalı kalem alt-grup bazlı insan verisi toplamak.
- Optimalite iddiası: kalibrasyon verisi üzerinde seçilen ağırlıklı ortalama, tam çözüldüğünde 'herhangi bir sabit ağırlıklı kuraldan zayıf biçimde daha iyi' (weakly lower calibration loss). Bu, yöntemin sezgisel kuralları kapsayan bir üst küme oluşturduğu anlamına geliyor — ama yalnızca kalibrasyon örnekleminde.
- Genellenebilirlik (yazarın tweet'indeki iddia): kalibre edilmiş ağırlıklar şehirler, zaman dönemleri, sektörler ve konu kümeleri arasında yararlı kalabiliyor. Bu, yöntemin cazibesini artıran en güçlü pratik iddia; ancak hangi koşulda bozulduğu tam metinde görülmeli.
- Veri: tüketici işlem verisi ve kamuoyu anketleri (iki uygulama alanı). Örneklem büyüklükleri, kullanılan LLM'ler ve iyileşme yüzdeleri ⚠️ tam metin olmadan doğrulanamadı.
- Yöntemsel konum: bu, 'silikon örneklem' (synthetic sample) literatürünün kalibrasyon ayağı. Sentetik popülasyonların dağılımsal doğruluğunu artırmayı hedefliyor; nedensel çıkarım değil, ölçüm uyumu (alignment) iddiası var.
- Sınır: yöntem toplulaştırılmış referansa dayandığı için grup-içi dağılımı düzeltmiyor olabilir; alt-grup ortalamaları eşleşirken varyans yanlış kalabilir. Bu, marjinal dağılımı tutturmakla ortak dağılımı tutturmanın farkı — polarizasyon ölçümünde kritik.
- ⚠️ Erişim: pubsonline.informs.org ve SSRN (abstract_id=4802019) Cloudflare ile 403 veriyor; r.jina.ai, doğrudan PDF (/doi/pdf/...) ve Delivery.cfm yolları denendi, hiçbiri geçmedi. Semantic Scholar'da kayıt yok, Unpaywall açık kopya göstermiyor, arXiv'de preprint yok. Bu kayıt yayıncı özeti + ilk sayfa görseli + yazar tweet'i düzeyinde tutuldu; sayısal sonuçlar UYDURULMADI.

## Turkey Context

Bu makale, Türkiye'de kamuoyu araştırması ve sosyal bilim metodolojisi açısından iki nedenle önemli. Birincisi, pratik: Türkiye'de anket maliyetleri yüksek, örneklem temsiliyeti kronik bir sorun (kent-kır, eğitim, Kürt seçmen, Alevi nüfus gibi alt gruplarda tabakalama zayıf). LLM tabanlı sentetik örneklemler, HuMCal gibi kalibrasyonla birleştiğinde, pahalı saha çalışmasının yerine geçmese bile 'ön test' ve 'dağılım kontrolü' işlevi görebilir — örneğin bir anketin marjinal dağılımını gerçek veriyle hizalayıp sapmayı raporlamak. İkincisi, risk: kalibrasyon yalnızca **marjinal** dağılımı eşitliyorsa, iki değişkenin ortak dağılımı (örneğin eğitim × dindarlık × parti tercihi) yanlış kalabilir. Bu, Türkiye'de yapılan 'sentetik seçmen' analizlerinde en sık yapılan hata: toplamlar tutuyor, kesişimler tutmuyor. Polarizasyon ve seçmen davranışı çalışan bir araştırmacı için doğru soru 'LLM anketi tutturuyor mu' değil, 'hangi kesişimlerde tutmuyor' olmalı. Üçüncüsü, yöntem ithalatı: Türkçe metinlerde LLM'lerin persona taklidi (ör. '35 yaşında İstanbul'da yaşayan muhafazakâr seçmen') İngilizceye kıyasla belirgin biçimde daha zayıf; HuMCal'ın ağırlıkları Türkçe prompt'larla yeniden kalibre edilmeden ithal edilemez. Dördüncüsü, kurumsal: TÜİK ve araştırma şirketleri hanehalkı verisini paylaşmadığı için kalibrasyon için gereken 'toplulaştırılmış insan referansı' bile çoğu zaman erişilebilir değil — yöntemin Türkiye'de uygulanabilirliği veri erişim rejimine bağlı. Beşincisi, tarihsel bağlam: Türkiye'de 2023 cumhurbaşkanlığı ve 2024 yerel seçimlerinde anket şirketlerinin sapması kamuoyunda büyük tartışma yarattı; HuMCal tam olarak bu tür bir sapmayı ölçülebilir kılan bir çerçeve sunuyor — 'hangi alt grupta, hangi ağırlıkla yanılıyoruz' sorusunu soruyor. Altıncısı, akademik teşvik: Türkiye'de ampirik sosyal bilimde veri toplama maliyeti arttıkça sentetik veriye kaçış hızlanacak; bu makalenin uyarısı, sentetik veriyi kalibre etmeden kullanmanın, ölçüm hatasını görünmez kılarak analizi daha güvenilir göstermesi. Yedincisi, ders: yöntem 'az insan verisiyle çok şey yapma' vaadi veriyor ama sıfır insan verisiyle hiçbir şey yapılamayacağını da açıkça söylüyor — Türkiye'de araştırma altyapısı tartışmasında bu, 'veri paylaşımı olmadan yöntem ithali işe yaramaz' sonucuna götürüyor.

## 🏷 Retorik Roller

- 🧩 **Yöntem**
