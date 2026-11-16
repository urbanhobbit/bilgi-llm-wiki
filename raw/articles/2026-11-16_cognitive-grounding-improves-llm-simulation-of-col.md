---
type: raw_article
title: Cognitive grounding improves LLM simulation of collective human behavior
description: 'Zhu ve Heydari (Northeastern University), LLM''lerin **insan yerine
  geçen katılımcı** olarak kullanıldığı literatüre temel bir itirazla giriyor: makul
  görünen bir yanıt, insan karar sürecinin kanıtı de...'
resource: https://www.nature.com/articles/s43588-026-01080-z
tags:
- kurator
- akademik
- high
timestamp: '2026-11-16T18:39:57Z'
source_file: 2026-11-16_cognitive-grounding-llm-collective-behavior.json
category: KURATOR; AKADEMİK ÖZEL
priority: high
roles:
- result
- method
- limitation
published: '2026-11-16'
---

# Cognitive grounding improves LLM simulation of collective human behavior

**Author(s):** Hongan Zhu, Babak Heydari (sorumlu yazar) — Northeastern University; kod/veri: Code Ocean kapsülü + GitHub (zhuhongan/cognitive-grounding-beer-game)

**Published:** 2026-11-16

**Source:** [https://www.nature.com/articles/s43588-026-01080-z](https://www.nature.com/articles/s43588-026-01080-z)

## Summary

Zhu ve Heydari (Northeastern University), LLM'lerin **insan yerine geçen katılımcı** olarak kullanıldığı literatüre temel bir itirazla giriyor: makul görünen bir yanıt, insan karar sürecinin kanıtı değildir — ve bu fark, ajanlar etkileştiğinde (gecikme ve geri besleme yoluyla yerel kararların toplu sonuçlara bileştiği yerde) en çok önem kazanır. Çözüm önerileri **'bilişsel temellendirme' (cognitive grounding)**: davranış modellerinin insan verisine uydurduğu karar kurallarını, kod olarak değil **nitel içerik olarak** LLM ajanının istemine koymak. Test alanı **Bier Distribution Game (Beer Game)** — oyuncuların siparişlerinin talep dalgalanmalarını büyüttüğü (bullwhip etkisi) klasik dört rollü tedarik zinciri deneyi. **231 oturum** ve **yedi LLM** üzerinde: temellendirme, yedi modelin tamamında yörünge uyumunu iyileştiriyor ve çıkarılan karar parametrelerini genel olarak insan-kalibre referansa kaydırıyor (rol ve model bazında eşitsiz). Temellendirilmemiş ajanlar oyunun **istikrarsızlığını** üretiyor ama **büyüklüğünü, zamanlamasını ve yayılımını** kaçırıyor. Etki, bağımsız ampirik veriye karşı ve alternatif istem/bellek tasarımlarında da korunuyor. Yazarların kendi formülasyonu: bilişsel olarak temellendirilmiş LLM'ler **aday davranışsal vekiller** (behavioral surrogates) — ama kullanım **göreve özgü doğrulamaya bağlı**.

## Key Points

- Künye: Nature Computational Science, çevrimiçi 16 Kasım 2026; DOI 10.1038/s43588-026-01080-z; yazarlar Hongan Zhu (ORCID 0000-0001-6424-2752) ve Babak Heydari (ORCID 0000-0002-4964-8655, sorumlu yazar). Crossref kaydı cilt/sayfa vermiyor (online-first).
- Özet (birebir): 'Large language models (LLMs) increasingly stand in for human participants, yet a plausible response is not evidence of a human decision process. The gap matters most when agents interact, where locally reasonable choices compound through delays and feedback into collective outcomes. Behavioral models fit decision rules to human data; we ask whether their qualitative content alone can drive LLM agents, an approach we call cognitive grounding. Here we show, across 231 sessions of the Beer Distribution Game... that grounding moves seven LLMs toward human-calibrated behavior. Ungrounded agents reproduce the game's instability but miss its magnitude, timing and propagation; grounding improves trajectory fit for every model and generally shifts inferred decision parameters toward the human-calibrated reference, although unevenly across roles and models. The effect holds against independent empirical data and under alternative prompting and memory designs. Cognitively grounded LLMs are therefore candidate behavioral surrogates, contingent on task-specific validation.'
- Tasarım (açık kod deposundan doğrulandı): dört rol (retailer, wholesaler, distributor, factory), **35 tur**; her model-koşul hücresinde **11 oturum** → 7 model × 3 koşul × 11 = **231 oturum**. Yörüngeler, Sterman'ın stok-yönetimi modelinden üretilen **insan-kalibre hedefle** karşılaştırılıyor; her oturumun gizli karar parametreleri **tersinir sinir ağı (BayesFlow 2.0.7 / Keras 3.10 / JAX)** ile çıkarılıyor.
- Üç istem koşulu: (1) **baseline** — oyun kurulumu, rol, amaç, role özgü mevcut durum; (2) **prompt** — buna **Sterman buluşsalının nitel tanımı** eklenir (asıl 'bilişsel temellendirme' koşulu); (3) **alt** — yerel karar ortamını tanımlayan **bilişsel yük** istemi. Üç protokol: birincil (her karar için yeni API çağrısı + tam kayıt sayfası), kalıcı konuşma (her rol tek konuşma), ve ek protokol (toplam açık siparişler + 2/4 turdaki boru hattı miktarları, ama yalnız 4 turluk kayan geçmiş).
- Modeller (yedi): Kimi K2 0905, Llama-3.1 8B, Llama-3.3 70B, Qwen-3.6-35B-A3B, [T-]OSS 20B, GPT-OSS 120B ve bir model daha (README tablosu okunurken son satır kesildi) — API erişimi OpenRouter üzerinden; sıcaklık 1.0 (GPT-OSS 20B için 0.2/0.6 duyarlılık koşuları), düşük akıl yürütme eforu.
- Ana bulgu: temellendirme **yedi modelin tamamında** yörünge uyumunu iyileştiriyor; parametreler insan referansına kayıyor ama **rol ve model bazında eşitsiz**. Temellendirilmemiş ajanlar bullwhip istikrarsızlığını üretiyor, ancak **büyüklük/zamanlama/yayılım** üçlüsünü kaçırıyor — yani 'doğru yönde yanlış büyüklükte' bir simülasyon.
- Sağlamlık (özetten): bağımsız ampirik veriye karşı ve alternatif istem/bellek tasarımlarında etki korunuyor; bu, bulgunun istem mühendisliği artefaktı olmadığı iddiasının dayanağı.
- Açık bilim: kod, veri ve eğitilmiş çıkarım ağı GitHub'da (zhuhongan/cognitive-grounding-beer-game, MIT lisansı) ve Code Ocean kapsülünde (10.24433/CO.2254887.v1); veri klasörlerinde her model-koşul için 11 oturumun tur bazlı sipariş/stok/backlog/sevkiyat ve kâr-maliyet kayıtları var. Bu, Nature dergisinde **tam metni kapalı** bir makale için nadir bir şeffaflık.
- Sınırlılık: **makale gövdesi okunamadı** — nature.com 'Access options' (meta access=No), PDF yolu HTML'e yönleniyor, rdcu.be paylaşım bağlantısı 202/boş döndü. Sonuç büyüklükleri (log-MSE iyileşmesi, parametre kaymaları, model sıralaması), şekil/tablolar ve tartışma **doğrulanmadı**. Kayıt; özet + açık kod deposu + Crossref künyesi üzerinden kuruldu. Tek bir oyun (Beer Game) ve tek bir görev ailesi üzerinden 'davranışsal vekil' iddiası kurulduğu için genelleme iddiası yazarlar tarafından da 'göreve özgü doğrulama' kaydıyla sınırlanıyor.

## Turkey Context

Bu makale, KURATOR hattının en çok ihtiyaç duyduğu şeyi veriyor: **LLM ile insan davranışı simüle etmenin ne zaman işe yaradığına dair test edilebilir bir ölçüt**. Türkiye'de seçmen/ kamuoyu simülasyonu tartışması (sentetik örneklem, LLM persona anketleri) şu an iki uç arasında sıkışmış: 'sentetik veri devrim' iddiası ile 'LLM'ler insanı temsil edemez' reddi. Bu makalenin ara konumu daha kullanışlı: ham persona değil, **davranış modelinin nitel içeriğiyle temellendirilmiş** ajan. Türkiye'de uygulama için üç sonuç: (1) **Oyun/etkileşim gerektiren** senaryolar (tedarik zinciri, fiyat paniği, kuyruk, seçim gecesi bilgi akışı) LLM ajanlarla simüle edilecekse, önce yerel bir davranış modeli (ör. enflasyon beklentisi altında stok davranışı) nitel olarak isteme gömülmeli — yoksa simülasyon 'doğru yönde yanlış büyüklükte' çıkar; (2) **büyüklük ve zamanlama** testi zorunlu: Türkiye'de 2021 kur şoku ve 2023 öncesi fiyatlama davranışı gibi olaylar, ajan simülasyonlarının amplifikasyon büyüklüğünü sınamak için doğal referans; (3) **açık kod/veri** pratiği doğrudan taklit edilebilir — Code Ocean kapsülü, dergi tam metni kapalı olsa bile yöntemin yeniden üretilmesini sağlıyor; Türkiye'de yayınlanan hesaplamalı sosyal bilim makalelerinde bu standart yok. Dördüncüsü, eleştirel: Türkiye bağlamında 'davranış modeli' bulmak kolay değil (Sterman'ın stok modeli gibi kalibre edilmiş modeller Türkçe literatürde yok); bu, yöntemin ithal edilmesindeki en büyük engel. Uyarı: makale tek oyun üzerinde çalışıyor, gövdesi okunmadı; 'LLM'ler insanı temsil edebiliyor' şeklinde aktarılmamalı.

