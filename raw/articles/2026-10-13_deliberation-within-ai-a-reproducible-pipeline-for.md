---
type: raw_article
title: 'Deliberation Within AI: A Reproducible Pipeline for Multi-Agent Deliberation
  Simulation'
description: 'ACM''nin Digital Government: Research and Practice dergisinde 13 Ekim
  2026''da çevrimiçi yayımlanan metodolojik makale, üretken yapay zeka ile yürütülen
  müzakere (deliberation) simülasyonlarının ancak b...'
resource: https://dl.acm.org/doi/10.1145/3858422
tags:
- kurator
- high
timestamp: '2026-10-14T13:06:38Z'
source_file: 2026-10-14_deliberation-within-ai-multi-agent-deliberation-simulation.json
category: KURATOR
priority: high
roles:
- gap
- method
- result
- limitation
published: '2026-10-13'
---

# Deliberation Within AI: A Reproducible Pipeline for Multi-Agent Deliberation Simulation

**Author(s):** Francesco Veri (Centre for Democracy Studies, University of Zurich — ORCID 0000-0002-9295-6776)

**Published:** 2026-10-13

**Source:** [https://dl.acm.org/doi/10.1145/3858422](https://dl.acm.org/doi/10.1145/3858422)

## Summary

ACM'nin Digital Government: Research and Practice dergisinde 13 Ekim 2026'da çevrimiçi yayımlanan metodolojik (methodological) makale, üretken yapay zeka ile yürütülen müzakere (deliberation) simülasyonlarının ancak belirli altyapı koşulları sağlandığında 'inandırıcı analitik araç' sayılabileceğini savunuyor. Francesco Veri (Zurich Üniversitesi, Centre for Democracy Studies), mevcut AI deliberation simülasyonlarının üç yapısal kırılganlığını teşhis ediyor: (1) akıcı konuşma çıktısının müzakere kalitesinin kanıtı sayılması, (2) yeniden üretilebilirliğin (reproducibility) zayıflığı, (3) görüş çeşitliliğini (viewpoint diversity) koruyacak güvencelerin ve sistematik değerlendirmenin yokluğu. Çözüm olarak aşamalı (stage-structured) ve yeniden üretilebilir bir hat öneriyor: persona doğrulama (persona validation), çoğulluk denetimi (plurality auditing) ve söylem-kalitesi değerlendirmesi (discourse-quality assessment). Yöntem iki çalışmayla sınanıyor: Haziran 2023 İsviçre federal referandumu (Climate and Innovation Act) üzerine bir simülasyon çalışması ve doğrudan vs. yapılandırılmış deliberation mimarilerini karşılaştıran bir toplu replikasyon (batch replication) çalışması. Bulgu: entegre ve teori-güdümlü yapılandırılmış hat, serbest (unconstrained) etkileşime kıyasla daha istikrarlı müzakere dinamikleri üretiyor — çoğulluğun korunması daha net, görüş güncellemeleri daha tutarlı. Aynı zamanda simülasyonlar bağlamsal temellendirme (contextual grounding) ve gerekçelendirme derinliği (justificatory depth) açısından insan mini-public'ların altında kalıyor. Veri makalesi, AI deliberation simülasyonlarını birikimli ve ampirik olarak sınanabilir araştırma için 'metodolojik altyapı' olarak konumlandırıyor — yani insan müzakeresinin ikamesi değil, dijital yönetişimde ve yapay zeka yönetişimi tartışmalarında test edilebilir bir araştırma aracı olarak. Türkiye'deki kutuplaşma ve müzakereci demokrasi (müzakereci demokrasi) literatürü için karşılaştırmalı bir yöntem referansı.

## Key Points

- Teşhis: AI deliberation simülasyonları metodolojik olarak kırılgan — akıcı konuşma çıktısı müzakere kalitesinin kanıtı sayılıyor, yeniden üretilebilirlik zayıf, görüş çeşitliliği için güvence ve sistematik değerlendirme yok.
- Öneri: aşamalı ve yeniden üretilebilir hat — persona doğrulama + çoğulluk denetimi + söylem kalitesi değerlendirmesi (üç aşama bir arada entegre mimari olarak kurgulanmalı, tek tek değil).
- Vaka 1: Haziran 2023 İsviçre federal referandumu (Climate and Innovation Act) üzerine simülasyon çalışması.
- Vaka 2: Toplu replikasyon deneyi — doğrudan (direct) ve yapılandırılmış (structured) deliberation mimarilerinin karşılaştırılması.
- Bulgular: yapılandırılmış hat daha istikrarlı müzakere dinamiği, daha net çoğulluk korunması ve daha tutarlı görüş güncellemesi üretiyor; serbest etkileşim bu istikrarı sağlamıyor.
- Sınırlılık: simülasyonlar bağlamsal temellendirme ve gerekçelendirme derinliğinde insan mini-public'ların altında kalıyor (yazar bunu açıkça kabul ediyor).
- Konum: makale kendini 'kanıtlanmış bulgu' değil, metodolojik kavram kanıtı (proof-of-concept) ve araştırma altyapısı olarak sunuyor.
- Katkı: yeniden üretilebilirlik, çoğulluk ve kalite değerlendirmesini aynı hatta birleştiren ilk kapsamlı çerçevelerden biri; 'AI-supported deliberation' araştırmasını kümülatif hale getirme iddiası.
- Kapsam notu: tek yazarlı, tek vaka + tek replikasyon setli bir yöntem makalesi; bulgular tekil vaka tasarımına bağlı, genelleme iddiası sınırlı.
- Yazar konumu: Centre for Democracy Studies, University of Zurich — müzakereci demokrasi ve dijital yönetişim (digital governance) alanı.

## Turkey Context

1) Yöntem aktarımı: 'yapay zeka ile müzakere simülasyonu' hattı Türkiye'de vatandaş meclisi/mini-public tartışmaları için düşük maliyetli bir ön-test aracı olarak kullanılabilir — ancak makale tam da bunun şartını gösteriyor: persona doğrulaması, çoğulluk denetimi ve söylem kalitesi ölçümü olmadan üretilen çıktı 'müzakere kanıtı' sayılamaz. 2) Metodolojik uyarı: Türkiye'de AI ile kamuoyu/senaryo simülasyonu yapan çalışmalar için 'yeniden üretilebilirlik' (kod, prompt, persona seti, değerlendirme rubriği açık paylaşımı) standart hâline getirilmelidir; aksi hâlde bulgular atıf yapılabilir bilgi üretmiyor. 3) Kavramsal köprü: müzakereci demokrasi (müzakereci demokrasi) literatüründeki 'çoğulluğun korunması' tartışması, Türkiye'de kutuplaşma koşullarında yapay zeka aracılığıyla yürütülecek tartışma tasarımlarının meşruiyet ölçütü olarak okunabilir. 4) Yönetişim bağlantısı: yapay zeka yönetişimi (yapay zeka yönetişimi) gündeminde 'AI ile demokrasi deneyleri' neyin kanıt sayılacağı sorusunu açıyor — Türkiye'de kamu kurumlarının AI destekli danışma/konsültasyon araçlarına yönelmesi durumunda bu makale bir denetim çerçevesi sağlıyor. 5) Uyarı: İsviçre referandumu tek vaka; bulgular Türkiye'nin yüksek kutuplaşmalı, çok partili bağlamına doğrudan aktarılamaz, uyarlama gerektirir.

