---
type: raw_article
title: Graph Theory for Visual Learners
description: 'Tivadar Danka''nın (The Palindrome) görsel öğretim odaklı grafik teori
  (çizge kuramı) rehberi: 14 bölümde temel tanımdan Ramsey sayılarına ve ağ merkeziliğine
  kadar inen bir tur. Metodolojik çerçeve **...'
resource: https://thepalindrome.org/p/graph-theory-for-visual-learners-320
tags:
- kurator
- medium
timestamp: '2026-11-11T17:42:23Z'
source_file: 2026-11-11_graph-theory-for-visual-learners.json
category: KURATOR
priority: medium
published: '2026-11-11'
---

# Graph Theory for Visual Learners

**Author(s):** Tivadar Danka (The Palindrome)

**Published:** 2026-11-11

**Source:** [https://thepalindrome.org/p/graph-theory-for-visual-learners-320](https://thepalindrome.org/p/graph-theory-for-visual-learners-320)

## Summary

Tivadar Danka'nın (The Palindrome) görsel öğretim odaklı grafik teori (çizge kuramı) rehberi: 14 bölümde temel tanımdan Ramsey sayılarına ve ağ merkeziliğine kadar inen bir tur. Metodolojik çerçeve **görselleştirme + somut uygulama** üzerine kurulu: her kavram önce kendi memleketinin trafik ağında (iki köprüyle bölünmüş bir şehir) gösteriliyor, sonra biçimsel tanım veriliyor.

**Kapsam:** (1) çizge = düğüm + kenar; çizim ile çizgenin kendisi ayrımı, izomorfizm, derece; (2) yürüyüş (walk) / yol (path) — Königsberg köprüleri ve Euler, çizge kuramının doğuşu; (3) bağlantılılık (ulaşılabilirlik bir denklik bağıntısıdır), k-bağlantılılık; (4) arama: BFS (katman katman, en kısa kenar sayılı yol garantisi) ve DFS (derine in, geri sar); (5) döngüler (cycle) ve dayanıklılık — bir döngüdeki herhangi bir kenarı silmek bağlantılılığı bozmaz; (6) ağaçlar: bağlantılı + döngüsüz = minimum bağlantılı (her kenar kritik) = maksimum döngüsüz = her düğüm çifti arasında **tek** yol; kök seçimi ve hiyerarşik sıralama; labirent + karar ağacı uygulamaları; (7) Hamilton yolları/döngüleri (her düğümü bir kez) ve genom dizilemede (shotgun sequencing) kullanımı; (8) düzlemsel (planar) çizgeler: Euler formülü v − e + f = 2, bundan türeyen e ≤ 3v − 6, K₅ ve K₃,₃'ün düzlemsizliği, Kuratowski teoremi (düzlemsizlik ancak ve ancak K₅ ya da K₃,₃'ün bir altbölümü altçizge olarak varsa); (9) düğüm renklendirme: kromatik sayı χ, Mycielskian inşası (üçgensiz ama keyfi yüksek χ), dört renk teoremi; (10) kenar renklendirme: kromatik indeks, Vizing teoremi (Δ ≤ χ′ ≤ Δ+1); (11) Ramsey teorisi: K₆'nın her iki renkli kenar boyamasında tek renkli üçgen vardır, R(3)=6; bilinen tam değerler yalnızca R(1)=1, R(2)=2, R(3)=6, R(4)=18; R(5) 43-46, R(6) 102-160, R(7) 205-492 aralığında; (12) yönlü ve ağırlıklı çizgeler: hesaplama çizgeleri (sinir ağları, LLM'ler milyarlarca düğümlü hesaplama çizgeleridir), Markov zincirleri, geçiş/komşuluk matrisi; (13) çizge ölçütleri: dengede dağılım = PageRank, arasındalık merkeziliği (betweenness centrality) ve darboğaz tespiti.

**Kullanıcıya değeri:** Kuramsal yenilik iddiası yok — bu bir **didaktik sentez**. Akademik atıf için değil, KURATOR hattında ağ/çizge temelli analizleri (kutuplaşma ağları, dezenformasyon yayılımı, merkezilik) açıklamak ve yöntem sözlüğü kurmak için kullanılmalı.

## Key Points

