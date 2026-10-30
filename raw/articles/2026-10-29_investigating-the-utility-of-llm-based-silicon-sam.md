---
type: raw_article
title: Investigating the Utility of LLM-Based “Silicon Samples” in Political Science
  Conjoint Experiments
description: Alice Malmberg (Johns Hopkins University, SNF Agora Institute), Public
  Opinion Quarterly'de yayımlanan araştırma notunda, zorunlu seçimli (forced-choice)
  konjoint deneylerinde LLM ile üretilmiş yanıtl...
resource: https://academic.oup.com/poq/article-abstract/doi/10.1093/poq/nfag069/9004733
tags:
- akademik
- genel
- high
timestamp: '2026-10-30T20:09:53Z'
source_file: 2026-10-29_malmberg-silicon-samples-conjoint-poq.json
category: AKADEMİK ÖZEL; GENEL
priority: high
roles:
- method
- result
- limitation
published: '2026-10-29'
---

# Investigating the Utility of LLM-Based “Silicon Samples” in Political Science Conjoint Experiments

**Author(s):** Alice Malmberg

**Published:** 2026-10-29

**Source:** [https://academic.oup.com/poq/article-abstract/doi/10.1093/poq/nfag069/9004733](https://academic.oup.com/poq/article-abstract/doi/10.1093/poq/nfag069/9004733)

## Summary

Alice Malmberg (Johns Hopkins University, SNF Agora Institute), Public Opinion Quarterly'de yayımlanan araştırma notunda, zorunlu seçimli (forced-choice) konjoint deneylerinde LLM ile üretilmiş yanıtlayıcıların — yazının deyimiyle 'silicon samples' — insan yanıtlayıcıların yerini alıp alamayacağını ilk kez sistematik olarak test ediyor. Tasarım doğrudan bir kıyaslamaya dayanıyor: üç model (GPT-4o-Mini, Llama 3.2 ve Magistral-small-2506) için, canlı bir konjoint örneklemindeki her yanıtlayıcının demografik profili (partizanlık, ideoloji, ırk, cinsiyet, yaş kategorisi, eyalet) birebir aynı şekilde modellere verilerek sentetik karşılıkları üretiliyor; ardından her iki grup aynı profil setlerini ve aynı öznitelik düzeylerini görüyor. Konjoint, ABD eyaletleri arasında taşınma tercihini modelleyen altı öznitelik içeriyor: kürtaj politikası, LGBTQ hakları, silah politikası, geçim maliyeti, suç oranı ve devlet okulu kalitesi. Her model için 15 tekrar × 2.000 görev = 30.000 görev üretiliyor; sıcaklık (temperature) hem modeller arası ortak değerlerde (0, 0,5, 1) hem de her modele özgü değerlerde test ediliyor. Bulgu net ve olumsuz: naif biçimde üretilen silicon samples, konjoint görevlerinde insan kararlarını simüle etmeye yetmiyor. Bireysel düzeyde insan-sentetik seçim uyumu (F1) GPT-4o-Mini'de 0,62-0,70, Magistral-small-2506'da 0,63-0,71 bandında kalırken Llama 3.2'de 0,41-0,48'e düşüyor; yani en iyi durumda bile üç görevde bir yanlış seçim var — bu, konjoint sonuçlarının ölçüm geçerliliği açısından doğrudan bir sorun. Daha önemlisi, demografik ortak değişkenlerin seçimleri biçimlendirme tarzı insanlarla modeller arasında sistematik olarak farklılaşıyor: aynı demografik profil, insan yanıtlayıcıda bir yönde hareket ederken modelde başka bir yönde (hatta ters yönde) etki üretiyor. Yazının iki katkısı buradan çıkıyor: konjoint bağlamında LLM yanıtlayıcı performansına dair betimsel bir referans tabanı oluşturmak ve naif silicon samples'ın demografik özellikler üzerinden insan seçimlerini çıkaramayacağını göstermek. Sonuç, 'LLM'lerle anket simülasyonu' literatürünün en hızlı büyüyen iddiasına doğrudan bir sınır çekiyor: sentetik yanıtlayıcı, profil düzeyinde ortalamaları yaklaşık tutturabilse bile birey düzeyinde ve ortak değişken etkilerinde insanı temsil etmiyor.

## Key Points

- Künye: Public Opinion Quarterly (OUP), research note, 29 Ekim 2026, DOI 10.1093/poq/nfag069; tek yazar Alice Malmberg, Johns Hopkins University SNF Agora Institute postdoktoral araştırmacısı. Makale kapalı erişim.
- Tasarım: zorunlu seçimli konjoint; her insan yanıtlayıcının demografik profili (PID, ideoloji, ırk, cinsiyet, yaş kategorisi, eyalet) birebir modele verilerek sentetik karşılığı üretiliyor, böylece insan ve silicon seçimler doğrudan eşleştirilebiliyor.
- Konjoint içeriği: ABD eyaletleri arasında taşınma tercihi; altı öznitelik — kürtaj politikası (4 düzey), LGBTQ hakları (4), silah politikası (3), geçim maliyeti (3), suç oranı (3), devlet okulu kalitesi (3). Her yanıtlayıcı iki görev, her görevde iki profil görüyor.
- Modeller ve ölçek: GPT-4o-Mini, Llama 3.2, Magistral-small-2506; her model için 15 tekrar × 2.000 görev = 30.000 görev. Temperature hem ortak (0, 0,5, 1) hem modele özgü değerlerde test edilmiş; reddetme (task refusal) oranları 30.000 görev üzerinden hesaplanmış.
- Bulgular: bireysel insan-sentetik seçim uyumu F1 = 0,62-0,70 (GPT-4o-Mini), 0,63-0,71 (Magistral-small-2506), 0,41-0,48 (Llama 3.2). Yani en iyi modelde bile yaklaşık her üç görevden biri insanla uyuşmuyor; Llama'da yarıdan fazlası uyuşmuyor.
- Kritik bulgu: demografik ortak değişkenlerin seçimler üzerindeki etkisi insanlarla modeller arasında sistematik olarak farklı; LLM'ler ortak değişkenleri insan yanıtlayıcılardan farklı işliyor. Bu, 'silicon sample demografik olarak eşleştirildiği için temsil edicidir' varsayımını çürütüyor.
- Analitik araç seti: AMCE'ler, marjinal ortalamalar, değişken önem skorları (variable importance), F1 skorları, yanlış pozitif/negatif oranları, işaret ve anlamlılık uyumu (Table 4) ve bootstrap güven aralıkları — çoğaltım dosyalarında tüm R kodları ve çıktı csv'leri açık.
- Açık bilim: çoğaltım paketi Harvard Dataverse'te CC0 lisansıyla (doi 10.7910/DVN/2LVYOO); ham silicon sample çıktıları, bootstrap dosyaları, F1 csv'leri, CHIP50 kod kitabı ve R betikleri dahil. Bu kayıttaki F1 değerleri ve tasarım ayrıntıları doğrudan bu paketten okundu.
- Dürüst sınırlılık: GPT-4o-Mini ve Magistral-small-2506 yazının yayımı sırasında emekliye ayrılmış (deprecated) modeller; yazar bu nedenle silicon sample üretim betiklerini vermiyor ve üretimin birebir tekrarlanamayacağını açıkça yazıyor — model sürümlerine bağlı sonuçların kırılganlığına dair sessiz bir uyarı.

## Turkey Context

Türkiye'de anket maliyetleri ve saha erişimi son yıllarda hızla kötüleşirken 'LLM ile sentetik yanıtlayıcı' fikri hem akademik hem ticari anket sektöründe cazip bir kısayol olarak dolaşıma girdi; Malmberg'in notu bu kısayolun en sık kullanıldığı yerden, konjoint deneylerinden, ampirik bir fren getiriyor. Türkiye açısından ilk sonuç doğrudan: aynı demografik etiketler (genç, Kürt, muhafazakâr, İstanbullu, üniversite mezunu) verildiğinde LLM'lerin bu etiketleri insanlarla aynı yönde işlememesi, Türkiye'de 'sentetik seçmen' veya 'sentetik parti seçmeni' üreten çalışmaların geçerliliğini ciddi biçimde zayıflatıyor. Bu, özellikle ulaşılması zor gruplarda (Alevi, Kürtçe konuşan, Roman, mülteci nüfuslar) sentetik örneklem kullanma hevesine karşı somut bir uyarı: modelin o gruba dair eğitim verisi hem az hem de stereotip ağırlıklıysa, ortak değişken etkisi ters işaretli çıkabilir. İkinci sonuç, yöntem tercihiyle ilgili: not, silicon sample'ın 'profil düzeyinde ortalama doğru çıktı' ile 'birey düzeyinde temsil' arasındaki farkı F1 skoruyla ölçüyor. Bu ayrım Türkiye'deki araştırma yöntemleri müfredatı için de ders niteliğinde: konjoint kullanan araştırmacılar (seçmen tercihi, aday profili, hizmet sunumu, mülteci algısı) için bu ayrım hayati: AMCE'ler sentetik veride kabaca tutturulsa bile alt grup farkları ve etkileşimler yanlış çıkar, ki Türkiye araştırmalarında asıl ilgi genellikle tam bu alt grup farklarında. Üçüncü nokta, açık bilim pratiği: yazar tüm kodu, ham çıktıları ve F1 hesaplarını CC0 ile Dataverse'e koymuş, hatta modeller emekliye ayrıldığı için üretimin tekrarlanamayacağını açıkça yazmış. Türkiye'de sentetik veriyle çalışan ekipler için bu, 'hangi model, hangi sürüm, hangi sıcaklık, hangi prompt, hangi tarih' kaydının zorunlu olduğunu gösteriyor; aksi halde bulgular bir yıl içinde doğrulanamaz hale gelir. Dördüncüsü, kurumsal bağlam: CHIP50 gibi 50 eyaleti kapsayan, eyalet düzeyinde kota uygulanmış, kamuya açık bir panel Türkiye'de yok; TÜİK mikro verisi araştırmacıya bu esneklikte açılmadığı için Türkiye'de benzer bir benchmark çalışması yapmak isteyen ekip önce kendi panelini kurmak zorunda — bu da silicon sample doğrulamasını Türkiye'de hem gerekli hem pahalı kılıyor. Son olarak politika tarafı: anket şirketlerinin müşterilere 'yapay zekâ ile 10 kat ucuza anket' sunduğu bir piyasada, POQ gibi bir dergide yayımlanan bu tür bir not, kamu ihalesi ve medya anketi sözleşmelerinde metodoloji denetimi için dayanak olarak kullanılabilir.

## 🏷 Retorik Roller

- 🧩 **Yöntem**
- 📊 **Bulgular**
- ⚠️ **Sınırlılıklar**

---

## 🔗 İlgili Bağlantılar
### 🧠 İlgili Kavramlar
- [[concepts/sentetik-populasyonlar.md|Sentetik Popülasyonlar ve Birey-Tabanlı Simülasyon]]
- [[concepts/siyaset-bilimi-metodolojisi.md|Siyaset Bilimi Metodolojisi]]
- [[concepts/olcum-araclari.md|Ölçüm Araçları]]
### 🏛 İlgili Kurum/Kişiler
- [[entities/academic-oup-com.md|Academic Oup Com]]
