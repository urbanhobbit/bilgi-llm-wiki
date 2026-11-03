---
type: raw_article
title: '2026 Ara Seçimlerinde Irksal Betimleyici Temsil Tahmini: Kuram Temelli Olasılıksal
  Ön-Analiz Planı'
description: Yuki Atsusaka (Houston Üniversitesi, Hobby School of Public Affairs)
  ve Kolbe A. Dumas (Houston Üniversitesi, Siyaset Bilimi), 3 Kasım 2026 ara seçimlerinde
  ABD Temsilciler Meclisi'nin **ırksal betiml...
resource: https://logical-model.github.io/predictions-2026/
tags:
- kurator
- akademik
- high
timestamp: '2026-11-03T03:55:20Z'
source_file: 2026-11-02_racial-descriptive-representation-2026-predictions.json
category: KURATOR; AKADEMİK ÖZEL
priority: high
roles:
- method
- gap
published: '2026-11-02'
---

# 2026 Ara Seçimlerinde Irksal Betimleyici Temsil Tahmini: Kuram Temelli Olasılıksal Ön-Analiz Planı

**Author(s):** Yuki Atsusaka, Kolbe A. Dumas

**Published:** 2026-11-02

**Source:** [https://logical-model.github.io/predictions-2026/](https://logical-model.github.io/predictions-2026/)

## Summary

Yuki Atsusaka (Houston Üniversitesi, Hobby School of Public Affairs) ve Kolbe A. Dumas (Houston Üniversitesi, Siyaset Bilimi), 3 Kasım 2026 ara seçimlerinde ABD Temsilciler Meclisi'nin **ırksal betimleyici temsilini** seçimden önce tahmin eden bir ön-analiz planı yayımlıyor. Yöntem, Atsusaka'nın (2021, *APSR*) 'mantıksal model'i üzerine kurulu: iki girdiyle çalışan **stratejik adaylık modeli**. Girdiler (1) bölgenin 2026 ırksal bileşimi (% CVAP) ve (2) 2024'te aynı gruptan adayların **ırksal zafer marjı**. Model, seçilebilir adayın kazanma şansını iki uç senaryonun (tam ırksal kutuplaşma ↔ geçen seçimin tekrarı) geometrik ortalaması olarak tahmin ediyor: Pr = Φ(√(M_adj × C) − 50). Tahmin: Temsilciler Meclisi'nde ortalama **7 Asyalı, 40 Siyahi, 39 Latin, 349 Beyaz** üye; yani 120. Kongre'de Beyazlar CVAP payına göre **14 puan fazla**, Siyahlar 5, Latinler 3, Asyalılar 3 puan eksik temsil edilecek. Modelin ayırt edici iddiası, bazı bölgelerde bir grubun nüfus çoğunluğu olmadığı hâlde yüksek olasılıkla kazanması — yani 'yüzde 50 eşiği' sezgisinin yanlış olduğu. Yazarlar, tahminlerini seçim sonrası kamuya açık biçimde değerlendireceklerini taahhüt ediyor (AUC-ROC, FPR/FNR, F1, Kappa, Brier, MAE/RMSE) ve makine öğrenmesi karşılaştırması ile 'packing' analizini ek analiz olarak planlıyor.

## Key Points

- Künye: Yuki Atsusaka (Hobby School of Public Affairs, University of Houston) ve Kolbe A. Dumas (Department of Political Science, University of Houston), 'Pre-Analysis Plan: Predicting Racial Descriptive Representation in the U.S. Congress: The Case of the 2026 Midterm Elections'. İlk sürüm 27 Ekim 2026, bu sürüm 2 Kasım 2026, 16 sayfa. OSF kaydı: osf.io/zuhac. Bölge düzeyi tahminler CSV olarak açık.
- Model: Atsusaka (2021, *American Political Science Review* 115(4): 1210-1225) 'mantıksal model' — Pr(Hedef grubun kazanması) = Φ(√(M_adj_{t-1} × C_t) − 50). C = hedef grubun 2026'daki seçmen payı (% CVAP); M_adj = 2024 ırksal zafer marjı + 50; Φ = standart normal dağılımın CDF'i. Karekök, iki uç senaryonun geometrik ortalaması fikrini taşıyor.
- Irksal zafer marjı (M) tanımı: hedef grubun en yüksek oy alan adayı ile karşılaştırma grubunun adayı arasındaki farkın yarısı + 50. Yorumu: 'kazananın ırkını değiştirmek için farklı oy vermesi gereken seçmenlerin asgari payı'. Bu terim, bölge demografisi dışındaki tüm yerel siyasi faktörleri (aday kalitesi, seçim rekabeti, partizan eğilim) tek bir sayıya indiriyor.
- Bu, siyaset biliminde 'mantıksal model' geleneğinin bir örneği: araştırma yöntemleri açısından veriye körlemesine dalmak yerine, önce kuram ve mantıkla kestirimde bulunmak. Kuramsal uyarı (yazarların kendi itirafı): model tek üyeli, çoğunluk usulü, ön seçimsiz sistemler için geliştirildi. ABD genel seçimlerine uygulanması, aday belirleme ve partizan yapı farkları nedeniyle hatalı tahmin üretebilir. Amaçlarından biri tam da bunu ölçmek: kuram ne kadar ileri gidebilir?
- Veri 1 — CVAP: 2020-2024 American Community Survey seçmen çağındaki vatandaş nüfus tahminleri, 2026'da yürürlükte olan bölge sınırlarına tabüle edildi. Dört grup karşılıklı dışlayan biçimde tanımlı: Siyahi, Asyalı (Pasifik Adalıları dahil) ve Beyazlar Hispanik değil.
- Ara dönem redistricting: Alabama, California, Florida, Louisiana, North Carolina, Ohio, Tennessee, Texas ve Utah'ta haritalar değişti. Model 'iki seçim arasında aynı bölge' varsaydığı için, 2024 ırksal marjı yeni bölgelere **nüfus oranıyla yeniden dağıtılarak** hesaplandı (eski bölgedeki adayın oyu, yeni bölgeye düşen 2020 nüfusu oranında paylaştırıldı).
- Veri 2 — aday ırkı: 2024'te 435 bölgede 1.128 aday. Oy toplamları ve sonuçlar Temsilciler Meclisi Kâtibi'nin resmî istatistiklerinden. Irk/etnisite kodlaması çok kaynaklı: Rutgers CAWP, FiveThirtyEight aday araştırması, Meclis Tarihçisi, NALEO, akademik replikasyon arşivleri, resmî biyografiler, aday açıklamaları, haberler → 674 aday için 915 atıflı kayıt (%59,8).
- Kodlama açığını kapatma: yayımlanmış tanımı olmayan adaylar için portre fotoğrafları önceden tanımlı bir 'agent arama protokolü' ile toplandı; Lee & Velez (2025) yöntemine dayanan DeepFace/PredEthnorace uygulaması 347 aday için altı kategori skoru üretti. Toplam kapsam 1.021 aday (%90,5); kodlanamayan 107 adayın neredeyse tamamı %5'in altında oy alan zayıf adaylar ve Beyaz olarak kodlandı.
- Bölge düzeyi tahminler: dört ırk grubu için her bölgede kazanma olasılığı hesaplandı; olasılık 0,9 üstü ve 0,1 altı bölgeler ayrı işaretlendi. Yazarların vurgusu: tahminler yüzde 50 nüfus eşiğine dayanan naif sınıflamadan çok daha incelikli — bazı bölgelerde grup çoğunluk değilken kazanıyor, azınlık-azınlık bölgelerinde ise Siyahi adayın kazanması bekleniyor.
- Eyalet düzeyi: grup-özel olasılıklar normalize edilip (p_g / Σp) kategorik dağılımdan 20.000 kez örneklem çekilerek sandalye sayısı simüle edildi. Sonuçlar: tek-iki sandalyeli küçük eyaletlerde (Hawaii hariç) tümü Beyaz; New York, Florida, Texas ve California'da azınlık temsili yoğun. Asyalı (5) ve Latin (17) temsili en çok California'da, Siyahi temsili en çok Georgia ve New York'ta (5'er sandalye).
- Ulusal tahmin: ortalama 7 Asyalı, 40 Siyahi, 39 Latin, 349 Beyaz üye — yani Meclis'in ~%80'i Beyaz, ~%20'si azınlık. Yazarlar ulusal düzeyin en zor tahmin olduğunu kabul ediyor: bir gruptaki sistematik hata diğerine taşabiliyor.
- Temsil açığı (Şekil 5): CVAP payları %66 Beyaz, %14 Siyahi, %12 Latin, %5 Asyalı. 2024'te gözlenen Meclis: %72 Beyaz, %11 Siyahi, %14 Latin, %4 Asyalı. 2026 tahmini: %80 Beyaz, %9 Siyahi, %9 Latin, %2 Asyalı → Beyaz fazla temsil +14 puan; Siyahi −5, Latin −3, Asyalı −3. ⚠️ Özette bu üç eksik temsil 'Asyalı, Siyahi, Latin sırasıyla 3, 3 ve 5' diye yazılmış; gövde metni ve Şekil 5 ise Siyahi −5, Latin −3, Asyalı −3 diyor. Kayıtta gövde/şekil esas alındı, tutarsızlık not edildi.
- Yorum sınırları (yazarların kendi notu): (1) yalnızca dört grup modellendi, melez ve diğer gruplar yok — bu yüzden fazla/eksik temsil toplamı sıfıra eşitlenmiyor; (2) referans olarak CVAP kullanıldığı için, Asyalı ve Latinlerin CVAP payı nüfus payından düşük olduğundan sonuçlar temsilin **alt sınırı** olarak okunmalı; (3) temsil açıklarının 2024'ten büyük çıkması modelin zayıflığından da kaynaklanabilir, ara dönem redistricting'ten de — yazarlar buna dair iddia kurmuyor.
- Değerlendirme taahhüdü: seçim sonrası resmî sonuçlar gelince bölge düzeyinde AUC-ROC, yanlış pozitif/negatif oranları, duyarlılık, özgüllük, F1, Kappa ve Brier skoru; eyalet düzeyinde MAE ve RMSE; ulusal düzeyde aynı mantık. Şu an 'hipotetik gerçek' olarak CVAP çoğunluğunun kazandığı varsayımıyla ön sonuçlar üretilmiş (ör. AUC 0,97-0,99 aralığı) — bunlar gerçek sonuç değil, yöntemin kendi kendini testi.
- Ek analizler: (a) redistricting olan/olmayan eyaletlerde performans ayrımı; (b) aynı çıktıları tahmin eden makine öğrenmesi modelleriyle karşılaştırma (veriden öğrenmeyen kuramsal model vs. tamamen veri-güdümlü yaklaşım); (c) her bölgenin belirli bir gruba göre ne kadar 'paketlendiği' (packing) ölçüsü. Takvim: Kasım 2026 veri toplama, Aralık 2026 değerlendirme, Ocak 2027 ML karşılaştırması, Şubat 2027 tamamlanma.
- Şeffaflık notları: hesaplama R paketi `logical` ile (github.com/YukiAtsusaka/logical); veri kodlamasında GPT-5.6 Terra (medium) yardımcı olarak kullanılmış; fotoğraf toplama protokolü, kaynak sayfalar ve dosya hash'leri arşivlenmiş; model sınıflandırmaları yayımlanmış kaynak tanımlarından ayrı tutulmuş.