- **Künye:** Tivadar Danka, "Graph Theory for Visual Learners", The Palindrome (Substack), 11 Kasım 2026, ücretsiz; 14 bölüm, ~5.950 kelime; video versiyonu var.
- 🚩 **Sayı tutarsızlığı (küçük):** X gönderisi '4000 kelimelik uzun bir yazı' diyor; Substack API `wordcount` alanı **5.953** veriyor (ücretli abonelik çağrısı ve video olmayan kısımlar dahil). Gönderi kendi metnini küçümsüyor, abartmıyor — kanıt değeri taşımayan ama not edilmesi gereken bir fark.
- **Königsberg → çizge kuramının doğuşu:** Euler'in yedi köprü problemi, çizge kuramının tarihsel başlangıcı olarak sunuluyor; yazarın çerçevesi 'iki arama algoritması (BFS/DFS) çizge kuramının neredeyse tamamını çözer' biçiminde.
- **Ağaç karakterizasyonları (dört eşdeğer tanım):** bağlantılı + döngüsüz; minimum bağlantılı (herhangi bir kenar silinince iki bileşene ayrılır); maksimum döngüsüz (herhangi iki düğüm arasına kenar eklemek döngü yaratır); her düğüm çifti arasında tek yol. Bu dördüncüsü hiyerarşik sıralamanın (kök + düzey) önkoşulu.
- **Düzlemsellik kanıtı:** Euler formülü v − e + f = 2 → e ≤ 3v − 6; K₅ için 3·5−6 = 9 < 10 olduğundan düzlemsiz. Kuratowski: bir çizge düzlemsizdir ancak ve ancak K₅ veya K₃,₃'ün altbölümü (subdivision) altçizge olarak bulunuyorsa.
- **Renklendirme:** dört renk teoremi (düzlemsel ⇒ χ ≤ 4) harita boyama örneğiyle; Mycielskian inşası üçgensiz çizgelerin kromatik sayısının sınırsız artırılabildiğini gösteriyor — yani 'yüksek χ, büyük klik gerektirmez'. Kenarda Vizing: χ′ ya Δ ya Δ+1.
- **Ramsey sayıları (kesin bilinen):** R(1)=1, R(2)=2, R(3)=6, R(4)=18; sonrası yalnızca aralık — R(5) ∈ [43,46], R(6) ∈ [102,160], R(7) ∈ [205,492]. Sosyal ağ yorumu: 18 kişilik bir ağda birbirini tanıyan ya da hiç tanımayan 4 kişi mutlaka vardır.
- **Sosyal bilim açısından en kullanışlı iki bölüm:** (a) **PageRank** = yönlü ağırlıklı çizge üzerinde rastgele yürüyüşün denge dağılımı; (b) **arasındalık merkeziliği** — tüm s−t en kısa yolları içinde v'den geçenlerin oranının toplamı; trafik verisi olmadan darboğazları (köprüler) ortaya çıkarıyor.
- **Yönlü çizge = asimetrik ilişki:** 'arkadaş olma' simetrik (küme olarak kenar), 'takip etme' asimetrik (demet olarak kenar). Fonksiyonlar ve hesaplama çizgeleri de yönlü çizge; geri yayılım için gradyanlar **kenarlara** yazılır → ağırlıklı çizge.
- **Sınırlılık:** Hakem değerlendirmesinden geçmiş bir kaynak değil; kaynakça ve atıf aparatı yok, sayısal/ampirik veri yok. Öğretici içerik olarak güvenilir, **kanıt olarak kullanılamaz**.

## Turkey Context

**Neden KURATOR'a giriyor:** Türkiye'de kutuplaşma ve dezenformasyon araştırmalarının en zayıf halkası **ağ (network) katmanı** — çalışmaların çoğu anket/ölçek düzeyinde kalıyor, etkileşim ağları ya hiç kurulmuyor ya yalnızca betimsel olarak raporlanıyor. Bu yazı, o katmanı kurmak için gereken asgari sözlüğü (derece, bağlantılılık, BFS/DFS, döngü/ağaç, merkezilik, PageRank) tek yerde ve Türkçeye çevrilebilir biçimde veriyor.

(1) **Yöntem transferi:** X/Twitter Türkiye verisiyle çalışan araştırmalar için arasındalık merkeziliği, 'hangi hesaplar köprü işlevi görüyor' sorusunun en savunulabilir operasyonelleştirmesi; yazının iki köprü benzetmesi doğrudan Türkiye'deki 'köşe yazarı → fenomen → taban' aktarım zincirlerine uygulanabilir. (2) **Dil sorunu:** Türkçe metodoloji literatüründe çizge kuramı terimleri (yürüyüş/yol/iz, düzlemsel, kromatik indeks, altbölüm) tutarsız kullanılıyor; bu metin, KURATOR içi ortak sözlük için referans alınabilir. (3) **Dikkat:** Yazı Türkiye'ye dair tek bir ampirik iddia içermiyor; Türkiye notuna yalnızca **yöntem** aktarımı olarak girmeli, bulgu olarak değil.

---

## 🔗 İlgili Bağlantılar
### 🧠 İlgili Kavramlar
- [[concepts/dezenformasyon.md|Dezenformasyon]]
- [[concepts/sosyal-kutuplasma.md|Sosyal Kutuplaşma ve Dijital Platformlar]]