## 🏷 Retorik Roller

- 🔍 **Araştırma Boşluğu**
- 🧩 **Yöntem**
- 📊 **Bulgular**
- ⚠️ **Sınırlılıklar**

---

## 🔗 İlgili Bağlantılar
### 🧠 İlgili Kavramlar
- [[concepts/muzakereci-demokrasi.md|Müzakereci Demokrasi]]
- [[concepts/sosyal-kutuplasma.md|Sosyal Kutuplaşma ve Dijital Platformlar]]
- [[concepts/yapay-zeka-demokrasi.md|Yapay Zeka ve Demokrasi]]
- [[concepts/yapay-zeka-yonetisimi.md|Yapay Zeka Yönetişimi]]
- [[concepts/siyaset-bilimi-metodolojisi.md|Siyaset Bilimi Metodolojisi (Research Methods)]]
- [[concepts/olcum-araclari.md|Ölçüm Araçları (Measurement Instruments)]]
### 🏛 İlgili Kurum/Kişiler
- [[entities/dl-acm-org.md|ACM Digital Library]]
### 📄 İlgili Makaleler
- [[raw/articles/2026-07-23_genai-deliberation-simulations.md|The Case for Using Generative AI to Run Deliberation Simulations (Rountree & Gastil, Journal of Deliberative Democracy)]]
- [[raw/articles/2026-09-03_diverging-effects-of-deliberation-how-perceived-th.md|Diverging Effects of Deliberation: Perceived Thoughtfulness About Political Issues and Character Judgments (PSPB)]]
