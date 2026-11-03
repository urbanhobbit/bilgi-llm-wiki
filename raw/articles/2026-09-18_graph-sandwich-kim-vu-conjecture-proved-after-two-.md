---
type: raw_article
title: 'Graph Sandwich: Kim-Vu Conjecture Proved After Two Decades'
description: Quanta Magazine'ın 18 Eylül 2026 tarihli haberine göre Natalie Behague,
  Daniel Il'kovič ve Richard Montgomery, 2004'te Jeong Han Kim (o dönem Microsoft
  Research) ile Van Ha Vu'nun (UCSD) ortaya attığı...
resource: https://arxiv.org/abs/2510.20765
tags:
- akademik
- genel
- medium
timestamp: '2026-11-03T07:38:22Z'
source_file: 2026-09-18_graph-sandwich-kim-vu-conjecture-proof.json
category: AKADEMİK ÖZEL; GENEL
priority: medium
roles:
- result
- method
published: '2026-09-18'
---

# Graph Sandwich: Kim-Vu Conjecture Proved After Two Decades

**Author(s):** Natalie Behague; Daniel Il'kovič; Richard Montgomery (kanıt); Paulina Rowińska (Quanta Magazine haberi)

**Published:** 2026-09-18

**Source:** [https://arxiv.org/abs/2510.20765](https://arxiv.org/abs/2510.20765)

## Summary

Quanta Magazine'ın 18 Eylül 2026 tarihli haberine göre Natalie Behague, Daniel Il'kovič ve Richard Montgomery, 2004'te Jeong Han Kim (o dönem Microsoft Research) ile Van Ha Vu'nun (UCSD) ortaya attığı **sandviç varsayımını** (sandwich conjecture) tam olarak kanıtladı. Sorun, rastgele grafikler kuramının en pratik sorusudur: düzenli (regular) rastgele grafikler — her düğümün derecesi aynı olan grafikler — gerçek ağları (sosyal gruplar, internet, beyindeki nöron bağlantıları) daha iyi temsil eder, ama kenarlar birbirine bağımlı olduğu için analiz edilmeleri çok daha zordur. Binom rastgele grafikler (her düğüm çifti için yazı-tura atılan G(n,p) modeli) ise kolay analiz edilir. Kim ve Vu, d = ω(log n) iken rastgele d-düzenli grafik G_d(n)'nin, kenar olasılıkları d/n'ye asimptotik olarak eşit iki binom grafiğin arasına sandviç edilebileceğini öne sürdü: p_* = (1-o(1))d/n ve p^* = (1+o(1))d/n olacak biçimde bir eşleme (coupling) vardır öyle ki P(G_* ⊂ G ⊂ G^*) = 1-o(1). Böyle bir sandviç, kolay modelde kanıtlanan her özelliğin zor modele bedava geçmesi anlamına gelir. Varsayımın alt dilimi (düzenli grafiğin bir binom grafiği içermesi) yıllar içinde kanıtlanmış, üst dilimi yalnızca belirli aralıklarda gösterilmişti; Gao, Isaev ve McKay 2020'de d ≫ log⁴n koşuluyla kısmi ispatı vermişti. Üçlü, Gao ve arkadaşlarının 2019'daki kenar-kenar inşa prosedürünü inceleyerek varsayımı tüm d için kanıtladı; böylece düzenli rastgele grafikler hakkındaki onlarca sonuç, binom grafikler hakkındaki mevcut literatürden tek bir akıcı ispata indirgenebilir hâle geldi. Gil Kalai sonucu 'meta-teorem' olarak adlandırıyor.

## Key Points

- Künye: kanıt metni arXiv:2510.20765 [math.CO], 'A proof of the Kim-Vu sandwich conjecture', Natalie Behague, Daniel Il'kovič, Richard Montgomery (Warwick Üniversitesi ve o dönemki öğrenci/postdoc bağlantıları). İlk sürüm 23 Ekim 2025, v2 8 Aralık 2025. 3 Kasım 2026 itibarıyla hakemli dergide yayımlanmamış; Crossref'te dergi DOI'si, arXiv API'de journal_ref yok — DOI yalnızca arXiv DOI'si (10.48550/arXiv.2510.20765). Popülerleştirme: Quanta Magazine, yazar Paulina Rowińska, 18 Eylül 2026. Düğümü sohbete düşen yüzey: @KirkDBorne tweet'i, 2 Kasım 2026, 'Graph Theory in the news!'.
- Varsayımın kurulumu: d = ω(log n) iken öyle p_* = (1-o(1))d/n, p^* = (1+o(1))d/n ve öyle bir eşleme (G_*, G, G^*) vardır ki G_* ~ G(n,p_*), G ~ G_d(n), G^* ~ G(n,p^*) ve P(G_* ⊂ G ⊂ G^*) = 1-o(1). Yani zor model (düzenli) iki kolay model (binom) arasına sıkıştırılır.
- Tarihsel zincir: 1959-60'ta Edgar Gilbert (Bell Labs, telefon ağları) ve bağımsız olarak Erdős–Rényi binom modeli; 1970'lerde binom grafiklerde Hamiltonian çevrim koşulları; aynı sorunun düzenli grafikler için çözümü 20 yıl daha aldı. 2004'te Kim–Vu varsayımı; 2019'da Gao–Isaev–McKay inşa prosedürü; 2020'de aynı üçlü d ≫ log⁴n için kısmi ispat; 2025'te tam ispat.
- İspat yöntemi (mimari düzeyinde): iki grafik aynı anda, kenar kenar inşa edilir. İlk ağırlıklı yazı-tura binom grafiğe kenar ekler; yazı gelirse aynı kenar düzenli grafiğe de eklenir. Tura gelirse binom grafik atlanır, ama düzenli grafiğin her düğümde aynı dereceyi tutturması gerektiği için ikinci bir ağırlıklı yazı-tura atılır; bu ikinci madeni paranın ağırlığı inşa ilerledikçe uyarlanarak tahmin edilir. Böylece alt dilim (düzenli ⊃ binom) garanti edilir. Üst dilim için süreç tersine çevrilir: iki tam grafikten başlanıp kenarlar tek tek çıkarılır, içerme ilişkisi korunarak düzenli ve binom grafiklere inilir.
- Sonuç: düzenli rastgele grafiklerin özellikleri artık sıfırdan kanıtlanmak zorunda değil; binom grafikler literatürü otomatik olarak devreye giriyor. Quanta'ya göre onlarca sonuç tek bir akıcı ispatta yeniden yazılabiliyor ve yeni sonuçlar şimdiden görünmeye başladı. Sıradaki hedef, alternatif katmanlardan (binom/düzenli/binom…) oluşan çok katmanlı sandviçler ve başka bileşenler.
- Tepkiler: Pu Gao (Waterloo) 'nosyon o kadar güzel ki'; Michael Krivelevich (Tel Aviv) 'kanıtlanmamış olması sinir bozucuydu… bir tür rahatlama'; Natalie Behague 'neredeyse gerçek olamayacak kadar iyi'. Gil Kalai (Hebrew University) sonucu 'araç kutusunu zenginleştiren' ve 'teknik dişleri keskinleştiren' bir meta-teorem olarak tanımlıyor.
- Sınırlılık: hakem değerlendirmesinden geçmemiş bir ön baskı söz konusu; Quanta metni ispatın hata terimlerini, d aralığının sınırlarını ve teknik lemmaları vermiyor — anlatı mimari düzeyinde. Ayrıca haber, ön baskıdan yaklaşık 11 ay sonra (Eylül 2026) yayımlandı; tweet ise haberden ~6 hafta sonra. Yani 'yeni sonuç' çerçevesi ile gerçek zaman çizelgesi arasında belirgin bir gecikme var.

## Turkey Context

Bu kaydın Türkiye gündemiyle doğrudan ilgisi yok; değeri yöntemsel ve bilim-iletişimi düzeyinde. Birincisi, ağ analizi altyapısı: Türkiye'de sosyal ağ araştırmaları (X/Twitter kutuplaşma çalışmaları, bot ve koordineli hesap ağları, dezenformasyon yayılımı) neredeyse istisnasız 'null model' olarak konfigürasyon modelini ya da derece-koruyan yeniden kablolamayı kullanıyor, ama bu modelin hangi koşullarda hedef ağın özelliklerini gerçekten taşıdığını tartışmıyor. Sandviç teoremi tam bu boşluğa oturuyor: derecesi sabit bir rastgele grafiğin, iki binom grafik arasında sıkıştırılabildiği kanıtlandığında, kolay modelde kanıtlanmış bir özellik (bağlantılılık, çap, dev bileşen, spektral boşluk) zor modele bedava geçiyor. Yani 'hesaplaması kolay modelden zoruna özellik transferi' artık bir varsayım değil, ispatlanmış bir meta-teorem. Türkiye'de ağ verisiyle çalışan ekiplerin araştırma yöntemleri bölümünde bu transferi açıkça yazması, sonuçların sağlamlığını artırır. İkincisi, bilim iletişimi: Türkçede matematik haberciliği neredeyse yok; Quanta'nın 18 Eylül 2026 tarihli metni, ispatı sosyal ağ benzetmesiyle anlatıyor ve popülerleştirmenin nasıl yapılması gerektiğine dair iyi bir örnek — teknik iddia (eşleme, olasılık 1-o(1)) korunuyor, abartı yok, ispatın sınırları (hakem değerlendirmesi, ön baskı) da okuyucuya bırakılıyor. Türkiye'de akademik bültenlerin 'yeni kanıtlandı' başlıklarını ön baskı gerçeğiyle birlikte vermesi, güven açığını azaltır. Üçüncüsü, 11 aylık gecikme: kanıt Ekim 2025'te arXiv'e düşmüş, popüler haber Eylül 2026'da çıkmış, Kirk Borne tweet'i Kasım 2026'da 'haber oldu' demiş. Türkiye'de de bilim haberi dolaşımı aynı gecikmeyle çalışıyor; izleme sistemleri 'yeni' etiketini arXiv tarihine göre vermeli, habere göre değil. Dördüncüsü, eğitim tarafı: çizge kuramı Türkiye'de lisans matematiğinde ayrık matematik dersinin bir bölümü olarak kalıyor; oysa bu sonuç, aynı teoremin (derece-koruyan rastgeleleştirme) doğrudan sosyal bilim uygulaması olduğunu gösteriyor — sosyoloji ve siyaset bilimi öğrencilerine 'ağ null modeli' anlatmak için elde somut bir köprü var. Beşincisi, uyarı: sonuç saf matematik; Türkiye'deki kutuplaşma literatürüne doğrudan uygulanabilmesi için ayrı bir köprü çalışması gerekir (ölçüm hatası, eksik gözlem, örneklem yanlılığı gibi ampirik sorunlar teoremde yok). Bu kaydı 'yöntem transferi fırsatı' olarak okumak doğru, 'Türkiye kutuplaşması kanıtlandı' biçiminde okumak yanlış olur.

## 🏷 Retorik Roller

- 📊 **Bulgular**
- 🧩 **Yöntem**

---

## 🔗 İlgili Bağlantılar
### 🧠 İlgili Kavramlar
- [[concepts/rastgele-graflar.md|Rastgele Grafikler ve Sandviç Eşlemesi]] — kanıtın doğrudan konusu: düzenli/binom rastgele grafikler ve özellik transferi sağlayan eşleme.
- [[concepts/siyaset-bilimi-metodolojisi.md|Siyaset Bilimi Metodolojisi]] — ampirik ağ çalışmalarında kullanılan derece-koruyan null modellerin teorik dayanağı; araştırma yöntemleri açısından transfer edilebilir bir sonuç.
- [[concepts/sosyal-kutuplasma.md|Sosyal Kutuplaşma]] — X/Twitter kutuplaşma ölçümünde null model seçimi doğrudan bu teoremin kapsamına girer.
### 🏛 İlgili Kurum/Kişiler
- [[entities/arxiv-org.md|Arxiv Org]]
- [[entities/quanta-magazine.md|Quanta Magazine]] — haberi yayımlayan dergi (Paulina Rowińska, 18 Eylül 2026); ispat metnine bağlantı vermeden duyurdu.
