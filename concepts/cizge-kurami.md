---
type: concept
title: Çizge Kuramının Temelleri
description: 'Düğüm-kenar dilinin asgari sözlüğü: yürüyüş/yol, bağlantılılık, BFS/DFS, döngü-ağaç, düzlemsellik, renklendirme, Ramsey sayıları, merkezilik ve PageRank. Ağ temelli sosyal bilim analizlerinin (kutuplaşma ağları, dezenformasyon yayılımı) önkoşulu.'
tags:
- akademik
- metodoloji
- ag-bilimi
- cizge-kurami
- merkezilik
timestamp: '2026-11-11T00:00:00Z'
created: 2026-11-11
updated: 2026-11-11
confidence: medium
---
# Çizge Kuramının Temelleri

Sosyal bilimde "ağ" (network) denilen şeyin biçimsel karşılığı **çizge**dir: düğümler (aktörler) ve kenarlar (ilişkiler). Bir çizge, çiziminden bağımsızdır — aynı yapının sonsuz sayıda çizimi olabilir (izomorfizm). Bu ayrım, ampirik ağ araştırmalarında görselleştirmenin kanıt sayılmaması gerektiğinin de matematiksel gerekçesidir.

**Temel dizge.** Yürüyüş (walk) = düğüm ve kenarların ardışık dizisi; tekrarlar kırpılarak **yol** (path) elde edilir. Ulaşılabilirlik bir denklik bağıntısıdır (yansımalı, simetrik, geçişli); bundan dolayı bağlantılılık bileşenlere ayrışır. **BFS** katman katman ilerler ve en az kenar sayılı yolu garanti eder; **DFS** derine iner, tükenince geri sarar — en kısa yolu garanti etmez. Döngü (cycle), kenar silinmesine karşı dayanıklılık üretir ama düğümler arasındaki yolu belirsizleştirir ve hiyerarşik sıralamayı engeller.

**Ağaç = dört eşdeğer tanım.** (1) bağlantılı ve döngüsüz; (2) minimum bağlantılı — herhangi bir kenar silinince iki bileşene ayrılır, yani hiçbir kenar fazlalık değildir; (3) maksimum döngüsüz — iki düğüm arasına yeni kenar eklemek döngü yaratır; (4) her düğüm çifti arasında **tek** yol vardır. Dördüncüsü, kök seçip düzey tanımlamayı (yani hiyerarşiyi) mümkün kılar; karar ağaçları ve labirent çözümü (DFS = sol-el kuralı) buradan çıkar.

**Düzlemsellik.** Düzlemsel çizgelerde Euler formülü: v − e + f = 2. Her kenar iki yüze, her yüz en az üç kenara komşu olduğundan 2e ≥ 3f, yani **e ≤ 3v − 6**. K₅ (5 düğüm, 10 kenar; 3·5−6 = 9 < 10) ve K₃,₃ düzlemsizdir; **Kuratowski teoremi** bunun tersini de verir: bir çizge düzlemsizdir ancak ve ancak K₅ ya da K₃,₃'ün bir altbölümü (subdivision) altçizge olarak bulunuyorsa.

**Renklendirme.** Kromatik sayı χ = komşuların farklı renk alması için gereken en az renk. **Dört renk teoremi:** düzlemsel ⇒ χ ≤ 4. Kritik nokta: yüksek χ, büyük bir klik (tam altçizge) gerektirmez — Mycielskian inşası üçgensiz çizgelerin χ'sini sınırsız artırır. Kenar renklendirmede **Vizing teoremi** çok daha keskin bir sınır verir: χ′ ya Δ ya Δ+1 (Δ = maksimum derece).

**Ramsey teorisi.** K₆'nın iki renkli her kenar boyamasında tek renkli bir üçgen vardır: R(3) = 6 (güvercin yuvası ilkesiyle kanıt). Tam bilinen değerler yalnızca R(1)=1, R(2)=2, R(3)=6, R(4)=18; sonrası aralık: R(5) ∈ [43,46], R(6) ∈ [102,160], R(7) ∈ [205,492]. Sosyal ağ okuması: 18 kişilik bir toplulukta, birbirini karşılıklı tanıyan ya da hiç tanımayan 4 kişi **zorunlu** olarak vardır.

**Neden metodoloji sayfası:** Ampirik ağ araştırmasında kullanılan iki ölçüt bu dizgeden türer. (a) **PageRank**, yönlü ağırlıklı çizge üzerindeki rastgele yürüyüşün **denge dağılımı**dır (Markov zinciri geçiş matrisinin durağan dağılımı). (b) **Arasındalık merkeziliği** (betweenness centrality), tüm s−t en kısa yolları içinde v düğümünden geçenlerin oranının toplamıdır; trafik/etkileşim verisi olmadan darboğazları görünür kılar. Kutuplaşma ve dezenformasyon ağlarında "hangi hesaplar köprü işlevi görüyor" sorusunun en savunulabilir operasyonelleştirmesi budur.

**Sınırlılık:** Bu sayfa, hakemsiz bir öğretici metinden (aşağıdaki kaynak) derlenmiş **yöntem sözlüğüdür**; ampirik bulgu içermez, kanıt olarak atıf yapılamaz. Matematiksel ifadeler ders kitabı düzeyinde standarttır.

**Bağlantılı kavramlar:** [[concepts/rastgele-graflar.md|Rastgele Grafikler ve Sandviç Eşlemesi]]

## İlgili Makaleler
- [[raw/articles/2026-11-11_graph-theory-for-visual-learners.md|Graph Theory for Visual Learners (Tivadar Danka, The Palindrome, 2026)]]
