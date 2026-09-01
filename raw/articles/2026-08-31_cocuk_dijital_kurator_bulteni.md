# KURATOR: Çocuklar ve Dijital Dünya - Haftalık Derleme

## 2026-08-31 | Hafta 35/2026

**Kapsam:** 29-31 Ağustos 2026 (önceki derleme: 23-28 Ağustos)
**Prepared by:** KURATOR Araştırma Ekibi

---

## 📋 YÖNETİCİ ÖZETİ

Bu hafta Telegram link akışı sessizdi (29-31 Ağustos arasında 4 ardışık ingestion çalışmasında yeni link çıkmadı; son categorized veri 28 Ağustos'a ait ve 29 Ağustos derlemesinde tüketilmişti). Bu nedenle derleme, doğrudan kaynak taramasıyla (arXiv API + erişilebilir politika/haber kaynakları) üretildi. Haftanın ana ekseni, **dünya genelinde çocuklara yönelik sosyal medya yasaklarının ana akım politika haline gelmesi** ve buna eşlik eden tartışmalardır: Birleşik Krallık under-16 yasağını resmen duyurdu (uygulama Bahar 2027), Türkiye'de 15 yaş altı düzenlemesi Resmi Gazete'de yayımlanarak altı ay sonra yürürlüğe girecek, AB Komisyonu ortak yaş doğrulama çerçevesini hızlandırıyor ve Meta, ABD eyaletleriyle 17,1 milyar dolarlık rekor anlaşmayla çocukları bağımlı kılan platform tasarımına ilişkin davaları sonlandırdı. Akademik cephede ise yasağa karşı çıkan iki güçlü 2026 çalışması öne çıkıyor: Avustralya yasağının çocuklar tarafından nasıl aşıldığını belgeleyen saha araştırması (Nansen ve ark.) ve "çocuk-uyumlu güvenlik" (child-fit security) paradigmasını öneren eleştirel çalışma (Ramokapane ve ark.).

### Top 5 Highlights:
1. 🇬🇧 **Birleşik Krallık under-16 sosyal medya yasağını duyurdu** — Avustralya modeli (Instagram, YouTube, TikTok, Snapchat, Facebook, X); mesajlaşma uygulamaları kapsam dışı; uygulama Bahar 2027
2. 🇹🇷 **Türkiye'de 15 yaş altı sosyal medya düzenlemesi yasalaştı** — yaş doğrulama zorunluluğu, ebeveyn kontrol araçları, oyun platformu yükümlülükleri; BTK yaptırım merdiveni (reklam yasağı → %50 bant genişliği daraltma)
3. 🇪🇺 **AB ortak yaş doğrulama çerçevesini hızlandırıyor** — 29 Nisan 2026 Tavsiyesi; üye devletler için 31 Aralık 2026 hedefi; DSA Art. 28 tabanlı
4. 🤖 **UK'de çocukların deepfake ihbarları rekor kırdı** — Report Remove 2026 ilk yarıda 420 ihbar aldı (2025 toplamı 397'yi geçti); vakaların çoğu CSAM eşiğini aşıyor
5. 🎓 **"Children Are Not the Enemy"** — yasak ve gözetim paradigmasına alternatif olarak çocuk-uyumlu güvenlik yaklaşımı (arXiv 2606.17957)

---

## 🎯 ARAŞTIRMA KONULARI

### 1. Küresel Sosyal Medya Yasağı Dalgası: Yasama Takvimi

