---
type: entity
title: Elections Archive
description: 'Sandık düzeyine kadar seçim sonuçlarını tutan, ajanlara anahtarsız MCP
  ve REST erişimi veren bağımsız arşiv (electionsarchive.com). Veri CC BY 4.0, kod
  AGPL-3.0; 256.160 seçim, 1923-2024 arası Türkiye verisi dahil.'
tags:
- akademik
- kuresel
- kurum
- secim-verisi
- veri-altyapisi
timestamp: '2026-11-04T04:35:00Z'
created: 2026-11-04
updated: 2026-11-04
sources:
- raw/articles/2026-11-04_elections-archive-ballot-box-level-election-result.md
---

# Elections Archive

## Genel Bakış

`electionsarchive.com` — seçim sonuçlarını **en küçük sayım birimine kadar** (ABD'de county, Türkiye'de sandık) tutan bağımsız bir arşiv. Her rakamın arkasında yayımlanmış bir kaynak var; her sonuç seti kendi lisansını kaydediyor. Veri **CC BY 4.0**, kod **AGPL-3.0**. Beta aşamasında; 4 Kasım 2026 itibarıyla 256.160 seçim.

## Ajan erişimi (anahtarsız)

| Kanal | Adres | Not |
|---|---|---|
| MCP | `https://electionsarchive.com/mcp` | streamable HTTP, okuma için anahtar yok |
| Skill | `npx skills add electarchive/electionsarchive` | Claude Code, Codex, Pi ve diğer kodlama ajanları |
| REST | `/api/v1` + `openapi.json` | arama, seçim/yarış/sayım birimi okuma |
| Sayfa biçimi | `<url>.md` / `<url>.json` ya da `Accept:` başlığı | her sayfa makine okunur |
| Özet | `llms.txt`, `agents.json` | tüm araçların listesi |

## Veri modeli

Yer → seçim → yarış → sayım birimi: `us/ga/2020-11-03-general/senate/fulton-county-ga`.

- `?vs=previous` (ya da `?vs=<seçim yolu|uuid>`) bir yarış sayfasında **her adayın ve her bölgenin önceki seçime göre puan değişimini** verir.
- `/compare?a=<uuid>&b=<uuid>` iki kişiyi, yeri veya partiyi yan yana koyar.
- `/coverage/{polity}` ve `/coverage/{polity}/gaps` kapsamı ve eksikleri şeffaf listeler.

## Canlı seçim gecesi uçları

`/api/v1/live/results?election=us/2026-11-03-general&office=senate|house|governor` ve `/live/race`.

Yanıtın `chambers` bloğu kontrol olasılığını ve beklenen sandalyeyi doğrudan verir; her yarış nesnesi `status` (called / counting / waiting), `counted` (sayılan oran), `margin`, `winner`, `isFlip`, `heldBy` alanlarını taşır.

**2026-11-04 04:27Z anlık görüntüsü:** Senato Demokrat kontrol olasılığı **%99,2**, beklenen **53-46**; Meclis Demokrat **%92,5**, beklenen **227-208**; valiliklerde 36 yarışın 18'i çağrılmış.

## Türkiye kapsaması

`/api/v1/coverage/tr`: **25.332 seçim, 27.678 yarış, 1923-2024**, en ince birim `tr.sandik` (sandık), il adları Türkçe. 2023 cumhurbaşkanlığı ilk turu API'den doğrulandı: Erdoğan %49,5, Kılıçdaroğlu %44,9, Oğan %5,2.

## Sınırlılıklar

- Beta; "called" kümesi AP/NBC'den dar ve yavaş (4 Kasım 04:27Z'de Senato'da 19 çağrı, AP/NBC'de 25).
- Ağır HTML sayfaları 30 sn'de dönebiliyor; toplu çekimde yalnızca `/api/v1` kullanılmalı.
- "Resmi sonuç" iddiası kaynak bazlı; YSK/eyalet SEC ile çapraz kontrol yine gerekli.

## Bu Wiki'de

Fırat Çiftçi'nin (@firatciftci) 2026-11-04 tarihli X gönderisiyle geldi: [[raw/articles/2026-11-04_elections-archive-ballot-box-level-election-result|kayıt sayfası]].

## İlgili

- [[concepts/abd-secim-sistemi.md|ABD Seçim Sistemi]]
- [[concepts/partizan-redistricting.md|Partizan Redistricting]]
- [[entities/pippa-norris.md|Pippa Norris]]
