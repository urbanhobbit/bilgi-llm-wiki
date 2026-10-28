---
type: raw_article
title: 'Read the Paper, Write the Code: Agentic Reproduction of Social-Science Results'
description: 'Sosyal bilimlerde tekrarlanabilirlik (reproducibility) tartışmasını
  ajan sistemlerine taşıyan bir ön baskı. Soru net: bir makalenin **kodunu hiç görmeden**,
  yalnızca yöntem anlatımı ve özgün veriyle s...'
resource: https://arxiv.org/abs/2604.21965
tags:
- kurator
- akademik
- high
timestamp: '2026-10-28T16:48:28Z'
source_file: 2026-10-28_batch-user-links-1-agentic-reproduction.json
category: AKADEMİK ÖZEL; KURATOR
priority: high
roles:
- method
- result
- gap
- policy
published: '2026-04-23'
---

# Read the Paper, Write the Code: Agentic Reproduction of Social-Science Results

**Author(s):** Benjamin Kohler; David Zollikofer; Alexander Hoyle; Elliott Ash; Johanna Einsiedler

**Published:** 2026-04-23

**Source:** [https://arxiv.org/abs/2604.21965](https://arxiv.org/abs/2604.21965)

## Summary

Sosyal bilimlerde tekrarlanabilirlik (reproducibility) tartışmasını ajan sistemlerine taşıyan bir ön baskı. Soru net: bir makalenin **kodunu hiç görmeden**, yalnızca yöntem anlatımı ve özgün veriyle sonuçlar yeniden üretilebilir mi? Yazarlar bunun için üç aşamalı bir hat kuruyor: (1) **çıkarım** — makaleden yapılandırılmış yöntem tarifi ve sayıları maskelenmiş tablo şablonları; (2) **yeniden uygulama** — ajan, her tablo için bir Python betiği yazıp orijinal veri üzerinde sandbox'ta çalıştırıyor; (3) **değerlendirme** — hücre hücre deterministik karşılaştırma ve hata atfı. Kritik tasarım tercihi "bilgi izolasyonu": ajan orijinal kodu, sonuçları ve makalenin tam metnini hiç görmüyor; böylece sonuçları ezberleyip kod içine gömmesi engelleniyor.

Deney: insan doğrulamasından geçmiş 48 makale, 4 ajan iskeleti (Claude Code, Codex CLI, OpenCode, SWE-Agent) × 4 model (GPT-5.4, GPT-5.3 Codex, Opus 4.6, GLM-5). Sonuçlar şaşırtıcı ölçüde iyi: ajanlar makalelerin **%92–100'ünde**, tabloların %82–97'sinde, hücrelerin %52–72'sinde kullanılabilir sonuç üretiyor; katsayılarda tamamlama %82, standart hatalarda %80. İşaret uyumu %78–91 (pozitif tahmin etme baseline'ı %68); en iyi ajan katsayıların %80'inden fazlasında orijinal %95 güven aralığının içinde kalıyor. Sıralama: en iyi **OpenCode + GPT-5.4** (ama en pahalı: makale başına ~7,5 USD, 5,6M token), ikinci küme Codex GPT-5.4/5.3 ve Claude Code Opus 4.6, en kötü SWE-Agent.

Asıl bulgu hata atfında: sapmaların **dörtte üçünden fazlası** belirli bir kaynağa bağlanabiliyor ve en büyük pay **"original error"** — yani makalenin yöntem anlatımı, altındaki kodu yeniden üretmeye yetecek kesinlikte değil. İkinci sırada eksik veri, üçüncüde çıkarım hattı hatası; **ajan hatası** ancak dördüncü sırada ve güçlü ajanlarda belirgin biçimde küçülüyor. Yazarların formülasyonu: darboğaz model kapasitesi değil, yöntemlerin **dokümantasyonu**. Örnekler somut: parti kodlamasının veride nasıl yapıldığının yazılmaması, hangi F-istatistiğinin kullanıldığının belirtilmemesi — ajanlar farklı varsayımlarla farklı sonuçlar üretiyor.