2026 yazında yasak dalgası belirgin biçimde hızlandı. NYT'nin 26-28 Ağustos kapsamına göre yaklaşık **40 ülke** çocukların sosyal medya kullanımını sınırlayan yasama süreçlerini tartışıyor; Reuters'ın 24 Ağustos analizine göre Avustralya (Aralık 2025'te dünyada ilk under-16 yasağı) modeli, Avrupa devletleri, Endonezya, Vietnam ve Brezilya dahil birçok ülkeye yayılıyor. 2026 ortası itibarıyla **15'ten fazla ülke** 14-16 yaş altı için bağlayıcı yasalar çıkardı veya yasama sürecine soktu. Meta'nın 17,1 milyar dolarlık ABD eyalet anlaşması (çocukları bağımlı kılan platform tasarımı iddiaları) bu dalgaya meşruiyet kazandırdı. Türkiye için kritik ders: yasakların tek başına yeterli olmadığı, yaş doğrulama teknik altyapısı, platform yaptırımları ve ebeveyn/çocuk desteğinin birlikte tasarlanması gerektiğidir.

### 2. Yaş Doğrulama ve Uygulanabilirlik Tartışması

AB Komisyonu'nun 29 Nisan 2026 tarihli Tavsiyesi, AB genelinde ortak yaş doğrulama teknolojileri için mimari şartname (EU age verification blueprint) öngörüyor ve üye devletleri 31 Aralık 2026'ya kadar uygulamaya çağırıyor. FPF analizi (12 Mayıs 2026), DSA'da açık asgari yaş veya yaş doğrulama maddesi bulunmadığını, bu nedenle gönüllülük/zorunluluk muğlaklığının sürdüğünü ancak ortaya çıkan DSA uygulamalarının (küçüklerin korunması kılavuzları) yaş güvencesini fiilen zorunlu kıldığını belirtiyor. Avustralya deneyimi ise uygulanabilirlik sınırını gösteriyor: Nansen ve ark.'nın 12-16 yaş grubuyla yürüttüğü beş odak grubu, çocukların yasağı "haksız ve etkisiz" gördüğünü ve platform erişim kontrollerini deneyerek zayıf noktaları öğrendiğini ortaya koyuyor. Bu bulgu, Türkiye'nin Kasım 2026'da yürürlüğe girecek yaş doğrulama uygulaması için doğrudan tasarım uyarısı niteliğinde.

### 3. Deepfake ve Yapay Zekâ Kaynaklı İstismar

IWF'nin Report Remove servisi, 2026'nın ilk altı ayında çocuklardan kendi görüntülerinin sahte/müstehcen versiyonlarına ilişkin **420 ihbar** aldı — 2025 yıl toplamını (397) şimdiden aştı. İhbar edilen manipüle görüntülerin çoğunluğu CSAM eşiğini geçiyor ve bir kısmı sextortion (şantaj) vakalarıyla bağlantılı. IWF CTO'su Dan Sexton'ın vurguladığı gibi, internetteki masum bir çocuk fotoğrafından CSAM üretmek artık teknik olarak önemsiz bir engel; mağdur çocuğun kendi başına yapabileceği hiçbir şey yok. NSPCC, AI ürünlerine "tasarım gereği güvenlik" (safety by design) entegre edilmesi çağrısını yineliyor. Türkiye'de de 2026'da yürürlüğe giren AI-CSAM düzenlemelerinin denetimi ve ihbar mekanizmalarının güçlendirilmesi bu veriler ışığında öncelik kazanıyor.

### 4. Okullarda Dijital Politikalar

ABD'de 2 Haziran 2026 itibarıyla **38 eyalet ve District of Columbia**, okul bölgelerinin öğrencilerin okulda cep telefonu kullanımını yasaklamasını veya kısıtlamasını zorunlu kılıyor; Kaliforniya'da AB 3216 (Newsom imzalı) 1 Temmuz 2026 itibarıyla yürürlükte. Bu dalga, "ekran süresi düzenlemesi" tartışmasını aile alanından kurumsal alana taşıyor: okullar artık telefon politikalarını pedagojik ve ruh sağlığı gerekçeleriyle yeniden tasarlıyor. Türkiye'de MEB'in mevcut telefon kısıtlamalarının bu uluslararası standartlarla karşılaştırmalı güncellenmesi, özellikle öğretmen eğitimi ve veli iletişimi boyutlarıyla ele alınmalıdır.

---

## 📚 AKADEMİK KAYNAKLAR

### 1. Children Are Not the Enemy: Child-Fit Security as an Alternative to Bans and Surveillance
**Yazarlar:** Kopo M. Ramokapane, Rui Huan, Zaina Dkaidek, Awais Rashid
**Tarih:** 2026-06-16 | **Kaynak:** arXiv (cs.CR/cs.CY)
**URL:** https://arxiv.org/abs/2606.17957 | **DOI:** 10.48550/arXiv.2606.17957

**ÖZET:**
Dijital teknolojiler çocukların öğrenme, oyun, iletişim, kimlik oluşumu ve toplumsal katılımının merkezine yerleşmiş durumda. Buna rağmen çocukların çevrimiçi güvenliğine yönelik baskın yaklaşımlar, kısıtlama mekanizmalarına — yasaklar, yaş kapıları, ebeveyn kontrolleri, izleme ve ekran süresi kısıtlamalarına — dayanıyor. Yazarlar bu yaklaşımların belirli bağlamlarda işe yarayabileceğini kabul etmekle birlikte, çocuk korumasını öncelikle "yetişkinler için tasarlanmış sistemlere erişimin kısıtlanması" sorunu olarak çerçevelemenin yanlış olduğunu savunuyor. Çalışma, çocukların güvenlik ihtiyaçlarını merkeze alan, onların bilişsel, duygusal ve gelişimsel kapasitelerine uygun tasarlanmış "çocuk-uyumlu güvenlik" (child-fit security) paradigmasını öneriyor. Bu paradigma, yasağın ve gözetimin yarattığı güven-gizlilik kayıplarını minimize ederken çocukların dijital katılım haklarını korumayı hedefliyor. Özellikle yasak dalgasının küreselleştiği 2026 ortamında, politika yapıcılara yasak-odaklı yaklaşımların ampirik olarak sınanmamış varsayımlarını sorgulatan önemli bir kuramsal müdahale.

**TÜRKİYE BAĞLAMI:**
Türkiye'nin 15 yaş altı sosyal medya düzenlemesi, tam da Ramokapane ve ark.'nın eleştirdiği "erişim kısıtlama" paradigmasına dayanıyor. Yasanın öngördüğü ebeveyn kontrol araçları ve "15 yaşını doldurmuş çocuklara özgü ayrıştırılmış hizmet" hükümleri, çocuk-uyumlu tasarım fikriyle kısmen örtüşse de, uygulamanın çocukların gizlilik ve katılım haklarını nasıl koruyacağı belirsiz. BTK'nın çıkaracağı yönetmeliklerde child-fit security ilkelerinin — çocuklarla birlikte tasarım, veri minimizasyonu, gizlilik varsayılanı — dikkate alınması, yasanın sırf kısıtlayıcı değil gelişimsel olarak da savunulabilir olmasını sağlayabilir. Ayrıca çalışmanın gözetim eleştirisi, Türkiye'de ebeveyn kontrol araçlarının çocuk-ebeveyn güvenini zedelemeyecek şekilde kurgulanması gerektiğine işaret ediyor.

**Priority:** Yüksek | **Action:** both

### 2. From Phreaking to Sneaking: Children's Circumvention of Social Media Age Verification Systems
**Yazarlar:** Bjorn Nansen, Helena Sandberg, Lauren Bliss, Shaanan Cohney
**Tarih:** 2026-05-01 | **Kaynak:** arXiv
**URL:** https://arxiv.org/abs/2605.00368 | **DOI:** 10.48550/arXiv.2605.00368

**ÖZET:**
Avustralya'nın sosyal medya yasağı yürürlükte; platformlar 16 yaş altı kullanıcıların hesap açmasını engellemek için makul adımlar atmakla yükümlü. Bu çalışma, 12-16 yaş arası 15 gençle yürütülen beş odak grubuna dayanarak çocukların yasağın etkililiğini, etkisini ve meşruiyetini nasıl değerlendirdiğini inceliyor. Katılımcılar yasağı büyük ölçüde haksız ve etkisiz buluyor; platform erişim kontrolleriyle karşılaştıkça yasağın nasıl işlediğini, nerede başarısız olduğunu öğreniyor ve aşma yöntemleri geliştiriyorlar (yaş beyanı manipülasyonu, ebeveyn hesapları, alternatif platformlar). Çalışma, yaş doğrulama sistemlerinin tasarımının çocukların "kaçınma öğrenmesini" (circumvention literacy) nasıl tetiklediğini gösteriyor: kısıtlamalar ne kadar görünür ve katıysa, çocuklar o kadar sistematik biçimde zayıf noktaları keşfediyor. Bulgular, yasağın caydırıcılık varsayımını ampirik olarak sorguluyor ve politika yapıcılara teknik + eğitim + destek kombinasyonunu öneriyor.

**TÜRKİYE BAĞLAMI:**
Türkiye'nin yaş doğrulama sistemi henüz yönetmelik aşamasında; Nansen ve ark.'nın Avustralya bulguları, uygulamanın ilk aylarında çocukların aşma davranışlarına hazırlıklı olunması gerektiğini gösteriyor. Özellikle "15 yaşını doldurmuş çocuklara özgü ayrıştırılmış hizmet" modelinin, yaş sınırına takılan 13-14 yaşındaki çocukları ebeveyn hesaplarına ve denetimsiz alternatif platformlara itme riski var. BTK yönetmeliğinin, kaçınma davranışlarını izleyen ve raporlayan bir teknik gösterge seti (örn. yaş beyanı anormallikleri, hesap transfer sinyalleri) içermesi önerilir. Ayrıca okul temelli dijital vatandaşlık eğitiminin, yasağın gerekçelerini çocuklara korkutmadan anlatacak şekilde güncellenmesi, meşruiyet algısını güçlendirebilir.

**Priority:** Yüksek | **Action:** both

### 3. Children's Online Safety Risks and Ethical Considerations in XR Games
**Yazarlar:** Zinan Zhang, Xinning Gui, Yubo Kou
**Tarih:** 2026-04-27 | **Kaynak:** arXiv (cs.HC)
**URL:** https://arxiv.org/abs/2604.24601 | **DOI:** 10.48550/arXiv.2604.24601

**ÖZET:**
Genişletilmiş gerçeklik (XR) teknolojileri çocukların oyun, öğrenme ve sosyalleşme biçimlerini yeniden şekillendiriyor; ancak ciddi güvenlik riskleri de getiriyor. Çalışma, XR oyunlarında çocuklara yönelik güvenlik risklerini ve etik hususları inceliyor: gerçek dünya kazaları (fiziksel çevreyle temas), gerçeklik yargısında zayıflama ve sanal tecavüz gibi rahatsız edici içeriklere maruz kalma. Yazarlar, XR oyun tasarımının çocuk korumasını içerecek şekilde nasıl yeniden düşünülmesi gerektiğini tartışıyor; sürükleyicilik ile güvenlik arasındaki gerilime dikkat çekiyor. Türkiye'de XR oyun pazarı ve okullarda VR uygulamaları hızla yaygınlaşırken, yaş derecelendirme sistemlerinin (yeni oyun platformu düzenlemesi kapsamında) XR içeriklerine uyarlanması için kavramsal çerçeve sunuyor.

**TÜRKİYE BAĞLAMI:**
Yeni Türk düzenlemesi oyun platformlarına derecelendirme ve ebeveyn kontrolü yükümlülüğü getiriyor; ancak XR içeriklerinin kendine özgü riskleri (fiziksel güvenlik, sürükleyici rahatsız edici içerik) mevcut derecelendirme kategorilerinde ayrıca ele alınmıyor. BTK'nın oyun platformu yönetmeliğinde XR/VR içeriklerine özgü yaş ve uyarı etiketlerinin tanımlanması, çalışmanın önerileriyle uyumlu bir adım olacaktır.

**Priority:** Orta-Yüksek | **Action:** kurator_only

### 4. ChildSafeAds Shared Task 2026: Commercial Content in Child-Facing YouTube Videos
**Yazarlar:** Thales Bertaglia, Catalina Goanta, Gerasimos Spanakis, Gunes Acar
**Tarih:** 2026-08-19 | **Kaynak:** arXiv (cs.CY)
**URL:** https://arxiv.org/abs/2608.19165 | **DOI:** 10.48550/arXiv.2608.19165

**ÖZET:**
Çocuklara ulaşması muhtemel YouTube videolarındaki ticari içeriğin tespitine odaklanan ortak görev (shared task). Veri seti 939 kanaldan 3.360 video içeriyor; her örnek SponsorBlock (kitle kaynaklı sponsor segment işaretleyen tarayıcı uzantısı) segmenti, transkript, video/kanal bilgisi ve bağlantılı satış veya hizmet sayfasıyla eşleştiriliyor. Çalışma, çocuklara yönelik içerikte gizli reklam ve ticari istismarın (advertorial, ürün yerleştirme, bağlantılı pazarlama) ölçekte tespitini amaçlıyor. Türkiye'de çocuk YouTube ekosisteminde sponsorlu içerik ve "unboxing" videolarının düzenlenmemiş büyümesi göz önüne alındığında, aldatıcı reklam yasağı hükmünün teknik denetimi için doğrudan uygulanabilir bir yöntem sunuyor.

**TÜRKİYE BAĞLAMI:**
Türkiye'deki yeni düzenleme sosyal ağ sağlayıcılarına "aldatıcı reklamları engelleyici tedbirler" yükümlülüğü getiriyor; ChildSafeAds metodolojisi, çocuklara yönelik YouTube içeriğinde bu tür reklamların otomatik tespiti için somut bir teknik referans. Reklam Kurulu ve BTK'nın denetim kapasitesinin bu tür araçlarla güçlendirilmesi önerilir.

**Priority:** Yüksek | **Action:** kurator_only

### 5. Excessive Screen Time is Associated with Mental Health Problems and ADHD in US Children and Adolescents
**Yazarlar:** Ying Dai, Na Ouyang
**Tarih:** 2025-08-13 | **Kaynak:** arXiv
**URL:** https://arxiv.org/abs/2508.10062 | **DOI:** 10.48550/arXiv.2508.10062

**ÖZET:**
2020-2021 Ulusal Çocuk Sağlığı Araştırması (NSCH) verileriyle 6-17 yaş arası **50.231** ABD'li çocuk ve ergeni analiz eden çalışma, aşırı ekran süresi ile kaygı, depresyon, davranış sorunları ve DEHB arasındaki ilişkiyi; fiziksel aktivite, uyku süresi ve uyku düzeninin bu ilişkideki aracı rolünü inceliyor. Tam etki modelleri (exact natural effect models) ve yapısal eşitlik modellemesiyle fiziksel aktivite ve uykunun paralel aracılık etkilerini ayrıştırıyor. Bulgular, ekran süresi müdahalelerinin yalnızca "süre kısıtlama"ya değil, fiziksel aktivite ve uyku hijyeni gibi aracı davranışlara da odaklanması gerektiğini gösteriyor — okul telefon yasaklarının ruh sağlığı gerekçelerine ampirik destek sağlıyor.

**TÜRKİYE BAĞLAMI:**
Türkiye'de ergen ruh sağlığı ve ekran süresi tartışması yoğunlaşırken, bu çalışmanın aracı değişken bulguları (uyku, fiziksel aktivite) MEB'in okul politikalarına ve ailelere yönelik rehberlik içeriklerine eklenebilir: yasak-odaklı yaklaşımdan ziyade "dengeli dijital yaşam" yaklaşımı. TÜİK çocuk araştırmaları ve yerli kohortlarla Türkiye'ye özgü aracılık analizleri yapılması önerilir.

**Priority:** Orta | **Action:** both

### 6. Reading Between the Signs: Predicting Future Suicidal Ideation from Adolescent Social Media Texts
**Yazarlar:** Paul Blum, Enrico Liscio, Ruixuan Zhang, Caroline Figueroa, Pradeep K. Murukannaiah
**Tarih:** 2025-08-25 | **Kaynak:** arXiv (cs.CY)
**URL:** https://arxiv.org/abs/2509.03530 | **DOI:** 10.48550/arXiv.2509.03530

**ÖZET:**
İntihar, ergen ölümlerinin önde gelen nedenlerinden biri; ancak risk faktörü tabanlı tahmin modelleri şansa yakın performans gösteriyor ve vakaların çoğu ruh sağlığı hizmetleriyle temas olmadan gözden kaçıyor. Çalışma, gençlerin sosyal medya paylaşımlarından gelecekteki intihar düşüncesini tahmin etmeyi deniyor; sosyal medyanın erken uyarı sinyali olarak potansiyelini ve etik sınırlarını tartışıyor. Türkiye'de genç intihar oranlarına ilişkin kaygılar ve platformların kriz müdahale mekanizmalarının (örn. X ve TikTok'un intihar önleme hatları) etkililiği bağlamında, veri-temelli erken uyarı sistemlerinin tasarım ilkeleri için referans niteliğinde.

