---
type: concept
title: 'Siyasal Temsil ve Tepkisellik (Political Representation)'
description: 'Seçmen tercihlerinin siyasa çıktısına ve gündeme ne ölçüde yansıdığı: siyasa uyumu, gündem kapsanması ve gündem ilerlemesi ayrımı; sabit maddeli anketlerden retrieval-augmented ölçüme uzanan yöntem hattı ve "ikinci/üçüncü yüz" tartışması.'
tags:
- kavram
- temsil
- siyaset-bilimi
- kamuoyu
- olcum
timestamp: '2026-11-06T16:00:00Z'
created: '2026-11-06'
updated: '2026-11-06'
sources:
- raw/articles/2026-11-03_velez-ewig-retrieval-augmented-surveys-for-measuri.md
related:
- concepts/betimleyici-temsil.md
- concepts/olcum-araclari.md
- concepts/yapay-zeka-demokrasi.md
confidence: medium
---

# Siyasal Temsil ve Tepkisellik

## Tanım

**Siyasal temsil**, seçmenlerin tercihlerinin karar alma sürecine ne ölçüde yansıdığıdır. Ampirik literatür bunu tek bir ölçüyle değil, üç ayrı aşamada ölçer:

| Aşama | Soru | Tipik ölçüm |
|---|---|---|
| **Siyasa uyumu** (policy congruence) | Seçmen çoğunluğu ile karar vericinin tercihi örtüşüyor mu? | Sabit maddeli kamuoyu anketi ↔ oy/kayıt verisi |
| **Gündem kapsanması** (agenda inclusion) | Seçmenin önemsediği konuya karşılık gelen bir öneri sistemde var mı? | Öncelik beyanı ↔ kanun teklifi/komisyon gündemi |
| **Gündem ilerlemesi** (agenda progression) | O öneri komisyonu/Genel Kurul'u geçti mi, kanunlaştı mı? | Süreç aşaması verisi |

Bu ayrım, gücün yalnız görünür oylarla değil **gündem yönetimiyle** de işlediğini söyleyen "ikinci yüz" (Bachrach & Baratz 1962; Schattschneider 1960) ve "üçüncü yüz" (Lukes) tartışmasının ampirik ayağıdır. Kingdon'un (1984) "sistemik gündem / kurumsal gündem" ayrımı da buraya bağlanır.

## Klasik ölçümün kısıtı

Standart yaklaşım, araştırmacının seçtiği sabit konu listesi üzerinden kamuoyu ile siyasa çıktısını karşılaştırır. İki sorun doğar:

- **Kapsam yanlılığı:** Seçmenin gerçekten önemsediği ama ankette yer almayan konu görünmez; anketteki maddede anlaşma varsa kişi "temsil edilmiş" sayılır (Wlezien 2017).
- **Aşama yanlılığı:** Yalnız oylama/kanunlaşma aşamasına bakıldığında, önerinin hiç doğmadığı ya da komisyonda öldüğü durumlar ölçü dışında kalır.

## Yeni yöntem hattı: retrieval-augmented survey

Velez ve Ewig (2026, *Political Analysis*) bu kısıtı şöyle aşıyor: katılımcı kendi önceliğini açık uçlu yazar → netleştirme adımı → gömme modeliyle kurumsal metin tabanından (ör. Kongre faturaları) **en yakın üç politika** getirilir → kişiye özel maddeler olarak destek ölçülür → LLM bu politikaların kişinin derdini karşılayıp karşılamadığını kodlar → gündem aşaması izlenir. Ayrıntı: [[raw/articles/2026-11-03_velez-ewig-retrieval-augmented-surveys-for-measuri.md|Velez & Ewig (2026)]].

**Ampirik sonuç (ABD, 118. Kongre):** gündem kapsanması %77, ilerlemesi %12; karşılayan faturaların %84'ü komisyonda tıkanıyor. Yani temsil sorunu çoğu zaman "konu gündeme hiç girmiyor" değil, **"komisyon kapısında duruyor"**.

## Neden önemli

- Temsil açığını "seçmen bilgisiz" ya da "parti disiplini" gibi tek nedene bağlamak yerine **süreç aşaması** bazında teşhis etmeyi sağlar.
- **Kimin önceliği ilerliyor** sorusunu ölçülebilir kılar: cinsiyet, gelir, eğitim, etnisite ve partizanlık kırılımlarında farklar görünür hale gelir (betimleyici temsil tartışmasından farklı olarak *siyasa* düzeyinde).
- Yöntem modüler: belediye bütçesi, kural koyma (rulemaking), parti programı gibi alanlara aynı hat taşınabilir.

## Sınırlılıklar ve uyarılar

- **"Üçüncü yüz" sessizliği:** Katılımcıların bir kısmı hiçbir öncelik beyan etmiyor (ABD örneğinde %15); bu grup düşük gelirli, düşük eğitimli ve daha az oy kullanan. Temsil ölçümü tam da sesi en az çıkan kesimi dışarıda bırakma riski taşır.
- Ölçüm **LLM kodlamasına** dayanır; insan kodlamasıyla uyuşma yüksek olsa da (%83,6) sistematik hata düzeltmesi (design-based supervised learning) gereklidir.
- Kurumsal metin tabanı ve aşama sınıflandırması ülkeye özgüdür; "temsil" sayıları ülkeler arası doğrudan karşılaştırılamaz.
- Temsil ≠ sorumluluk (accountability): seçmen önceliğinin gündeme girmesi, seçmenin bunu ödüllendirdiği anlamına gelmez.

## Türkiye notu

TBMM'nin kanun teklifleri, komisyon gündemleri ve tutanakları açık; yani kapsanma/ilerleme ölçümü **teknik olarak mümkün**. Türkiye literatüründe bu ölçüm sistematik olarak yapılmıyor: seçmen önceliği ile teklif üretimi arasındaki bağ, komisyonda tıkanma oranları ve bunun parti/etnisite/cinsiyet kırılımı boş alan. Aynı yöntem için iki ön koşul: (1) Türkçe metin gömme hattı ve nötr teklif özetleri, (2) "öncelik beyan etmeyen" kesimin oranının ölçülmesi — bu oran Türkiye'de siyasal uzaklaşmanın göstergesi olarak kendi başına değerli bir veri.

İlgili: [[concepts/betimleyici-temsil.md|betimleyici temsil]] (kimlik aynası), [[concepts/olcum-araclari.md|ölçüm araçları]], [[concepts/yapay-zeka-demokrasi.md|yapay zeka ve demokrasi]].
