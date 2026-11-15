---
type: raw_article
title: 'Agent Reach: one CLI giving agents access to login-walled platforms'
description: 'Ajanlara **giriş duvarı arkasındaki platformları** açan bir CLI: X,
  Reddit, YouTube, Bilibili, XiaoHongShu, V2EX, Xueqiu, LinkedIn, Facebook, Instagram
  için `agent-reach <kanal> <eylem>` biçiminde tek...'
resource: https://github.com/Panniantong/Agent-Reach
tags:
- genel
- low
timestamp: '2026-11-15T18:18:24Z'
source_file: 2026-02-24_agent-reach-cli-agent-internet-access.json
category: GENEL
priority: low
published: '2026-02-24'
---

# Agent Reach: one CLI giving agents access to login-walled platforms

**Author(s):** Neo Reid (Panniantong) ve katkıcılar — 470+ commit'in 423'ü tek yazarda (LohseZSai 18, nyxst4ck 9, diğerleri ≤5)

**Published:** 2026-02-24

**Source:** [https://github.com/Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach)

## Summary

Ajanlara **giriş duvarı arkasındaki platformları** açan bir CLI: X, Reddit, YouTube, Bilibili, XiaoHongShu, V2EX, Xueqiu, LinkedIn, Facebook, Instagram için `agent-reach <kanal> <eylem>` biçiminde tek komut, çıktı **JSON** (ajan tüketimi için tasarlanmış: `ok`, `result`, `error.hint`). README'de hedef ajanlar arasında **Hermes Agent** açıkça sayılıyor. Mimari fikri, bu wiki'nin kendi 'rota merdiveni' pratiğiyle aynı: her platform-eylem için **sıralı yedekli araç listesi** (ör. Bilibili'de önce bili-cli, sonra kamuya açık API; web okumada önce Jina Reader, sonra Exa) — platform değişince yalnız liste güncelleniyor, ajan tarafı sabit kalıyor. Kanallar üç kademede: **varsayılan** (bilibili, v2ex, github, youtube, web — giriş gerekmez), **opsiyonel** (xiaohongshu, xueqiu, reddit, linkedin, boss, xiaoyuzhou), **deneysel** (twitter, facebook, instagram — 'platform anti-scraping daha sert, her an bozulabilir'). Bağımlılık yükü küçük (requests, loguru, pyyaml, sabitlenmiş yt-dlp), ruff+mypy yapılandırması var. **Güvenlik duruşu:** tasarım gereği salt-okunur (paylaşma/yorum/beğeni/DM yok), kimlik bilgisi istemiyor, tüm durumu `~/.agent-reach/` altında tutuyor, kimlik sızdırma/URL güvenliği için ayrı testler var. **Riskler (kritik):** (1) kurulum yolu **ajanın kendi kendine çalıştırdığı** bir belge — `curl -LsSf astral.sh/uv | sh` + `uv tool install <release zip>`; repoya yapılacak bir saldırı doğrudan makinede kod çalıştırmak demek, bu yüzden sürüm sabitlenip artefakt doğrulanmalı; (2) **PyPI'da `agent-reach` adı bu proje DEĞİL** — README bunu açıkça uyarıyor, yani isim çakışması/typosquat riski mevcut; (3) girişli kanallarda **kullanıcının Chrome çerezlerini** kendi özel tarayıcısına kopyalıyor ('ana hesap' uyarısı ve 'küçük hesap kullanın' tavsiyesi README'de var) — hesap kapatma ve ToS ihlali riski; (4) **tek kişiye bağımlılık** ve sponsor gelirinin proxy/tarama sağlayıcılarından (Bright Data, RapidProxy, BrowserAct) gelmesi, 'ücretsiz API' vaadinin kırılgan kısmını tam da buraya yıkıyor.

## Turkey Context

Bu depo **boru hattı uyumu** açısından koşullu değerli, ama genel bir 'internet erişimi' aracı olarak değil. Türkiye araştırma hattı için dört değerlendirme: **(1) X kanalı: HAYIR.** Bu wiki'nin X rotası `api.fxtwitter.com` üzerinden girişsiz çalışıyor, ToS riski yok ve kararlı; Agent Reach'in twitter kanalı 'deneysel', girişe ve çerez kopyalamaya dayalı, üstelik veri merkezi IP'sinden giriş challenge'ı yiyeceği için cron işlerinde güvenilmez. Gerçek hesabın çerezini bir CLI'ya kopyalamak, günlük iş akışında kabul edilemez bir risk. **(2) Reddit / LinkedIn / Facebook / Instagram: şimdilik HAYIR** — aynı gerekçe (giriş + deneysel). **(3) Çin platformları: EVET, ama dar kapsamda.** Bilibili altyazıları, XiaoHongShu notları, V2EX tartışmaları ve Xueqiu verisi, genel aramanın gerçekten zayıf olduğu alanlar; AI yönetişimi ve platform politikası yazılarında 'Çin'de platform düzenlemesi nasıl tartışılıyor' sorusu için birincil malzeme sağlar. Bu kanallar **varsayılan** kademede (bilibili, v2ex) veya girişli opsiyonel kademede; Bilibili/V2EX girişsiz çalıştığı için sunucuda risksiz denenebilir. **(4) Kurulum disiplini.** Sunucu headless olduğu için 'Chrome'dan çerez kopyalama' adımı zaten işlemez; QR/kod ile giriş ise GUI ister. Yani bu makinede yalnız **girişsiz kanallar** anlamlı. Öneri: `uv tool install` ile sürüm sabitlenmiş kurulum, yalnız varsayılan kanallar (`bilibili`, `v2ex`, `github`, `youtube`, `web`), X/Reddit/IG kanalları **kapalı**; kurulumu ajanın kendi kendine çalıştırdığı `install.md` yoluyla değil, release zip'i elle indirip inceleyerek yapmak. YouTube ASR katkısı (Groq Whisper) mevcut `youtube-content` becerisiyle örtüşüyor — marjinal.

---

## 🔗 İlgili Bağlantılar
### 🏛 İlgili Kurum/Kişiler
- [[entities/github-com.md|Github Com]]
