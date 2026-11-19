---
type: concept
title: Veri Bağışı (Data Donation) Yöntemi
description: Katılımcıların platformlerden indirdikleri kendi dijital verilerini (akış geçmişi, izleme süresi, arama kaydı) araştırmaya bağışlaması; öz-bildirime dayanmayan doğrudan maruz kalma ölçümü.
tags:
- kavram
- yontem
- veri-bagisi
- sosyal-medya
- olcum
timestamp: '2026-11-18T00:00:00Z'
created: '2026-11-18'
updated: '2026-11-18'
sources: []
related: []
confidence: high
---

# Veri Bağışı (Data Donation) Yöntemi

## Tanım
Katılımcı, platformun **kendi veri indirme aracıyla** (ör. TikTok/Instagram/Meta "download your data") aldığı arşivi araştırmacıya bağışlar. Araştırmacı **gerçekte ne izlendiğini** görür — anket değil, kayıt.

## Neden Önemli: Üç Ölçüm Hatasını Kapatır
| Sorun | Öz-bildirim | Veri bağışı |
|---|---|---|
| Hatırlama hatası | Yüksek (ekran süresi sistematik olarak yanlış bildirilir) | Yok |
| Sosyal istenirlik | Var ("haber okuyorum" demek daha iyi görünür) | Yok |
| Sentetik hesap | Simülasyon ≠ gerçek akış | Gerçek akış |

## Uygulama (Oostrum vd. 2026, PsyArXiv j73bg)
- **n = 147**, 16-25 yaş, ~**6,7 milyon** TikTok videosu, Ekim 2023-Mayıs 2026
- Çıkarılan alanlar: transkript, açıklama, hashtag, **izleme süresi**
- Sınıflandırma: Llama 3.1-70B, insan kodlamasıyla doğrulanmış (konu F1 = 0,80; α = 0,62-0,79)

## Sınırlar
- Yalnızca **kamuya açık** içerik; özel hesaplar ve DM kapsam dışı
- Yalnızca **metin** (transkript) → görsel/işitsel aşağılama kaçar → bulgular **alt sınır**
- **KVKK/GDPR:** akış geçmişi kişisel veri; açık rıza + anonimleştirme zorunlu
- Örneklem **kendi kendini seçer** (bağışlamayı kabul edenler)

## Türkiye Notu
Teknik engel yok (veri indirme araçları çalışıyor), asıl engel **hukuki**: KVKK açık rıza + etik kurul. Türkiye'de moderasyon testi **kopyalanamaz** çünkü AB DSA şeffaflık veritabanı eşdeğeri yok.

## İlgili Kavramlar
- [[concepts/nefret-soylemi.md|Nefret Söylemi]]
- [[concepts/platform-seffaflik.md|Platform Şeffaflığı]]
- [[concepts/olcum-araclari.md|Ölçüm Araçları]]

## İlgili Makaleler
- [[raw/articles/2026-11-18_news-politics-societal-issues-and-hate-on-youths-d.md|Oostrum vd. (PsyArXiv 2026) — gençlerin bağışlanmış TikTok akışları]]
