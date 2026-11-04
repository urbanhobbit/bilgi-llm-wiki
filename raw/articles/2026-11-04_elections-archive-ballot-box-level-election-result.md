---
type: raw_article
title: 'Elections Archive: ballot-box level election results with a keyless agent
  API'
description: 'Elections Archive, seçim sonuçlarını **sandık/sayım birimi düzeyine
  kadar** tutan ve ajanlara anahtarsız erişim veren bir arşiv: 256.160 seçim, her
  rakamın arkasında yayımlanmış bir kaynak, veri CC BY...'
resource: https://electionsarchive.com/agents
tags:
- kurator
- high
timestamp: '2026-11-04T04:31:14Z'
source_file: 2026-11-04_elections-archive-ballot-box-api.json
category: KURATOR
priority: high
roles:
- method
published: '2026-11-04'
---

# Elections Archive: ballot-box level election results with a keyless agent API

**Author(s):** Elections Archive (bağımsız arşiv; veri CC BY 4.0, kod AGPL-3.0). Paylaşan: Fırat Çiftçi (@firatciftci), 2026-11-04 03:32 UTC — @yagiznizipli ve @X'e yanıt

**Published:** 2026-11-04

**Source:** [https://electionsarchive.com/agents](https://electionsarchive.com/agents)

## Summary

Elections Archive, seçim sonuçlarını **sandık/sayım birimi düzeyine kadar** tutan ve ajanlara anahtarsız erişim veren bir arşiv: 256.160 seçim, her rakamın arkasında yayımlanmış bir kaynak, veri CC BY 4.0 (kaynağın kendi lisansı farklıysa o geçerli), kod AGPL-3.0. Ajan erişimi üç kanaldan: (1) **MCP sunucusu** `https://electionsarchive.com/mcp` (streamable HTTP, okuma için anahtar gerekmiyor); (2) `npx skills add electarchive/electionsarchive` ile kurulan hazır *skill* (Claude Code, Codex, Pi ve diğer kodlama ajanları); (3) **REST API** `/api/v1` + OpenAPI tanımı. Her sayfa `.md` ya da `.json` sonekiyle (veya `Accept: text/markdown|application/json` başlığıyla) makine okunur biçimde geliyor; `llms.txt` ve `agents.json` tüm araçları listeliyor. Adres şeması: yer → seçim → yarış → sayım birimi (`us/ga/2020-11-03-general/senate/fulton-county-ga`). Kritik özellik: bir yarış sayfasına `?vs=previous` ya da `?vs=<seçim yolu>` eklenince her adayın ve her bölgenin **önceki seçime göre değişimi (puan farkı)** geliyor; `/compare?a=&b=` iki kişiyi/yeri/partiyi yan yana koyuyor. Seçim gecesi için `/api/v1/live/results` (parametreler: `election`, `office`, `state`, `status`, `sort=closest|updated`) ve `/live/race` var. Yanıtın `chambers` bloğu doğrudan kontrol olasılığı ve beklenen sandalye veriyor: 2026-11-04 04:27Z itibarıyla **Senato: Demokrat kontrol olasılığı %99,2, beklenen 53-46**; **Meclis: Demokrat %92,5, beklenen 227-208**; valiliklerde 36 yarışın 18'i çağrılmış. Her yarış nesnesi `status` (called/counting/waiting), `counted` (sayılan oran), `margin`, `winner`, `isFlip`, `heldBy` alanlarını taşıyor. Türkiye kapsaması araştırma açısından asıl sürpriz: `/api/v1/coverage/tr` **25.332 seçim, 27.678 yarış, 1923-2024**, en ince birim `tr.sandik` (sandık). 2023 cumhurbaşkanlığı ilk turu API'den doğrulandı: Erdoğan %49,5, Kılıçdaroğlu %44,9, Oğan %5,2. Sınırlılıklar: site beta; 'called' kümesi AP/NBC'den dar ve yavaş (aynı dakikada Senato'da 19 çağrı vs AP/NBC 25); ağır HTML sayfaları 30 sn'de dönebiliyor, bu yüzden API/REST yolu tercih edilmeli.

## Key Points

- Kapsam: 256.160 seçim, en küçük sayım birimine kadar; her rakam kaynaklı; veri CC BY 4.0, kod AGPL-3.0.
- Ajan erişimi anahtarsız: MCP (`/mcp`, streamable HTTP), hazır skill (`npx skills add electarchive/electionsarchive`), REST `/api/v1` + OpenAPI.
- Her sayfa `.md`/`.json` soneki ya da `Accept` başlığıyla okunur; `llms.txt` ve `agents.json` makine için özet sunuyor.
- `?vs=previous` eklentisi her adayın/bölgenin önceki seçime göre puan değişimini veriyor — 'neyin değiştiği' analizi için doğrudan kullanılabilir.
- Canlı uçlar: `/live/results` (election/office/state/status, sort=closest|updated) ve `/live/race`; yanıtta kontrol olasılığı + beklenen sandalye (`chambers`).
- 2026-11-04 04:27Z: Senato Demokrat kontrol %99,2 (beklenen 53-46), Meclis Demokrat %92,5 (beklenen 227-208), valilik 18/36 çağrıldı.
- Yarış nesnesi alanları: status, counted (sayılan oran), margin, winner, isFlip, heldBy, calledAt, chance.
- Türkiye: 25.332 seçim / 27.678 yarış / 1923-2024 / sandık düzeyi; 2023 CB ilk turu API'den doğrulandı (Erdoğan 49,5 / Kılıçdaroğlu 44,9 / Oğan 5,2).
- Kapsam boşlukları `/coverage/{polity}/gaps` ile sorgulanabiliyor — hangi yıl/hangi düzey eksik şeffaf.
- Caveat: beta; 'called' kümesi AP/NBC'den geride; ağır sayfalarda HTML fetch timeout, API kullanılmalı.

## Turkey Context

Türkiye ayağı, ABD seçimi ayağından daha değerli olabilir: arşiv **sandık düzeyinde** 1923-2024 verisi tutuyor (25.332 seçim, 27.678 yarış, il adları Türkçe). Bu, Türkiye'de ilçe/sandık bazlı seçim analizi yapan araştırmacı için normalde YSK ham verisi + ayrı temizlik demek; burada hazır ve `?vs=previous` ile 2018→2023 tipi karşılaştırma tek parametre. Kutuplaşma/oy verme çalışmaları açısından üç kullanım: (1) sandık düzeyi homojenlik/heterojenlik ölçümleri, (2) seçim çevresi yeniden dağıtım etkilerinin (partizan redistricting literatürü) Türkiye'de karşılaştırmalı testi, (3) 2023 gibi kritik seçimlerde il/ilçe bazlı değişimin mekânsal görselleştirmesi. Uyarı: veri CC BY 4.0, atıf zorunlu; kapsam 2024'te bitiyor, 2028/2026 güncel seçimler için arşivin güncellenmesi beklenmeli. Ayrıca 'resmi sonuç' iddiası kaynak bazlı — YSK ile çapraz kontrol yine gerekli.

## 🏷 Retorik Roller

- 🧩 **Yöntem**
