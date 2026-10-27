---
title: "HAL Open Archive (hal.science)"
created: 2026-10-27
updated: 2026-10-27
type: entity
tags:
  - platform
  - repository
  - open-access
  - academic-institution
sources:
  - raw/articles/2026-09-25_one-sentence-at-a-time-a-quantitative-history-of.md
---

# HAL Open Archive (hal.science)

Fransa'nın ulusal açık erişim arşivi (Hyper Articles en Ligne); CNRS ve CCSD tarafından işletilir. Barındırdığı kayıtlar `hal-<id>` biçimindedir ve her sürüm ayrı numaralanır (`v1`, `v2`). Fransız sosyal bilimler, iktisat, felsefe ve bilim tarihi literatürü için en geniş ücretsiz tam metin kaynağıdır; yayıncı sürümü kapalı olan makalelerin kabul edilmiş (accepted) metinleri sıklıkla burada bulunur.

**Erişim notu (2026-10):** `hal.science` sayfaları ve `/document` PDF uç noktası **Anubis** proof-of-work duvarı ile korunuyor; düz `curl`, tarayıcı taklidi ve `r.jina.ai` render'ı challenge HTML'i döndürür, microlink `&pdf` render'ı ise yalnız arşivin PDF görüntüleyicisinin 1. sayfasını verir.

**Doğrulanmış kurtarma yolu:**
- Künye: `https://api.archives-ouvertes.fr/search/?q=halId_s:hal-<id>&wt=json` — `title_s`, `authFullName_s`, `abstract_s`, `producedDate_s`, `docType_s`, `fileMain_s`, `journalTitle_s` alanları anahtarsız gelir.
- Tam metin alternatifi: OpenAlex kaydındaki `locations[]` içinden OSF/SocArXiv, DIAL (UCLouvain), arXiv veya yayıncı sürümüne geçilir — HAL'in kendi PDF'i genellikle en zor yoldur.

**Bağlantılı çalışmalar:** [[raw/articles/2026-09-25_one-sentence-at-a-time-a-quantitative-history-of.md|One Sentence at a Time: A Quantitative History of Rationality in Economic Thought]] (hal-05431080; Anubis nedeniyle tam metin SocArXiv v3 üzerinden okundu)
