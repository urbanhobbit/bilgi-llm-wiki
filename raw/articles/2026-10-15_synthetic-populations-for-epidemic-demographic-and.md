---
type: raw_article
title: Synthetic populations for epidemic, demographic and mobility modeling
description: Torre, Artigues, Faucher, Ramasco, Valdano ve arkadaşlarının (ISI Foundation,
  IFISC-CSIC, Sorbonne/INSERM, IMEDEA, UPF) ön baskısı, birey-tabanlı (agent-based)
  modellerin altyapısı olan sentetik popül...
resource: https://arxiv.org/abs/2610.21784
tags:
- kurator
- medium
timestamp: '2026-10-19T13:27:39Z'
source_file: 2026-10-19_synthetic-populations-epidemic-demographic-mobility.json
category: KURATOR
priority: medium
roles:
- gap
- method
- result
- limitation
published: '2026-10-15'
---

# Synthetic populations for epidemic, demographic and mobility modeling

**Author(s):** Davide Torre; Miguel Artigues; Benjamin Faucher; Roberto Alcaraz; Jacopo D'Ignazi; Antonia Tugores; Mattia Mazzoli; Daniela Paolotti; José J. Ramasco; Eugenio Valdano (ISI Foundation Torino; IFISC CSIC-UIB; IMEDEA; Universitat Pompeu Fabra; Sorbonne Université/INSERM)

**Published:** 2026-10-15

**Source:** [https://arxiv.org/abs/2610.21784](https://arxiv.org/abs/2610.21784)

## Summary

Torre, Artigues, Faucher, Ramasco, Valdano ve arkadaşlarının (ISI Foundation, IFISC-CSIC, Sorbonne/INSERM, IMEDEA, UPF) ön baskısı, birey-tabanlı (agent-based) modellerin altyapısı olan sentetik popülasyonlar için İspanya, Fransa ve İtalya'yı kapsayan harmonize bir veri seti sunuyor. Yazarların tespit ettiği boşluk iki katmanlı: mevcut sentetik popülasyonlar ya tek bir ülkeye/şehre özgü tasarlanıyor ya da ülke çapında kapsamı gerçekçi ve AÇIK mekânsal ayrıntıyla birleştiremiyor; bu yüzden hane, işyeri, boş zaman mekânı ve günlük hareketlilik arasındaki ilişki modellenemiyor ve hedefli politika değerlendirmesi (okul kapatma, işyeri mesafelenmesi, aşılama kampanyası) zayıflıyor. Çözüm, üç ülkenin farklı format ve çözünürlükteki nüfus sayımı kaynaklarını (İspanya INE, Fransa INSEE, İtalya ISTAT) tek bir veri şemasında birleştiren bir üretim hattı: her ajan için yaş, cinsiyet, mesleki durum (çalışan/öğrenci/çalışmayan), ekonomik sektör, hane üyeliği ve hane tipi, ikamet binası (kadastro/istatistik kayıtları), ana faaliyet binası (gerçek işyeri ve okul kayıtları, OSM bina envanteriyle birleştirilmiş), belediye düzeyinde işe gidiş-geliş akışları (OD matrisleri; İspanya'da cep telefonu verisi) ve günlük zaman kullanımı programı (ulusal zaman kullanımı anketleri, toplu iş sözleşmeleri, OSM açılış saatleri). Çıktı üç veri çerçevesi: agents, buildings, schedules; her satır bir ajan, kimlik alanları ülke kod sistemlerine (ISTAT, INE PPMMM, INSEE) bağlı, hane tipi 0-9 arası ortak bir taksonomiye eşlenmiş. Doğrulama üç aşamalı ve ciddi: (1) yaş piramidi — toplam nüfus hatası İspanya'da -%0,04 (MAPE %0,12), İtalya'da -%0,03 (MAPE %0,11), Fransa'da -%2,51 (MAPE %2,85; yalnızca metropoliten Fransa, hane sayısı %7,94 eksik); (2) mekânsal dağılım — İtalya'da Roma'nın 2.798 sayım bölgesinin %98,4'ü tam isabet, il (NUTS-3) düzeyinde hatalar -%0,13 ile -%0,002 arası; İspanya'da Madrid'in 1.597 bölgesinde medyan hata +%5,9; Fransa'da IRIS medyanı -%2,6; (3) hareketlilik — sentetik ve gerçek OD seyahat olasılıkları arasında Pearson r = 0,9998 (İspanya), 0,9612 (Fransa), 0,9842 (İtalya); (4) hane içi eş-bulunma matrisi ile temas anketleri karşılaştırması — İtalya Prem ve ark. (2017) ile r=0,97, Fransa aynı çalışmayla r=0,94, İspanya Prem ve ark. (2021) ile r=0,91; Polymod ile İtalya r=0,87, Fransa r=0,82. Yani coğrafi açıklığı eklemek, yaş yapılı hane karışımı sadakatini bozmuyor — makalenin ana savı bu. Sınırlar açıkça yazılmış: İtalya'da hane üretimi 2001 nüfus sayımı mikro verisine, OD matrisleri 2011 sayımına dayanıyor (zaman uyumsuzluğu); İspanya'da zaman kullanımı ve hane mikro verisi yalnızca toplulaştırılmış/temsili örneklem düzeyinde; OD matrisleri seyahat amacı içermiyor ve küçük belediyelerde seyrek akışlar yüksek varyans üretiyor; Fransa'da işe gidiş akışları meslek/sosyo-ekonomik statüye göre stratifiye değil ve okul kapasiteleri bina ayak izinden tahmin edilmiş; kadastro ve OSM kapsamı yerel olarak eksik olabiliyor. Veri seti DIGITAL.CSIC deposunda (DOI 10.20350/digitalCSIC/17518) yayınla birlikte açılacak; kod da yayınla birlikte paylaşılacağı belirtiliyor. Makale, hesaplamalı sosyal bilim (computational social science) ve hesaplamalı epidemiyoloji altyapısı olarak okunmalı: politika müdahalelerinin in silico testi, afet/çevresel maruziyet analizi ve kentsel hareketlilik simülasyonu için yeniden kullanılabilir bir taban.

