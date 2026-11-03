---
type: concept
title: Katılımcıların Ankette Yapay Zekâ Kullanımı
description: 'Anket ve deney katılımcılarının açık uçlu yanıtları üretken yapay zekâya yazdırması: yazarlık atfı belirsizliği, veri kalitesi/geçerlilik kaybı ve araştırmacının dışlama kararlarının yöntemsel sonuçları.'
tags:
- akademik
- metodoloji
- anket-yontemi
- veri-kalitesi
- yapay-zeka
timestamp: '2026-11-03T00:00:00Z'
created: 2026-11-03
updated: 2026-11-03
confidence: medium
---
# Katılımcıların Ankette Yapay Zekâ Kullanımı

Anket araştırmalarında yapay zekâ tartışması genellikle araştırmacı tarafında yürür (soru yazımı, kodlama, sentetik yanıt üretimi). Bu kavram, tartışmanın diğer tarafını adlandırır: **gerçek katılımcının kendi yanıtını üretken bir yapay zekâ aracına yazdırması**.

**Neden yöntemsel bir sorun:**
- **Yazarlık atfı belirsizliği:** Bir yanıtın insan mı model mi olduğu, mevcut göstergelerle (akıcılık, kalıp ifadeler, uzunluk, sözcük dağarcığı, biçimlendirme) güvenilir biçimde belirlenemez. Bu örüntüler "olası gösterge"dir, kanıt değildir; uzman değerlendiriciler arasında uyum da düşüktür.
- **Veri kalitesi ve geçerlilik:** Model yanıtları daha homojen ve daha olumlu eğilimlidir; hassas sorularda toplumsal varyasyonu maskeleyebilir. Bu, kutuplaşma, hoşgörü, azınlık algısı gibi ölçümlerde sistematik yanlılık demektir.
- **Araştırmacı kaynaklı kararlar:** Şüphe, veri toplandıktan sonra ortaya çıktığında araştırmacı eleme yapmak zorunda kalır; dışlama ölçütü kişisel yargıya bağlıysa çalışmanın geçerliliği ve tekrarlanabilirliği zarar görür.
- **Etik ve onam:** Aydınlatılmış onam metinleri katılımcı AI kullanımını genellikle kapsamaz; sonradan yapılan dışlamaların meşruiyeti bu boşluğa takılır.

**Kanıtlanmış vaka:** Julia Goetze'nin *Research Methods in Applied Linguistics* 5(3) (2026, 100392) tarihli deneyimsel vaka raporunda, açık uçlu yanıtlarda AI şüphesi analitik örneklemi 259'dan 29 katılımcıya indirdi (180'i şüphe, 50'si eksik/İngilizce olmayan veri veya uygunsuzluk); çok aşamalı tarama, veri işaretleme ve beş kişilik uzman paneli belirsizliği gidermedi.

**Ampirik eğilim:** Zhang, Xu ve Alvero (2025, *Sociological Methods & Research*) ABD'deki bir çevrimiçi panelde katılımcıların %34'ünün açık uçlu sorularda LLM kullandığını bildirdiğini gösterdi; LLM yanıtları insan yanıtlarına göre daha homojen ve daha olumlu.

**Alandaki kurumsal yanıt:** AAPOR'un *Responsible AI Integration in Survey Research* raporu (Mayıs 2026) ve anket metodolojisi literatüründeki yorumlar (nature.com, Ağustos 2026), saha çapında kanıta dayalı kılavuz ihtiyacını tanımlıyor. Türkçe literatürde bu konuda çalışma yok.

**Pratik önlemler (Goetze'nin çerçevesi ve alan pratiği):** onam metnine katılımcı AI kullanımını yasaklayan/raporlayan madde; veri toplamadan önce dışlama protokolünün tanımlanması; çok aşamalı tarama ve işaretleme; dışlanan yanıt sayısı ve gerekçesinin raporlanması; şüphenin kanıt sayılmaması.

**Ayrım:** [[concepts/sentetik-populasyonlar.md|Sentetik Popülasyonlar]] araştırmacının yanıt üretmesini, bu kavram ise katılımcının yanıtını makineye yazdırmasını anlatır; ikisi farklı veri kalitesi sorunlarıdır ve farklı önlemler gerektirir.

**Bağlantılı kavramlar:** [[concepts/siyaset-bilimi-metodolojisi.md|Siyaset Bilimi Metodolojisi]], [[concepts/yapay-zeka-destekli-gorusmeler.md|Yapay Zekâ Destekli Görüşmeler]], [[concepts/sentetik-populasyonlar.md|Sentetik Popülasyonlar]]

## İlgili Makaleler
- [[raw/articles/2026-12_participant-ai-use-in-survey-research.md|Participant AI Use in Survey Research]] — Goetze (2026), RMAL 5(3), 100392: 259 → 29 örneklem kaybı, beş uzman değerlendirici, üç yöntemsel meydan okuma.
