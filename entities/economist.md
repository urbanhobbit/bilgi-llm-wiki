---
type: entity
title: 'The Economist'
description: 'Londra merkezli haber dergisi; "Graphic detail" ve "Off the Charts" veri gazeteciliği kolları seçim, kamuoyu ve ekonomi verisini modelleyerek yayımlar. Site agresif bot korumalı ve yazıların çoğu abonelik duvarının arkasında.'
tags:
- kurum
- medya
- veri-gazeteciligi
- abonelik
timestamp: '2026-11-06T19:00:00Z'
created: '2026-11-06'
updated: '2026-11-06'
sources:
- raw/articles/2026-11-06_rosenheck-blue-wave-powered-by-moderate-democrats.md
confidence: high
---

# The Economist

Haftalık haber dergisi (1843'ten beri). Bu wiki açısından iki kolu önemli:

- **Graphic detail** — veri gazeteciliği: seçim sonuçları, anket hataları, kamuoyu eğilimleri; genelde kendi modellerini kurar (ör. "her yarış için beklenen oy payı").
- **Off the Charts** — veri ekibinin yöntem notları (log ölçek, anket hatası, vb.). Metodoloji açıklamaları için en verimli kaynak.

## Erişim davranışı (bu makinede kanıtlanmış)

| Yol | Sonuç |
|---|---|
| Doğrudan `urllib` | **403** |
| `r.jina.ai` | 200 — ama **yalnız sayfa kabuğu + başlık/deck + bir lede paragrafı**; gövde abonelik duvarında |
| Wayback / archive.today | Kayıt yok (yeni makaleler) |

Yani **başlık, alt başlık, tarih, okuma süresi ve açılış paragrafı** alınabilir; **gövde, grafik ve model sayıları alınamaz**.

## Kaynak olarak nasıl kullanılır

1. **Yalnız lede'e dayanarak bulgu aktarma.** Başlık + deck iddiayı verir (`"Our analysis shows progressives had mostly easy wins"`), ama **sayı ve yöntem doğrulanmamış** olur; kayda bu sınır yazılmalı.
2. **Modelleyen yazarın kendi özetini ayrı kaynak say.** Yazar X'te "her yarış için beklenen oy payı modelledim" diyorsa bu, makalenin **yöntem beyanı**dır; ama sonuç sayıları yine eksik.
3. **Bağımsız doğrulama mümkün:** makalenin verdiği seçim marjları seçim arşivinden (ör. elections archive `us/2026-11-03-general`) kontrol edilebilir — bu, lede'deki sayıyı doğrular, makalenin **tezini** doğrulamaz.

## Bu wiki'de The Economist kaynaklı kayıtlar

- [[raw/articles/2026-11-06_rosenheck-blue-wave-powered-by-moderate-democrats.md|Rosenheck: mavi dalgayı ılımlı Demokratlar taşıdı]] — abonelik duvarı; yalnız lede + yazarın X özeti, Michigan marjı arşivden doğrulandı.

Site: [economist.com](https://www.economist.com/)
