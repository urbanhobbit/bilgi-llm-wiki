---
type: raw_article
title: Early and reliable short-video news verification through event-aware shot modeling
  and cross-modal evidence fusion
description: Jiaxuan Wang'ın (Pingdingshan Üniversitesi, Gazetecilik ve İletişim Okulu)
  Scientific Reports makalesi, kısa video haberlerde yanıltıcı anlatıların çoğu zaman
  'tek tek gerçek' bileşenlerden kurulduğu ...
resource: https://www.nature.com/articles/s41598-026-76343-w
tags:
- kurator
- high
timestamp: '2026-10-20T08:04:18Z'
source_file: 2026-10-20_short-video-news-verification-ease-fact.json
category: KURATOR
priority: high
roles:
- gap
- method
- result
- limitation
published: '2026-10-19'
---

# Early and reliable short-video news verification through event-aware shot modeling and cross-modal evidence fusion

**Author(s):** Jiaxuan Wang (School of Journalism and Communication, Pingdingshan University, Pingdingshan, Henan, Çin)

**Published:** 2026-10-19

**Source:** [https://www.nature.com/articles/s41598-026-76343-w](https://www.nature.com/articles/s41598-026-76343-w)

## Summary

Jiaxuan Wang'ın (Pingdingshan Üniversitesi, Gazetecilik ve İletişim Okulu) Scientific Reports makalesi, kısa video haberlerde yanıltıcı anlatıların çoğu zaman 'tek tek gerçek' bileşenlerden kurulduğu saptamasından hareket ediyor: doğru görüntü yanlış başlıkla, eski sahne güncel olay gibi, altyazı konuşmanın anlamını tersine çevirecek biçimde eşleştirilebiliyor. Bu yüzden tüm videoyu tek havuzda toplayan (whole-video aggregation) ve modaliteleri ayrım gözetmeden birleştiren (undifferentiated fusion) yaklaşımların iki şeyi görünmez kıldığını savunuyor: çelişkinin *hangi anda* doğduğu ve çelişen kaynağın *güvenilir olup olmadığı*. Önerdiği EASE-Fact çerçevesi dört parçadan oluşuyor. (1) Sıralı görsel birimler üzerinde, başlık koşullu geçişleri yakalayan nedensel bir 'olay evrimi' transformatörü (CEET): her çekim için öğrenilmiş bir geçiş vektörü üretiliyor, zaman farkı yanlılığı (time-gap bias) ve nedensel maske ile yalnızca geçmiş birimler kullanılıyor; tanısal fark Δ_i = h_i − h_{i−1} çelişkinin yerini işaretliyor. (2) Tiplendirilmiş çapraz-modal ilişkileri (C–V, C–A, C–O, V–A, V–O) modelleyen ve her ilişkiye güvenilirlik ağırlığı veren bir yönlendirici (RCER): ASR güveni, OCR karakter güveni, ses/görüntü geçerli-kare oranından türetilen kalite katsayısı dikkat skoruna katılıyor; böylece 'çelişki yok' ile 'kanıt yok' ayrılıyor (görünürlük maskesi + kalite yanlılığı + eksiklik okuma katmanı). (3) Tam video sınıflandırması veren Core modeli ve ayrı eğitilmiş, önek-yerel (prefix-local) ön işleme ile 'taahhüt edilmiş' transkriptlere dayanan akış (streaming) konfigürasyonu — böylece gözlem sınırı yalnızca dikkat katmanında değil, segmentasyon/ASR/OCR/getirme hattında da korunuyor. (4) Full modeli: sorgunun yayın zamanından önceki teyit/çürütme kayıtlarını getiren (BM25 + yoğun retrieval, RRF füzyonu, 5 adaylık çapraz-kodlayıcı çürütme sınıflandırıcısı) ve kullanılabilir kanıt yoksa Core tahminini birebir koruyan tarihsel kanıt dalı. Değerlendirme FakeSV (Çince, Douyin+Kuaishou) ve FakeTT (İngilizce, TikTok) üzerinde yürütülüyor. Core, Macro-F1'de FakeSV'de %91,51, FakeTT'de %90,13 elde ediyor; Full FakeSV'de %92,60'a çıkıyor (+1,09 puan, eşleştirilmiş GA [0,53; 1,71]). Aynı omurga üzerinde birleştirme (concat) %82,22 ve FakingRecipe %84,96'da kalıyor. Ancak güçlü VLMs karşılaştırmalarında fark istatistiksel olarak anlamlı değil: FakeSV-VLM'e karşı +1,66 puan GA [−0,05; 3,45] (Holm p = 0,155); MAGIC³-içerik'e karşı +1,36 [−0,16; 2,94]. Tarihsel kanıt dalının kazancı da büyük ölçüde 'aynı olay' kayıtlarından geliyor: aynı olay dışlandığında kazanç +0,41 puana, kapsam %36,16'dan %18,82'ye düşüyor; olay-ayrık (event-disjoint) beş katlamada Core %89,76 ± 0,54, Full %90,11 ± 0,49. Makalenin asıl metodolojik katkısı bu dürüstlük: yazarlar kendi çerçevesinin 'genel fact-checking' değil, *denetlenebilir bir ön tarama/önceliklendirme* aracı olduğunu, iç çelişkinin olgusal yanlışlık kanıtı sayılamayacağını ve akış hattının geleceğe bakmadığının 1.200 karşılaştırmada sıfır olasılık farkıyla gösterildiğini açıkça yazıyor.

## Key Points

- Künye: Scientific Reports, 19 Ekim 2026, DOI 10.1038/s41598-026-76343-w; tek yazar (Jiaxuan Wang, Pingdingshan Üniversitesi, Henan/Çin); CC BY-NC-ND açık erişim. Yayınlanan sürüm 'Accelerated Article Preview' — kabul edilmiş ama dizgi öncesi metin; Crossref'te kaynakça sayısı henüz 0, bu yüzden atıf sayısı/etki değerlendirmesi için erken.
- Sorun tanımı: kısa video haber başlık + görüntü + konuşma + ekran metni taşır; yanıltıcı anlatı bileşenlerin her biri gerçekken doğar. Tüm videoyu toplayan modeller çelişkinin zamanını, modaliteleri ayrım gözetmeden birleştiren modeller ise kaynağın güvenilirliğini gizler.
- Veri: FakeSV (Çince, Douyin + Kuaishou) kronolojik ikili bölünmesi 2.536/546/542 (eğitim/doğrulama/test), toplam 3.624 öğe (1.814 gerçek, 1.810 yanlış), ortalama süre 39,88 sn; FakeTT (İngilizce, TikTok) 1.393/299/299, toplam 1.991 (ortalama 47,69 sn). FakeSV testi 238 gerçek + 304 yanlış, 206 olay; eğitim ve test 162 olayı paylaşıyor.
- Tarihsel kanıt envanteri: 1.871 teyit/çürütme kaydı ikili etiketlerden ayrı; kronolojik protokolde yalnızca eğitim dönemine ait 1.466 kayıt kullanılabilir. Olay-ayrık protokolde 1.145 kayıt uygun, 726 kayıt dışlanıyor.
- Ana sonuç (tam video, Macro-F1, 5 tohum ortalaması): Core %91,51 ± 0,24 (FakeSV) ve %90,13 ± 0,30 (FakeTT); Full %92,60 ± 0,29 (FakeSV). Aynı-omurga concat %82,22, FakingRecipe %84,96, FakeSV-VLM %89,84, MAGIC³-içerik %90,14.
- İstatistiksel sınır: FakeSV-VLM'e karşı fark +1,66 puan ama %95 GA [−0,05; 3,45] ve Holm p = 0,155; MAGIC³-içerik'e karşı +1,36 [−0,16; 2,94]. Yani gözlenen ortalama daha yüksek, fakat %5 düzeyinde üstünlük kurulmuş değil. GA'lar 10.000 olay-blok bootstrap; permütasyon testleri olay bloğu değişimiyle.
- Tarihsel kanıtın gerçek büyüklüğü: Full–Core farkı +1,09 puan (GA [0,53; 1,71]) ama aynı-olay kayıtları dışlandığında +0,41 puana, kapsam %36,16 → %18,82'ye iniyor; olay-ayrık katlamalarda fark +0,35. Başka bir deyişle kazancın önemli kısmı 'benzer olayı hatırlama'dan geliyor, görülmemiş olaya genellemeden değil.
- Akış (streaming) performansı: gerçek zamanlı gözlem sınırında FakeSV Core-online 5/10/20/30 sn ve EOF'ta %79,63 / %84,58 / %88,76 / %90,28 / %91,22; Full-online %81,47 / %85,96 / %89,89 / %91,17 / %92,13. FakeTT Core-online 20 sn'de %86,07, EOF %89,62.
- Uyarı üretimi: doğrulama kümesinde kümülatif yanlış-alarm oranı ≤ %5 kısıtıyla kilitlenen eşiklerle, FakeSV'de kümülatif tespit oranı EOF'ta %90,13 (Core) / %92,43 (Full), yanlış alarm EOF'ta %4,62 / %4,20; FakeTT Core %90,34 tespit, %4,88 yanlış alarm. İlk eşik geçişi anında uyarı veriliyor, sonraki olasılıklar uyarıyı geri almıyor.
- Geleceğe-bakmama kanıtı: 20 sn'de hâlâ süren 100 FakeSV videosunda 10/20 sn sonrası içerik değiştirilip karıştırılıp uzatıldığında (2 model × 2 gözlem anı × 3 düzenleme × 100 video = 1.200 karşılaştırma) olasılık farkı, sınıf değişimi ve verilmiş uyarı değişimi sıfır. Kısıt: deterministik uygulama ve test edilen düzenlemelerle sınırlı.
- Bileşen katkıları (FakeSV, Macro-F1): başlık koşullamayı kaldırmak %89,43, öğrenilmiş durum artımını kaldırmak %89,98, zaman-farkı yanlılığını kaldırmak %90,50, güvenilirlik yanlılığını kaldırmak %90,12; yerelleştirme kaybını kaldırmak öğe F1'ini az etkilerken ilişki AP'sini %89,54'ten %77,12'ye düşürüyor — öğe düzeyi doğruluk yerel açıklamayı doğrulamıyor.
- Eksik kaynak dayanıklılığı: ASR+OCR birlikte kaybolduğunda sıfır-doldurma %86,48, yalnız maskeleme %87,79, tam RCER %88,61; kalibrasyon hatası (ECE) sırasıyla %6,72 / %5,30 / %4,41. Sıcaklık ölçekleme (Core T=1,37; kapsanan Full T=1,29) ECE'yi %5,62→%2,34 ve %4,71→%1,89'a indiriyor.
- Manuel yerelleştirme (asıl sınır): 64 olaydan 120 özgün FakeSV videosu (80 yanlış, 40 gerçek); yanlışların yalnızca 54'ünde yerelleştirilebilir çelişki var (67 aralık), 26'sında yok — 19'u dış olgusal bilgi gerektiriyor, 7'sinde iddia granülerliği belirsiz. İlişki P/R/F1 %78,46/75,20/76,80; IoU 0,3/0,5'te temporal AP %68,92/54,67; Top-1 %74,07 (40/54); ortalama tIoU %48,36. Gerçek 40 videonun 4'ünde yanlış çelişki (%10, video başına 0,125 sahte aralık).
- Hesaplama maliyeti: Core içerik ağı ≈553,68M parametre (DINOv2 86,58M, VideoMAE 86,22M, XLM-R 278,04M, WavLM 94,70M, yeni 8,14M); Full +0,41M. Whisper-large-v3 (1.543,49M), TransNetV2 (4,99M) ve PP-OCRv4 (15,80M) eklenince tam hat ≈2.118M. 40 sn'lik referans girdide P50/P95 gecikme: içerik ağı 2,41/3,96 sn, tam hat 9,84/16,37 sn; tepe bellek 11,96/12,48 GB (RTX 4090, BF16). Özellikler önbellekteyken füzyon 0,043/0,081 sn.
- Eğitim bütçesi: Core 5 tohum için 21,40 GPU-saat (FakeSV) ve 14,75 GPU-saat (FakeTT); olay-ayrık 5 katlama × 5 tohum ≈106,25 GPU-saat. Ayar seçimi yalnızca doğrulama kümesinde: RRF eşiği 0,35 ve çürütme olasılığı eşiği 0,60 (doğrulama Macro-F1 %92,18; kapsam %37,00; EOF yanlış pozitif %6,23).
- Sınırlar (yazarların kendi beyanı): etiketler öğe düzeyinde ve artık belirsizlik taşıyor; manuel alt küme küçük ve 26 yanlış öğe içsel olarak yerelleştirilemiyor; ASR/OCR güveni anlamsal doğruluğun zayıf vekili (eksik olumsuzlama veya yanlış sayı/birim iddiayı tersine çevirebiliyor); tüm modalitelerde tutarlı biçimde tekrarlanan yanlış yer/tarih hiç iç çelişki bırakmıyor; retrieval aynı olayın farklı alt iddiasına ait kaydı getirebiliyor (olay ilişkisi ≠ semantik çürütme); yalnızca Çince ve İngilizce platformlar — başka dil, son dakika haberi, hiciv veya eşgüdümlü yükleme kampanyalarına aktarım gösterilmedi.
- Tekrar üretilebilirlik: veri FakeSV/FakeTT (HuggingFace: Celina-love-sweet/FakeSV-VLM_data); kod Zenodo 10.5281/zenodo.23237961; tahmin kayıtları, bölünme listeleri ve manuel anotasyonlar yazara talep üzerine. Tek yazarlı ve fon dışı bir çalışma.

## Turkey Context

Türkiye için bu makalenin değeri, yönteminden çok ölçüm disiplininde: kısa video (TikTok, Reels, Shorts) Türkiye'de haber tüketiminin ana yüzeylerinden biri ve 2023 seçimleri ile 2024 yerel seçimlerinde videolu yanlış bilgi örnekleri (deprem görüntülerinin yeniden dolaşıma sokulması, 'sandık kayması' videoları, göçmen karşıtı kurgusal klipler) tekrar tekrar gündeme geldi; buna karşın Türkçe kısa video haber veri seti kamuya açık değil, Teyit / Doğruluk Payı / Malumatfuruş gibi kuruluşlar teyidi elle ve ağırlıklı olarak metin üzerinden yürütüyor. (1) Doğrudan aktarım zor: model FakeSV/FakeTT üzerinde eğitilmiş, Türkçe veri yok; XLM-R tabanlı kodlayıcı çok dilli olsa da Türkçe ASR (Whisper) hataları, eklemeli morfoloji ve altyazı/OCR kalitesi kalibrasyonu bozar — yeniden eğitim olmadan kullanmak yanıltıcı olur. (2) Aktarılabilir olan tasarım: yayın zamanı öncesi teyit kayıtlarını getirme (temporal admissibility), 'kanıt yok' ile 'çelişki yok' ayrımı ve akış hattında geleceğe bakmama denetimi, Türkçe bir hatta olduğu gibi taşınabilir. (3) Kurumsal kullanım açısından gerçekçi vaat, editöryel önceliklendirme: yüz binlerce videoyu tek tek izlemek yerine 'hangi saniyede hangi bileşen çelişiyor' çıktısıyla insan doğrulayıcıya sıra vermek. Makalenin kendi uyarısı burada kritik: bu bir 'doğruluk' üretmiyor, iç çelişki gösteriyor; dış olgu gerektiren 19/26 örnekte olduğu gibi, Türkiye'deki tipik yanlış bilgi de çoğunlukla dış kaynaktan doğrulanmayı gerektirir. (4) Düzenleme tarafı: RTÜK ve 2025–2026 dijital düzenlemeleri dezenformasyonla mücadelede 'içerik kaldırma' ekseninde tartışılırken, bu tür bir ön tarama katmanı sansür riski taşımadan şeffaflık/denetim aracı olarak konumlandırılabilir; ancak skorların kamuya açık 'yanlış' damgası olarak kullanılmaması şartıyla.

## 🏷 Retorik Roller

- 🔍 **Araştırma Boşluğu**
- 🧩 **Yöntem**
- 📊 **Bulgular**
- ⚠️ **Sınırlılıklar**

---

## 🔗 İlgili Bağlantılar
### 🧠 İlgili Kavramlar
- [[concepts/kisa-video-haber-dogrulama.md|Kısa Video Haber Doğrulama (Short-Video News Verification)]]
- [[concepts/media-literacy-fact-checking.md|Media Literacy and Fact-Checking (Medya Okuryazarlığı ve Doğrulama)]]
### 🏛 İlgili Kurum/Kişiler
- [[entities/nature-com.md|Nature Com]]