## 🏷 Retorik Roller

- 📊 **Bulgular**
- 🧩 **Yöntem**
- ⚠️ **Sınırlılıklar**

---

## 🔗 İlgili Bağlantılar
### 🧠 İlgili Kavramlar
- [[concepts/sentetik-populasyonlar.md|Sentetik Popülasyonlar ve Birey-Tabanlı Simülasyon]] — LLM ajanlarının insan katılımcı yerine geçmesi: sentetik popülasyon literatürünün 'temsil geçerliliği' sorusuna doğrudan müdahale.
- [[concepts/kuram-operasyonellestirme-llm.md|Kuramın LLM ile Operasyonelleştirilmesi]] — Yöntemin özü: davranış modelinin (Sterman stok modeli) nitel içeriğini kod yerine isteme koyup ajanı onunla yönlendirmek.
- [[concepts/yapay-zeka-ile-bilimsel-modelleme.md|Yapay Zeka ile Bilimsel Modelleme]] — LLM tabanlı simülasyonun kalibrasyonu ve doğrulanması: 'plausible response ≠ human decision process' ölçütü.
- [[concepts/olcum-araclari.md|Ölçüm Araçları (Polarization Measurement)]] — Değerlendirme ölçütü: yörünge uyumu (relative log-MSE), bullwhip büyüklüğü ve parametre çıkarımı ile insan-kalibre referansa mesafe ölçümü.

### 🏛 İlgili Kurum/Kişiler
- [[entities/nature-com.md|Nature Com]]
- [[entities/nature-computational-science.md|Nature Computational Science]] — Makalenin yayımlandığı dergi.
- [[entities/babak-heydari.md|Babak Heydari]] — Sorumlu yazar.
- [[entities/hongan-zhu.md|Hongan Zhu]] — İlk yazar.
- [[entities/northeastern-university.md|Northeastern University]] — Yazarların kurumu.