## Turkey Context

Türkiye için iki düzeyde ders var. Birincisi yöntemsel: Atsusaka-Dumas, seçim öncesi tahmin yaparken üç şeyi birden yapıyor — kuramı açıkça yazıyor (tek denklem), veriyi ve kodlama protokolünü yayımlıyor, ve tahminlerini seçim sonrası **kamuya açık metriklerle** değerlendirme taahhüdü veriyor (ön-kayıt disiplini). Türkiye'de seçim tahmini neredeyse tamamen anket şirketlerinin itibarına dayanıyor; hangi modelin, hangi varsayımla, hangi hata payıyla konuştuğu şeffaf değil. Bu ön-analiz planı, Türkiye'de 'seçim tahmini' pratiğinin akademik standardı olarak okunabilir: ön-kayıt + açık kod + seçim sonrası puanlama. İkincisi siyasi: betimleyici temsil açığı Türkiye'de de ölçülebilir bir olgu — Meclis'te Kürt, Alevi, Roman, Hristiyan azınlıkların ve kadınların oranı ile nüfus payları arasındaki fark sistematik olarak çalışılmıyor; Atsusaka'nın mantıksal modeli, iki girdiyle (bölgenin sosyolojik bileşimi + önceki seçimde o gruptan adayın marjı) Türkiye'de il/ilçe düzeyinde uygulanabilir. Bu, 'kota mı, serbest rekabet mi' tartışmasına ampirik bir zemin kazandırır. Üçüncüsü, redistricting paralelliği: Türkiye'de seçim çevresi değişiklikleri (il sayısının artması, ilçelerin birleştirilmesi, milletvekili dağılımı) aynı işlevi görüyor — ve aynı yöntemsel sorunu doğuruyor: bölge sınırı değişince önceki seçimin marjı doğrudan taşınamaz. Yazarların çözümü (oyları yeni bölgelere nüfus oranıyla dağıtmak) Türkiye için de uygulanabilir bir teknik. Dördüncüsü, uyarı: yazarlar tahminlerini seçimden önce yayımlayarak 'sonradan akıllılık' (post-hoc rationalization) ihtimalini kapatıyor; Türkiye'de seçim analizi literatürünün en zayıf halkası tam olarak bu. Beşincisi, yapay zekâ kullanımı: yazarlar aday ırkı kodlamasında GPT-5.6 Terra'yı yardımcı olarak kullanıyor ama bunu dipnotta açıkça bildiriyor ve model sınıflandırmasını yayımlanmış kaynaklardan ayrı tutuyor — Türkiye'de benzer bir çalışma yapılacaksa, LLM çıktısının tek başına 'veri' sayılmaması ve ayrı bir kodlama katmanı olarak raporlanması gerekiyor. Altıncısı, siyasi ders: 'yüzde 50 eşiği' sezgisinin çürütülmesi, azınlık temsili tartışmalarında en sık başvurulan argümanı (çoğunluk olmadan temsil olmaz) zayıflatıyor; Türkiye'de il/ilçe düzeyinde benzer bir analiz, hangi bölgelerde Kürt seçmenin aday çıkarabildiğini sayısal olarak gösterebilir.

