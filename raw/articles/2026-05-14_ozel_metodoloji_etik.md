# AKADEMİK ÖZEL TARAMA
## Metodoloji, Etik ve Güncel Tartışmalar
**Tarih:** 14 Mayıs 2026 | **Kapsam:** Ocak 2025 – Mayıs 2026
**Kaynak:** arXiv (cs.SI, cs.CY, cs.CL, cs.AI)

---

## YÖNETİCİ ÖZETİ (200-300 kelime)

Bu haftaki akademik özel tarama, sosyal bilimlerde yapay zekâ metodolojisi, etik/teori ve güncel tartışmalar olmak üzere üç kategoride toplam 9 makaleyi kapsamaktadır.

**Metodoloji alanında** üç önemli çalışma öne çıkıyor: Birincisi, *Proxy Presumption* makalesi, embedding tabanlı sosyal ölçümlerin geçerlilik sorununu ele alarak araştırmacılara Yapı Geçerliliği Protokolü (CVP) sunuyor. İkincisi, LLM'lerin sosyal bilim etiketlemesinde kullanımında prompt varyasyonunun yarattığı ölçüm belirsizliğini Inter-Prompt Reliability (IPR) çerçevesiyle analiz ediyor. Üçüncüsü ise LLM'lerin insan davranışını incelemek için bilimsel bir araç olarak kullanımını "Üçüncü Hırs" kavramıyla kuramsallaştırıyor.

**Etik/Teori alanında**, algoritmik hesap verebilirliğin yalnızca açıklama değil, aynı zamanda usuli haklar gerektirdiğini savunan *Beyond Explanation* makalesi öne çıkıyor. AI ajanlarının hukuki kimliği ve sorumluluğu üzerine *How to Count AIs* önemli bir çerçeve sunarken, *Bridging the Gap in the Responsible AI Divides* AI Güvenliği ve AI Etiği arasındaki gerilimi aşmak için "critical bridging" yaklaşımını öneriyor.

**Güncel Tartışmalar alanında**, AI destekli akran değerlendirmesinin "jagged AI" (düzensiz AI) profili sergilediği, platform moderasyonunun seçim dönemlerinde yetersiz kaldığı ve dijital emek platformlarında ücret baskılamanın matematiksel modellerle açıklandığı makaleler dikkat çekiyor. Her üç kategorideki bulgular, Türkiye'deki akademik ve düzenleyici tartışmalar için doğrudan çıkarımlar taşımaktadır.

---

## 1) METODOLOJİ

### Makale 1: The Proxy Presumption: From Semantic Embeddings to Valid Social Measures
- **Yazarlar:** Baishi Li, Ta Yu, Kelvin J. L. Koa, Ke-Wei Huang
- **Tarih:** 8 Mayıs 2026
- **URL:** https://arxiv.org/abs/2605.07409
- **Kategori:** cs.CL, cs.LG, stat.AP

**ÖZET (250-300 kelime)**

Doğal Dil İşleme (NLP), hesaplamalı sosyal bilim için birincil bir araç haline gelmekte, araştırmacılar giderek artan oranda embedding'leri yenilik, yaratıcılık ve önyargı gibi gizli yapıları ölçmek için kullanmaktadır. Ancak bu geçiş temel bir geçerlilik sorunuyla karşı karşıyadır: "Proxy Presumption" (Vekil Varsayımı), yani geometrik özelliklerin (ör. kosinüs mesafesi) doğrudan sosyal kavramların ölçümü olarak kullanılması. Yazarlar, açık doğrulama olmadan denetimsiz temsillerin, hedef yapı ile konu, stil ve yazarlık gibi karıştırıcı niteliklerin iç içe geçmiş karışımları olarak kaldığını savunmaktadır. Semantik embedding'ler ile geçerli sosyal ölçümler arasındaki boşluğu kapatmak için Çalışma, Yapı Geçerliliği Protokolü'nü (Construct Validity Protocol - CVP) tanıtmaktadır. Nedensel temsil öğrenimi ve psikometriden yararlanan CVP, kavramsallaştırmadan nicel doğrulamaya kadar titiz bir süreç sunmaktadır. Ayrıca, embedding uzayında karıştırıcı etkenleri azaltmak için LLM'leri kullanan Karşıolgusal Nötralizasyon (Counterfactual Neutralization) adlı yeni bir yöntem önerilmektedir. Standart bir Geçerlilik Paketi (Validity Suite) sağlayarak — ayırt edici, artımlı ve tahmine dayalı geçerlilik testlerini içeren — bu çalışma, araştırma topluluğuna sezgisel vekilleri sağlam, bilimsel olarak savunulabilir araçlara dönüştürmek için bir araç seti sunmaktadır.

**TÜRKİYE BAĞLAMI (200+ kelime)**

Türkiye'de hesaplamalı sosyal bilim alanında yapılan çalışmalar hızla artmakla birlikte, metodolojik titizlik konusunda önemli boşluklar bulunmaktadır. Özellikle Türkçe doğal dil işleme çalışmalarında, embedding tabanlı ölçümlerin geçerliliği nadiren sistematik olarak sorgulanmaktadır. Bu makalenin önerdiği Yapı Geçerliliği Protokolü (CVP), Türkiye'deki araştırmacılar için özellikle değerlidir çünkü:

1. **Türkçe kaynakların sınırlılığı:** Türkçe için eğitilmiş embedding modelleri, İngilizce modellere kıyasla daha küçük ve daha az temsili külliyatlarla çalıştığından, Proxy Presumption sorunu daha da akuttur. CVP, bu modellerin sosyal bilim araştırmalarında kullanılmadan önce sistematik olarak doğrulanmasını sağlayabilir.

2. **Türkiye'de sosyal medya araştırmaları:** Türkiye'de siyasi kutuplaşma, dezenformasyon ve kamuoyu yoklamaları üzerine yapılan çalışmalarda embedding tabanlı ölçümler yaygınlaşmaktadır. Ancak bu ölçümlerin ne ölçüde geçerli olduğu sorusu genellikle ihmal edilmektedir.

3. **Akademik yayın baskısı:** Türkiye'de uluslararası yayın baskısı, araştırmacıları hızlı sonuç veren ancak metodolojik olarak zayıf yöntemlere yöneltebilmektedir. CVP ve Geçerlilik Paketi, bu tür aceleci yaklaşımları dengeleyecek bir kontrol mekanizması işlevi görebilir.

