---
type: concept
title: Kolektif Zeka ve Grup Kararı
description: Grupların dağıtılmış bilgiyi bir araya getirerek karar vermesi; bilgi paylaşımı (availability) ile bilgi kullanımı (integration) arasındaki kopukluk ve AI kolaylaştırıcıların rolü.
tags:
- kavram
- kolektif-zeka
- karar-alma
- yapay-zeka
- hidden-profile
timestamp: '2026-11-18T00:00:00Z'
created: '2026-11-18'
updated: '2026-11-18'
sources: []
related: []
confidence: medium
---

# Kolektif Zeka ve Grup Kararı

## Tanım
Grupların tek tek üyelerin bilgisinden daha iyi (ya da daha kötü) karar vermesi. Klasik sorun: **hidden profile** — kritik bilgi üyelere **asimetrik** dağıtıldığında gruplar paylaşılan (ortak) bilgiyi tartışıp **eşsiz bilgiyi** konuşmuyor; sonuç, herkesin bildiğini tekrarlayan ve çoğu zaman **yanlış** bir karar.

## Temel Ayrım: Availability ≠ Integration
- **Availability (bulunurluk):** doğru bilginin masaya gelmesi.
- **Integration (bütünleştirme):** gelen bilginin nasıl tartıldığı, yorumlandığı ve karara dönüştüğü.
- Kanıt (Alsobay vd. 2026, CSCW): LLM kolaylaştırıcı **availability**'yi ciddi biçimde artırıyor (d = 0,61), ama **integration**'a dokunmadığı için **karar kalitesi değişmiyor**.

## Kolaylaştırma Bulguları (Alsobay vd. 2026)
| Ölçüt | Sonuç |
|---|---|
| Paylaşılan bilgi | LLM vs yok: **+2,9 bilgi**, d = 0,61 (p<0,001); insan kolaylaştırıcı ve tek mesaj **anlamlı fark yaratmadı** |
| Mekanizma | **Minimum** katkı artıyor, maksimum değişmiyor → **sessiz üye** konuşuyor (extensive margin) |
| Herkesin katkı verdiği grup | **%61** (LLM) vs %39-47 (diğerleri) |
| Kolaylaştırıcı davranışı | Üyeye doğrudan seslenme: **%68 (LLM)** vs %25 (insan); her grupta ulaşma: LLM %100, insan %77 |
| Karar kalitesi | Optimal seçim %31/%21/%30/%23 — **anlamlı fark yok** (p=0,42) |

## Neden Önemli
- \"Daha fazla bilgi paylaşımı daha iyi karar getirir\" varsayımı **yanlış** olabilir.
- AI kolaylaştırıcıların gerçek katma değeri **süreç adaleti ve katılım** tarafında (herkes konuşuyor, bilgi dengeli yayılıyor), **karar isabeti** tarafında değil.

## İlgili Kavramlar
- [[concepts/muzakereci-demokrasi.md|Müzakereci Demokrasi]]
- [[concepts/cok-ajanli-etnografya.md|Çok-Ajanlı Etnografya]]
- [[concepts/sentetik-odak-gruplari.md|Sentetik Odak Grupları]]

## İlgili Makaleler
- [[raw/articles/2026-09-23_bringing-everyone-to-the-table-an-experimental-stu.md|Alsobay, Rothschild, Hofman & Goldstein (CSCW 2026) — LLM kolaylaştırmalı grup kararı]]
