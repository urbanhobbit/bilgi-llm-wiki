---
type: concept
title: Askeri Doktrin ve Ulusal Güvenlik Stratejisi Metinleri
description: 'Devletlerin kendi güvenlik tehditlerini nasıl adlandırdığını ölçen birincil
  kaynak türü: ulusal güvenlik stratejileri, savunma beyaz kitapları ve askeri doktrinler.
  Gannon (2026) külliyatı üzerinden metin-madenciliği ile karşılaştırmalı analiz.'
tags:
- kurator
- national-security-strategy
- text-as-data
- military-doctrines
- comparative-politics
timestamp: '2026-11-27T14:00:00Z'
created: 2026-11-27
updated: 2026-11-27
sources:
- raw/articles/2026-11-27_military-doctrines-nss-corpus-gannon.md
related:
- metin-madenciligi
- electoral-nationalization
- affective-polarisation
confidence: medium
---

# Askeri Doktrin ve Ulusal Güvenlik Stratejisi Metinleri

## Tanım

Devletin kendi güvenlik tehditlerini, düşmanlarını ve önceliklerini resmi olarak tanımladığı **birincil belge** türü. Anket verisi öznel beyana, haber verisi medya filtresine dayanırken; ulusal güvenlik stratejisi belgesi devlet aygıtının kendi çerçevelemesini doğrudan verir. Bu nedenle "tehdit algısı"nı ölçmenin en doğrudan — ama en az kullanılan — yoludur.

## Belge Türleri

- **National Security Strategy (NSS)** — hükümetin bütününü kapsayan, başbakan/cumhurbaşkanı düzeyinde onaylanan genel strateji. Karşılaştırmalı analizde en değerli ama en seyrek tür.
- **Defense White Paper** — savunma bakanlığı çıkışlı, silahlı kuvvetler odaklı beyaz kitap. Avrupa ve Asya'da NSS'ten daha yaygın.
- **Military Doctrine** — silahlı kuvvetlerin operasyonel doktrini; tehdit tanımından çok kuvvet kullanımına odaklanır.
- **Sektörel stratejiler** — siber güvenlik, terörle mücadele, yapay zekâ stratejisi. Tehdit tanımı içerir ama kapsamı dardır.

## Metin Olarak Analiz (text-as-data)

- **Tehdit çerçevelemesi:** Hangi aktörler "tehdit" olarak adlandırılıyor; sıralama yıllar içinde nasıl değişiyor.
- **Stratejik kültür:** Aynı tehdide farklı devletlerin verdiği yanıtın söylemsel farkı (savunmacı/revizyonist, çok taraflı/tek taraflı).
- **Devletlerarası ilişki ölçümü:** Bir devletin diğerini metinde anma biçimi (nötr / işbirlikçi / düşmanca) ikili ilişki göstergesi olarak kullanılabilir — Gannon'un working paper'ının yöntemi.
- **Zaman serisi kırılmaları:** 1991, 2001, 2014, 2022 gibi dönüm noktalarının strateji metinlerine yansıması.

## Veri Altyapısı

Gannon (2026) külliyatı: 823 belge, 112 ülke/bölge/örgüt, 1962–2025, CC0 lisans, PDF + tam metin + 128-token chunk katmanları. Detay: [[raw/articles/2026-11-27_military-doctrines-nss-corpus-gannon.md]]. Bu, alanın şu anki en geniş açık veri seti; önceki çalışmalar tek ülke veya 10–20 belgelik el yapımı örneklemlere dayanıyordu.

## Sınırlılıklar

- **Yayın yanlılığı:** Gizli tutulan stratejiler veri setinde yok; "erişilebilen belgeler" külliyatı, "var olan belgeler" külliyatı değil.
- **Dil yanlılığı:** İngilizce olmayan belgeler çevrilmemiş; İngilizce metin analizi yapan çalışmalar sistematik olarak İngilizce yayın yapan devletlere yanlı olur.
- **Tür homojenliği varsayımı:** "NSS" tanımı ülkeden ülkeye değişiyor; aynı etiket altındaki belgeler farklı kurumsal statülerde olabilir (kanun, kararname, bakanlık planı). Türkiye örneğinde bir "Stratejik Plan"ın NSS sayılması bu sorunu görünür kılıyor.
- **Belge sayısı ≠ kapasite:** 38 belgeyle Avustralya'nın listenin başında olması, askeri kapasiteden çok kurumsal yayın pratiğini yansıtıyor.

## Türkiye Bağlantısı

Külliyatta Türkiye'den yalnızca 5 belge var (2000 ve 2007 savunma beyaz kitapları, 2013 siber güvenlik stratejisi, 2019 Stratejik Plan, 2021 yapay zekâ stratejisi). 2007 sonrası genel bir ulusal güvenlik stratejisi belgesinin bulunmaması iki şekilde okunabilir: (a) belge üretilmiyor, (b) üretiliyor ama kamuya açık değil. Her iki durumda da Türkiye'nin tehdit çerçevelemesi karşılaştırmalı metin analizinde **veri boşluğu** olarak duruyor — bu, MGK/Savunma Bakanlığı arşivlerine dayanan bir tamamlayıcı çalışma için doğal bir araştırma sorusu.
