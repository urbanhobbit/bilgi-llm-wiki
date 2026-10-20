---
type: concept
title: Kısa Video Haber Doğrulama (Short-Video News Verification)
description: Kısa video haberlerde başlık, görüntü, konuşma ve altyazının çapraz tutarlılığını denetleyen
  hesaplamalı doğrulama hattı; öğe düzeyi sınıflandırma ile yerelleştirilebilir çelişki arasındaki ayrım.
tags:
- kavram
- short-video
- kısa video
- video news verification
- misinformation
- multimodal
- fact-checking
timestamp: '2026-10-20T08:15:00Z'
created: '2026-10-20'
updated: '2026-10-20'
sources:
- 10.1038/s41598-026-76343-w
related:
- dezenformasyon
- media-literacy-fact-checking
confidence: medium
---

# Kısa Video Haber Doğrulama (Short-Video News Verification)

## Tanım
Kısa video haber, başlık (iddia), görüntü, konuşma ve ekran metnini (OCR) aynı anda taşır. Yanıltıcı bir
kısa video, **tek tek gerçek** bileşenlerden üretilebilir: doğru görüntü yanlış başlıkla, eski sahne güncel
olay gibi, altyazı ise konuşmanın anlamını tersine çevirecek biçimde eşleştirilebilir. Bu nedenle kısa video
doğrulaması, "içerikte sahte var mı" sorusundan çok **bileşenler arası tutarsızlığın nerede ve ne zaman
doğduğu** sorusuna bakar.

## Neden ayrı bir hat
- **Zaman yapısı:** Anlam, ardışık çekimlerin (shot) sıralı değişimiyle kurulur; tüm videoyu tek bir havuza
  indirgeyen toplulaştırma (whole-video aggregation) çelişkinin yerini görünmez kılar.
- **Kaynak görünürlüğü:** ASR/OCR eksik veya düşük güvenliyse, "çelişki yok" ile "kanıt yok" farklı şeylerdir;
  ikisini ayırmayan füzyon, sessiz kalan modaliteyi kanıt sayar.
- **Gözlem sınırı (observation boundary):** Erken uyarı veren bir sistem, ön işleme (segmentasyon, transkript,
  OCR) dahil hiçbir aşamada gelecekteki kareyi kullanmamalıdır; yalnızca nedensel dikkat (causal attention)
  bunu garanti etmez.
- **Öğe etiketi ≠ yerelleştirme:** Veri seti etiketleri öğe düzeyindedir ve her yanlış öğenin içsel bir
  çelişki içerdiğini garanti etmez; bu yüzden sınıflandırma ve aralık yerelleştirme ayrı değerlendirilir.

## Literatürdeki hatlar
- **Benchmark ve bağlam:** FakeSV (Çince, Douyin/Kuaishou; içerik + sosyal bağlam) ve FakeTT (İngilizce,
  TikTok); FakingRecipe üretim sürecini (materyal seçimi, kurgu) modeller.
- **Tutarlılık tabanlı yöntemler:** modaliteler arası uyumsuzluğu ölçen CA-FVD; ikili/küresel/token düzeyi
  tutarlılığı birleştiren ve belirsiz örnekleri VLM'e yönlendiren MAGIC³; maskelenmiş yeniden kurma + akıl
  yürütme damıtması (PCDD); zamansal hipergraf (HyperClaim).
- **VLM ve araştırmacı ajanlar:** FakeSV-VLM, Fact-R1, CSI, ExMRD; komşu video ve teyit kayıtlarıyla
  çalışan NEED. Kapasite ve bilgi erişimi farklı olduğu için skorlar doğrudan karşılaştırılamaz.
- **Tarihsel kanıt:** Yayın zamanı sorgudan önce olan teyit/çürütme kayıtlarını getirme (retrieval); buradaki
  kritik ayrım, **olay ilişkisi ≠ semantik çürütme** — aynı olayın farklı bir alt iddiasına ait kayıt
  getirilebilir.

## Tipik metrikler
Öğe düzeyi: Accuracy, Macro-F1, AUC, kalibrasyon (ECE/Brier). Yerelleştirme: ilişki P/R/F1, IoU 0.3/0.5'te
temporal AP, Top-1 isabet, ortalama tIoU. Akış (streaming): sabit gözlem sürelerinde (5/10/15/20/30 s ve EOF)
F1, kümülatif tespit oranı (CDR) ve kümülatif yanlış alarm oranı (FPR), ilk eşik geçişi gecikmesi.

## Türkiye bağlamı
TikTok, Instagram Reels ve YouTube Shorts Türkiye'de haber tüketiminin ana yüzeylerinden biri; buna karşın
Türkçe kısa video haber veri seti (FakeSV/FakeTT eşdeğeri) kamuya açık değil. Teyit, Doğruluk Payı ve
Malumatfuruş gibi kuruluşlar teyidi elle ve metin ağırlıklı yürütüyor; videonun *hangi saniyesinde* hangi
bileşenin çeliştiğini gösteren bir çıktı, editöryel önceliklendirme için doğrudan kullanışlı olurdu. Türkçe
morfolojisi ve ASR hataları, çok dilli kodlayıcı (XLM-R) üzerine kurulu hatlarda ayrıca doğrulama gerektirir.

## İlgili Makaleler
- [[raw/articles/2026-10-20_early-and-reliable-short-video-news-verification-through-eve.md|EASE-Fact: olay-farkında çekim modelleme ve çapraz-modal kanıt füzyonu (Wang, 2026)]]