4. **Disiplinlerarası kapasite:** Türkiye'de bilgisayar bilimleri ve sosyal bilimler arasındaki işbirliği henüz emekleme aşamasındadır. Bu makale, iki alan arasında ortak bir metodolojik dil oluşturulmasına katkı sağlayabilir.

**Metodolojik Değerlendirme (100+ kelime)**

Makale, psikometri ve nedensel çıkarım literatürünü NLP alanına başarıyla taşıyarak disiplinlerarası bir köprü kurmaktadır. En güçlü yönü, soyut bir sorunu (geçerlilik) somut, uygulanabilir bir protokole (CVP) dönüştürmesidir. Ancak, CVP'nin pratikte uygulanmasının hesaplama maliyeti yüksek olabilir. Ayrıca, Karşıolgusal Nötralizasyon yönteminin farklı dillerde (özellikle düşük kaynaklı dillerde) nasıl performans göstereceği belirsizdir. Yine de, hesaplamalı sosyal bilim için bir "kalite standardı" oluşturma potansiyeli nedeniyle metodoloji alanında çığır açıcı bir çalışmadır.

---

### Makale 2: What Is Actually Being Annotated? Inter-Prompt Reliability as a Measurement Problem in LLM-Based Social Science Labeling
- **Yazar:** Jingyuan Liu
- **Tarih:** 2 Nisan 2026
- **URL:** https://arxiv.org/abs/2604.16413
- **Kategori:** cs.CY, cs.AI

**ÖZET (250-300 kelime)**

