---
title: "Substack"
created: 2026-10-27
updated: 2026-10-27
type: entity
tags:
  - platform
  - newsletter
  - publishing
sources:
  - raw/articles/2026-10-27_emotions-as-global-low-dimensional-brain-flow-patterns.md
---

# Substack

Bülten (newsletter) yayıncılık platformu; akademisyenlerin ve araştırmacıların hakemsiz, serbest biçimli yazılarını yayımladığı fiilî bir kanal hâline geldi. Vault'ta bu tür kayıtlar **hakemsiz** olarak işaretlenir: bir Substack yazısı veri içerebilir ama akran değerlendirmesinden geçmemiştir.

**Künye ve tam metin:** Sayfa HTML'i JS ile render edildiği için tarayıcıda eksik görünebilir. Güvenilir yol, yazı slug'ı üzerinden **public API**: `https://<publication>.substack.com/api/v1/posts/<slug>` — `title`, `subtitle`, `post_date`, `wordcount`, `canonical_url`, `body_html`/`body_text` alanları anahtarsız gelir. Paywall sinyali: `audience` alanı (`everyone` = açık, `only_paid` = ücretli). Ücretli yazılarda yalnız `truncated_body_text` / teaser gelir — o durumda `note`'a "paywall" yazılmalı, içerik tahmin edilmemelidir.

**Bağlantılı çalışmalar:** [[raw/articles/2026-10-27_emotions-as-global-low-dimensional-brain-flow-patterns.md|Emotions as global low-dimensional brain flow patterns]] (Neural Flows / Michael W. Cole, `audience: everyone`)
