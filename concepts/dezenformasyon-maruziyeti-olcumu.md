---
type: concept
title: Dezenformasyon Maruziyetinin Ölçümü (Measuring Misinformation Exposure)
description: 'Sosyal medyanın dezenformasyona maruz bırakma etkisini ölçme yöntemleri: yönlendirme (referral) analizi, tıklama akışı verisi ve karşı-olgusal simülasyon.'
tags:
- kavram
- metodoloji
- dezenformasyon
- olcum
- platform-arastirmasi
timestamp: '2026-11-02T00:00:00Z'
created: 2026-11-02
updated: 2026-11-02
sources:
- raw/articles/2026-06-09_multi-platform-referrers-of-misinformation-a-compa.md
confidence: medium
---
# Dezenformasyon Maruziyetinin Ölçümü

Sosyal medyanın insanları dezenformasyona ne kadar maruz bıraktığını ölçme sorunu. Alanın büyük kısmı **yönlendirme (referral) analizi** kullanır: dezenformasyon ziyaretlerinin hemen öncesinde hangi platformun olduğunu saymak.

## İki paradigma

- **Doğrudan yönlendirici paradigması** (direct referrer): yalnızca platform ziyaretini doğrudan izleyen dezenformasyon ziyaretlerini sayar. Ucuz ve yaygın; ama platformun dolaylı etkisini görmez.
- **Gömülü yönlendirici paradigması** (embedded referrer): aracı siteler üzerinden yönlendirmeyi ve platformdan ayrıldıktan sonra süren bilgi arama davranışını da hesaba katar. Karşı-olgusal simülasyonla işletilir: "platform olmasaydı bu kişinin yolu ne olurdu?"

## Ampirik sonuç (Dahlke vd. 2026)

1.240 kişinin üç aylık tarama verisinde (21 milyon sayfa, 395.936 oturum) gömülü paradigma, doğrudan paradigmadan **1,5 ila 15+ kat** daha büyük etkiler üretiyor. Twitter'da doğrudan %2,17 iken gömülü %12,27; Facebook'ta %9,25 → %14,07; liberal dezenformasyonda Facebook %11,43 → %58,56.

## Tasarım önkoşulları

- Tıklama akışı (clickstream) veya veri bağışı (data donation) paneli — anketle ölçülemez.
- Dezenformasyon sitelerinin dış derecelendirmelerle tanımlanması (NewsGuard, fact-checker listeleri, Lin vd. kalite skorları).
- Kişi düzeyinde geçiş matrisleri + saptırma oranları (diversion ratios) ile karşı-olgusal yol simülasyonu.
- Cihaz kompozisyonunun raporlanması: etkiler masaüstünde mobilin birkaç katı çıkıyor.

## Bağlantılı

[[concepts/dezenformasyon.md|Dezenformasyon]] · [[concepts/filtre-baloncuklari.md|Filtre Baloncukları ve Yankı Odaları]]
