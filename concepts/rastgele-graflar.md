---
type: concept
title: Rastgele Grafikler ve Sandviç Eşlemesi
description: 'Rastgele grafik modelleri (binom G(n,p), düzenli G_d(n), konfigürasyon modeli) ve bu modeller arasında özellik transferi sağlayan eşleme (coupling) teknikleri; Kim-Vu sandviç varsayımının 2025''te tam kanıtı.'
tags:
- akademik
- metodoloji
- rastgele-graflar
- ag-bilimi
- olasilik
timestamp: '2026-11-03T00:00:00Z'
created: 2026-11-03
updated: 2026-11-03
confidence: medium
---
# Rastgele Grafikler ve Sandviç Eşlemesi

Ağ (network) araştırmalarının matematiksel temeli: gözlenen bir ağın yapısal özelliklerinin ne kadarının rastlantıyla açıklanabileceğini sınamak için rastgele grafik modelleri "null model" olarak kullanılır.

- **Binom (Erdős–Rényi / Gilbert) grafik G(n,p):** her düğüm çifti bağımsız olarak p olasılıkla bağlanır. Analizi kolaydır; gerçek ağların derece dağılımını ve kümelenmesini temsil etmez.
- **Düzenli rastgele grafik G_d(n):** her düğümün derecesi tam olarak d'dir. Gerçek ağlara daha yakındır ama kenarlar birbirine bağımlı olduğu için analizi belirgin biçimde zordur.
- **Konfigürasyon modeli / derece-koruyan yeniden kablolama:** ampirik çalışmalarda en sık kullanılan null model; derece dizisini koruyarak kenarları rastgele yeniden dağıtır.

**Sandviç varsayımı (Kim–Vu, 2004):** d = ω(log n) iken öyle p_* = (1-o(1))d/n, p^* = (1+o(1))d/n ve öyle bir eşleme (G_*, G, G^*) vardır ki G_* ~ G(n,p_*), G ~ G_d(n), G^* ~ G(n,p^*) ve P(G_* ⊂ G ⊂ G^*) = 1-o(1). Yani zor model, iki kolay model arasına sıkıştırılır.

**Neden önemli:** Böyle bir eşleme, binom grafikler için kanıtlanmış özelliklerin (bağlantılılık, dev bileşen, çap, spektral boşluk) düzenli grafikler için bedava geçmesini sağlar; düzenli grafikler hakkındaki sonuçlar tek bir "meta-teorem" üzerinden yeniden yazılabilir. Ampirik karşılığı: derece-koruyan null modelin hangi koşullarda hedef ağın özelliklerini gerçekten taşıdığı sorusuna teorik dayanak.

**Durum:** Alt dilim (düzenli ⊃ binom) yıllar içinde kanıtlandı; Gao–Isaev–McKay (2019 prosedürü, 2020'de d ≫ log⁴n için kısmi ispat); 2025'te Behague–Il'kovič–Montgomery varsayımı tüm d için kanıtladı (arXiv:2510.20765, hakem değerlendirmesi sürüyor).

**Bağlantılı kavramlar:** [[concepts/siyaset-bilimi-metodolojisi.md|Siyaset Bilimi Metodolojisi]], [[concepts/sosyal-kutuplasma.md|Sosyal Kutuplaşma]]

## İlgili Makaleler
- [[raw/articles/2026-09-18_graph-sandwich-kim-vu-conjecture-proved-after-two-.md|Graph Sandwich: Kim-Vu Conjecture Proved After Two Decades]] — Quanta Magazine (18 Eylül 2026); sandviç varsayımının tam kanıtı ve düzenli/binom rastgele grafikler arasında özellik transferi.
