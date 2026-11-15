---
type: raw_article
title: The Structure and Content of Meaning in Speech Reflects Mental Health
description: PsyArXiv'de 15 Ekim 2026'da yayımlanan (v1, hakem öncesi) çalışma, ruh
  sağlığı ile konuşmanın **anlamsal yapısı** arasında nicel bir köprü kuruyor. Leckie,
  Meuret, Ritz, Losiewicz, Craske ve Foster (I...
resource: https://osf.io/preprints/psyarxiv/we2gj_v1
tags:
- akademik
- genel
- medium
timestamp: '2026-11-15T08:58:28Z'
source_file: 2026-10-15_speech-semantics-persistent-homology-mental-health.json
category: AKADEMİK ÖZEL; GENEL
priority: medium
roles:
- method
- result
- limitation
published: '2026-10-15'
---

# The Structure and Content of Meaning in Speech Reflects Mental Health

**Author(s):** Luke Leckie; Alicia E. Meuret; Thomas Ritz; Olivia M. Losiewicz; Michelle G. Craske; Jacob G. Foster — Indiana University (Informatics, Cognitive Science, Center for Possible Minds), Southern Methodist University, UCLA, Santa Fe Institute

**Published:** 2026-10-15

**Source:** [https://osf.io/preprints/psyarxiv/we2gj_v1](https://osf.io/preprints/psyarxiv/we2gj_v1)

## Summary

PsyArXiv'de 15 Ekim 2026'da yayımlanan (v1, hakem öncesi) çalışma, ruh sağlığı ile konuşmanın **anlamsal yapısı** arasında nicel bir köprü kuruyor. Leckie, Meuret, Ritz, Losiewicz, Craske ve Foster (Indiana University, SMU, UCLA, Santa Fe Institute), iki çok merkezli randomize kontrollü denemeden gelen **N=82** yetişkinin (18-60 yaş; ort. 33,81, SS=11,94; %63'ü doğumda kadın atanmış) Pozitif Duygu Tedavisi (PAT) sürecindeki **altı seanslık** (seans 2-7) imgelemsel 'savoring' anlatılarını inceliyor: toplam **341 anlatı**. Yöntem iki katmanlı: (1) Sentence-BERT (all-MiniLM-L6-v2) ile 90 kelimelik kayan pencereler (yüzde 10 kelime adımı) yüksek boyutlu vektörlere gömülüyor ve her anlatı anlamsal bir **yörünge** olarak modelleniyor; (2) **kalıcı homoloji** (persistent homology) ile bu nokta bulutundaki **anlam döngüleri** — anlatı daha önce konuşulan bir temaya geri döndüğünde oluşan topolojik halkalar — sayılıyor. Bulgular: döngü sayısı depresyon (β=0,10; p=0,027), kaygı (β=0,21; p=0,016), stres (β=0,19; p=0,019) ve negatif duygudurum (β=0,19; p=0,022) ile **pozitif**; pozitif duygudurum ile ilişkisiz (β=-0,01; p=0,90), göreli duygudurumla sınırda negatif (β=-0,15; p=0,073) — tüm p değerleri Benjamini-Hochberg düzeltmeli. Döngü içeren anlatılarda 'negatif sabitlenme' içeriği belirgin yüksek (χ²=15,99; p=0,004), yani döngüler yalnızca biçim değil, içerik olarak da ruminatif çekirdeğe bağlı. İçerik düzleminde depresyon hem hedonik hem kişilerarası sevinçte, kaygı yalnızca kişilerarası sevinçte, stres ise hedonik ve ödaimonik sevinçte düşüşle işaretli; kaygı ve negatif duygudurum ayrıca sevinç yörüngesinin **oynaklığıyla** (affective volatility) ilişkili. Kritik sınır: dilsel özellikler ruh sağlığını **yansıtıyor ama aracılık etmiyor** — PLS bileşeni tüm ölçütlerle (pozitif duygudurum hariç) ilişkili, açıklanan ek varyans ΔR²=0,01-0,10, ancak hiçbir aracılık yolu anlamlı değil. Yazarlar bunu 'anlatma eyleminin, anlatının içeriğinden ve yapısından bağımsız olarak iyileşmeyi sürebileceği' biçiminde yorumluyor.

## Turkey Context

Türkiye açısından üç ayrı hat açılıyor. **Birincisi, ölçüm siyaseti.** Çalışma, ruh sağlığını özbildirim ölçeklerinin (DASS-21, PANAS) 'post hoc statik yargılarından' kurtarıp konuşmanın kendi geometrisine taşımayı öneriyor. Türkiye'de ruh sağlığı taraması neredeyse tamamen özbildirim ve klinik görüşmeye dayanıyor; TÜİK ve Sağlık Bakanlığı verilerinde depresyon/kaygı yaygınlığı bu yöntemlerle üretiliyor. Döngü sayısı gibi bir yapısal ölçüt, özellikle **damgalama nedeniyle semptom gizlemenin** yaygın olduğu bağlamlarda özbildirim yanlılığını aşmanın yolu olarak düşünülebilir — ama bu umut, aşağıdaki iki koşula bağlı. **İkincisi, dil ve model transferi.** Yöntemin çekirdeği Sentence-BERT'in İngilizce anlamsal uzayı; Türkçe için aynı yörünge geometrisi doğrudan varsayılamaz. Türkçe konuşma dilinde tema geri dönüşleri, eklemeli yapı ve uzun cümleler yüzünden pencere tabanlı gömme farklı gürültü üretir; bu nedenle Türkçe bir tekrar çalışması, BERTurk/Turkish-MiniLM gibi modellerle ve mutlaka Türkçe konuşma transkriptleriyle kurulmalı. Literatürde DASS-21'in Türkçe geçerlilik çalışmaları var; bu, en azından sonuç ölçütü tarafını karşılaştırılabilir kılıyor. **Üçüncüsü ve en önemlisi, ETİK ve KVKK.** Terapötik transkriptlerden 'ruh sağlığı parmak izi' çıkarma fikri, Türkiye'de 6698 sayılı KVKK kapsamında **özel nitelikli kişisel veri** (sağlık verisi) statüsündedir; özel nitelikli verilerde açık rıza aranır ve amaçla sınırlılık ilkesi katı bir şekilde uygulanır. Bu tür bir ölçüt bir kez 'çalışır' hale gelirse, özel sektörde (sigorta, işe alım, okul rehberliği, dijital platformlar) 'erken uyarı' adı altında kullanılma riski yüksektir — yazarların kendisi de gelecek çalışmalarda 'riskli bireyleri belirleme' işlevini olumlu bir hedef olarak çerçeveliyor, oysa aynı araç bir damgalama ve dışlama aygıtına dönüşebilir. Ayrıca bulguların en zayıf halkası tam da Türkiye'nin ilgisini çekecek kısım: döngüler iyileşmeyi **aracılamıyor**, yani 'konuşma yapısını düzeltirsek tedavi hızlanır' iddiası bu veriyle desteklenmiyor. Türkiye'deki psikoterapi politikası tartışmalarında (seans sayısı, kamu geri ödemesi, çevrimiçi terapi) bu aracın bir 'kalite ölçütü' olarak dolaşıma sokulmasına karşı temkinli olunmalı.

## 🏷 Retorik Roller

- 🧩 **Yöntem**
- 📊 **Bulgular**
- ⚠️ **Sınırlılıklar**

---

## 🔗 İlgili Bağlantılar
### 🧠 İlgili Kavramlar
- [[concepts/metin-madenciligi.md|Metin Madenciliği ve Hesaplamalı Metin Analizi]]
### 🏛 İlgili Kurum/Kişiler
- [[entities/osf-io.md|Osf Io]]