**TÜRKİYE BAĞLAMI:**
BTK ve platformların kriz içeriklerine müdahale protokolleri geliştirilirken, bu tür tahmin modellerinin yanlış pozitif/negatif riskleri, veri gizliliği ve ergen rızası etik çerçeveleriyle birlikte değerlendirilmeli; Türkiye'de 112/ruh sağlığı hatlarıyla entegrasyon pilotları düşünülebilir.

**Priority:** Orta | **Action:** both

### Okuma Listesi (önceki dönem)
- **Ge Wang, Jun Zhao, Max Van Kleek, Nigel Shadbolt** — "Protection or punishment? relating the design space of parental control apps and perceptions about them" (arXiv 2109.05347, 2021) — ebeveyn kontrol uygulamalarının aşırı kısıtlama ve gözetiminin çocuk-ebeveyn ilişkisini zedeleme riski
- **Darren Cook ve ark.** — "Can We Automate the Analysis of Online Child Sexual Exploitation Discourse?" (arXiv 2209.12320, 2022) — çevrimiçi istismar söyleminin otomatik analizi
- **Vinh-Thong Ta** — "A safety risk assessment framework for children's online safety" (arXiv 2401.14713, 2024) — çocuk çevrimiçi güvenliği risk değerlendirme çerçevesi
- **Jun Zhao** — "Are Children Well-Supported by Their Parents Concerning Online Privacy Risks?" (arXiv 1809.10944, 2018) — ebeveyn desteğinin sınırları

