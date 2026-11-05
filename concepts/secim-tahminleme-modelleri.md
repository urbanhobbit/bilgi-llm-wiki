---
type: concept
title: Seçim Tahminleme Modelleri (Election Forecasting)
description: 'Seçim sonuçlarını önceden kestirmeye yönelik model aileleri: siyasal iktisat/fundamentals modelleri, anket ortalamaları, eyalet düzeyi modeller, bahis piyasaları ve AI tabanlı simülasyonlar; 2026 ABD ara seçimleri özel sayısı üzerinden.'
tags:
- kavram
- secim
- tahminleme
- anket
- abd
- modelleme
timestamp: '2026-11-05T00:00:00Z'
created: 2026-11-05
updated: 2026-11-05
sources:
- raw/articles/2026-10-20_forecasting-the-2026-us-midterm-elections-ps-polit.md
confidence: medium
---

# Seçim Tahminleme Modelleri

Seçim sonucunu önceden kestirmek için kullanılan model aileleri. Her aile farklı bir sinyale dayanır ve farklı biçimde yanılır:

| Aile | Sinyal | Zayıf nokta |
|---|---|---|
| **Fundamentals / siyasal iktisat** | Ekonomi, onay oranı, görevde kalma süresi | Kampanya ve aday etkilerini kaçırır; "normal" dönem varsayar |
| **Anket ortalamaları** | Kamuoyu yoklamaları | Sistematik örneklem/katılım hatası; ortak önsel → ortak hata |
| **Eyalet/tek yarış modelleri** | Bölge düzeyi demografi ve geçmiş | Veri seyrekliği; sınır değişikliklerine duyarlı |
| **Bahis piyasaları** | Fiyat = olasılık | Manipülasyon, likidite, aşırı güven |
| **AI / sentetik persona** | LLM ile seçmen simülasyonu | Eğitim verisi yanlılığı, kalibrasyon eksikliği |

## Neden oybirliği uyarı işaretidir

2026 ABD ara seçimlerinde Meclis için **12/12 tahmin** aynı yönü gösterdi ve tuttu. Ama oybirliği bağımsız doğrulama değildir: modeller aynı anket ortalamasını ve aynı "iktidar partisi kaybeder" önselini paylaştığında **hataları da paylaşır**. Aynı yapı Türkiye'de 2023 seçimlerinde anket şirketlerinin topluca yanılmasında görüldü.

## 2026 dersi

Senato tahminlerinde çoğunluk dar bir Cumhuriyetçi zafer bekliyordu; Demokratlar çoğunluğu aldı. Tahmin hatasının kaynağı üç başlıkta aranmalı:
1. **Model hatası** — fundamentals değişkenleri 2026'yı temsil etmiyor.
2. **Veri hatası** — anketler/örneklemler sapmalı.
3. **Rejim değişikliği** — kutuplaşma, seçim ortası redistricting, emeklilik dalgası gibi yapısal kırılmalar.

Bu üçünü ayırmadan "model yanıldı" demek, bir sonraki seçim için hiçbir şey öğretmez.

## Bağlantılı

- [[raw/articles/2026-10-20_forecasting-the-2026-us-midterm-elections-ps-polit.md|Forecasting the 2026 US Midterm Elections — PS özel sayısı]]
- [[concepts/abd-secim-sistemi.md|ABD Seçim Sistemi]]
- [[concepts/olcum-araclari.md|Ölçüm Araçları]]
