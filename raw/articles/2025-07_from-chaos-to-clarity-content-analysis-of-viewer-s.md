---
type: raw_article
title: 'From Chaos to Clarity: Content Analysis of Viewer Sentiments Using YouTube
  Videos on Misinformation'
description: '**Tam metin okundu (yazarın gönderdiği PDF; 18 sayfa, ~50 bin karakter).**
  Baral ve Fazlunnisa H. (University of Madras, Kütüphane ve Enformasyon Bilimi),
  YouTube''da **"misinformation"** anahtar kelim...'
resource: https://www.researchgate.net/publication/417538197
tags:
- kurator
- medium
timestamp: '2026-11-13T18:20:00Z'
source_file: 2026-11-13_from-chaos-to-clarity-youtube-viewer-sentiments-metadata-only.json
category: KURATOR
priority: medium
roles:
- method
- result
published: 2025-07
---

# From Chaos to Clarity: Content Analysis of Viewer Sentiments Using YouTube Videos on Misinformation

**Author(s):** Ramakrushna Baral (UGC-JRF Research Scholar) & Fazlunnisa H. (Assistant Professor) — Department of Library and Information Science, University of Madras, Chennai

**Published:** 2025-07

**Source:** [https://www.researchgate.net/publication/417538197](https://www.researchgate.net/publication/417538197)

## Summary

**Tam metin okundu (yazarın gönderdiği PDF; 18 sayfa, ~50 bin karakter).** Baral ve Fazlunnisa H. (University of Madras, Kütüphane ve Enformasyon Bilimi), YouTube'da **"misinformation"** anahtar kelimesiyle dolaşımdaki videoların meta verisini ve izleyici yorumlarının duygu tonunu inceliyor. Bu bir **alımlama/duygu analizi** çalışması: videoların doğruluk denetimi yapılmıyor, izleyicinin bu videolara verdiği duygusal tepki ölçülüyor.

**Veri ve yöntem.** YouTube API V3, **Webometric Analyst 4.0** yazılımı üzerinden, **Eylül 2024**'te tek kesit: 514 video + meta verisi (video/channel ID, başlık, açıklama, süre, görüntüleme, beğeni, yorum sayısı). Yorumlar video ID üzerinden çekildi: **496.541 yorum**. Temizlik: İngilizce dışı ve müzik videoları (103 video) elendi → **411 video / 400.492 yorum**; tokenizasyon + stop-word + emoji temizliği sonrası duygu analizine giren **301.957 yorum**. Duygu analizi **sözlük tabanlı**: R'de `syuzhet` kütüphanesi + **NRC Lexicon** (`get_nrc_sentiment`) ile 8 duygu (anger, anticipation, disgust, fear, joy, sadness, surprise, trust) ve pozitif/negatif kutup. Konu analizi için R `wordcloud` (başlık + açıklama metinleri).

**Zaman örüntüsü.** İlk video **2012**; 2012–2016 arasında yalnızca **7 video** (konu neredeyse yok). İlk sıçrama **2017** (ABD başkanlık seçimi ve "fake news" tartışması), ikinci sıçrama **2020** (Covid-19). En yüksek yıllık üretim **2024: 87 video**; videoların **~%85'i son beş yılda** yüklenmiş.

**En çok izlenen 10 video.** 1) Bloomberg Originals — "It's Getting Harder To Spot A Deep Fake Video": **8.418.879** görüntüleme (toplamın **%7,06**'sı). 2) Last Week Tonight (John Oliver): **7.194.543** (%6,03). 3) The Daily Show — "Coronavirus misinformation & toilet paper panic": **3.745.538**. Liste ağırlıklı olarak ABD merkezli komedi/geç-late-night ve sağ eğilimli yorum kanallarından (Steven Crowder, Fox News, SNL) oluşuyor.

**En çok beğenilen 10 video (Tablo 2).** 1) John Oliver **165.040** beğeni (%4,98) · 2) "Springfield, Ohio Migrant issue is not FAKE NEWS" (Empty Pockets Garage, James) **131.209** · 3) Steven Crowder "CNN is Fake News | Change My Mind" **106.914**.

**Duygu dağılımı (NRC).** **trust 336.426** > **fear 251.851** > anticipation 212.238 > anger 194.752 > sadness 187.636 > joy 163.810 > disgust 148.319 > surprise 112.125. Kutup: **pozitif 492.318** vs **negatif 450.518** — yazarların yorumu: izleyici "misinformation" videolarına **güven eğiliminde**, ama korku/öfke de güçlü.

**Konu bulutu.** En sık kelimeler: "misinformation" **424**, "news" **195**, "fake" **135**. Temalar: sosyal medya platformları (Facebook, YouTube, Twitter, TikTok), ABD siyaseti (Trump, Biden, Clinton, election), sağlık (Covid, vaccines, pandemic, medical), eğitim/okuryazarlık, savaş ve iklim.

⚠️ **Kendi okumamın uyarıları (metin içi tutarsızlıklar):** (a) Metin, "Springfield, Ohio" videosunun **4,02,208** beğeniyle ikinci olduğunu söylüyor; **Tablo 2 aynı video için 131.209** gösteriyor — ikisinden biri hatalı. (b) Metin John Oliver videosunun "en çok izlenen" olduğunu ima ediyor; Tablo 1'de birinci Bloomberg (8,4 mn), Oliver ikinci (7,2 mn). (c) Duygu sayıları (pozitif+negatif = 942.836) yorum sayısından (301.957) yüksek: NRC sözlüğü yorum başına birden çok duygu terimi saydığı için toplamlar yorum sayısıyla karşılaştırılamaz — makale bunu açıklamıyor. (d) "misinformation" kelimesinin konu bulutunda birinci çıkması kısmen **arama teriminin kendisi** olmasından; yazarlar bunu kabul ediyor.

