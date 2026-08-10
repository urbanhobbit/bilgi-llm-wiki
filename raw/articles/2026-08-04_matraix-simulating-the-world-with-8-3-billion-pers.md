---
type: raw_article
title: 'MatrAIx: Simulating the World with 8.3 Billion Persona Agents'
description: arXiv:2608.04205 (4 Ağustos 2026) — Harvard & MIT organizasyonlu büyük
  işbirliği (eş başyazarlar Xiaomin Li [Harvard] ve Yuexing Hao [MIT]; danışma komitesinde
  Paul Pu Liang, James Zou, Marinka Zitnik...
resource: https://arxiv.org/abs/2608.04205
tags:
- kurator
- high
timestamp: '2026-08-10T06:14:29Z'
source_file: 2026-08-08_matraix-simulated-users.json
category: KURATOR
priority: high
roles:
- method
- result
published: '2026-08-04'
---

# MatrAIx: Simulating the World with 8.3 Billion Persona Agents

**Published:** 2026-08-04

**Source:** [https://arxiv.org/abs/2608.04205](https://arxiv.org/abs/2608.04205)

## Summary

arXiv:2608.04205 (4 Ağustos 2026) — Harvard & MIT organizasyonlu büyük işbirliği (eş başyazarlar Xiaomin Li [Harvard] ve Yuexing Hao [MIT]; danışma komitesinde Paul Pu Liang, James Zou, Marinka Zitnik, Yilun Du, Dawn Song, Asu Ozdaglar, Philip Torr dahil). MatrAIx, yapay zeka sistemlerini ve dijital ürünleri heterojen kullanıcılarla test etmek için nüfus ölçeğinde (population-scale) simüle kullanıcı değerlendirme altyapısı. İnsan değerlendirmesi pahalı, yavaş ve ölçeklenmesi zor; offline benchmark'lar ise kullanıcı çeşitliliğini ve etkileşimli davranışı soyutlar. MatrAIx üç bileşenden oluşuyor: (1) Persona 8B — 1.290 kategorik boyutlu şemayla 8,3 milyar persona kaydı; sentetik kayıtlar bağımlılık grafiğinden (korelasyonlu nitelikler + uyumluluk kuralları), insan-temelli kayıtlar altı kaynaktan (Wikipedia biyografileri, Amazon yorumları, Stack Overflow Developer Survey, General Social Survey, PRISM Alignment profilleri, onaylı MatrAIx anketi) çekiliyor; ~1 milyon kişilik kalite filtrelenmiş coreset (599.847 insan-temelli + 400.000 sentetik) yayınlanıyor; (2) MatrAIx Playground — dört ortam: Survey, AI Chatbot, Web, App; (3) MatrAIx Applications — 25+ alanda (Ticaret, Yazılım, Finans, Sağlık) 1.010 görev. Sekiz temsili görevde 18.189 değerlendirme denemesi yapıldı; persona ajanları Claude Opus 4.8, GPT 5.5 ve Claude Haiku 4.5 ile çalıştırıldı. Bulgular: fiyat artışı sonrası tereddüt, AI asistanı başarısız olduktan sonra devam etme isteği, gecikme toleransı gibi kararların persona geçmişine göre nasıl değiştiğini yakalıyor. İki doğrulama çalışması: (1) 400 denemelik kontrollü çalışmada persona uyumu %91,5 (366/400); (2) insan ve LLM hakemler insan-temelli persona çıkarım kalitesini değerlendirdi — insan ortalaması 4,135/5; GPT 5.5 ve Claude Opus 4.8 puanları insan ortalamasına %79,2 ve %93,8 oranında bir puan içinde. Eleştirel bağlam: makale, simüle kullanıcıların gerçek insan davranışını temsil etme sınırlarını da tartışıyor (grup içi varyasyonu düzleştirme, stereotip amplifikasyonu, persona alanlarını yok sayma — Santurkar 2023, Wang 2025a, Li 2025a). Yapay zeka değerlendirme metodolojisinde insan değerlendirmesi yerine geçebilecek simüle kullanıcı yaklaşımının en iddialı örneği.

## Key Points

- arXiv:2608.04205, 4 Ağustos 2026; Harvard & MIT (Li & Hao eş başyazarlar; Zou, Zitnik, Song, Torr danışma kurulunda)
- Persona 8B: 1.290 boyutlu şemada 8,3 milyar persona kaydı; ~1M coreset (599.847 insan-temelli + 400.000 sentetik) yayında
- 4 ortam (Survey, AI Chatbot, Web, App) + 1.010 görev (25+ alan); 18.189 deneme, 3 frontier model (Claude Opus 4.8, GPT 5.5, Claude Haiku 4.5)
- Doğrulama: persona uyumu %91,5 (400 deneme); insan puanı 4,135/5 — LLM hakemler insanla uyumlu
- Kullanım: fiyat duyarlılığı, chatbot başarısızlık sonrası devam isteği, gecikme toleransı gibi kullanıcı-alt grup farklılıklarını yakalıyor
- Sınırlar: simüle kullanıcılar gerçek insan davranışını tam temsil etmiyor — varyasyon düzleşmesi, stereotip amplifikasyonu riskleri tartışılıyor
- X paylaşımı (HowToPrompt): 'Harvard ve MIT 8,3 milyar sanal insanlı AI simülasyonu inşa etti' — MatrAIx

## 🏷 Retorik Roller

- 🧩 **Yöntem**
- 📊 **Bulgular**

---

## 🔗 İlgili Bağlantılar
### 🧠 İlgili Kavramlar
- [[concepts/olcum-araclari.md|Ölçüm Araçları (Polarization Measurement)]]
- [[concepts/onvargi-ve-stereotipler.md|Önyargı ve Stereotipler]]