## Key Points

- Künye: arXiv:2610.21784 [physics.soc-ph], 15 Ekim 2026 (v1), 31 sayfa; hakem değerlendirmesinden geçmemiş ön baskı; 10 yazar, ISI Foundation (Torino) + IFISC (CSIC-UIB) + IMEDEA + UPF + Sorbonne/INSERM.
- Boşluk: mevcut sentetik popülasyonlar ya tek ülkeye/şehre özgü ya da ülke çapında kapsamı ince mekânsal çözünürlükle birleştiremiyor; sonuç, hane-işyeri-boş zaman-hareketlilik etkileşiminin gerçekçi temsil edilememesi.
- Katkı veri setinin kendisi: İspanya, Fransa, İtalya için her ajanın yaş, cinsiyet, mesleki durum, sektör, hane tipi, ikamet binası, iş/okul binası, POI ve günlük zaman programı atanmış, sayım bölgesi (census tract) düzeyinde konumlanmış harmonize popülasyon.
- Tasarım: sayım bölgesinde hane tipi örnekleme → yaş/cinsiyet piramidinden birey atama → yoğunluğa göre coğrafi yerleştirme → OD matrisleriyle işe/okula gidiş atama → zaman kullanımı anketleri ve toplu iş sözleşmeleriyle günlük program.
- Çıktı şeması: agents (code, dwelling_id, household_type 0-9, person_id, age, sex, activity 0/1/2, cell_group, sector, cell_dest, ref_dest), buildings (kapasite + coğrafi referans) ve schedules; ülke kodları ISTAT/INE/INSEE sistemlerine bağlı, ortak hane tipi taksonomisiyle karşılaştırılabilir.
- Doğrulama - demografi: toplam nüfus hatası İspanya -%0,04 (MAPE %0,12), İtalya -%0,03 (MAPE %0,11), Fransa -%2,51 (MAPE %2,85; metropoliten Fransa, hane sayısı %7,94 eksik, tek kişilik hane payı +2,02 puan fazla).
- Doğrulama - mekân: Roma'nın 2.798 sayım bölgesinin %98,4'ü tam isabet; İtalya il düzeyinde hata -%0,13…-%0,002; Madrid 1.597 bölgede medyan +%5,9 (%90 aralık -%13,7…+%16,5); Fransa IRIS medyanı -%2,6.
- Doğrulama - hareketlilik ve temas: OD seyahat olasılıkları ile Pearson r = 0,9998 (ES) / 0,9612 (FR) / 0,9842 (IT), tümü p<0,001; hane eş-bulunma matrisi İtalya Prem 2017 r=0,97, Fransa r=0,94, İspanya Prem 2021 r=0,91; Polymod ile r=0,87 (IT) ve 0,82 (FR) — coğrafi açıklık, yaş yapılı hane karışımı sadakatini bozmuyor.
- Sınırlar: İtalya'da 2001 hane mikro verisi + 2011 OD matrisi (zaman uyumsuzluğu); İspanya'da yalnızca toplulaştırılmış veri, seyahat amacı yok; küçük belediyelerde OD akışları seyrek ve yüksek varyanslı; Fransa'da işe gidiş akışları meslek grubuna göre stratifiye değil, okul kapasitesi ayak izinden tahmin; kadastro/OSM kapsamı yerel olarak eksik.
- Erişim: veri seti DIGITAL.CSIC DOI 10.20350/digitalCSIC/17518 (yayınla birlikte açılacak), girdi verileri INE/INSEE/ISTAT, kod yayınla birlikte. Yeniden üretilebilirlik iddiası bu nedenle şu an kısmen doğrulanabilir durumda.
- Yöntemsel konum: bu bir 'hesaplamalı sosyal bilim altyapısı' makalesi — yeni bir nedensel bulgu değil, birey-tabanlı simülasyonların (salgın kontrolü, afet maruziyeti, kentsel hareketlilik, demografi) ortak tabanı.

