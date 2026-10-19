---
type: raw_article
title: Simulated responses from large language models are weak proxies for human economic
  preferences across 74 countries
description: Chen, Wang, Wang ve Bhatia'nın Nature Human Behaviour'da yayımlanan açık
  erişimli çalışması, 'LLM sentetik anket verisi insan anketinin yerini alabilir mi?'
  sorusunu bugüne kadarki en geniş karşılaştı...
resource: https://www.nature.com/articles/s41562-026-02611-4
tags:
- kurator
- high
timestamp: '2026-10-19T13:41:45Z'
source_file: 2026-10-19_llm-weak-proxies-economic-preferences-74-countries.json
category: KURATOR
priority: high
roles:
- gap
- method
- result
- limitation
- policy
published: '2026-10-12'
---

# Simulated responses from large language models are weak proxies for human economic preferences across 74 countries

**Author(s):** Fadong Chen; Qijun Wang; Lei Wang; Sudeep Bhatia (Zhejiang University; University of Pennsylvania)

**Published:** 2026-10-12

**Source:** [https://www.nature.com/articles/s41562-026-02611-4](https://www.nature.com/articles/s41562-026-02611-4)

## Summary

Chen, Wang, Wang ve Bhatia'nın Nature Human Behaviour'da yayımlanan açık erişimli çalışması, 'LLM sentetik anket verisi insan anketinin yerini alabilir mi?' sorusunu bugüne kadarki en geniş karşılaştırmalı tasarımla test ediyor ve cevap net biçimde 'şimdilik hayır, ama tamamen de değil'. Tasarım: 2012 Gallup World Poll kapsamında toplanan Global Preference Survey (GPS; 76 ülke, 80.000'den fazla katılımcı) insan verisiyle birebir eşleştirilmiş 67.201 katılımcı × 74 ülke üzerinde 'sanal GPS' yürütülüyor. Her GPS katılımcısının demografik profili (cinsiyet, yaş, bilişsel yetenek) ve ülke bilgisi sistem istemine, GPS sorusu kullanıcı istemine yazılıyor; altı ekonomik tercih alanı (risk alma, sabır, negatif karşılıklılık, pozitif karşılıklılık, altruizm, güven) simüle ediliyor. Ödeme tutarları yerel para biriminde, anket dili mümkün olduğunca ülkenin en çok örneklenen dili (Google Translate ile çeviri), sıcaklık 0. Ana analizde 12 LLM konfigürasyonu (yerel dil koşulu: GPT-3.5-turbo, GPT-4o-mini, GPT-4o, GPT-4.1-mini, GPT-5.4-mini, GPT-5.4, Gemini-2.0-Flash, Gemini-2.5-Flash, DeepSeek-V3; artı üç İngilizce-only koşul) ve sekiz takip deneyiyle toplam 20 konfigürasyon, model başına ~70.000 persona, toplam 1.390.525 gözlem üretiliyor. Bulgular dört katmanlı ve katmanlar arasındaki fark makalenin ana mesajı: (1) BİREY DÜZEYİ — ülke içi Spearman korelasyonlarının %87,5'inin %95 güven aralığı sıfırın üzerinde, yani 'zayıf ama sistematik' bir hizalama var; MSE'ler 1,567 (risk alma) ile 1,963 (güven) arasında, yani risk tercihi en iyi, güven en kötü temsil edilen tercih. (2) DEMOGRAFİK DÜZEY — cinsiyet, yaş ve bilişsel yetenek gradyanlarının yönü 216 karşılaştırmanın 168'inde (%77,8; %95 GA 71,6–83,1) doğru kestiriliyor. (3) KÜLTÜREL DÜZEY — Inglehart–Welzel, Hofstede ve Schwartz boyutlarında 1.080 karşılaştırmanın yalnızca 520'si (%48,1; %95 GA 45,1–51,2) tutuyor, yani yazı parayla değil: kültürel farklar şans düzeyinde. Fark istatistiksel olarak anlamlı (χ²=62,27; p<0,001). (4) ÜLKE DÜZEYİ — hata ülke yapısına göre değişiyor: model hatası ekonomik gelişmişlik ve dijital bağlantı düzeyiyle (IDI) birlikte artıyor, nüfus büyüklüğü veya internet kullanıcı sayısıyla değil. Üstelik modeller BİRBİRİYLE insandan daha fazla uyuşuyor (modeller arası ortalama MSE 1,377 < LLM–GPS 1,827), yani ortak bir Batılı/eğitimli/İngilizce ağırlıklı önsavı paylaşıyorlar. En çarpıcı üç bulgu: (a) YENİ MODEL DAHA İYİ DEĞİL — GPT-5.4 ve GPT-5.4-mini, GPT-3.5-turbo/GPT-4o ailesinden istatistiksel olarak farklı değil (Welch t=0,851; FDR-p=0,726); (b) YAYIMLANMIŞ BULGULARI ÇOĞALTAMIYOR — GPS'e dayanan 35 yayımlanmış ülke düzeyi ilişkinin (ör. sabır–kişi başı GSYH) en iyi model yalnızca 16'sını (%45,7) aynı yönde ve anlamlılıkta yeniden üretiyor; birey düzeyi 18 demografik ilişkinin ise %50–78'i çoğaltılıyor; (c) CİNSİYET YANLILIĞI — kadınların prososyal tercihleri sistematik olarak fazla tahmin ediliyor (altruizm 12/12 modelde, güven 11/12 modelde) ve bu sapma cinsiyet stereotiplerinin güçlü olduğu ülkelerde büyüyor. Ablasyon deneyleri teşhis niteliğinde: sistem isteminden ülke etiketini çıkarmak, demografik bilgiyi çıkarmaktan daha az zarar veriyor — yani modeller demografiyi kullanıyor, kültürü değil. Ayrıca LLM yanıtları insana göre çok daha az çeşitlilik taşıyor; sıcaklığı 1'e çıkarmak bunu kısmen düzeltiyor, insan düzeyine ulaşmıyor. Yazarların sonucu dengeli: LLM'ler hipotez üretme, erken aşama tasarım tanılama, etik açıdan hassas karşı-olgusal senaryoları ön tarama ve ölçüm aracı olma gibi işlerde kullanılabilir; ancak ülkeler arası temsili anketlerin, makro düzey çıkarımın ve politika değerlendirmesinin güvenilir vekili DEĞİL. Sınırlar kendi metinlerinde: GPS 2012'de toplandığı için içerik eğitim verisinde bulunabilir (ezber riski; ancak parafraz ve İngilizce-only deneyleri bu açıklamayı desteklemedi, dolayısıyla hizalama bir üst sınır olarak okunmalı), tercihlerde on yıllık seküler kayma, mekanizmalar opak, ablasyonlar ağırlıklı olarak GPT-5.4-mini ve tek persona tasarımıyla yapıldı, ülke etiketi kültürel bağlamın zayıf bir operasyonelleştirmesi. Veri ve kod OSF'te açık (osf.io/pt2n4), GPS verisi kamuya açık (gps.econ.uni-bonn.de).

## Key Points

- Künye: Fadong Chen, Qijun Wang, Lei Wang, Sudeep Bhatia, 'Simulated responses from large language models are weak proxies for human economic preferences across 74 countries', Nature Human Behaviour, 12 Ekim 2026, DOI 10.1038/s41562-026-02611-4, CC BY-NC-ND açık erişim.
- Tasarım: GPS (Global Preference Survey, 2012 Gallup World Poll; 76 ülke, 80.000+ kişi) ile birebir eşleştirilmiş 67.201 katılımcı / 74 ülke üzerinde 'sanal GPS'; 6 tercih alanı (risk alma, sabır, negatif ve pozitif karşılıklılık, altruizm, güven).
- Ölçek: 12 ana LLM konfigürasyonu (GPT-3.5-turbo, GPT-4o(-mini), GPT-4.1-mini, GPT-5.4(-mini), Gemini-2.0/2.5-Flash, DeepSeek-V3; 9 yerel dil + 3 İngilizce-only) ve 8 takip deneyi = 20 konfigürasyon; model başına ~70.000 persona; toplam 1.390.525 gözlem; sıcaklık 0.
- Birey düzeyi: ülke içi Spearman korelasyonlarının %87,5'inin %95 GA'sı sıfırın üzerinde — 'zayıf ama sistematik' hizalama; MSE 1,567 (risk alma) – 1,963 (güven), yani risk tercihi en iyi, güven en kötü temsil edilen alan.
- Demografik düzey: cinsiyet/yaş/bilişsel yetenek gradyanlarının yönü 216 karşılaştırmanın 168'inde doğru (%77,8; GA 71,6–83,1).
- Kültürel düzey: Inglehart–Welzel, Hofstede ve Schwartz boyutlarında 1.080 karşılaştırmanın yalnızca 520'si tutuyor (%48,1; GA 45,1–51,2) — yani şans düzeyinde; demografik oranla fark anlamlı (χ²=62,27; p<0,001).
- Ülke yapısı: hata ekonomik gelişmişlik ve dijital bağlantı (IDI) ile artıyor, nüfus veya internet kullanıcı sayısıyla değil; modeller birbirleriyle insandan daha çok uyuşuyor (modeller arası MSE 1,377 < LLM–GPS 1,827) → ortak Batı-merkezli önsav.
- Yeni model avantajı yok: GPT-5.4 / GPT-5.4-mini, GPT-3.5-turbo ve GPT-4o ailesinden farklı değil (Welch t=0,851; FDR-p=0,726) — 'yeni sürüm sorunu çözer' beklentisini çürütüyor.
- Çoğaltma testi: GPS'e dayanan 35 yayımlanmış ülke düzeyi ilişkinin en iyi model yalnızca 16'sını (%45,7) aynı yönde/anlamlılıkta çoğaltıyor (5% düzeyinde 12/29); birey düzeyi 18 demografik ilişkide oran %50–78.
- Cinsiyet yanlılığı: kadınların prososyal tercihleri fazla tahmin ediliyor (altruizm 12/12 modelde, güven 11/12), sapma güçlü cinsiyet stereotipli ülkelerde daha büyük — ülke düzeyi normların model çıktısına sızdığını gösteriyor.
- Ablasyon teşhisi: demografik bilgiyi istemden çıkarmak, ülke etiketini çıkarmaktan DAHA çok zarar veriyor → modeller demografiyi kullanıyor, kültürü kullanmıyor. Yanıt çeşitliliği insanın altında; sıcaklık=1 kısmen düzeltiyor, kapatmıyor.
- Dengeli sonuç: LLM'ler hipotez üretimi, tasarım tanısı, hassas karşı-olgusalların ön taranması ve ölçüm aracı olarak kullanılabilir; ülkeler arası temsili anket, makro çıkarım ve politika değerlendirmesinde güvenilir vekil DEĞİL.
- Sınırlar (yazarların kendi beyanı): GPS 2012 verisi eğitim kümesinde olabilir → hizalama bir üst sınır (parafraz ve İngilizce-only deneyleri ezber açıklamasını desteklemedi); seküler tercih kayması; mekanizmalar opak; ablasyonlar ağırlıklı GPT-5.4-mini ve tek persona tasarımı; ülke etiketi kültürün zayıf operasyonelleştirmesi.
- Açık bilim: veri ve kod OSF'te (osf.io/pt2n4), GPS verisi kamuya açık (gps.econ.uni-bonn.de) — bulgular bağımsız olarak yeniden üretilebilir.

## Turkey Context

Türkiye'de anket temelli araştırma pahalı ve yavaş; 'LLM'e sorduk, KONDA/TÜİK anketine gerek yok' türü kısa yol arayışı özellikle siyasal davranış ve kutuplaşma literatüründe cazip. Bu makale o kısa yolun sınırını sayısal olarak koyuyor ve Türkiye özelinde üç sonucu doğrudan ilgilendiriyor. (1) Hata yapısı gelişmişlik ve dijital bağlantı düzeyine bağlı: yazarların bulgusu, ekonomik olarak az gelişmiş ve dijital olarak daha az bağlı ülkelerde hizalamanın daha zayıf olduğu yönünde. Türkiye bu eksende alt-orta grupta yer aldığı için, Türk katılımcıları temsil ettiği iddia edilen sentetik örneklemlerin kültürel boyutlarda sistematik olarak yanlış olması beklenir — özellikle dindarlık, geleneksel değerler ve cinsiyet rolleri gibi Türkiye'de siyasal davranışın güçlü yordayıcıları olan boyutlarda. (2) Cinsiyet yanlılığı bulgusu (kadınların prososyal tercihlerinin fazla tahmini, güçlü stereotipli ülkelerde daha büyük) Türkiye'de cinsiyet uçurumu çalışan araştırmacılar için doğrudan uyarı: LLM tabanlı sentetik veri, tam olarak ölçmek istediğiniz farkı yapay olarak büyütür veya küçültür. (3) Çoğaltma testi (%45,7) metodolojik bir standart öneriyor: Türkiye'de LLM ile üretilen 'sentetik anket' sonuçları, mevcut ampirik bulgularla (ör. Dünya Değerler Araştırması Türkiye dalgası, ESS/ISSP, yerel panel verileri) çoğaltma testinden geçirilmeden yayımlanmamalı. Öte yandan makale, LLM'leri tamamen dışlamıyor: Türkiye'de saha maliyeti yüksek olduğu için, hipotez ön taraması, ölçek/İstem tasarımı tanısı ve etik açıdan hassas karşı-olgusal senaryoların (ör. mülteci karşıtlığını artıran/azaltan koşullar) ön testi için kullanmak savunulabilir — yeter ki bu kullanım 'veri' değil 'tasarım aracı' olarak çerçevelensin. Kurumsal düzeyde çıkarım: TÜBİTAK/üniversite etik kurulları ve dergi hakemleri için, LLM ile üretilmiş anket verisinin insan verisi yerine geçtiği iddialarında ülke/kültür düzeyi doğrulama talep etmek makul bir standart haline geliyor.

## 🏷 Retorik Roller

- 🔍 **Araştırma Boşluğu**
- 🧩 **Yöntem**
- 📊 **Bulgular**
- ⚠️ **Sınırlılıklar**
- 🏛 **Politika Önerisi**

---

## 🔗 İlgili Bağlantılar
### 🧠 İlgili Kavramlar
- [[concepts/olcum-araclari.md|Ölçüm Araçları (Polarization Measurement)]]
- [[concepts/onvargi-ve-stereotipler.md|Önyargı ve Stereotipler]]
### 🏛 İlgili Kurum/Kişiler
- [[entities/nature-com.md|Nature Com]]
