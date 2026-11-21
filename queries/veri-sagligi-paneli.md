---
type: query
title: "Veri Sagligi Paneli"
created: 2026-11-21
tags: [data-health, triage, maintenance]
---

# Veri Sagligi Paneli — 2026-11-21

## Ozet

- Toplam dugum: **2198**
- Ham makale: **1694** (diskte 1714 dosya)
- Kavram: **127**
- **Kavramsiz makale: 268**
- **Izole kavram: 1**
- **Bundle'a girmemis dosya: 20**
- Kavram-kavram kenar (min_cooc>=5): **241** / 978 olası cift

## Kritik Bug: ID Truncation

Bundle'daki 0 dugum ID'si 64 karakterde kesilmis.
Ornek: `raw/articles/2026-11-06_the-winning-formula-of-the-populist-radical-right-`
(gercek dosya adi `.md` ile bitiyor, ID kesik).
Bu yuzden diskteki dosyalarla eslesmiyor ve bazi makaleler grafige girmiyor.
**Duzeltme:** bundle olusturma betiginde ID normalizasyonu (`os.path.splitext`) kullan.

## Bakim Kuyrugu (oncelik sirasi)

### 1. Bundle'a girmemis 20 dosya
- `raw/articles/2026-03-26-edmo-weekly-pulse.md`
- `raw/articles/2026-04-01-edmo-weekly-pulse.md`
- `raw/articles/2026-04-16-edmo-weekly-pulse.md`
- `raw/articles/2026-04-23-edmo-weekly-pulse.md`
- `raw/articles/2026-04-30-edmo-weekly-pulse.md`
- `raw/articles/2026-05-07-edmo-weekly-pulse.md`
- `raw/articles/2026-05-07_encode-d3-4-best-practices.md`
- `raw/articles/2026-05-14-edmo-weekly-pulse.md`
- `raw/articles/2026-05-21-edmo-weekly-pulse.md`
- `raw/articles/2026-05-29-edmo-weekly-pulse.md`
- `raw/articles/2026-06-04-edmo-weekly-pulse.md`
- `raw/articles/2026-06-11-edmo-weekly-pulse.md`
- `raw/articles/2026-06-18-edmo-weekly-pulse.md`
- `raw/articles/2026-06-25-edmo-weekly-pulse.md`
- `raw/articles/2026-06-26-nature-polarization.md`
- `raw/articles/2026-06-26-pnas-heart-rate.md`
- `raw/articles/2026-07-03-edmo-weekly-pulse.md`
- `raw/articles/2026-07-09-edmo-weekly-pulse.md`
- `raw/articles/2026-07-16-edmo-weekly-pulse.md`
- `raw/articles/2026-07-24-edmo-weekly-pulse.md`

### 2. Kavramsiz makaleler (268)
`triage-queue.json` icinde listelendi. Haftalik 15 dk: LLM kavram onerir, sen onaylarsin.

### 3. Izole kavramlar (1)
- `concepts/siyasal-homogami` — Siyasal Homogami

## Yeniden Uretim

```
python3 scripts/build-weighted-graph.py
```

## Sonraki adim

MCP sunucusu (`mcp/wiki_server.py`) bu paneli `data_health` uc noktasi olarak sunacak.
