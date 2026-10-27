---
type: raw_article
title: 'Conversations at Scale: Robust AI-led Interviews'
description: 'Nitel görüşmeyi binlerce kişiye ölçekleyen, tek ajanlı ve açık kaynaklı
  bir LLM görüşmeci platformu; hem yöntem hem de dört ayrı uygulama alanında doğrulama
  sunuyor. Künye: Geiecke & Jaravel (LSE/CEPR...'
resource: https://www.restud.com/conversations-at-scale-robust-ai-led-interviews/
tags:
- kurator
- high
timestamp: '2026-10-27T09:26:44Z'
source_file: 2026-10-06_conversations-at-scale-robust-ai-led-interviews.json
category: KURATOR
priority: high
roles:
- gap
- method
- result
- limitation
published: '2026-10-06'
---

# Conversations at Scale: Robust AI-led Interviews

**Author(s):** Friedrich Geiecke (LSE), Xavier Jaravel (LSE & CEPR)

**Published:** 2026-10-06

**Source:** [https://www.restud.com/conversations-at-scale-robust-ai-led-interviews/](https://www.restud.com/conversations-at-scale-robust-ai-led-interviews/)

## Summary

Nitel görüşmeyi binlerce kişiye ölçekleyen, tek ajanlı ve açık kaynaklı bir LLM görüşmeci platformu; hem yöntem hem de dört ayrı uygulama alanında doğrulama sunuyor. Künye: Geiecke & Jaravel (LSE/CEPR), The Review of Economic Studies'te kabul edilmiş makale, DOI 10.1093/restud/rdag114 — DOI kayıtlı fakat doi.org Crossref 'pending publication' sayfasına düşüyor, yani hakem süreci tamamlanmış ama dergi künyesi (cilt/sayı/sayfa) henüz Crossref'e işlenmemiş. Okunan metin: restud.com'da yayımlanan 30 Eylül 2026 tarihli 51 sayfalık manuscript; ilk sürüm SSRN'de 2024'te 'with a Simple Open-Source Platform' adıyla çıkmış.

Soru: nitel görüşmenin ayırt edici yanı, araştırmacının veriyi karşılıklı etkileşimle *üretmesi*. Bu derinlik korunurken ölçek kazanılabilir mi? Yazarlar tek bir LLM'in açık uçlu sorular sorduğu, yanıtları takip ettiği ve ayrıntı için sonda ürettiği (sabit anket değil) bir platform kuruyor: metin ve ses görüşmesi, konuya göre tek paragraf prompt değişimiyle uyarlanabilir, 30–60 dakikalık görüşmeler, RAG yok, ince ayar yok.

Doğrulama 1 — insan uzmanla kıyas: 20 transkript, her biri iki sosyoloji doktora öğrencisi tarafından kör değerlendirildi (40 puan). 'Aynı katılımcıyla 30 dk çevrimiçi metin görüşmesinde uzmanın yapabileceği' referansına göre ortalama 2,93/5 (s.e. 0,167); 5 üzerinden puanların hiçbiri 5 değil. Modalite ayrıştırıldığında (Tablo II): **AI sesli 3,93** > insan yüz yüze 3,51 > AI metin 2,98 > insan çevrimiçi metin 2,42. Yüz yüze referansına göre ise insan yüz yüze 3,53 ≈ AI sesli 3,50 > AI metin 2,70 > insan çevrimiçi metin 1,99. Yani AI görüşmesi çevrimiçi metin görüşmesinin insan versiyonunu açık ara geçiyor, sesli modda yüz yüze insan uzmana yaklaşıyor.

Doğrulama 2 — beş büyük uygulama (hepsi Prolific/Bilendi gibi platform örneklemleri): (1) **Hayatın anlamı**, N=461 ABD temsili: AI görüşmesi kişi başı 470 kelime, açık uçlu anket 195 kelime (+%141); %77,11'i açık uçlu soruyu tercih etmeyeceğini, %41,79'u gelecekte AI ile görüşmeyi tercih edeceğini söylüyor (insan %19,40). (2) **Fransa erken genel seçimi** (Haziran 2024), N=383: yüksek kutuplaşma döneminde seçmen gerekçeleri; örneklem temsili değil (genç, düşük gelirli, sola eğik: %65 / seçim günü %28). (3) **Eğitim ve meslek seçimi**, N=102: eğitimde en çok anılan faktör kişisel ilgi/tutku (%68), sonra kariyer-getiri (%36), hayati olaylar (%35), mentor (%34); meslek seçiminde tutku %39, maddi teşvik %33. (4) **Trump politikalarına dair zihinsel modeller** (Nisan 2025), N=793: aynı politika farklı kişilerde zıt nedensel zincirlerle yorumlanıyor (tarifeler: tüketici fiyatları ↑ vs imalat işleri geri gelir); ardından 300 kişilik kapalı uçlu anketle doğrulama — negatif tarife anlatısına %87 'tamamen katılıyorum', anlatıların kapsayıcılığı %76–81. (5) **Sesli görüşme / enflasyonun nedenleri** (Ocak 2025), N=338 temsili: %54,73'ü gelecekte insan yerine AI ile görüşmeyi tercih ediyor, %53,55'i mikrofonla konuşmayı yazmayı tercih ediyor, özet kalitesi 3,69/4.

Model karşılaştırması: GPT-4o, GPT-4.1, Claude Sonnet 4 ve açık ağırlıklı Llama 3.1 405B / Llama 4 Maverick 17B; sesli modda Whisper transkripsiyon + gpt-4o-audio-preview (doğrudan ses üreten model). Maliyet: Prolific'te 30 dk görüşme için katılımcı ücreti ~4 $; AI çıkarım maliyeti kısa metin görüşmesinde katılımcı başına yarım doların altında.

İddia ve sınır: AI görüşmesi yüz yüze görüşmenin yerine değil, tamamlayıcısı — sözel/sözsüz ipuçları, saatler süren görüşme planları ve rapport kurma insan görüşmeciye özgü kalıyor. Uzman puanları arasında ciddi heterojenlik var (iki değerlendirici arası korelasyon 0,55; aykırı gözlem çıkarılınca 0,69), yani '2,93' tek başına kesin bir ölçü değil. Tek ajanlı mimari hız ve düzenlenebilirlik sağlıyor ama çok uzun görüşmelerde veya yüksek riskli konularda çok ajanlı yapılar daha güvenli olabilir. Kod ve talimatlar github.com/friedrichgeiecke/interviews (ayrıca Colab notebook + video eğitimler); anonimleştirilmiş veri ve kod Zenodo 10.5281/zenodo.21702419.

## Key Points

- Künye: Geiecke, F. & Jaravel, X. (2026), 'Conversations at Scale: Robust AI-led Interviews', The Review of Economic Studies (kabul edilmiş); DOI 10.1093/restud/rdag114 doi.org'da Crossref 'pending publication' sayfasına düşüyor — yani cilt/sayı/sayfa henüz Crossref'te yok. Okunan metin restud.com'daki 30 Eylül 2026 tarihli manuscript (51 s.).
- Platform: tek ajanlı LLM görüşmeci, açık uçlu ana sorular + bağlama duyarlı sonda üretimi; metin ve sesli mod; konu değişimi için promptun tek paragrafı değiştiriliyor. RAG yok, ince ayar yok; görüşme uzunluğu tipik 30–60 dk, alfanümerik 'kod' ile görüşme bitirme/iptal mekanizması.
- Uzman değerlendirmesi: 20 transkript × 2 kör değerlendirici (sosyoloji doktora öğrencileri, Cambridge/Harvard/JHU/LSE/Oxford) = 40 puan; 30 dk çevrimiçi metin referansına göre ortalama 2,93/5 (s.e. 0,167) — 'ortalama insan uzman' düzeyi.
- Modalite sıralaması (metin referansı): AI sesli 3,93 > insan yüz yüze 3,51 > AI metin 2,98 > insan çevrimiçi metin 2,42. Yüz yüze referansında: insan yüz yüze 3,53 ≈ AI sesli 3,50 > AI metin 2,70 > insan çevrimiçi metin 1,99.
- Hayatın anlamı (N=461, ABD temsili): AI görüşmesi 470 kelime/kişi, açık uçlu anket 195 kelime (+%141); %77,11 açık uçlu soruyu tercih etmezdi; %41,79 gelecekte AI'ı, %19,40 insanı tercih ediyor. En çok anılan anlam kaynakları ebeveynlik, iş, arkadaşlar; evcil hayvan bakımı %17 ile dinden (%16) biraz yüksek — anketin kaçırdığı bir kategori.
- Fransa erken seçimi (Haziran 2024, N=383): yüksek kutuplaşma döneminde seçmen gerekçeleri ve 'problem gündemi' öncelikleri, yakın uçlu ölçek kullanmadan; ancak Prolific örneklemi temsili değil (genç, düşük gelir, sol eğilim %65 vs seçim günü %28; iptal niyeti seçim gününün çok altında).
- Eğitim/meslek seçimi (N=102): eğitimde kişisel ilgi-tutku %68, kariyer-getiri %36, hayati olaylar %35, mentor %34, aile %25; meslek seçiminde tutku %39, maddi teşvik %33, mentor %1, aile %8. Katılımcıların yalnızca %17,65'i gelecekte insan görüşmeci tercih ediyor.
- Zihinsel modeller (Trump politikaları, Nisan 2025, N=793): nitel görüşmeden çıkarılan 35 anlatı (15 pozitif / 20 negatif) 300 kişilik kapalı uçlu anketle test edildi — negatif tarife zincirine %87,04 'tamamen katılıyorum'; anketin gerekçeleri kapsama oranı %76–81. Nitel → nicel hipotez üretimi döngüsünün somut gösterimi.
- Sesli görüşme (enflasyon, Ocak 2025, N=338 temsili): %54,73 insan yerine AI, %53,55 mikrofonla konuşma tercih ediyor; özet kalitesi 3,69/4. Model doğrudan ses üretiyor (gpt-4o-audio-preview), transkripsiyon Whisper ile.
- Test edilen modeller: GPT-4o, GPT-4.1, Claude Sonnet 4, Llama 3.1 405B, Llama 4 Maverick 17B. Maliyet: katılımcı ücreti ~4 $ (Prolific, 30 dk), AI çıkarımı katılımcı başına 0,5 $'ın altında (kısa metin görüşmesi).
- Açıklık: kod github.com/friedrichgeiecke/interviews, Colab notebook, video eğitimler; anonimleştirilmiş veri + kod Zenodo 10.5281/zenodo.21702419 (makalenin Data Availability beyanı).
- Sınırlılık: uzman puanlarında yüksek heterojenlik (değerlendiriciler arası korelasyon 0,55; aykırı gözlem hariç 0,69), yüz yüze görüşmenin yerini almıyor, tek ajanlı mimari uzun/karmaşık görüşmelerde ve hassas konularda riskli olabilir, Fransa örneklemi temsili değil, anlatı yaygınlığını transkriptten tahmin etmek zor (bu yüzden kapalı uçlu anketle doğrulama yoluna gidilmiş).

## Turkey Context

Türkiye için en pratik başlık maliyet ve saha erişimi: nitel görüşme burada ağırlıkla yüz yüze, tek tek ve pahalı yapılıyor; aynı bütçeyle yüzlerce kişiye ulaşmak araştırma şirketleri için de üniversite ekipleri için de oyunu değiştirir. Platform açık kaynak ve tek ajanlı olduğu için Türkçe promptla kurmak teknik olarak zahmetsiz — asıl sınav Türkçe görüşme kalitesi: yazılı Türkçede modeller akıcı, ama sonda üretiminde klişeye kaçma ve resmi dil kullanma eğilimi var; 'doğal sohbet' hissi Türkçede İngilizceye göre daha zayıf kalabilir. Bunun ölçülmesi gerekiyor, varsayılmaması.

Siyasi açıdan daha ilginç olan bulgu, yazarların gerekçesi: kutuplaşmış seçimlerde seçmen, yargılamayan bir muhatap olarak AI'a görüşünü daha rahat açabilir. Türkiye'de siyasal tercih ve iktidar algısı üzerine görüşmelerde 'sosyal istenirlik' ve kendini sansürleme bilinen bir sorun; AI görüşmecinin burada insan görüşmeciden daha az baskı üretip üretmediği, doğrudan test edilebilir ve KURATOR'ün ilgi alanına giren bir soru. Buna karşılık aynı özellik veri kalitesini de bozabilir: insan görüşmeci sessiz kaldığında katılımcı ayrıntı verir, AI'da susma payı yok.

Uyarı niteliğinde: Fransa örneğinde örneklemin sola eğikliği ve iptal niyetinin gerçek iptal oranının çok altında çıkması, AI görüşmesinin temsil sorununu çözmediğini gösteriyor — ölçek artıyor, temsil artmıyor. Türkiye'de çevrimiçi panel altyapısı ve gönüllü katılım eğilimi göz önüne alındığında bu sapma daha da büyük olabilir; AI ile ölçek kazanırken örneklem tasarımını ayrıca kurmak gerekiyor.

## 🏷 Retorik Roller

- 🔍 **Araştırma Boşluğu**
- 🧩 **Yöntem**
- 📊 **Bulgular**
- ⚠️ **Sınırlılıklar**

---

## 🔗 İlgili Bağlantılar
### 🧠 İlgili Kavramlar
- [[concepts/yapay-zeka-destekli-gorusmeler.md|Yapay Zeka Destekli Görüşmeler (AI Interviewing)]] — alanın ölçek iddiasını en geniş biçimde sınayan çalışma: 461–793 kişilik örneklemler, uzman puanlaması ve sesli mod.
- [[concepts/siyaset-bilimi-metodolojisi.md|Siyaset Bilimi Metodolojisi]] — nitel görüşmeyi nicel ölçeğe taşıyan tasarım; araştırma yöntemleri açısından ölçek-temsil ödünleşiminin somut örneği.
- [[concepts/olcum-araclari.md|Ölçüm Araçları (Polarization Measurement)]] — 1–5 uzman puanı, transkriptten LLM ile kategori çıkarma ve anketle doğrulama: ölçümün geçerlilik zinciri.
### 🏛 İlgili Kurum/Kişiler
- [[entities/restud-com.md|The Review of Economic Studies (restud.com)]] — makalenin kabul edildiği dergi; ücretsiz tam metin PDF'i dergi sitesinden indirildi.
- [[entities/github-com.md|GitHub (github.com)]] — açık kaynak görüşme platformu: `github.com/friedrichgeiecke/interviews` (Colab notebook + video eğitimler).

## İlgili Makaleler
- [[raw/articles/2026-10-20_can-ai-interview-comparing-ai-led-to-human-led-cha.md|Can AI interview? Comparing AI-led to Human-led Chat Interviews]] — aynı alanda randomize karşılaştırma (N=41, yerel 7B model); Geiecke & Jaravel'in 2024 sürümünü referans alıyor.