Büyük dil modelleri (LLM'ler), hesaplamalı sosyal bilimde etiketleme amacıyla giderek daha fazla kullanılmaktadır, ancak prompt varyasyonu altında metodolojik güvenilirlikleri belirsizliğini korumaktadır. Bu makale, Inter-Prompt Reliability (IPR — Promptlar Arası Güvenilirlik) kavramını tanıtarak, anlamsal olarak eşdeğer ancak dilsel olarak farklı prompt'lar arasında LLM çıktılarının istikrarını değerlendirmek için bir çerçeve sunmaktadır. Değerlendiriciler Arası Güvenilirlik (Inter-Rater Reliability) kavramından türetilen IPR, hem tutarlılığı hem de stokastisiteyi yakalamak için İkili Uyum Oranı (Pairwise Agreement Rate - PAR) ve dağılımını kullanmaktadır. Çerçeve, iki farklı görevde test edilmiştir: TREC (yorumlayıcı) ve Politifact (bilgi temelli). Sonuçlar, LLM etiketlemesinin yorumlayıcı görevlerde önemli ölçüde stokastik varyasyon sergilediğini, bilgi temelli görevlerde ise daha istikrarlı göründüğünü göstermektedir. Prompt'lar arasında çoğunluk oylamasının tekrarlanabilirliği önemli ölçüde artırdığı ve varyansı azalttığı da gösterilmiştir. Bulgular, LLM prompt'unun bir ölçüm aracı olarak işlev gördüğünü ancak ifadesinin metodolojik belirsizlik içerdiğini ortaya koymaktadır. Gelecekteki LLM tabanlı CSS çalışmaları için, araştırmacıların tek prompt değerlendirmesinden dağılımsal istikrar ve prompt birleştirmeye geçmeleri önerilmektedir.

**TÜRKİYE BAĞLAMI (200+ kelime)**

Türkiye'de sosyal bilim araştırmalarında LLM'lerin etiketleme aracı olarak kullanımı henüz yaygınlaşmamış olsa da, bu alandaki potansiyel büyüktür. Özellikle şu bağlamlarda önemlidir:

1. **Türkiye'de sosyal medya içerik analizi:** Türkiye'de siyasi söylem, nefret söylemi ve dezenformasyon üzerine yapılan içerik analizlerinde insan kodlayıcılar arası güvenilirlik zaten bir sorunken, LLM'lerin bu amaçla kullanılması IPR gibi çerçeveleri zorunlu kılmaktadır.

2. **Türkçe prompt mühendisliği:** Türkçenin sondan eklemeli yapısı, prompt varyasyonunun etkisini İngilizceye kıyasla daha karmaşık hale getirebilir. Aynı anlama gelen farklı Türkçe prompt'lar, anlamdaki küçük ek değişiklikleri nedeniyle çok farklı çıktılar üretebilir.

3. **Türkiye'de akademik kaynak kısıtları:** Türkiye'deki araştırma grupları, genellikle tek bir LLM modeline (örneğin, erişilebilir bir API üzerinden) erişebilmekte ve bu da metodolojik çeşitliliği sınırlamaktadır. IPR çerçevesi, bu tür kısıtlı durumlarda bile daha sağlam sonuçlar elde edilmesine yardımcı olabilir.

4. **Düşük kaynaklı dil dezavantajı:** Türkçe, LLM'ler için orta kaynaklı bir dil olduğundan, İngilizceye kıyasla daha yüksek prompt varyasyonu gösterebilir. Bu, IPR gibi yöntemlerin Türkçe bağlamda özellikle önemli olabileceğini göstermektedir.

**Metodolojik Değerlendirme (100+ kelime)**

Bu makale, LLM tabanlı içerik analizinde temel bir metodolojik sorunu ele alması açısından önemlidir. IPR çerçevesi, hesaplamalı sosyal bilimde ölçüm güvenilirliği için standart bir yaklaşım haline gelebilecek potansiyele sahiptir. Çalışmanın en güçlü yönü, geleneksel değerlendiriciler arası güvenilirlik kavramını LLM bağlamına uyarlaması ve somut bir metrik (PAR) sunmasıdır. Ancak çalışma yalnızca iki görev türünü test etmiştir; farklı dillerde ve daha karmaşık etiketleme şemalarında IPR'nin nasıl performans göstereceği henüz bilinmemektedir. Ayrıca, çoğunluk oylamasının gelişmiş modellerde aynı derecede etkili olup olmayacağı sorgulanmalıdır.

---

### Makale 3: The Third Ambition: Artificial Intelligence and the Science of Human Behavior
- **Yazarlar:** W. Russell Neuman, Chad Coleman
- **Tarih:** 7 Mart 2026
- **URL:** https://arxiv.org/abs/2603.07329
- **Kategori:** cs.AI, cs.CL, cs.CY

**ÖZET (250-300 kelime)**

Çağdaş yapay zekâ araştırmaları, iki baskın hedef etrafında örgütlenmiştir: üretkenlik (AI sistemlerini iş ve ekonomik çıktıyı hızlandırmak için araç olarak gören) ve uyum (alignment — giderek daha yetenekli sistemlerin güvenli ve insani değerlerle uyumlu davranmasını sağlamaya odaklanan). Bu makale, üçüncü bir hedefi tanımlamakta ve geliştirmektedir: büyük dil modellerinin (LLM'ler) insan davranışını, kültürünü ve ahlaki muhakemesini incelemek için bilimsel araçlar olarak kullanılması. Eşi benzeri görülmemiş miktarda insan üretimi metin üzerinde eğitilen LLM'ler, insanların sosyal alanlarda nasıl tartıştığı, gerekçelendirdiği, anlattığı ve normları müzakere ettiğine dair büyük ölçekli düzenlilikleri kodlamaktadır. Makale, bu modellerin insan sembolik davranışının "yoğunlaştırılmış temsilleri" (condensates) olarak anlaşılabileceğini savunmaktadır. Bu üçüncü hedefi, hesaplamalı sosyal bilim, içerik analizi, anket araştırması ve karşılaştırmalı-tarihsel sorgulama gelenekleri içinde konumlandırırken, model çıktısını kanıt olarak ele almanın epistemik sınırlarını da netleştirmektedir. Makale, temel modeller ile ince ayarlı sistemler arasında ayrım yapmakta, hizalama müdahalelerinin eğitim sırasında öğrenilen kültürel düzenlilikleri nasıl sistematik olarak yeniden şekillendirebileceğini veya gizleyebileceğini göstermektedir. Prompt tabanlı deneyler, sentetik popülasyon örneklemesi, karşılaştırmalı-tarihsel modelleme ve ablasyon çalışmaları gibi yeni metodolojik yaklaşımları gözden geçirmektedir.

**TÜRKİYE BAĞLAMI (200+ kelime)**

Bu makale, Türkiye'deki sosyal bilim araştırmaları için önemli bir kavramsal çerçeve sunmaktadır:

1. **Türk sosyal bilimlerinde metodolojik dönüşüm:** Türkiye'de sosyal bilimler, geleneksel olarak nitel yöntemler (mülakat, içerik analizi) ile nicel yöntemler (anket, istatistiksel analiz) arasında bölünmüştür. "Üçüncü Hırs" kavramı, bu iki geleneği LLM'ler aracılığıyla birleştirme potansiyeli sunmaktadır.

2. **Türk kültürü ve normlarının analizi:** Türkçe LLM'ler, Türk kültürel normlarını, ahlaki değerlerini ve toplumsal dinamiklerini incelemek için eşsiz bir fırsat sunmaktadır. Ancak Neuman ve Coleman'ın uyardığı gibi, hizalama müdahaleleri bu kültürel düzenlilikleri bozabilir — Türkçe modellerin Batılı değerlerle hizalanması, Türk kültürel özgünlüğünü yansıtmama riski taşır.

3. **Türkiye'de kamuoyu araştırmaları:** Makalede bahsedilen "sentetik popülasyon örneklemesi", Türkiye'deki geleneksel kamuoyu yoklamalarının yöntemsel sorunlarına (örneğin, düşük katılım oranları, sosyal beğenirlik yanlılığı) alternatif bir yaklaşım sunabilir.

4. **Akademik altyapı eksikliği:** Türkiye'de hesaplamalı sosyal bilim altyapısı sınırlıdır. Bu makale, disiplinlerarası merkezlerin kurulması ve sosyal bilimcilerin temel programlama ve AI okuryazarlığı kazanması gerektiğine işaret etmektedir.

**Metodolojik Değerlendirme (100+ kelime)**

Bu makale, LLM'lerin sosyal bilimdeki rolünü kavramsallaştırmada önemli bir adımdır. "Üçüncü Hırs" kavramı, AI araştırmasının hedeflerini yeniden çerçevelemek için ikna edici bir yol sunarken, aynı zamanda okuyucuyu bu yaklaşımın epistemik sınırlamaları konusunda da uyarmaktadır. Makalenin en güçlü yönü, felsefi derinlik ile pratik metodolojik rehberlik arasında denge kurmasıdır. Ancak, makalenin önerdiği yöntemlerin çoğu henüz deneysel olarak test edilmemiştir ve "condensate" metaforu her ne kadar yaratıcı olsa da, ampirik olarak doğrulanabilir bir hipotezden çok bir kavramsal çerçeve olarak kalmaktadır.

---

## 2) ETİK/TEORİ

### Makale 1: Beyond Explanation: Evidentiary Rights for Algorithmic Accountability
- **Yazar:** Matthew Stewart
- **Tarih:** 24 Mart 2026
- **URL:** https://arxiv.org/abs/2603.22716
- **Kategori:** cs.CY

**ÖZET (250-300 kelime)**

Algoritmik hesap verebilirlik literatürü ağırlıklı olarak açıklamaya (explanation) odaklanmış, etkilenen tarafların kararların neden alındığını anlamalarına yardımcı olmayı amaçlamıştır. Bu makale, bu odağın yetersiz olduğunu savunmaktadır. Açıklama olmadan kanıta erişim (evidentiary access), anlamlı bir itiraz (contestation) sağlamaz. Bir kişiye "risk puanınız 0.73'tü" dendiğinde kararı anlar ancak puanı doğrulayamaz, alternatifleri test edemez veya karşı kanıt üretemez. Makale, çekişme başarısızlıklarının bir taksonomisini sunarak, hesap verebilirlik müdahalelerinin çoğunun yalnızca bir başarısızlık modunu (opaklık) ele aldığını, diğer dördünü ele almadığını göstermektedir. Algoritmik karar alma bağlamlarını kapsayan 168 yasal vakayı analiz eden çalışma, itirazın iki aşamalı bir yapıyla karşı karşıya olduğunu bulmuştur: usuli aşama (kanıta erişim) ve doktrinel aşama (maddi sorumluluk kuralları). Dava edilen vakalar arasında, kanıta erişimi olmayanlar neredeyse hiç başarılı olamazken (%9), erişimi olanlar sorumluluk kalkanlarının olmadığı alanlarda %97'ye varan oranlarda başarılı olmuştur. Yazar, karşıolgusal sorgulama hakları (counterfactual interrogation rights) önermektedir: etkilenen tarafların, model iç işleyişini ifşa etmeden, değiştirilmiş girdilerle karar sistemlerini sorgulamasına ve sonuçların değişip değişmediğini gözlemlemesine olanak tanıyan haklar.

**TÜRKİYE BAĞLAMI (200+ kelime)**

Türkiye'de algoritmik hesap verebilirlik, özellikle son yıllarda artan dijital dönüşüm ve yapay zekâ kullanımıyla birlikte kritik bir önem kazanmıştır:

1. **Türkiye'de kredi skorlaması ve risk değerlendirmesi:** Türkiye'de bankacılık ve finans sektörü, kredi başvurularında algoritmik karar verme sistemlerini yaygın olarak kullanmaktadır. Vatandaşların bu sistemlerin kararlarına itiraz etme hakları sınırlıdır ve Stewart'ın önerdiği "evidentiary rights" çerçevesi, Türkiye'deki finansal düzenlemeler için önemli çıkarımlar sunmaktadır.

2. **KVKK ve algoritmik şeffaflık:** Türkiye'nin Kişisel Verileri Koruma Kanunu (KVKK), AB Genel Veri Koruma Yönetmeliği'ne (GDPR) benzer hükümler içerse de, algoritmik kararlara itiraz hakkı konusunda yeterli düzenleme bulunmamaktadır.

3. **İstihdam ve insan kaynakları:** Türkiye'de büyük şirketler işe alım süreçlerinde giderek daha fazla AI tabanlı araç kullanmaktadır. Adayların bu araçların kararlarına itiraz edebilmesi için Stewart'ın önerdiği usuli haklar çerçevesi kritik önem taşımaktadır.

4. **Yargısal denetim:** Türkiye'de idari kararlara karşı yargı yolu açık olmakla birlikte, algoritmik kararların yargısal denetimi için henüz spesifik bir mekanizma geliştirilmemiştir. Makalenin 168 vaka üzerinden yaptığı ampirik analiz, Türkiye'de de benzer bir çalışmanın yapılması gerektiğini göstermektedir.

**Metodolojik Değerlendirme (100+ kelime)**

Bu makale, algoritmik hesap verebilirlik tartışmasını "açıklama"dan "usuli haklar"a kaydırarak literatüre önemli bir katkı sunmaktadır. 168 yasal vakayı kapsayan ampirik analiz, argümanı somut verilerle desteklemektedir. Ancak yazarın da kabul ettiği gibi, veriler seçim etkisi (selection effect) içermektedir — mahkemeye taşınan vakalar, tüm algoritmik kararların temsili bir örneği değildir. Karşıolgusal sorgulama hakları konsepti yaratıcı olmakla birlikte, teknik uygulanabilirliği (özellikle karmaşık derin öğrenme modellerinde) belirsizdir. Yine de, AI düzenlemeleri için önemli bir kavramsal çerçeve sunmaktadır.

---

### Makale 2: How to Count AIs: Individuation and Liability for AI Agents
- **Yazarlar:** Yonathan Arbel, Peter Salib, Simon Goldstein
- **Tarih:** 24 Şubat 2026
- **URL:** https://arxiv.org/abs/2603.10028
- **Kategori:** cs.CY, cs.AI

**ÖZET (250-300 kelime)**

Yakın gelecekte milyonlarca AI ajanı ekonomide yaygınlaşacak, otonom olarak milyarlarca eylem gerçekleştirecektir. Kaçınılmaz olarak, işler ters gidecek, insanlar dolandırılacak, yaralanacak, hatta öldürülecektir. Hukuk, bir şekilde bu yaklaşan dalgayı yönetmek zorunda kalacaktır. Ancak bir AI zarara neden olduğunda, kimsenin sorumlu tutulabilmesinden önce cevaplanması gereken ilk soru şudur: Bunu Hangi AI Yaptı? AI'ları tanımlamak olağandışı derecede zordur. AI'ların bedenleri yoktur. İstedikleri gibi kopyalanabilir, bölünebilir, birleşebilir, sürü halinde hareket edebilir ve yok olabilirler. Makale, AI'ları tanımlamanın hukuki sorununu kapsamlı bir şekilde teşhis etmektedir. İki tür kimlik gereklidir: "ince" (thin) ve "kalın" (thick). İnce kimlik, her AI eylemini bir insan asile bağlar — AI ajanlarını yapan ve kullanan insanları sorumlu tutmak için gereklidir. Kalın kimlik ise AI ajanlarını kendi aralarında ayırır — milyonlarca AI varlığını ayrık, kalıcı birimlere ayırarak istikrarlı, tutarlı hedeflere sahip olmalarını sağlar. Makale ayrıca bir çözüm sunar: "Algoritmik Şirket" (Algorithmic Corporation veya A-corp) — kendi adına mülk sahibi olabilen, sözleşme yapabilen ve dava açabilen yasal-kurgusal bir varlık. İnsanlar tarafından sahip olunan ancak AI'lar tarafından yönetilen A-corp'lar, AI eylemlerini bir insan sahibine bağlayarak ince kimlik sorununu ve kendi kendine örgütlenme yoluyla kalın kimlik sorununu çözmektedir.

**TÜRKİYE BAĞLAMI (200+ kelime)**

Bu makale, Türkiye'nin AI düzenlemesi için hayati öneme sahip bir çerçeve sunmaktadır:

1. **Türk hukuk sisteminde AI sorumluluğu:** Türkiye'de henüz AI ajanlarının hukuki statüsüne ilişkin spesifik bir düzenleme bulunmamaktadır. Mevcut Türk Borçlar Kanunu ve Türk Ceza Kanunu, geleneksel fail-sorumluluk ilişkisine dayandığından, otonom AI ajanlarının neden olduğu zararların tazmininde yetersiz kalacaktır.

2. **Dijital Türkiye vizyonu ve AI:** Türkiye'nin Ulusal Yapay Zekâ Stratejisi (2021-2025), AI'ın ekonomik potansiyeline odaklanırken, hukuki sorumluluk ve hesap verebilirlik konularını yeterince ele almamıştır. "A-corp" modeli, Türkiye'deki AI girişimleri için bir işletme yapısı alternatifi sunabilir.

3. **Sigorta ve düzenleme:** Makalede önerilen AI sorumluluk çerçevesi, Türkiye Sigortacılık ve Özel Emeklilik Düzenleme ve Denetleme Kurumu (SEDDK) için AI kaynaklı zararların sigortalanması konusunda yol gösterici olabilir.

4. **Uluslararası uyum:** AB AI Yasası gibi uluslararası düzenlemelere uyum sağlamaya çalışan Türkiye için, AI ajanlarının kimliklendirilmesi ve sorumluluğu konusundaki bu teorik çerçeve, yerel düzenlemelerin şekillendirilmesinde önemli bir referans noktası olabilir.

**Metodolojik Değerlendirme (100+ kelime)**

Bu makale, hukuk ve AI kesişiminde nadir bulunan bir teorik derinlik sunmaktadır. "İnce" ve "kalın" kimlik ayrımı, AI sorumluluğu sorununu analiz etmek için kullanışlı bir kavramsal araçtır. "A-corp" önerisi yaratıcı olmakla birlikte, pratik uygulanabilirliği (özellikle uluslararası hukuk bağlamında) sorgulanmaya açıktır. Makale, AI ajanlarının self-örgütlenme dinamiklerini ekonomik teşviklerle açıklarken oyun teorisinden yararlanmakta, ancak bu modellerin gerçek dünyadaki karmaşık AI sistemlerini ne ölçüde yansıttığı belirsizdir. Yine de, AI hukuku literatürüne önemli bir katkıdır.

---

### Makale 3: Bridging the Gap in the Responsible AI Divides
- **Yazarlar:** Bálint Gyevnár, Atoosa Kasirzadeh
- **Tarih:** 15 Mart 2026
- **URL:** https://arxiv.org/abs/2603.14495
- **Kategori:** cs.CY, cs.AI

**ÖZET (250-300 kelime)**

AI Güvenliği (AIS) ve AI Etiği (AIE) arasındaki gerilimler, AI yönetişimi ve AI hakkındaki kamu tartışmalarında giderek daha fazla su yüzüne çıkmakta ve yazarların "sorumlu AI bölünmeleri" (responsible AI divides) olarak adlandırdığı olguya yol açmaktadır. Makale, bu gerilimlerle başa çıkmanın dört modunu kategorize eden bir model sunmaktadır: radikal yüzleşme, kopma, bölmeli bir arada yaşama ve kritik köprü kurma. Yazarlar, kritik köprü kurmanın, özellikle köprü kurma problemlerine odaklanarak, sorumlu AI'yı ilerletmek için en uygun yapıcı yollardan birini sunduğunu araştırmaktadır. 3.550 makaleden oluşan bir veri kümesini analiz etmek için hesaplamalı araçlar kullanarak, AIE ve AIS araştırma alanlarını haritalamakta ve hem belirgin hem de örtüşen problemleri tanımlamaktadırlar. Bulgular, tematik bölünmeler ve örtüşmeler olduğunu göstermektedir. Örneğin, AIE uzun süredir adaletsizliğin ve somut AI zararlarının üstesinden gelmeyle uğraşırken, AIS öncelikle AI yeteneklerinden kaynaklanan risklerin hafifletilmesine odaklanan bir öngörü yaklaşımını benimsemiştir. Aynı zamanda, hem AIE hem de AIS'te şeffaflık, tekrarlanabilirlik ve yetersiz yönetişim mekanizmaları etrafında önemli örtüşmeler bulunmaktadır. Makale, işbirlikçi AI yönetişimini geliştirmek için köprü kurma problemlerine odaklanmayı önermekte ve paylaşılan hususları sorumlu AI'ya işbirlikçi bir yaklaşıma entegre etmek için bir dizi öneri sunmaktadır.

**TÜRKİYE BAĞLAMI (200+ kelime)**

Türkiye'de AI yönetişimi, AI Güvenliği ve AI Etiği arasındaki bölünmenin henüz farkında olmayan bir aşamadadır. Bu makale, Türkiye için şu açılardan önemlidir:

1. **Türkiye'de AI stratejisi ve etik:** Türkiye'nin Ulusal Yapay Zekâ Stratejisi, etik ilkelerden bahsetmekle birlikte, AI güvenliği konusunda spesifik hedefler belirlememiştir. Makaledeki "kritik köprü kurma" yaklaşımı, Türkiye'nin AI stratejisini güncellerken iki alanı birleştirmesi için bir yol haritası sunabilir.

2. **Akademik bölünmeler:** Türkiye'de AI etiği çalışmaları genellikle sosyal bilimler ve felsefe bölümlerinde, AI güvenliği ise mühendislik ve bilgisayar bilimlerinde yürütülmektedir. Bu iki topluluk arasında neredeyse hiçbir diyalog bulunmamaktadır. Makale, disiplinlerarası işbirliği için bir model sunmaktadır.

3. **Düzenleyici kapasite:** Türkiye'de AI düzenlemesi, Ticaret Bakanlığı, Sanayi ve Teknoloji Bakanlığı ve Kişisel Verileri Koruma Kurumu gibi farklı kurumlar arasında dağılmış durumdadır. Bu kurumlar arasındaki koordinasyon eksikliği, "sorumlu AI bölünmeleri"nin kurumsal bir yansımasıdır.

4. **Sivil toplum ve savunuculuk:** Türkiye'de AI etiği alanında çalışan sivil toplum kuruluşları (örneğin, Dijital Haklar Koalisyonu) genellikle AIE perspektifine odaklanırken, teknik AIS topluluğuyla bağlantıları sınırlıdır. Makale, bu aktörler arasında köprü kurmak için kavramsal bir araç sağlamaktadır.

**Metodolojik Değerlendirme (100+ kelime)**

Bu makale, AIE ve AIS arasındaki gerilimi sistematik olarak haritalandırması ve 3.550 makaleyi kapsayan hesaplamalı analiziyle dikkat çekmektedir. Dört modlu sınıflandırma (radikal yüzleşme, kopma, bölmeli bir arada yaşama, kritik köprü kurma), alandaki farklı pozisyonları anlamak için kullanışlı bir araçtır. En güçlü yönü, teorik analizi pratik önerilerle birleştirmesidir. Ancak, "critical bridging"in nasıl uygulanacağına dair somut adımlar sınırlıdır ve önerilerin çoğu soyut kalmaktadır. Ayrıca, 3.550 makalelik veri setinin seçim kriterleri ve kapsamı hakkında daha fazla ayrıntıya ihtiyaç vardır.

---

## 3) GÜNCEL TARTIŞMALAR

### Makale 1: Jagged AI in Scientific Peer Review: Evidence from POMP Data Analysis
- **Yazarlar:** Jin Wook Lee, William Szegda, Zhisheng Song, Edward L. Ionides
- **Tarih:** 8 Mayıs 2026
- **URL:** https://arxiv.org/abs/2605.07855
- **Kategori:** stat.AP

**ÖZET (250-300 kelime)**

AI araçlarının bilimsel akran değerlendirmesindeki performansı büyük ölçüde keşfedilmemiş bir alandır. Temel zorluk, AI'nın bazı alanlarda güçlü yetenek artışları sergilerken diğerlerinde yetersiz kaldığı "jagged AI" (düzensiz AI) olgusudur. Bu çalışma, POMP (partially observed Markov process) veri analizlerini inceleme bağlamında bu düzensizliği araştırmıştır. Michigan Üniversitesi yüksek lisans dersi kapsamında dört dönem boyunca tamamlanmış 72 POMP projesi incelenmiş, insan değerlendirmeleri ile dört farklı AI değerlendirme ajanı karşılaştırılmıştır. AI değerlendiriciler, insanların gözden kaçırdığı teknik hataları ve geçersiz çıkarım metodolojisini yakalamada başarılı olurken, yorumlayıcı hatalar, anlatı tutarlılığı ve alan bilgisine dayalı model eleştirisinde insan standartlarının gerisinde kalmıştır. Düzensizlik tüm ajanlar için benzer bulunmuş, bu da bunun öncelikle altta yatan AI modelinin bir özelliği olduğunu göstermektedir. Skill dosyası yapılandırması, ajanların hangi zayıflıkları vurguladığını değiştirmiş, ancak düzensizliği ortadan kaldırmamıştır. Bu bulgular, AI destekli akran değerlendirmesinin tam otomasyon yerine insan-AI işbirliği gerektirdiğini göstermektedir.

**TÜRKİYE BAĞLAMI (200+ kelime)**

Bu makale, Türkiye'deki akademik yayın süreçleri için doğrudan çıkarımlar içermektedir:

1. **Türkiye'de akran değerlendirmesi sorunları:** Türkiye'deki akademik dergilerde hakem bulma zorluğu, değerlendirme sürelerinin uzunluğu ve kalite kontrolü sorunları yaygındır. AI destekli akran değerlendirmesi, bu sorunların bazılarını hafifletebilir. Ancak makalenin gösterdiği gibi, AI'nın "jagged" profili, özellikle yorumlayıcı değerlendirmelerde insan denetimini zorunlu kılmaktadır.

2. **TÜBİTAK ve ULAKBİM dergileri:** Türkiye'deki akademik dergilerin önemli bir kısmı TÜBİTAK/ULAKBİM bünyesinde yayın yapmaktadır. Bu dergilerin akran değerlendirme süreçlerinde AI araçlarını kullanma potansiyeli bulunmakla birlikte, teknik hataları yakalama becerisinin yorumlayıcı bağlamda sınırlı olduğu unutulmamalıdır.

3. **Akademik teşvik sistemi:** Türkiye'deki akademik teşvik sistemi, uluslararası yayın sayısını ödüllendirmekte, ancak yayın kalitesini yeterince denetlememektedir. AI destekli akran değerlendirmesi, bu denetim açığını kapatmaya yardımcı olabilir.

4. **Dil engeli ve "jaggedness":** AI modellerinin Türkçe akademik metinlerdeki performansı İngilizceye kıyasla daha düzensiz olabilir. Bu, Türkiye'de AI destekli akran değerlendirmesi uygulamalarında daha dikkatli bir yaklaşım gerektirmektedir.

**Metodolojik Değerlendirme (100+ kelime)**

Bu çalışma, "jagged AI" kavramını somut bir bağlamda test etmesi açısından değerlidir. 72 proje ve dört farklı AI ajanı kullanan deneysel tasarım, bulguların güvenilirliğini artırmaktadır. En önemli katkısı, AI'nın akran değerlendirmesinde insanın yerini alamayacağını ancak tamamlayıcı bir araç olarak değerli olabileceğini göstermesidir. Ancak çalışma yalnızca bir ders kapsamındaki projeleri incelemiştir; farklı disiplinlerde ve daha büyük ölçekte tekrarlanması gerekmektedir. Skill dosyası yapılandırmasının etkileri de daha ayrıntılı incelenmelidir.

---

### Makale 2: When Transparency Falls Short: Auditing Platform Moderation During a High-Stakes Election
- **Yazarlar:** Benedetta Tessa, Gautam Kishore Shahi, Amaury Trujillo, Stefano Cresci
- **Tarih:** 21 Nisan 2026
- **URL:** https://arxiv.org/abs/2604.19285
- **Kategori:** cs.SI, cs.CY, cs.HC

**ÖZET (250-300 kelime)**

Büyük siyasi olaylar sırasında sosyal medya platformları artan sistemik risklerle karşılaşmaktadır. Ancak, platformların moderasyon uygulamalarını bu dönemlerde nasıl ayarladıkları belirsizdir. Dijital Hizmetler Yasası (DSA) Şeffaflık Veritabanı, ilk kez içerik moderasyonunu büyük ölçekte sistematik olarak inceleme fırsatı sunmaktadır. Bu çalışma, 2024 Avrupa Parlamentosu seçimlerini çevreleyen sekiz aylık bir dönemde Avrupa'daki en büyük sekiz sosyal medya platformunun 1,58 milyar kendi bildirdiği moderasyon eylemini analiz etmiştir. Bulgular, platformların moderasyon stratejilerinde seçimler etrafında anlamlı bir değişiklik göstermediğini ortaya koymuştur. Bu, platformların somut ayarlamalar yapıp yapmadığı veya veritabanının yapısının bunları maskeleyip maskelemediği sorusunu gündeme getirmektedir. Ayrıca, Şeffaflık Veritabanı'nın lansmanından bir yıl sonra, platformların şeffaflık ve hesap verebilirliğine ilişkin ilk endişelerin hâlâ devam ettiği görülmüştür. Bulgular, mevcut öz-düzenleyici yaklaşımların sınırlarını vurgulamakta ve çevrimiçi platformların demokratik süreçleri koruma sorumluluklarını yerine getirmelerini sağlamak için daha güçlü uygulama ve daha iyi veri erişim mekanizmalarına ihtiyaç olduğunu göstermektedir.

**TÜRKİYE BAĞLAMI (200+ kelime)**

Bu makale, Türkiye'deki sosyal medya düzenlemeleri ve seçim süreçleri için kritik öneme sahiptir:

1. **Türkiye'de sosyal medya yasası:** 5651 sayılı İnternet Ortamında Yapılan Yayınların Düzenlenmesi ve Bu Yayınlar Yoluyla İşlenen Suçlarla Mücadele Edilmesi Hakkında Kanun, sosyal medya platformlarına içerik çıkarma ve kullanıcı verilerini paylaşma yükümlülüğü getirmektedir. Ancak yasa, platformların moderasyon politikalarında seçim dönemlerinde nasıl bir değişiklik yapması gerektiği konusunda spesifik hükümler içermemektedir.

2. **2023 ve 2024 seçimleri:** Türkiye'de 2023 cumhurbaşkanlığı ve 2024 yerel seçimleri sırasında sosyal medya platformlarının moderasyon uygulamaları yoğun tartışma konusu olmuştur. Bu makalenin bulguları — platformların seçim dönemlerinde moderasyon stratejilerini değiştirmediği — Türkiye bağlamında da geçerli olabilir.

3. **Düzenleyici kurum eksikliği:** AB'nin DSA'sına benzer kapsamlı bir dijital hizmetler yasası Türkiye'de bulunmamaktadır. Bilgi Teknolojileri ve İletişim Kurumu (BTK) ve Radyo ve Televizyon Üst Kurulu (RTÜK) gibi kurumların yetkileri sınırlı ve dağınıktır.

4. **Dezenformasyonla mücadele:** Türkiye'de seçim dönemlerinde dezenformasyon önemli bir sorundur. Makalede önerilen şeffaflık mekanizmaları, Türkiye'de kamuoyunun platform moderasyonunu bağımsız olarak denetlemesine olanak tanıyabilir.

**Metodolojik Değerlendirme (100+ kelime)**

Bu çalışma, 1,58 milyar moderasyon eylemini kapsayan benzersiz ölçeğiyle dikkat çekmektedir. DSA Şeffaflık Veritabanı'nın sağladığı veriler sayesinde, platformların kendi bildirdiği eylemleri analiz ederek önemli bir boşluğu doldurmaktadır. Ancak, veriler platformların kendi bildirimlerine dayandığından, bildirim yanlılığı (self-reporting bias) önemli bir sınırlamadır. Platformların gerçek moderasyon uygulamaları, bildirilenlerden farklı olabilir. Ayrıca, çalışma yalnızca AB platformlarını incelemiştir; Türkiye gibi farklı düzenleyici rejimlerdeki platform davranışları farklılık gösterebilir.

---

### Makale 3: Stochastic Wage Suppression on Gig Platforms and How to Organize Against It
- **Yazarlar:** Ana-Andreea Stoica, Celestine Mendler-Duenner, Moritz Hardt
- **Tarih:** 17 Nisan 2026
- **URL:** https://arxiv.org/abs/2604.15962
- **Kategori:** cs.HC, cs.CY

**ÖZET (250-300 kelime)**

Dijital emek platformları, veri etiketleme ve AI modellerinin kırmızı takım testinden, yolculuk paylaşımı ve yemek dağıtımına kadar insan girdisi elde etmek için giderek daha fazla kullanılmaktadır. Bu tür piyasalarda temel bir endişe, platformların düşük maliyetli işgücü bolluğundan yararlanarak ücretleri baskılama yeteneğidir. Çalışma, bu sömürü modelini incelemek için yeni bir posted-price tedarik modeli sunmaktadır. Bir platformun, sırayla gelen işçilere fiyatlar teklif ederek M görevi tamamlamaya çalıştığı bir model önerilmektedir. İlk olarak, işçilerin tahmini maliyeti hakkında doğal varsayımlar altında, platformun M görevin tamamını O(M) bekleme süresiyle tamamlamasına rağmen toplam işgücü maliyetinin yalnızca O(log(M)/M) oranını ödediği basit bir fiyatlandırma stratejisi olduğu gösterilmiştir. Bu sonuç, platformların işçilerin işgücü maliyeti konusundaki belirsizliğinden nasıl yararlanarak ücretleri etkili bir şekilde baskılayabildiğini vurgulamaktadır. Ardından, dijital emek piyasalarında ücretleri artırmak ve refahı teşvik etmek için bir kaldıraç olarak kolektif eylem incelenmektedir. Özellikle, bir fiyat tabanına bağlı kalmayı taahhüt eden küçük bir hedeflenmiş düşük maliyetli işçi koalisyonunun, platformun toplam harcamasını logaritmikten lineer O(M)'ye çıkarmaya zorladığı gösterilmiştir. Buna karşılık, eşit büyüklükte rastgele örneklenmiş bir koalisyon büyük ölçüde etkisiz kalmaktadır.

**TÜRKİYE BAĞLAMI (200+ kelime)**

Türkiye'de dijital emek platformları (Getir, Yemeksepeti, Trendyol, Armut gibi) hızla büyümekte ve milyonlarca çalışanı etkilemektedir:

1. **Türkiye'de platform ekonomisi:** Türkiye, getir gibi hızlı teslimat platformlarının doğduğu ülke olmasına rağmen, platform çalışanlarının hakları konusunda kapsamlı bir düzenleme bulunmamaktadır. Makaledeki ücret baskılama modeli, Türkiye'deki platform çalışanlarının karşılaştığı sorunları matematiksel olarak açıklamaktadır.

2. **Sendikalaşma ve kolektif eylem:** Türkiye'de platform çalışanlarının sendikalaşma oranı düşüktür. Makalenin gösterdiği gibi, hedeflenmiş düşük maliyetli işçi koalisyonlarının ücret baskılamayı kırmadaki etkinliği, Türkiye'deki platform çalışanları için örgütlenme stratejilerine ışık tutmaktadır.

3. **Kayıt dışı ekonomi:** Türkiye'de platform çalışanlarının önemli bir kısmı kayıt dışı çalışmaktadır. Bu, makalede bahsedilen "düşük maliyetli işgücü bolluğu" durumunu Türkiye'de daha da şiddetlendirmektedir.

4. **Yasal düzenleme ihtiyacı:** Türkiye'de 2024 yılında yürürlüğe giren bazı düzenlemeler (örneğin, motokuryeler için çalışma koşulları) platform çalışanlarının durumunu kısmen iyileştirmiş olsa da, makalede önerilen türden kapsamlı bir ücret koruma mekanizması henüz mevcut değildir.

**Metodolojik Değerlendirme (100+ kelime)**

Bu makale, platform ekonomisinde ücret sömürüsünü matematiksel olarak modellemesi açısından önemli bir katkı sunmaktadır. Posted-price modeli ve kolektif eylem analizi, teorik bilgisayar bilimi ile politik ekonominin kesiştiği nadir bir çalışmadır. En güçlü yönü, soyut matematiksel sonuçların (log(M)/M oranı) somut politik çıkarımlara (kolektif eylem stratejileri) dönüştürülmesidir. Ancak model varsayımlarının gerçek dünya platform piyasalarını ne ölçüde yansıttığı sorgulanmalıdır; örneğin, işçilerin maliyet tahminleri hakkındaki bilgi asimetrisi varsayımı güçlüdür. Sentetik deneyler dışında gerçek dünya verisiyle doğrulama yapılmamıştır.

---

## OKUMA LİSTESİ (Reading List)

| Zorluk | Makale | Konu | Öncelik |
|--------|--------|------|---------|
| ★★★☆☆ | The Proxy Presumption | Embedding geçerliliği, psikometri | Yüksek |
| ★★★★☆ | Inter-Prompt Reliability | LLM etiketleme güvenilirliği | Yüksek |
| ★★☆☆☆ | The Third Ambition | LLM'ler sosyal bilim aracı olarak | Orta |
| ★★★☆☆ | Beyond Explanation | Algoritmik hesap verebilirlik, usuli haklar | Yüksek |
| ★★★★☆ | How to Count AIs | AI ajan sorumluluğu, hukuk | Yüksek |
| ★★★☆☆ | Bridging the RAI Divides | AI Güvenliği vs AI Etiği | Orta |
| ★★★☆☆ | Jagged AI in Peer Review | AI destekli akran değerlendirmesi | Yüksek |
| ★★☆☆☆ | When Transparency Falls Short | Platform moderasyonu, seçimler | Orta |
| ★★★★☆ | Stochastic Wage Suppression | Platform ekonomisi, ücret sömürüsü | Yüksek |

---

## GLOSSARY (Terimler Sözlüğü)

- **Proxy Presumption (Vekil Varsayımı):** Bir temsilin (embedding) geometrik özelliklerinin, doğrudan sosyal bir kavramın ölçümü olarak kullanılması varsayımı.
- **Construct Validity Protocol (Yapı Geçerliliği Protokolü):** Bir ölçüm aracının gerçekten ölçmeyi amaçladığı kavramı ölçüp ölçmediğini sistematik olarak değerlendiren süreç.
- **Inter-Prompt Reliability (Promptlar Arası Güvenilirlik):** Anlamsal olarak eşdeğer ancak dilsel olarak farklı prompt'lar arasında LLM çıktılarının istikrarı.
- **Evidentiary Rights (Kanıta Erişim Hakları):** Algoritmik kararlara maruz kalan bireylerin, bu kararların dayandığı kanıtlara erişme ve bunları sorgulama hakkı.
- **Counterfactual Interrogation Rights (Karşıolgusal Sorgulama Hakları):** Etkilenen tarafların, model iç işleyişini ifşa etmeden, farklı girdilerle karar sistemlerini test etme hakkı.
- **Algorithmic Corporation (A-corp):** Kendi adına işlem yapabilen, insanlar tarafından sahip olunan ancak AI ajanları tarafından yönetilen yasal-kurgusal varlık.
- **Jagged AI (Düzensiz AI):** AI sistemlerinin bazı alanlarda yüksek performans gösterirken diğerlerinde beklenmedik şekilde düşük performans göstermesi olgusu.
- **Stochastic Wage Suppression (Stokastik Ücret Baskılama):** Platformların, işçilerin işgücü maliyeti konusundaki belirsizliğinden yararlanarak ücretleri sistematik olarak düşük tutması stratejisi.
- **Responsible AI Divides (Sorumlu AI Bölünmeleri):** AI Güvenliği (AIS) ve AI Etiği (AIE) toplulukları arasındaki kavramsal ve pratik gerilimler.
- **Third Ambition (Üçüncü Hırs):** LLM'lerin üretkenlik ve uyumun ötesinde, insan davranışını incelemek için bilimsel araçlar olarak kullanılması hedefi.

---

## SONRAKİ HAFTA TAKİP EDİLECEKLER

### İzlenecek Anahtar Kelimeler:
- computational social science + LLM validation
- algorithmic accountability + evidentiary rights
- AI-assisted peer review + jaggedness
- platform economy + wage suppression + collective action
- responsible AI + bridging frameworks
- AI agent liability + legal personhood

### İzlenecek Yazarlar:
- **Matthew Stewart:** Algoritmik hesap verebilirlik ve usuli haklar üzerine yeni çalışmaları takip edilmeli.
- **Yonathan Arbel (ve ekibi):** AI hukuku ve A-corp modelinin geliştirilmesi.
- **Moritz Hardt / Ana-Andreea Stoica:** Platform ekonomisi ve kolektif eylem üzerine yeni modeller.
- **Bálint Gyevnár & Atoosa Kasirzadeh:** AI Güvenliği ve AI Etiği arasındaki köprü çalışmaları.
- **Edward L. Ionides:** Jagged AI ve akran değerlendirmesi üzerine takip çalışmaları.

### Takip Edilecek Konular:
1. **AB AI Yasası uygulamaları:** DSA Şeffaflık Veritabanı'nın evrimi ve platform moderasyonuna etkisi.
2. **LLM tabanlı ölçüm araçlarının geçerlilik standartları:** CVP protokolünün farklı dillerde test edilmesi.
3. **Platform çalışanlarının örgütlenme stratejileri:** Özellikle Türkiye'deki Getir ve Yemeksepeti çalışanları örneğinde.
4. **Akran değerlendirmesinde AI kullanımına ilişkin etik kurallar:** Yayınevleri ve konferansların bu konudaki politikaları.
5. **AI ajanlarının hukuki statüsü:** AB AI Yasası ve ulusal düzenlemelerdeki gelişmeler.

---

*Rapor otomatik olarak oluşturulmuştur. Kaynak: arXiv API (cs.SI, cs.CY, cs.CL, cs.AI, cs.HC). Tarih: 14 Mayıs 2026.*