## Key Points

- Baral, R. & Fazlunnisa, H. (2025), 'From Chaos to Clarity: Content Analysis of Viewer Sentiments Using YouTube Videos on Misinformation', Journal of Library Management 14(2): 33–50 (Temmuz–Aralık 2025), ISSN 2278-5523.
- Kurum: University of Madras, Kütüphane ve Enformasyon Bilimi Bölümü (Baral: UGC-JRF araştırma görevlisi; Fazlunnisa: yardımcı doçent). Dergi MANLIBNET yayını; DOI yok, Crossref/OpenAlex'te kayıtlı değil.
- Veri: YouTube API V3 + Webometric Analyst 4.0, arama terimi 'misinformation', Eylül 2024 tek kesit — 514 video ve 496.541 yorum toplandı.
- Temizlik: 103 İngilizce-dışı/müzik videosu elendi → 411 video / 400.492 yorum; tokenizasyon + emoji temizliği → duygu analizine giren 301.957 yorum.
- Duygu analizi: R 'syuzhet' + NRC Lexicon (8 duygu + pozitif/negatif); konu analizi: R 'wordcloud' (başlık + açıklama).
- Zaman örüntüsü: ilk video 2012; 2012–2016 yalnız 7 video; sıçramalar 2017 (ABD seçimi) ve 2020 (Covid); zirve 2024 (87 video); videoların ~%85'i son 5 yılda.
- En çok izlenen: Bloomberg deep fake videosu 8.418.879 (%7,06); John Oliver 7.194.543 (%6,03); The Daily Show 3.745.538.
- En çok beğenilen: John Oliver 165.040 (%4,98); Springfield/Empty Pockets Garage 131.209; Steven Crowder 106.914.
- Duygu sıralaması: trust 336.426 > fear 251.851 > anticipation 212.238 > anger 194.752 > sadness 187.636 > joy 163.810 > disgust 148.319 > surprise 112.125.
- Kutup: pozitif 492.318 vs negatif 450.518 — yazarlar 'izleyici güven eğiliminde ama korku/öfke güçlü' sonucunu çıkarıyor.
- Konu bulutu: 'misinformation' 424, 'news' 195, 'fake' 135; temalar sosyal medya platformları, ABD siyaseti, Covid/aşı, eğitim, savaş ve iklim.
- Metin içi tutarsızlık: Springfield videosu için metinde 402.208, Tablo 2'de 131.209 beğeni; John Oliver'ın 'en çok izlenen' olduğu iddiası Tablo 1 ile çelişiyor.
- Duygu toplamları (942.836) yorum sayısıyla (301.957) uyuşmuyor — NRC terim bazlı sayım; makale açıklamıyor.
- Teorik katkı iddiası: LIS alanında YouTube meta verisi + izleyici duygu analizini birleştiren 'ilk çalışma' olduğu iddiası; yöntem yeniliği değil, uygulama alanı iddiası.
- Sınırlılıklar (yazarların belirtmedikleri): yalnız İngilizce yorum; tek anahtar kelime ('misinformation') → kavramın kendisiyle ilgili videolar, dezenformasyonun tamamı değil; Eylül 2024 tek kesit; API erişim/sıralama kısıtları; yorum duygusu ≠ inanç ölçümü.

## Turkey Context

Türkiye açısından iki değeri var, ikisi de **yöntemsel**:

**1) Uygulanabilir şablon.** Türkiye'de YouTube, Reuters Institute verilerine göre haber erişiminde en yüksek paya sahip platformlardan biri; buna karşın Türkçe içerikte izleyici duygu analizi neredeyse hiç yapılmıyor. Bu makalenin hattı (YouTube API → meta veri + yorum → NRC sözlüğüyle duygu) Türkçe'ye uyarlanabilir; ama **NRC'nin Türkçe kapsamı zayıf**, Türkçe duygu sözlüğü (ör. SentiTurkNet) veya çok dilli model gerekir. Bu, aktarımın en kırılgan noktası.

**2) Kritik metodolojik uyarı — anahtar kelime tuzağı.** Çalışma "misinformation" kelimesini **arayan** videoları inceliyor; yani dezenformasyonun kendisini değil, **dezenformasyon hakkında konuşan** içeriği. Türkçe'de aynı hata "dezenformasyon" veya "yalancı" aramasıyla yapılırsa, medyanın kendi kendini anlattığı bir örneklem elde edilir; izleyicinin gerçekten maruz kaldığı yanlış bilgi ekosistemi görünmez. Türkiye çalışması tasarlanırken iki ayrı örneklem gerekir: (a) kavram hakkında içerik, (b) doğrulanmış yanlış iddiaları taşıyan içerik (ör. Teyit/Doğruluk Payı arşivlerinden geriye doğru izleme).

**3) Kullanılabilir bulgu:** Türkiye'de dezenformasyon içeriğinin büyük ölçüde **olay kırılmalarında** (seçim, afet, pandemi) üretildiği hipotezi bu makalenin zaman serisi örüntüsüyle uyumlu; ama Türkiye için bu, bu veriyle **doğrulanmış değil**.

⚠️ Dergi DOI'siz ve dizinlenmemiş; bulgular **kanıt hiyerarşisinde zayıf** konumda. Türkiye analizinde yöntem referansı olarak atıflanabilir, bulgu referansı olarak dikkatli kullanılmalı.

## 🏷 Retorik Roller

- 🧩 **Yöntem**
- 📊 **Bulgular**

---

## 🔗 İlgili Bağlantılar
### 🧠 İlgili Kavramlar
- [[concepts/dezenformasyon.md|Dezenformasyon]]
- [[concepts/olcum-araclari.md|Ölçüm Araçları (Polarization Measurement)]]