Sağlamlık testleri de var: tekrar koşularda tabloların %80'inden fazlasında not farkı en fazla bir kademe, ama katsayı düzeyinde gürültü yüksek (katsayıların yaklaşık yarısı kendinden istatistiksel olarak farklı); eğitim verisi sızması testinde kesim öncesi/sonrası makaleler arasında anlamlı fark yok. Sonuç önerisi: kod "ne yapıldı"nın, makale "neden yapıldı"nın otoritesi olarak ayrıştırılmalı ve ikisi arasındaki uyum otomatik olarak denetlenmeli.

## Key Points

- Soru: kod olmadan, yalnızca yöntem + veri ile sonuç üretilebilir mi? — büyük ölçüde evet
- 48 makale, 4 iskelet × 4 model; hücre tamamlama %52–72, katsayı %82
- En büyük hata kaynağı ajan değil: makalenin yöntem belirsizliği ('original error')
- En iyi: OpenCode + GPT-5.4; en pahalı da o (~7,5 USD/makale)
- Öneri: kod = 'ne yapıldı', makale = 'neden'; uyum otomatik denetlenmeli

## Turkey Context

Türkiye'de sosyal bilim yayıncılığının en kronik sorunu tam da makalenin bulduğu yerde: yöntem bölümü, altındaki analizi başkasının yeniden kurabileceği ayrıntıda yazılmıyor. Türkçe makalelerde veri setinin nereden geldiği, değişken kodlaması, örneklem filtreleri ve tahmin yöntemi çoğu zaman tek paragrafta geçiştiriliyor; kod ve veri paylaşımı ise istisna. Bu, TR Dizin ve ulusal dergilerde "tekrarlanabilirlik" bir yayın ölçütü olmadığı için kurumsal olarak da ödüllendirilmiyor. Makalenin çerçevesi burada bir **kalite ölçütü** öneriyor: bir hakemin/okuyucunun, makalenin yöntem metninden analizi yeniden kurabilmesi.

Üç somut kullanım alanı var. Birincisi, **lisansüstü eğitim ve tez denetimi**: ajan destekli yeniden üretim, bir tezin ampirik bölümünün gerçekten anlaşılıp anlaşılmadığını ölçmenin en pratik yolu; makale başına 1–7 USD maliyet, BAP bütçesiyle bölüm ölçeğinde bir "reproducibility audit" yapmayı fizibl kılıyor. İkincisi, **dergi editörlüğü**: TR Dizin taranan dergilerde veri-kod beyanı zorunluluğu ve "machine-readable methods" şablonu, makalenin işaret ettiği darboğazı doğrudan hedefler; Türkiye'de sosyal bilim dergilerinin çoğu için bu, hakem yükünü artırmadan kaliteyi yükseltebilecek bir müdahale.

Üçüncüsü, **KURATOR hattının kendi iş akışı**: bültenlerde ve wiki sayfalarında aktardığımız sayılar da aynı sorundan muzdarip — kaynağın yöntem metni zayıfsa, aktardığımız bulgu da kırılgan. Ajan destekli yeniden üretim, atıf yaptığımız ampirik iddiaları (ör. kutuplaşma ölçümleri, dezenformasyon etkisi) rutin olarak sınamak için kullanılabilir; en azından "bu sayı yeniden üretilebilir mi" sorusunu kayıt altına almak, bülten kalitesini yükseltir. Ek not: yazarların "bilgi izolasyonu" tasarımı, bizim ajanları veri/kod ile çalıştırırken sızıntıyı nasıl engelleyeceğimize dair de ders veriyor — sonucu gören ajan, sonucu üretmeye eğilimlidir.

## 🏷 Retorik Roller

- 🧩 **Yöntem**
- 📊 **Bulgular**
- 🔍 **Araştırma Boşluğu**
- 🏛 **Politika Önerisi**

---

## 🔗 İlgili Bağlantılar
### 🧠 İlgili Kavramlar
- [[concepts/siyaset-bilimi-metodolojisi.md|Siyaset Bilimi Metodolojisi]]
- [[concepts/bilimsel-iletisim.md|Bilimsel İletişim (Science Communication)]]
- [[concepts/harness-engineering.md|Harness Engineering (Agent Harness Mühendisliği)]]
### 🏛 İlgili Kurum/Kişiler
- [[entities/arxiv-org.md|arXiv]]
### 📄 İlgili Makaleler
- [[raw/articles/2026-06-26_depolarization-toolkit-an-agentic-ai-framework.md|Depolarization Toolkit: An Agentic AI Framework]]