## Turkey Context

Türkiye'de birey-tabanlı salgın ve hareketlilik modelleri için en büyük engel tam olarak bu makalenin çözdüğü sorun: nüfus sayımı mikro verisi ile mekânsal ayrıntıyı birleştiren açık bir sentetik popülasyon yok. TÜİK'in ADNKS tabanlı nüfus verileri mahalle düzeyine kadar iniyor, ancak hane tipi/hane büyüklüğü dağılımı, meslek-sektör kırılımı ve işe gidiş akışları çoğunlukla toplulaştırılmış ve erişimi kısıtlı biçimde yayımlanıyor; ulaşım OD matrisleri ise tek tek büyükşehirlerin (İBB gibi) ulaşım ana planı çalışmalarında kalıyor, ülke çapında açık değil. Bu, COVID-19 döneminde Türkiye için kurulan ajan-tabanlı modellerin neden genellikle il/ilçe düzeyinde homojen karışım varsayımına düştüğünü açıklıyor. Pratik çıkarımlar: (1) İstanbul için deprem senaryolarında bina-hane eşleştirmesiyle maruziyet hesabı yapılacaksa, buradaki hat (kadastro → bina → hane → birey) Türkiye'de kısmen uygulanabilir, çünkü OSM bina kapsamı büyükşehirlerde iyi ve adres tabanlı nüfus kayıtları mevcut; darboğaz hane kompozisyonu ve işe gidiş akışları. (2) TÜİK'in Hanehalkı İşgücü ve Zaman Kullanımı araştırmaları, İspanya/İtalya'daki gibi toplulaştırılmış marjinal dağılım sağlıyor — sentetik üretim için yeterli olabilir, ancak doğrulama için temas anketi (Polymod benzeri) verisi Türkiye'de yok; bu doğrulama boşluğu literatürde sık atlanıyor. (3) Açık veri ve yeniden üretilebilirlik açısından makalenin kendi sınırı da öğretici: veri 'yayınla birlikte açılacak' deniyor; Türkiye'de kurulacak benzer bir hat için lisans/erişim belirsizliği baştan planlanmalı. (4) Siyasi davranış araştırmaları için dolaylı katkı: seçmen davranışını mekânsal ajan-tabanlı modellerle simüle etmek isteyenler için hane ve mahalle düzeyi eşleştirme şablonu sağlıyor — kutuplaşmanın mahalle düzeyi ayrışmasını (segregation) modellemek için doğrudan kullanışlı bir iskelet.

## 🏷 Retorik Roller

- 🔍 **Araştırma Boşluğu**
- 🧩 **Yöntem**
- 📊 **Bulgular**
- ⚠️ **Sınırlılıklar**

---

## 🔗 İlgili Bağlantılar
### 🧠 İlgili Kavramlar
- [[concepts/siyaset-bilimi-metodolojisi.md|Siyaset Bilimi Metodolojisi]]
### 🏛 İlgili Kurum/Kişiler
- [[entities/arxiv-org.md|Arxiv Org]]
