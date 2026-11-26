---
type: concept
title: Ölçüm Araçları (Polarization Measurement)
description: Kutuplaşma ve partizanliği ölçen anket/psikometrik araçlar; bulguların araca bağımlılığı.
tags:
- kavram
- metodoloji
- olcum
- kutuplasma
timestamp: '2026-07-31T00:00:00Z'
created: '2026-07-31'
updated: '2026-11-26'
sources:
- raw/articles/2026-10-14_timoneda-synthetic-imputation-sparse-categories.md
related: []
confidence: medium
---

# Ölçüm Araçları

## Tanım
Kutuplaşma araştırmalarında kullanılan ölçüm araçları: termometreler, duygu bataryaları, sosyal mesafe ölçekleri, parti kimliği gücü ölçekleri vb.

## Önem
- **Bankert & Zingher (2026):** Partizanlik-kutuplaşma ilişkisi kullanılan ölçüm aracına göre önemli ölçüde değişiyor; bulgular araca bağımlı.
- **Holliday (2026):** Kesitsel anketler, panel verisi olmadan hardening/churn ayrımını yapamaz — ölçüm tasarımı kritik.

## İlgili Makaleler
- [[raw/articles/2026-07-23_partisan-hearts-polarized-minds.md|Partisan Hearts, Polarized Minds?]]
- [[raw/articles/2026-07-31_changing-partisanship-contributes-significantly-to.md|Changing Partisanship Contributes Significantly to Rising Affective Polarization]]

## Sınıflandırıcı temelli ölçümde seyrek kategori sorunu

Anket aracına bağımlılığın metin-kodlama karşılığı: **etiketli veri miktarına bağımlılık**. Seyrek bir kategori (ör. "nostaljik söylem", "dezenformasyon") az örnekle kodlandığında sınıflandırıcı hem eğitimde hem değerlendirmede zayıflıyor; ölçüm hatası aşağı-akış tahminlere taşınıyor. Timoneda (2026) bu hatayı **sentetik imputasyon** ile eğitim öncesinde azaltmayı öneriyor; Egami vd. (2023) DSL ise eğitim sonrasında düzeltme yapıyor. İkisi farklı aşamalarda çalıştığı için tamamlayıcı — ayrıntı: [[concepts/sentetik-imputasyon-seyrek-kategoriler.md]]

Temel uyarı: sentetik artırma, ölçüm aracının kendisini iyileştirmez; yalnızca az örnekli kategoride varyansı düşürür. Kategori tanımının kuramsal geçerliliği ayrı bir soru olarak durur (bkz. [[concepts/kuram-operasyonellestirme-llm.md]]).