---

## 📰 HABERLER VE RAPORLAR

### 1. GOV.UK — Birleşik Krallık under-16 sosyal medya yasağını duyurdu
**Kaynak:** Department for Science, Innovation & Technology | **Tarih:** 2026-07-17 (güncelleme)
**URL:** https://www.gov.uk/government/publications/fact-sheet-new-rules-to-protect-children-online/fact-sheet-new-rules-to-protect-children-online

UK hükümeti, Mart-Mayıs 2026 ulusal konsültasyonunun ardından (ebeveynlerin %90'ı, gençlerin üçte ikisi under-16 yasağını destekliyor) Avustralya modeliyle under-16 sosyal medya yasağına gideceğini açıkladı. Kapsam: Instagram, YouTube, TikTok, Snapchat, Facebook, X; WhatsApp ve Signal gibi mesajlaşma hizmetleri hariç. 16-17 yaş için sosyal medya serbest ancak canlı yayın ve yabancılarla iletişim özellikleri (oyun dahil) varsayılan olarak kapalı olacak. İlk düzenlemeler yıl sonuna kadar, uygulama Bahar 2027. Yaş kontrolleri mevcut hesap verileri (hesap yaşı 16+ yıl, kredi kartı bağlantısı vb.) üzerinden; ayrıca zorunlu ara ver (mandatory breaks) ve AI chatbot korumaları gündemde. Türkiye bağlamında önemli: UK, mesajlaşma uygulamalarını yasak kapsamı dışında tutarak "iletişim hakkı" ile "riskli özellik" ayrımını netleştiriyor — Türk düzenlemesinin kapsam tanımı için karşılaştırmalı bir model.

### 2. Habertürk/AA — Türkiye: 15 yaş altı sosyal medya düzenlemesi Resmi Gazete'de
**Kaynak:** Habertürk (AA) | **Tarih:** 2026-05-01
**URL:** https://www.haberturk.com/15-yas-altina-sosyal-medya-yasagi-ne-zaman-basliyor-15-yas-alti-sosyal-medya-yasagi-yururluge-girdi-mi-3881647

TBMM Genel Kurulu'nda kabul edilen kanunla (doğum izni paketiyle birlikte) 15 yaş altına sosyal medya yasağı getirildi; temel hükümler yayım tarihinden **6 ay sonra** yürürlüğe girecek (≈ Kasım 2026). Sosyal ağ sağlayıcıları 15 yaşını doldurmamış çocuklara hizmet sunamayacak, yaş doğrulama dahil gerekli tedbirleri alacak; 15 yaşını doldurmuş çocuklar için "ayrıştırılmış hizmet" sunulacak. Ebeveyn kontrol araçları (hesap ayarları, ücretli işlemlerde ebeveyn izni, kullanım süresi izleme/sınırlama) ve aldatıcı reklam yasağı getiriliyor. Yaptırım merdiveni: günlük erişimi 10 milyon üzeri sağlayıcılar kararları en geç 1 saat içinde uygulayacak; 30 gün içinde uyulmazsa BTK reklam yasağı; 3 ay içinde uyulmazsa sulh ceza hakimliği kararıyla **%50 bant genişliği daraltma**. Oyun platformları: derecelendirilmemiş oyunları en yüksek yaş kriterine göre derecelendirerek sunabilecek; günlük 100 bin üzeri erişimli yurt dışı kaynaklı platformlar Türkiye'de temsilci belirleyecek; ihlalde 1-10 milyon TL idari para cezası.

### 3. The Guardian — UK'de çocukların deepfake ihbarlarında rekor artış
**Kaynak:** The Guardian (Dan Milmo) | **Tarih:** 2026-08-08
**URL:** https://www.theguardian.com/technology/2026/aug/08/uk-children-explicit-deepfake-images-ai

Report Remove servisi 2026'nın ilk yarısında çocuklardan kendi görüntülerinin sahte/manipüle müstehcen versiyonlarına ilişkin **420 ihbar** aldı — 2025 toplamını (397) aştı. IWF, 2025-2026'daki manipüle görüntü ihbarlarının çoğunun CSAM eşiğini geçtiğini; bazı mağdurların sextortion (şantaj) hedefi olduğunu bildirdi. "Nudification" araçlarının yaygınlaşması, masum çocuk fotoğraflarından istismar materyali üretimini kolaylaştırıyor. UK'de AI üretimi CSAM zaten suç; hükümet ayrıca bir AI modelinin istismar materyali üretecek şekilde uyarlanmasını ve dağıtımını suç saydı. NSPCC'den Rani Govender: "Teknoloji şirketleri AI ürünlerini, bu materyalin en başta üretilmesini önleyen güçlü korumalar gömmeden piyasaya sürememeli." Türkiye bağlamı: benzer ihbar mekanizması (Report Remove gibi hash tabanlı kaldırma) ve AI-CSAM düzenlemelerinin uygulanabilirliği için doğrudan model.

### 4. Future of Privacy Forum — AB Komisyonu'nun yaş doğrulama yaklaşımı
**Kaynak:** FPF (Bianca-Ioana Marcu, Daniel Hales) | **Tarih:** 2026-05-12
**URL:** https://fpf.org/blog/the-eu-commissions-approach-to-age-verification-mobile-apps-dsa-enforcement-and-challenging-national-social-media-bans/

AB Komisyonu 29 Nisan 2026'da AB genelinde ortak yaş doğrulama teknolojileri için Tavsiye yayımladı; üye devletleri 31 Aralık 2026'ya kadar uygulamaya çağırıyor ve bir "EU age verification blueprint" (kamuya açık teknik şartname) geliştirmeyi hedefliyor. FPF analizi: DSA'nın hiçbir maddesi asgari yaş veya yaş doğrulamayı açıkça zorunlu kılmıyor — gönüllülük/zorunluluk belirsiz; ancak DSA Art. 28 (küçüklerin korunması) ve 2025 tarihli Küçüklerin Korunması Kılavuzları üzerinden yaş güvencesi fiilen bekleniyor. Komisyon ayrıca üye devletlerdeki ulusal sosyal medya yasaklarını DSA çerçevesinde sorguluyor. Bu, "ulusal yasaklar vs. AB ortak çerçevesi" geriliminin 2026'nın ikinci yarısında ana politika çatışması olacağını gösteriyor; Türkiye'nin AB ile uyum tartışmalarında izlemesi gereken bir eksen.

### 5. The New York Times — Meta'nın 17,1 milyar dolarlık anlaşması ve küresel yasak dalgası
**Kaynak:** NYT | **Tarih:** 2026-08-26 / 2026-08-28
**URL:** https://www.nytimes.com/2026/08/26/world/americas/children-social-media-restrictions-global-movement-meta.html

Meta, ABD eyaletleri ve bölgeleriyle, platformlarının çocukları bağımlı kıldığı iddiaları üzerine **17,1 milyar dolara kadar** varan anlaşmayla bir dizi davayı sonlandırdı. NYT, yaklaşık 40 ülkenin çocukların sosyal medya kullanımını sınırlayan yasama süreçlerinde olduğunu; geçen yıl içinde küresel çapta bir dizi yasak ve kısıtlama uygulandığını bildiriyor. Anlaşma, "bağımlılık yapıcı tasarım" iddialarına karşı platformların maliyetini gösteren dönüm noktası niteliğinde — ancak düzenleme dalgasının platform davranışını ne ölçüde değiştireceği belirsiz. Türkiye bağlamı: yerel yaptırım merdiveninin (reklam yasağı, bant daraltma) platformları müzakere masasına oturtma potansiyeli, bu küresel emsal ışığında değerlendirilmeli.

### 6. K-12 Legal Insights — ABD'de okul telefon yasakları 38 eyalete ulaştı
**Kaynak:** K-12 Legal Insights | **Tarih:** 2026-08-06
**URL:** https://www.k-12legalinsights.com/2026/08/screening-screen-time-more-states-are-implementing-cell-phone-bans-in-k-12-schools/

2 Haziran 2026 itibarıyla **38 eyalet ve District of Columbia**, okul bölgelerinin öğrenci cep telefonu kullanımını yasaklamasını veya kısıtlamasını zorunlu kılıyor; Kaliforniya AB 3216 (1 Temmuz 2026 itibarıyla) dahil. Eyalet düzeyindeki bu hızlı yayılım, telefon yasağı tartışmasını pedagojik ve ruh sağlığı gerekçeleriyle kurumsallaştırdı; uygulama kılavuzları, istisnalar (özel gereksinimli öğrenciler, acil iletişim) ve veri toplama boyutlarında çeşitlilik gösteriyor. Türkiye'de MEB'in okul telefon kısıtlamalarının güncellenmesinde, bu eyalet modellerindeki istisna ve değerlendirme mekanizmaları karşılaştırmalı referans olabilir.

### 7. Reuters — Avustralya'dan Avrupa'ya: çocukların sosyal medya erişimini kısıtlama dalgası
**Kaynak:** Reuters | **Tarih:** 2026-08-24
**URL:** https://www.reuters.com/legal/government/australia-europe-countries-move-curb-childrens-social-media-access-2026-08-24/

Avustralya Aralık 2025'te dünyada ilk under-16 sosyal medya yasağını uygulayan ülke oldu (TikTok, YouTube, Instagram, Facebook kapsamda); ardından Avrupa devletleri ve Endonezya, Vietnam, Brezilya gibi ülkeler benzer düzenlemeleri gündemine aldı. 2026 ortası itibarıyla 15'ten fazla ülke bağlayıcı yasak yasası çıkardı veya sürece soktu. Dalganın ortak özelliği, ispat yükünün platform mimarisine kaydırılması (yaş doğrulama, tasarım gereği güvenlik). Türkiye bu dalganın içinde konumlanıyor; uygulama sonuçlarının (Avustralya deneyimi) izlenmesi, Türk düzenlemesinin ince ayarı için kritik.

---

## 🔍 KARŞILAŞTIRMALI ANALİZ

| Ülke/Bölge | Yaklaşım | Kapsam | Yaş Doğrulama | Yaptırım | Türkiye İçin Ders |
|-----------|----------|--------|---------------|----------|-------------------|
| 🇦🇺 Avustralya | Kanuni yasak (dünyada ilk) | Under-16; TikTok, YouTube, Instagram, Facebook, X | Platformlar "makul adımlar" | Hesap engeli; para cezaları | Uygulanabilirlik: çocuklar sistemi aşmayı öğreniyor (Nansen 2026) |
| 🇬🇧 Birleşik Krallık | Kanuni yasak + özellik kısıtlaması | Under-16 yasak; 16-17'de canlı yayın/yabancı iletişim kapalı; mesajlaşma hariç | Mevcut hesap verileri, kademeli | Bahar 2027 uygulama; AI chatbot korumaları | "İletişim hakkı" ile "riskli özellik" ayrımı — kapsam tasarımı modeli |
| 🇪🇺 AB | Ortak çerçeve (DSA Art. 28) | Küçükler için yüksek gizlilik/güvenlik standardı | Tavsiye + blueprint; 31 Ara 2026 hedefi; gönüllülük muğlak | DSA uygulamaları; ulusal yasaklara itiraz | Ulusal yasaklar ile AB ortak çerçevesi gerilimi — uyum izleme |
| 🇹🇷 Türkiye | Kanuni yasak + platform yükümlülüğü | Under-15 yasak; 15+ ayrıştırılmış hizmet; oyun platformları | Sosyal ağ sağlayıcı yükümlülüğü | 1 saat uygulama, reklam yasağı, %50 bant daraltma, 1-10M TL ceza | Yaptırım merdiveni en sertlerden; uygulama takvimi Kasım 2026 |
| 🇺🇸 ABD (eyaletler) | Okul odaklı + eyalet yasaları | Okul telefon yasakları (38 eyalet); CA AB 3216 | Değişken | Okul politikaları; Meta 17,1 milyar $ anlaşması | Okul politikalarında istisna ve veri toplama mekanizmaları |

**Sentez:** Küresel eğilim, saf "yasak"tan "yaş doğrulama + özellik kısıtlaması + tasarım gereği güvenlik" kombinasyonuna kayıyor. Türkiye'nin yaptırım merdiveni caydırıcılık açısından güçlü; ancak akademik kanıt (Nansen, Ramokapane) yasakların çocukların katılım hakları ve aşma davranışları nedeniyle tek başına yetersiz kalacağını gösteriyor. En güçlü model, UK'nin yaptığı gibi iletişim haklarını koruyup riskli özellikleri hedefleyen kademeli tasarım + güçlü ebeveyn desteği + okul politikaları bütünüdür.

---

## 💡 ÖNERİLER

### Acil (0-3 ay)
1. **BTK yaş doğrulama yönetmeliği taslağına child-fit security ilkelerinin eklenmesi** — Ramokapane ve ark.'nın önerdiği çocuklarla birlikte tasarım, veri minimizasyonu ve gizlilik varsayılanı ilkeleri; ayrıca Nansen bulgularına göre kaçınma davranışı izleme göstergeleri.
2. **Deepfake/CSEA ihbar mekanizması** — Report Remove modelinde hash tabanlı kaldırma + çocuk dostu ihbar formu (deepfake işaretleme kutusu dahil) için BTK/Adalet Bakanlığı pilotu.
3. **Okul telefon politikası güncellemesi** — MEB'in mevcut kısıtlamalarının ABD'nin 38 eyalet modeline göre istisna mekanizmalarıyla (özel gereksinim, acil iletişim) gözden geçirilmesi.

### Kısa Vadeli (3-6 ay)
1. **AI ürünlerinde tasarım gereği güvenlik** — NSPCC çağrısı doğrultusunda, çocuklara yönelik AI ürünlerinde istismar materyali üretimini engelleyen korumaların zorunlu kılınması (UK örneği: model uyarlamayı suç sayma).
2. **Çocuklara yönelik YouTube içeriğinde gizli reklam denetimi** — ChildSafeAds metodolojisinin Reklam Kurulu/BTK denetiminde pilot kullanımı; aldatıcı reklam hükmünün teknik uygulaması.
3. **Ebeveyn kontrol araçlarının güven temelli tasarımı** — Wang ve ark.'nın "koruma mı ceza mı" bulguları ışığında, kontrol araçlarının çocuk-ebeveyn ilişkisini zedelemeyen biçimde kurgulanması için sivil toplumla ortak çalışma.

### Orta Vadeli (6-12 ay)
1. **AB yaş doğrulama çerçevesiyle uyum izleme** — Komisyon'un 31 Aralık 2026 hedefi ve blueprint şartnamesinin Türk uygulamasına teknik yansımaları için düzenli izleme; ulusal yasaklar-AB çerçevesi geriliminin takibi.
2. **Çocuk-uyumlu ayrıştırılmış hizmet standardı** — 15+ çocuklara özgü hizmetin (yaş-uygun tasarım, reklamsız/az reklamlı mod) içerik ve gizlilik standartlarının BTK ile birlikte tanımlanması.
3. **Türkiye'ye özgü ekran süresi-ruh sağlığı kohort çalışması** — Dai & Ouyang'ın aracı değişken modelinin (uyku, fiziksel aktivite) Türkiye verisiyle çalışılması; politika kararlarına yerel kanıt.

---

## 📊 İSTATİSTİKLER & TABLOLAR

| # | İstatistik | Kaynak | Tarih |
|---|-----------|--------|-------|
| 1 | UK'de çocuk deepfake ihbarları: 420 (H1 2026) — 2025 toplamını (397) aştı | IWF / Report Remove (Guardian) | 2026-08-08 |
| 2 | UK ebeveynlerin %90'ı under-16 sosyal medya yasağını destekliyor | GOV.UK konsültasyon | 2026-07-17 |
| 3 | ABD'de okul telefon yasağı/kısıtlaması zorunlu kılan eyalet: 38 + DC | K-12 Legal Insights | 2026-08-06 |
| 4 | Bağlayıcı sosyal medya yasağı çıkaran/sürece sokan ülke: 15+ (2026 ortası) | Rebirth Distribution / Reuters | 2026-08-24 |
| 5 | Meta'nın ABD eyaletleriyle anlaşması: 17,1 milyar $ | NYT | 2026-08-26 |
| 6 | AB üye devletleri için ortak yaş doğrulama uygulama hedefi: 31 Aralık 2026 | AB Komisyonu (FPF) | 2026-05-12 |
| 7 | Ekran süresi-DEHB/ruh sağlığı çalışması örneklemi: 50.231 çocuk (NSCH) | Dai & Ouyang (arXiv 2508.10062) | 2025-08-13 |
| 8 | Türkiye 15 yaş altı düzenlemesi yürürlük: yayımdan 6 ay sonra (≈ Kasım 2026) | Habertürk/AA | 2026-05-01 |

---

## 📖 KAYNAKÇA

### Akademik Kaynaklar
1. Ramokapane, K.M., Huan, R., Dkaidek, Z. & Rashid, A. (2026). Children Are Not the Enemy: Child-Fit Security as an Alternative to Bans and Surveillance. arXiv:2606.17957. https://arxiv.org/abs/2606.17957 ✅
2. Nansen, B., Sandberg, H., Bliss, L. & Cohney, S. (2026). From Phreaking to Sneaking: Children's Circumvention of Social Media Age Verification Systems. arXiv:2605.00368. https://arxiv.org/abs/2605.00368 ✅
3. Zhang, Z., Gui, X. & Kou, Y. (2026). Children's Online Safety Risks and Ethical Considerations in XR Games. arXiv:2604.24601. https://arxiv.org/abs/2604.24601 ✅
4. Bertaglia, T., Goanta, C., Spanakis, G. & Acar, G. (2026). ChildSafeAds Shared Task 2026: Commercial Content in Child-Facing YouTube Videos. arXiv:2608.19165. https://arxiv.org/abs/2608.19165 ✅
5. Dai, Y. & Ouyang, N. (2025). Excessive Screen Time is Associated with Mental Health Problems and ADHD in US Children and Adolescents. arXiv:2508.10062. https://arxiv.org/abs/2508.10062 ✅
6. Blum, P., Liscio, E., Zhang, R., Figueroa, C. & Murukannaiah, P.K. (2025). Reading Between the Signs: Predicting Future Suicidal Ideation from Adolescent Social Media Texts. arXiv:2509.03530. https://arxiv.org/abs/2509.03530 ✅
7. Chu, M.D. ve ark. (2025). BigTokDetect: A Clinically-Informed Vision-Language Modeling Framework for Detecting Pro-Bigorexia Videos on TikTok. arXiv:2508.06515. https://arxiv.org/abs/2508.06515 ✅

### Haberler ve Raporlar
1. GOV.UK (2026-07-17). Fact sheet: New rules to protect children online. https://www.gov.uk/government/publications/fact-sheet-new-rules-to-protect-children-online/fact-sheet-new-rules-to-protect-children-online ✅ (urllib erişimi)
2. Habertürk/AA (2026-05-01). 15 yaş altına sosyal medya yasağı ne zaman başlıyor? https://www.haberturk.com/15-yas-altina-sosyal-medya-yasagi-ne-zaman-basliyor-15-yas-alti-sosyal-medya-yasagi-yururluge-girdi-mi-3881647 ✅
3. The Guardian (2026-08-08). Rising number of UK children report seeing explicit deepfakes. https://www.theguardian.com/technology/2026/aug/08/uk-children-explicit-deepfake-images-ai ✅
4. Future of Privacy Forum (2026-05-12). The EU Commission's Approach to Age Verification. https://fpf.org/blog/the-eu-commissions-approach-to-age-verification-mobile-apps-dsa-enforcement-and-challenging-national-social-media-bans/ ✅
5. TechPolicy.Press (2025-09-26). What Europe's Digital Services Act Says About Age Assurance. https://www.techpolicy.press/what-europes-digital-services-act-says-about-age-assurance/ ✅
6. The New York Times (2026-08-26/28). A Movement to Restrict Social Media for Children Has Taken Hold Globally; Why Countries Are Pushing Social Media Bans. https://www.nytimes.com/2026/08/26/world/americas/children-social-media-restrictions-global-movement-meta.html ⚠️ (erişim engeli, başlık/meta verisi)
7. Reuters (2026-08-24). From Australia to Europe, countries move to curb children's social media access. https://www.reuters.com/legal/government/australia-europe-countries-move-curb-childrens-social-media-access-2026-08-24/ ⚠️ (erişim engeli, başlık/meta verisi)
8. K-12 Legal Insights (2026-08-06). Screening Screen Time: More States are Implementing Cell Phone Bans in K-12 Schools. https://www.k-12legalinsights.com/2026/08/screening-screen-time-more-states-are-implementing-cell-phone-bans-in-k-12-schools/ ⚠️ (403, başlık/meta verisi)
9. NCSL (2026-04-07). Social Media and Children 2026 Legislation. https://www.ncsl.org/technology-and-communication/social-media-and-children-2026-legislation ⚠️ (403, başlık/meta verisi)

### Türkiye Kaynakları
1. Habertürk/AA (2026-05-01). 15 yaş altına sosyal medya yasağı (Resmi Gazete duyurusu, TBMM Genel Kurul). https://www.haberturk.com/15-yas-altina-sosyal-medya-yasagi-ne-zaman-basliyor-15-yas-alti-sosyal-medya-yasagi-yururluge-girdi-mi-3881647 ✅
2. CGTN Türk (2026-04-22). TBMM'den Geçti: 15 Yaş Altına Sosyal Medya Yasağı Geldi. https://www.cgtnturk.com/tbmmden-gecti-15-yas-altina-sosyal-medya-yasagi-geldi ⚠️ (başlık/meta verisi)

---

## 🔗 KAYNAKLAR

### Platformlar
- arXiv (api): çocuk güvenliği, CS.CY/CS.HC/CS.CR kategorileri — haftalık tarama
- GOV.UK Online Safety: https://www.gov.uk/society-and-culture/online-safety
- AB Dijital Strateji: https://digital-strategy.ec.europa.eu
- Future of Privacy Forum Blog: https://fpf.org/blog/
- NCSL Teknoloji ve İletişim: https://www.ncsl.org/technology-and-communication
- IWF Report Remove: https://reportremove.org.uk

### Gelecek Hafta İzlenecek Konular
- Türkiye BTK yaş doğrulama yönetmeliği taslağının yayımlanması (yürürlük Kasım 2026 öncesi)
- AB Komisyonu age verification blueprint şartnamesinin teknik detayları
- UK under-16 yasak düzenlemelerinin (Regulations) yıl sonu taslağı
- Meta-ABD eyaletleri 17,1 milyar $ anlaşmasının uygulama takvimi
- Avustralya yasağının 1. yıl değerlendirme raporları
- Report Remove 2026 yıl sonu istatistikleri (deepfake ihbarları)

---

## 📝 SÖZLÜK

- **Yaş doğrulama (age verification):** Kullanıcının yaşını kimlik, kredi kartı veya dijital kimlik cüzdanı gibi araçlarla doğrulama; AB'de 31 Aralık 2026 hedefiyle ortak çerçeve oluşturuluyor.
- **Yaş güvencesi (age assurance):** Yaş doğrulamayı da içeren daha geniş yöntem yelpazesi (tahmin, beyan, davranışsal sinyaller); DSA Art. 28 bağlamında platformlardan beklenen standart.
- **Child-fit security (çocuk-uyumlu güvenlik):** Ramokapane ve ark.'nın önerdiği; yasak ve gözetim yerine çocukların gelişimsel ihtiyaçlarına göre tasarlanmış güvenlik yaklaşımı.
- **Ayrıştırılmış hizmet:** Türk düzenlemesinde 15 yaşını doldurmuş çocuklara sunulacak, yaş-gelişim uyumlu ayrı hizmet.
- **Report Remove:** IWF/NSPCC'nin çocukların mahrem görüntülerini anonim ihbar edip hash (dijital parmak izi) ile platformlardan kaldırtma servisi.
- **CSAM (Child Sexual Abuse Material):** Çocuğun cinsel istismarını gösteren materyal; UK'de AI üretimi CSAM ve model uyarlama suç sayılıyor.
- **Sextortion:** Mahrem görüntüleri yayınlama tehdidiyle şantaj; deepfake vakalarında artış görülüyor.
- **DSA Art. 28:** Dijital Hizmetler Yasası'nın küçüklere yüksek gizlilik, güvenlik ve emniyet sağlama yükümlülüğü maddesi.
- **Bant genişliği daraltma:** Türk düzenlemesinde yükümlülüklerini yerine getirmeyen platformlara sulh ceza hakimliği kararıyla uygulanabilecek %50 trafik daraltma yaptırımı.

---

*Kaynak erişim notu: ✅ = doğrudan içerik çekildi; ⚠️ = bot koruması/erişim engeli nedeniyle başlık ve arama meta verisi esas alındı. Telegram link akışı 29-31 Ağustos'ta boş olduğundan derleme doğrudan kaynak taramasıyla üretilmiştir.*

---

## 🔗 İlgili Bağlantılar
### 🧠 İlgili Kavramlar
- [[concepts/ai-generated-disinformation.md|AI-Generated Disinformation (Yapay Zeka Dezenformasyonu)]]
- [[concepts/cocuk-dijital-katilim.md|Çocukların Dijital Katılımı]]
- [[concepts/cocuk-dijital-kisitlamalar.md|Çocuklar için Dijital Kısıtlamalar]]
- [[concepts/cocuk-istismari.md|cocuk-istismari]]
- [[concepts/cocuk-veri-gizliligi.md|Çocuk Veri Gizliliği]]
- [[concepts/dijital-vatandaslik.md|Dijital Vatandaşlık]]
- [[concepts/ekran-suresi.md|Ekran Süresi]]
- [[concepts/sosyal-medya-genclik.md|Sosyal Medya ve Gençlik]]
- [[concepts/sosyal-medya-yasagi-tartismasi.md|Sosyal Medya Yasağı Tartışması]]
- [[concepts/yapay-zeka-cocuklar.md|Yapay Zeka ve Çocuklar]]
- [[concepts/yas-dogrulama.md|Yaş Doğrulama Teknolojileri]]
### 🏛 İlgili Kurum/Kişiler
- [[entities/arxiv-org.md|arXiv]]
- [[entities/guardian.md|Guardian]]
- [[entities/new-york-times.md|New York Times]]
- [[entities/www-reuters-com.md|Reuters]]
- [[entities/www-theguardian-com.md|The Guardian]]
