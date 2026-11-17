---
type: concept
title: Nefret Söylemi
description: Korumalı kimlik özelliklerine (etnisite, din, cinsiyet kimliği, cinsel yönelim) yönelen, ceza hukuku ile ifade özgürlüğü arasında sıkışan ve platform yönetişiminin merkezinde duran söylem biçimi; otomatik tespiti çok-etiketli sınıflandırma, kimlik özniteliği çıkarımı ve yanlılık denetimi gerektirir.
tags:
- kavram
- nefret-soylemi
- hate-speech
- icerik-moderasyonu
- yapay-zeka
timestamp: '2026-11-17T00:00:00Z'
created: '2026-11-17'
updated: '2026-11-17'
sources: []
related: []
confidence: medium
---

# Nefret Söylemi

## Tanım
Nefret söylemi, bir kişi ya da grubu korumalı bir kimlik özelliği (etnisite, din, cinsiyet kimliği, cinsel yönelim, engellilik) nedeniyle hedef alan, aşağılayan veya şiddete teşvik eden söylem. Hukuki tanımı ülkeden ülkeye değişir — Norveç Ceza Kanunu § 185, Türkiye'de TCK 216 — ve BM Medeni ve Siyasi Haklar Sözleşmesi'nin ifade özgürlüğü ile ayrımcılık yasağı arasındaki gerilimini taşır. Otomatik tespit literatürü, tanım çokluğunu **çok-etiketli** bir şemaya çevirir: potansiyel nefret (PH), potansiyel ofansif (PO), potansiyel saldırgan (PA), nötr (N).

## Araştırma
- **Hashmi & Yayilgan (2026), *Machine Learning and Knowledge Extraction* 8(9):292:** İngilizce–Norveççe 14.008 örneklik iki dilli veri kümesi (11.528 EN / 2.480 NO; X + Facebook kamuya açık gönderiler, iki aylık toplama) üzerinde altı aşamalı etik tasarım çerçevesi. NorBERT-small makro F1 0,92 / alt-küme doğruluğu 0,94; dil bazında İngilizce 0,92, Norveççe 0,89, kod-değiştiren metin 0,87 — **dil kırılımı, tek dilli raporlanan skorların olduğundan iyi göründüğünü** gösteriyor. Kimlik kaynaklı yanlılık eşanlamlı artırma + kimlik-koşullu etiket-karşıtlığı artırması + dengeli kayıp yeniden ağırlıklandırma ile azaltılmış; artık farklar bazı kimlik çiftlerinde sürüyor.
- **Adillik ölçümü dar:** yalnızca flip rate (FR) ve tahmin olasılığı değişimi; demografik parite, eşitlenmiş odds ve kesişimsel adillik ölçülmemiş. Nefret söylemi tespitinde "yüksek F1" ile "adil model" arasındaki boşluğun tipik örneği.
- **Veri erişimi = araştırma kapasitesi:** veri kümesi GDPR/gizlilik gerekçesiyle yayımlanmamış; aynı koruma rejimi (KVKK, GDPR) Türkiye'deki araştırmacılar için de etiketli Türkçe korpus üretimini fiilen engelliyor. Alanın ilerlemesi model mimarisinden çok **veri yönetişimine** bağlı.
- **Kolluk kullanımı:** yazarlar aracı cezalandırma değil önleyici müdahale hedefleme (hangi ortamların programa ihtiyacı var) olarak konumlandırıyor; gerçek zamanlı toplama ve operasyonel konuşlandırma henüz yok.

## İlgili Kavramlar
- [[concepts/yapay-zeka-yonetisimi.md|Yapay Zeka Yönetişimi]]
- [[concepts/dijital-haklar.md|Dijital Haklar]]
- [[concepts/dezenformasyon.md|Dezenformasyon]] — nefret söylemi ile bilgi bozukluğu ayrı olgular; aynı platform altyapısında kesişir

## İlgili Makaleler
- [[raw/articles/2026-09-21_ethical-and-socially-aware-english-norwegian-hate-.md|Ethical and Socially Aware English–Norwegian Hate Speech Detection: A Systematic Design Framework]] — Hashmi & Yayilgan, MAKE 8(9):292, 2026