## 🏷 Retorik Roller

- 🧩 **Yöntem**
- 🔍 **Araştırma Boşluğu**

---

## 🔗 İlgili Bağlantılar
### 🧠 İlgili Kavramlar
- [[concepts/betimleyici-temsil.md|Betimleyici Temsil ve Mantıksal Modeller]] — Kaydın teorik çekirdeği: temsil açığı ve olasılıksal tahmin.
- [[concepts/abd-secim-sistemi.md|ABD Seçim Sistemi]] — Bölge yapısı, ara seçim döngüsü ve Oy Hakkı Yasası rejimi.
- [[concepts/partizan-redistricting.md|Partizan Redistricting]] — 2026 haritaları ve marjların yeni bölgelere yeniden dağıtılması.
- [[concepts/siyaset-bilimi-metodolojisi.md|Siyaset Bilimi Metodolojisi]] — Ön-kayıt, açık kod ve seçim sonrası puanlama disiplini.
### 🏛 İlgili Kurum/Kişiler
- [[entities/yuki-atsusaka.md|Yuki Atsusaka]] — Ortak yazar, modelin geliştiricisi.
- [[entities/kolbe-dumas.md|Kolbe A. Dumas]] — Ortak yazar.
- [[entities/university-of-houston.md|University of Houston]] — Yazarların kurumu.
- [[entities/american-political-science-review.md|American Political Science Review (APSR)]] — Modelin kaynak makalesinin dergisi.
- [[entities/open-science-framework.md|Open Science Framework (OSF)]] — Ön-analiz planının kaydı.
