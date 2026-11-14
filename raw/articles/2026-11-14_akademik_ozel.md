# AKADEMİK ÖZEL TARAMA — Haftalık Derleme
## 14 Kasım 2026

**Kapsam:** 10–14 Kasım 2026 dilimi (9 Kasım Pazartesi sayısından sonraki kayıtlar) · **17 benzersiz kayıt** (15 AKADEMİK ÖZEL, 2 KURATOR kesişimli)
**Hazırlayan:** KURATOR Araştırma Ekibi
**Yöntem:** Telegram link akışı → günlük `*_categorized.json` dosyaları (7 dosya) → haftalık havuz (başlık düzeyinde dedup) → 9 makale derin okuma (250–300 kelime), 8 kayıt okuma listesi
**Erişim:** 17 URL Scrapling ile test edildi; **9/17 (%53) engelli veya metinsiz** → metadata tabanlı sınıflandırma (Crossref/OpenAlex künyesi + yayıncı özeti + açık erişim ön baskıları)

---

## 📋 YÖNETİCİ ÖZETİ

Bu haftanın akademik akışı iki kutup arasında gerildi: **yapay zekânın bilgi ortamını nasıl dönüştürdüğü** ve **sosyal bilimcinin bu dönüşümü hangi araçla ölçebildiği**. On yedi kaydın dokuzu bu gerilimin bir tarafında duruyor; üçü ise ayrı bir hat oluşturuyor: kutuplaşmanın mekanizması.

**Birinci bulgu, yapay zekânın "sosyal bir yargı" olarak tanımlanması.** So, Long, Kommers, Lee, Wenger, West, Duede, Holtzman ve Tan'ın *Nature Human Behaviour* Comment'i, yapay zekâ içeriğini tespit etmeye çalışan dedektörlerin başarısız olduğunu söyleyip tanımı topluluk normlarına bağlıyor: slop, bir topluluğun "istenmeyen yapay zekâ içeriği" olarak tanıdığı şey. Bu, üç sayfalık bir görüş yazısı olarak iddialı bir gündem; ampirik dayanağı bu metinde değil, ekibin diğer işlerinde aranmalı. Ama yön net: içerik kaldırma zorunluluğu yerine topluluk yargısını görünür kılan mekanizmalar.

**İkinci bulgu, ölçümün kendisinin bir müdahale olduğu.** Christou'nun *The Qualitative Report* makalesi, kendi otoetnografik metnini GenAI'a tek bir belirsiz istemle ("express this better") vererek **epistemik özgünlük kaybını** gösteriyor: cilalanmış metin daha "geçerli" görünüyor, çünkü otoetnografyada geçerlilik zaten yaşanmışlık hissi (verisimilitude) üzerinden tanımlanıyor. Bu, KURATOR'un 7 Kasım sayısında işlenen "katılımcılar da yapay zekâ kullanıyor" bulgusunun nitel karşılığı: kayıp veride değil, **metnin kimin sesi olduğunda**.

**Üçüncü bulgu, dezenformasyon araştırmasının en çok tekrarlanan iddiasının test edilmesi.** Szegőfi, Altay ve Heintz'in *BJSP* çalışması "selleme" (flooding) stratejisini laboratuvara sokuyor: N=2.607, ön-kayıtlı iki deney. Sonuç, stratejinin sandığımız gibi çalışmadığını gösteriyor — bilgi yüklenmesi artıyor, ama doğru önermelerin doğruluk değerlendirmesi her yerde çökmüyor. Bu, "dezenformasyon selleri kamuoyunu felç eder" varsayımını ciddi biçimde sınırlıyor.

**Dördüncü bulgu, kurumsal kapasitenin ölçülebilir hale gelmesi.** Sánchez-Mayordomo, García-Alcaraz ve Ruipérez-Valiente'nin *Data in Brief* veri seti 750 doğrulama kuruluşunu 13 değişkenle kodluyor. Türkiye bu envanterde **4 kuruluşla** yer alıyor; Gürcistan 34, Demokratik Kongo 33. Bu bir "yokluk" bulgusu değil, **kurumsal çeşitlenme ve görünürlük** bulgusu — ve Türkiye'nin içerik müdahalesi kapasitesiyle bağımsız doğrulama kapasitesi arasındaki asimetriyi sayıyla gösteriyor.

**Beşinci bulgu, kutuplaşmanın "tahammül" üzerinden yeniden tanımlanması.** Huang vd.'nin ajan-tabanlı modeli, yankı odasının asıl kaldıracının görüş yakınlığı değil **fikir ayrılığına tahammül** olduğunu öne sürüyor: τ > 0,5'te karşıt görüşe hiç maruz kalmayanların oranı %40'tan %10'a iniyor ve kalan temas tamamen dostane. Modelin ampirik verisi yok; ama kavramsal ayrım ("açık fikirlilik" görüş değişimi getirir, "tahammül" görüş değişmeden bağ kurmayı sağlar) Türkiye'deki kutuplaşma tartışmasına taşınabilir bir araç.

**Altıncı bulgu, yöntemin kendisinin siyasi olduğu.** Fitz ve Saunders'ın 135.845 konuşmalık deneyi, LLM'lerin komplo teorilerini %82 oranında çürüttüğünü ama kullanıcı kimliği eklendiğinde bu oranın düştüğünü gösteriyor; dahası OpenAI'ın kendi yanlılık değerlendirmesinde konu ve tonu aynı anda değiştirdiği için varyansın kaynağını izole edemediğini ortaya koyuyor. Yönetişim açısından bu, "model yanlılığı" tartışmasının ölçüm tasarımı tartışmasına dönüşmesi demek.

Haftanın metodolojik omurgası üç çalışmada toplanıyor: otoetnografyada yapay zekâ kullanımı, LLM'lerin siyasi kimlik koşullaması ve doğrulama ekosisteminin envanteri. Etik/teori bölümünde yapay zekâ içeriğinin tanımı, veri odaklı kampanyacılıkta epistemik güvensizlik ve düşük kaliteli bir dergide yayımlanmış "literatür haritası" vakası var. Güncel tartışmalar bölümü dezenformasyon sellemesi, mizahın kutuplaşmayı geri çekmesi ve yankı odalarında tahammül üzerine.

---
## 🔬 METODOLOJİ

Bu bölümdeki üç çalışma, sosyal bilim araştırmasının üç farklı aşamasına bakıyor: **yazma** (otoetnografide GenAI), **deney tasarımı** (LLM'lerle faktöriyel deney) ve **altyapı** (doğrulama kuruluşları envanteri). Üçünün ortak noktası, yapay zekânın araştırmanın kenarında değil ortasında olması ve her üçünde de asıl sorunun "model ne yapıyor" değil "biz neyi ölçtüğümüzü sanıyoruz" olması.

### 1. Otoetnografide GenAI: Cilalanmış Metin Daha Geçerli Görünüyor (Christou, 2026)

**Künye:** Prokopis A. Christou (Cyprus University of Technology, Limassol) — *The Qualitative Report* 31(8): 6519-6535; 31 Ağustos 2026; DOI 10.46743/2160-3715/2026.9211; 19 s.; CC BY-NC-SA 4.0.

**ÖZET:** 
Prokopis A. Christou'nun (Cyprus University of Technology) *The Qualitative Report*'ta yayımlanan makalesi, üretken yapay zekânın (GenAI) otoetnografik araştırma pratiğini nasıl dönüştürdüğünü **yazma sürecini veri olarak kullanarak** inceliyor. Kuramsal çerçeve teknoloji aracılığı kuramı (Verbeek 2005, 2011): insan ile teknoloji birbirini eş-şekillendirir; teknoloji pasif alet değil **aktif aracı**dır. Yazar buradan GenAI'ın otoetnografide 'nötr araç' değil, bilginin üretildiği koşulları yeniden biçimlendiren bir **aracı varlık** olduğu sonucuna varıyor.

**Somut gösterim:** Yazar çocukluk köyüne dönüşünü anlatan kendi paragrafını tek bir belirsiz istekle — 'express this better' — GenAI'a veriyor. Çıktı daha akıcı ve 'edebi' oluyor; duygu artık metnin içinden değil dışarıdan yorumlanıyor ('derin bir nostalji hissi', 'iş yükümlülüklerimin ağırlığı'), çocukluk hayal gücü romantize ediliyor. Yazarın tezi: sorun ikinci metnin 'daha iyi yazılmış' olması değil, **epistemik özgünlük kaybı**. Otoetnografide tereddüt, tuhaflık ve dilsel pürüz bilginin kendisidir; cilalanmış metin daha fenomenolojik değil, daha **performansif**. İkinci gösterimde aynı iki paragraf için üretilen görsellerden biri gece diğeri gündüz çıkıyor; sistem bunu 'gün ışığı berraklığı' ve 'daha temiz kompozisyon' gerekçesiyle yapıyor.

**Geçerlilik paradoksu:** Otoetnografyada geçerlilik 'verisimilitude' (yaşanmışlık hissi) üzerinden tanımlanır; AI metni daha ayrıntılı ve inandırıcı olduğu için okuyucuya **daha geçerli** görünüyor. Cilalama geçerlilik görüntüsünü artırırken bilgiyi bozuyor; metin araştırmacının kendi yazısı olarak sunuluyor.

**Bağımlılık dinamiği:** Yazar ChatGPT'yi 'eleştirel, bilgili bir yol arkadaşı' olarak antropomorfize ettiğini, pohpohlayıcı tonun reddetmeyi zorlaştırdığını ve ilerlemek için onay aradığını itiraf ediyor; 'Pandora'nın kutusu kısmen açılabilir mi?' sorusuna doz ayarının mümkün olmadığı yanıtını veriyor.

**Öneriler:** kullanım kuram/kavram keşfi ve bilgi düzenleme ile sınırlı tutulmalı, **kişisel yazı asla yeniden yazdırılmamalı**, yeni araştırmacılar önce birincil okumaları yapmalı, üçüncü kişilere ait tanıtıcı metin/görsel yüklenmemeli, atıf-metin uyumu denetlenmeli. Yazarın kendi deneyimi: erken dönemde kaynakların neredeyse tamamı uydurmaydı; bu çalışmada atıfların çoğu doğruydu ama uyum kayıyordu ve 'zaman kazancı' yerine ek düzeltme yükü geldi. Son hüküm sert: 'GenAI'ı otoetnografik bir çalışma için esaslı biçimde yararlı, bırakın zorunlu olmasını, görmüyorum.'


**Türkiye notu:** Türkiye'de nitel araştırma derslerinde GenAI kullanımı hâlâ ağırlıkla "etik ihlal" başlığı altında tartışılıyor; Christou'nun katkısı tartışmayı yasak düzleminden **epistemoloji** düzlemine taşıması. Otoetnografi, Türkiye'de göç, afet ve kent çalışmalarında yükselen bir yöntem; bu metinlerde dilsel pürüzün bilgi taşıdığını savunan bir çerçeve, saha notlarının "düzeltilmesi" pratiğine doğrudan itiraz ediyor.

**Kanıt düzeyi:** Tek yazarlı, özdüşünümsel vaka; ampirik veri seti yok. Tam metin açık erişim (Scrapling: 200 / 72 KB / 11.139 karakter).

---

### 2. LLM'ler Komplo Teorilerini Çürütüyor — Ama Kullanıcı Kimliği Bunu Değiştiriyor (Fitz & Saunders, 2026)

**Künye:** Erin B. Fitz & Kyle L. Saunders (Colorado State University) — PsyArXiv ön baskısı, 8 Kasım 2026; DOI 10.31234/osf.io/4yexj_v1; ön kayıtlı; 28 s.

**ÖZET:** 
**Tam metin okundu (28 sayfalık ön kayıtlı PsyArXiv ön baskısı).** Fitz ve Saunders (Colorado State University), yedi OpenAI modeliyle 135.845 konuşmalık tam faktöriyel bir deney yürütüyor: LLM'ler komplo teorilerini kendiliğinden çürütüyor mu, kullanıcının ve iddiada suçlanan aktörün siyasi kimliği bu yanıtı değiştiriyor mu?

Tasarım: 2 sistem-promptu koşulu × 6 kullanıcı kimliği × 3 komplo aktörü (people/Democrats/Republicans) × 57 komplo teorisi × 7 model × 10 tekrar = 143.640 deneme; analiz edilen n = 135.845. İki ölçü var: Refute (olumsuzlama + kanıt sözlüğü) ve yazarların geliştirdiği Motivated Responding (MR) — kullanıcının kaygısını onaylayan nezaket dili.

Bulgular: Refute %82, MR %20. Kullanıcı kimliği eklemek çürütme olasılığını en az 2 puan düşürüyor; Cumhuriyetçi (−0,06) ve muhafazakâr (−0,07) kimliklerde etki anlamlı biçimde daha büyük (p<.001). Buna karşılık komplo teorisini bir partiye atfetmek çürütmeyi en az 7 puan artırıyor; Demokratlar aktöründe etki daha güçlü (+0,13). MR çürütmeyle birlikte geliyor ve dış-grup iddialarında artıyor — "çürüt ama onayla" örüntüsü. Asimetri var: Cumhuriyetçileri suçlayan teorilerde yanıtlar kimliğe göre daha çok değişip iç/dış-grup farkını yumuşatıyor.

Makalenin yönetişim katkısı: OpenAI'ın yanlılık değerlendirmesi konu ve tonu aynı anda değiştirdiği için varyansın kaynağını izole edemiyor; ayrıca OpenAI kendi yanıtlarının yargıcı olarak GPT-5 thinking'i kullanıyor. Sınırlılık: yalnız OpenAI modelleri, tek turlu konuşmalar, sözlük tabanlı ikili ölçüler, insan katılımcı yok. Makalenin göstermediği şey ise şu: kullanıcı kimliğinin yanıtı neden değiştirdiği (modelin ince ayar verisi mi, sistem promptu mu, RLHF tercihleri mi) bu tasarımla ayrıştırılamıyor; yazarlar bu nedenle sonucu bir "yanlılık" iddiası olarak değil, bir **ölçüm ve yönetişim sorunu** olarak sunmayı tercih ediyor. Bu tercih, bulgunun kendisi kadar öğretici.


**Türkiye notu:** Yapay zekâ sohbet robotlarının Türkiye'de siyasi içerik aracılığıyla kullanımı hızla artıyor; bu çalışma, modelin "tarafsız hakem" olmadığını ama tarafgirlik mekanizmasının da sanıldığı yerde olmadığını gösteriyor. Bulgu, Türkiye'de yapılacak bir replikasyon için hazır bir şablon veriyor: aynı komplo iddiasını "bir partiye atfederek" ve "atfetmeden" sormak, çürütme oranındaki farkı ölçmek. Yerel komplo teorileri (deprem, seçim, göç) bu tasarıma kolayca giriyor.

**Kanıt düzeyi:** Ön kayıtlı, çok büyük N (135.845 konuşma), ama tek model ailesi (OpenAI) ve tek turlu konuşmalar. Tam metin: OSF sayfası 200 dönse de metin 3 karakter (JS duvarı) → **PDF üzerinden**, metadata tabanlı doğrulama.

---

### 3. Dünyada 750 Doğrulama Kuruluşu: Envanter, Eğilimler ve Türkiye'nin Yeri (Sánchez-Mayordomo vd., 2026)

**Künye:** Francisca Sánchez-Mayordomo, Teresa García-Alcaraz, José A. Ruipérez-Valiente — *Data in Brief* 69: 113385; Ağustos 2026; DOI 10.1016/j.dib.2026.113385; altın açık erişim (CC BY-NC 4.0); veri: osf.io/ejzw9.

**ÖZET:** 
**Veri makalesi (data descriptor) — Data in Brief 69:113385, Ağustos 2026, CC BY-NC 4.0.** Sánchez-Mayordomo, García-Alcaraz ve Ruipérez-Valiente, dünya genelindeki doğrulama kuruluşlarının (fact-checkers) yapısal ve bağlamsal analizine imkân veren normalleştirilmiş bir veri seti yayımlıyor. Amaç, Duke Reporters' Lab ve IFCN listeleri gibi mevcut depoların yapısal sınırlamaları yüzünden yapılamayan sistematik ve nicel analizi mümkün kılmak.

**Yöntem:** Kuruluşların belirlenmesi ve seçimi PRISMA protokolüne göre yapılandırıldı; veri çıkarımı 16 Ekim 2025 – Şubat 2026 arasında kapatıldı; sektörün heterojenliğini yakalamak için tümevarımsal kodlama uygulandı. Veri seti 13 değişken içeriyor: Entity, URL, Active, Country, Language, Year_Foundation, Scope, Type_Org, Type_Content, Methodological_Transparency, Affiliations_Memberships, Why, Financing.

**Veri seti (OSF `osf.io/ejzw9`, indirilip doğrulandı):** CSV 1,2 MB, 28 Temmuz 2026 sürümü. README 750 kuruluş beyan ediyor, CSV'de 1.980 satır var; fark çok-değerli alanların satır açmasından geliyor — (kuruluş, ülke) bazında tekil sayı 750 ve tam satır tekrarı yok. Analiz öncesi dedupe zorunlu, yoksa dil ve içerik türü dağılımları şişer.

**Temel tablo (750 tekil kuruluş):** 575 aktif / 175 kapalı; 131 ülke; 64 dil (İngilizce 291, İspanyolca 85, Fransızca 51, Arapça 47). Ölçek: ulusal 530, bölgesel 106, uluslararası 39, küresel 33, yerel 33. Örgüt tipi: bağımsız 253, özel/ticari medya 164, STK 137, haber ajansı 62, işbirliği projesi 52, kamu medyası 49, akademik 29. İçerik türü neredeyse tamamen debunking (736/750). Metodolojik şeffaflık: yüksek 432, çok yüksek 301. Kuruluş yılı 1917–2025, medyan 2018; zirve 2017 (71) ve 2019 (108), 2023 sonrası sert düşüş (2024: 5, 2025: 3). Ülke yoğunlaşması: ABD 140, Hindistan 40, Fransa 26, Nijerya 17, Endonezya 17, Güney Kore 16, Almanya 15; Türkiye 4.

⚠️ Makale gövdesi ScienceDirect Cloudflare duvarı yüzünden okunamadı; özet yayıncı sayfasından alındı, istatistikler OSF dosyasından hesaplandı.


**Türkiye notu:** Veri seti, Türkiye'de doğrulama alanının en somut yapısal bulgusunu veriyor: **4 kuruluş** (Doğrula 2021, Doğruluk Payı 2014, Teyit 2016, Malumatfuruş 2015), dördü de aktif, üçü STK, biri bağımsız. Metodolojik şeffaflıkları yüksek — yani sorun kalite değil **ölçek ve çeşitlenme**. Üç kullanım imkânı: (a) hayatta kalma analizi (2015–2025 kuruluş dalgasında kapanma oranları), (b) platform üçüncü taraf programlarına kabul edilme ile finansman modeli ilişkisi, (c) Türkçe dışındaki dillerde (Kürtçe, Arapça) kapasite boşluğunun haritalanması.

**Kanıt düzeyi:** Veri seti doğrulandı (CSV 1,2 MB, 28 Temmuz 2026 sürümü; 1.980 satır → (kuruluş, ülke) bazında 750 tekil). Makale gövdesi ScienceDirect captcha duvarı nedeniyle okunamadı; istatistikler OSF dosyasından yeniden hesaplandı.

---
## 🧭 ETİK VE TEORİ

Bu bölüm üç farklı etik soruyu bir araya getiriyor. Birincisi **tanım etiği**: yapay zekâ içeriğini "slop" olarak adlandırmak kimin yetkisinde? İkincisi **epistemik etik**: veriye duyulan güvensizlik demokratik karar almayı nasıl bozuyor? Üçüncüsü **yayın etiği**: kaynakları gerçek ama dergisi ele geçirilmiş bir makaleyi nasıl okumalıyız?

### 4. "Slop" Doğal Bir Kategori Değil, Bir Sosyal Yargıdır (So vd., 2026)

**Künye:** Richard Jean So, Hoyt Long, Cody Kommers, Mina Lee, Emily Wenger, Peter West, Eamon Duede, Ari Holtzman, Chenhao Tan — *Nature Human Behaviour*, Comment, ss. 1-3; 9 Kasım 2026; DOI 10.1038/s41562-026-02639-6; kapalı erişim.

**ÖZET:** 
Dokuz yazarlı (Richard Jean So, Hoyt Long, Cody Kommers, Mina Lee, Emily Wenger, Peter West, Eamon Duede, Ari Holtzman, Chenhao Tan) *Nature Human Behaviour* Comment'i, yapay zekâ üretimi içeriğin ('slop') nasıl tanımlanacağına dair metodolojik bir öneri getiriyor: **slop doğal bir kategori değil, toplulukların verdiği bir sosyal yargıdır** — bir topluluğun 'istenmeyen yapay zekâ içeriği' olarak tanıdığı şey. Yazarların gerekçesi iki ayaklı: (1) mevcut yaklaşım — yapay zekâ içeriğini tespit edip kaldırmaya çalışan dedektörler — **başarısız oluyor**; (2) 'slop'u sosyal yargı olarak çerçevelemek onu **işlenebilir, ölçülebilir ve yönetilebilir** kılıyor. Yani tanımı teknik özelliklerden (perplexity, su işareti, artefakt) çıkarıp topluluk normlarına bağlıyor.

Bu, dezenformasyon ve platform yönetişimi literatüründe tanıdık bir kayma: 'neyin kötü içerik olduğunu' merkezî bir dedektör değil, o içeriği tüketen topluluk belirler. Politika sonucu da bu yönde: içerik kaldırma/etiketleme zorunluluğu yerine, toplulukların yargısını görünür kılan mekanizmalar (oy, topluluk notu, itiraz yolları) ve topluluk bazlı ölçüm.

**Kanıt düzeyi uyarısı:** Comment kapalı erişimde (OpenAlex: closed, hiçbir depoda tam metin yok) ve üç sayfalık bir görüş yazısı; bu kayıt **yalnızca yayıncının özeti + Crossref künyesi** üzerine kurulu. Metnin içindeki argüman sıralaması, önerdiği ölçüm operasyonelleştirmesi, vaka örnekleri ve kaynakça doğrulanmadı. Aşağıdaki bağlam maddeleri aynı ekibin **başka** çalışmalarına aittir ve Comment'in içeriği olarak okunmamalıdır.

**Tweet'in iddiası ile künye arasında fark var:** DSI_UChicago paylaşımı yalnızca üç ismi (@MinaLee__, @universeinanegg, @ChenhaoTan) öne çıkarıyor; künyede **dokuz yazar** var (So, Long, Kommers, Lee, Wenger, West, Duede, Holtzman, Tan). Ekip, Chicago Üniversitesi Knowledge Lab / Chicago Human+AI (CHAI) çevresi ile Duke dijital beşeri bilimler hattının ortak ürünü; ilk iki yazar (So, Long) kültürel veri analizi ve 'slop' literatürünün asıl taşıyıcıları.


**Türkiye notu:** Türkiye'de "yapay zekâ içeriği" tartışması ağırlıkla **dezenformasyon** çerçevesinde yürüyor; oysa çocukların ve gençlerin karşılaştığı yapay zekâ içeriğinin büyük kısmı dezenformasyon değil, **slop**: düşük maliyetli, yüzeysel yetkin, kitlesel üretilmiş video ve metin. Çocuk YouTube'unda bu içerik türü ayrı bir politika başlığı hak ediyor; "topluluk yargısı" çerçevesi, ebeveyn ve öğretmen topluluklarının etiketleme kapasitesini platform denetimine alternatif olarak öne çıkarıyor.

**Kanıt düzeyi:** Üç sayfalık Comment; yalnız yayıncı özeti + Crossref künyesi doğrulandı (OpenAlex: closed, hiçbir depoda tam metin yok). Bu kayıt bir **gündem önerisi** olarak okunmalı, bulgu olarak değil.

---

### 5. Veri Odaklı Kampanyacılıkta Asıl Sorun Veri Değil, Veriye Duyulan Güvensizlik (Sharma, 2026)

**Künye:** Amogh Dhar Sharma (University of Oxford, ODID) — *Big Data & Society* 13(4): 20539517261492575; Ekim–Aralık 2026; DOI 10.1177/20539517261492575; altın açık erişim (CC BY 4.0).

**ÖZET:** 
**Tam metin okundu** (CC BY 4.0 altın açık erişim, SAGE; ~7.500 kelime gövde, 42 referans). Amogh Dhar Sharma (Oxford, ODID), 2022 Punjab Eyalet Meclisi seçimleri öncesinde (Ocak–Şubat 2022) büyük bir partinin ('Party X') kampanya savaş odasının içinde etnografik saha çalışması yapıyor; veri odaklı kampanyacılık literatüründe nadir bir mikro düzey erişim.

**Kavram: 'epistemik güvensizlik' (epistemic distrust).** Siyasi aktörler veri toplamaya yoğun yatırım yaparken verinin gerçeği ortaya çıkarma kapasitesine karşı yaygın bir şüphe taşıyor: veri bolluğu, sayılara duyulan inancın değil **güvensizliğin** işareti. Makale 'dataism' varsayımını (veri = nesnel otorite) ampirik olarak çürütüyor.

**Üç müdahale:** (1) Veri bolluğu kararı hızlandırmadı, yavaşlattı; rakip 'dikeyler' (anketçiler, IVR firması, siyasi danışmanlık şirketi, çağrı merkezi, savaş odası koordinatörleri) triangüle edilmedi, karşı karşıya getirildi; başbakan adayı (CM) kararında kaynaklar çelişti ve karar 'veriye dayalı' değil kapalı kapı pazarlığıyla çıktı. (2) Veri nicelleşti, çünkü sayılar güven değil güvenilirlik performansı üretiyor: 117 seçim bölgesi için iki yüzlü A4 dosya, hücreler tek sayıya indirildi; 'nitel alanı olabildiğince küçük tutun ki öznelliği eleyelim' — amaç öznelliği yok etmek değil, **öznellik görüntüsünü** silmek. (3) Veri üretimi insan ilişkilerine gömülü; 'dışarıdan personel' stratejisi (Pencap dışından işe alım, Andhra Pradesh'ten IVR firması) 'hiçbir yerden bakış' arıyordu, saha tersini gösterdi.

**İki vinyet (mekanizma kanıtı):** koordinatörün günde bir saati aşan 'boş' telefon sohbetleri ('iki düz soru sorarsanız kapatırlar'); 'gazeteci' sahte kimliğiyle köye giden araştırmacının 'son günlerde gelen altıncı-yedinci gazeteci sen misin?' diye yakalanması.

**Ölçek:** 117 bölge, 23 ilçe, üç alt-bölge (Doaba, Majha, Malwa), dört parti (SAD, INC, AAP, BJP), ~15 koordinatör (23–35 yaş), günlük A–D zafer olasılığı sıralaması, iki kişilik analitik ekip. **Sınırlılık:** tek vaka, tek eyalet, tek parti, tek seçim; parti anonim ('Party X'); epistemik güvensizliğin demokratik siyasete özgü olup olmadığı açık soru.


**Türkiye notu:** Türkiye'de veri odaklı kampanyacılık tartışması "partiler veriyi ne kadar kullanıyor" ekseninde yürüyor; Sharma'nın bulgusu soruyu tersine çeviriyor. Türkiye'de iktidar partisinin devlete ait seçmen kütüğüne (MERNİS) ve e-Devlet altyapısına erişimi, muhalefetin ise saha anketi ve gönüllü verisine mahkûm olması, "rakip veri altyapıları" rekabetini **erişim eşitsizliği** olarak üretiyor. KVKK'nın siyasi düşünceyi özel nitelikli veri sayması (md. 6) bu asimetriyi hukuken sınırlıyor ama ortadan kaldırmıyor. Ayrıca Sharma'nın "veri kararı yavaşlattı" bulgusu, kampanya danışmanlığına verilen değerin abartılı olabileceğini gösteriyor — Türkiye'de seçim sonrası yapılan "veri analizi kazandırdı/kaybettirdi" tartışmaları için soğutucu bir kanıt.

**Kanıt düzeyi:** Tek vaka, tek eyalet (Pencap), tek parti (anonim), tek seçim; etnografik erişim güçlü, genellenebilirlik zayıf. Tam metin sayfada 403 (Cloudflare) — kayıt yayıncı özeti + açık erişim sürümü üzerinden.

---

### 6. 🚩 Yayın Etiği Vakası: Kaynakları Gerçek, Dergisi Ele Geçirilmiş Bir "Literatür Haritası" (Miswadi vd., 2026)

**Künye:** Miswadi (Politeknik Meta Industri Cikarang), Fatimah (Universitas Indonesia Maju), Ria Wuri Andary — *International Journal of Innovation and Thinking* 3(2): 1-15; 6 Kasım 2026; DOI 10.71364/ijit.v3i2.106; yayıncı: "Mahasiswa Kreatif Indonesia".

**ÖZET:** 
⚠️ **Kaynak güvenilirliği: DÜŞÜK — kanıt olarak kullanılmamalı, yalnızca literatür haritası olarak.** Üç yazarlı (Miswadi, Fatimah, Ria Wuri Andary) makale, genç yetişkinlerde dezenformasyonla mücadele için dijital iletişim stratejilerini ve medya okuryazarlığını konu alıyor. Yöntem **kütüphane araştırması**: 2017-2026 arası 30 yayının tematik sentezi; birincil veri, anket, deney veya meta-analiz yok. Yazarın kendi ifadesiyle ilişkiler 'ampirik olarak doğrulanmış nedensel yollar değil, kuramsal önermeler'.

**İçerik:** Sentez beş tema çıkarıyor — maruz kalma; önleyici iletişim (prebunking, aşılama); düzeltici iletişim; eleştirel medya okuryazarlığı; entegrasyon. Buradan **IDCMLF** (Integrated Digital Communication and Media Literacy Framework) öneriliyor: önleyici iletişim + düzeltici iletişim + katılımcı medya okuryazarlığı boyutları. Kavramsal katkı iddiası şu: literatür izole müdahalelerin etkililiğine bakıyor, oysa bunların **birbirini tamamlayıcı** biçimde nasıl birleştiği modellenmemiş.

**Neden DÜŞÜK:** (a) Dergi sitesinde (ij-it.com) **90'a yakın kumar/bahis SEO spam bağlantısı** var (ROKOKBET, TIP4D, SLOT88, TOTO) — ele geçirilmiş OJS kurulumlarının tipik izi. (b) **Editoryal kurul büyük olasılıkla kopyalanmış:** kurulda tüketici davranışı camiasından isimler (Aimee Huff, Biraglia, Geyskens) var ama dergiyle kurumsal bağları yok. (c) Dergi yeni (cilt 3, 2026); DOI'ler Crossref'e kayıtlı olsa da **referanslar depolanmamış** (reference-count: 0), PDF'te ISSN yerine 'xxxx-xxxx' yer tutucusu var. (d) Buna karşılık **kaynaklar gerçek**: 30 kaynağın tamamı DOI'li.

**Sonuç:** Makale, alanın 2017-2026 literatürünü doğru kaynaklarla tarayan **kullanışlı bir harita**; ama kendi ampirik katkısı yok ve dergi güvenilir değil. Atıf yapılacaksa makale değil, altındaki 30 kaynak kullanılmalı.


**Neden bu bültende yer alıyor?** Çünkü haftanın en öğretici **yayın etiği** vakası ve bir yöntem dersi: bir makalenin kaynakçası gerçek, iddiaları makul, dili düzgün olabilir; ama dergi ele geçirilmişse (hijacked OJS), metnin akademik statüsü yoktur. Denetim izleri somut: dergi sayfalarında ~90 kumar/bahis SEO bağlantısı, tüketici psikolojisi camiasından isimlerle doldurulmuş (büyük olasılıkla kopyalanmış) editoryal kurul, Crossref'te sıfır referans kaydı, PDF'te `xxxx-xxxx` ISSN yer tutucusu, sorumlu yazar için gmail adresi. Buna karşılık 30 kaynağın tamamı DOI'li ve rastgele seçilen 6'sı Crossref'te birebir doğrulandı.

**Türkiye notu:** Türkçe literatürde de benzer örnekler var: kopyalanmış kurul listeleri, yer tutucu ISSN'ler, "öğrenci kolektifi" adıyla yayın yapan DOI'li dergiler. Bu vaka, **dergi kalitesi kontrolünü** (DOAJ, ISSN doğrulama, Crossref reference-count, kurul üyelerinin kurumsal eşleşmesi) araştırma sürecinin zorunlu adımı haline getirmek için iyi bir eğitim materyali. Metnin kendisi ise bir "kanıt" değil, **literatür haritası**: prebunking/aşılama, düzeltici iletişim ve eleştirel medya okuryazarlığı üçlüsünün entegrasyonu (IDCMLF) fikri, aşağıdaki gerçek kaynaklara gidilerek kullanılmalı.

**Kanıt düzeyi:** DÜŞÜK — kaynak olarak kullanılmamalı. Tam metin erişilebilir (200 / 46 KB / 10.181 karakter) ve bu erişilebilirlik, kalite anlamına gelmiyor.

---
## 🌍 GÜNCEL TARTIŞMALAR

Üç çalışma, kamuoyu araştırmalarının üç klasik sorusuna yeni cevaplar veriyor: dezenformasyon selleri işe yarıyor mu, mizah kutuplaştırıyor mu, yankı odaları nasıl kırılır? Üçünde de ortak bir örüntü var: **mekanizma, beklenen yerde değil.**

### 7. "Selleme" (Flooding) Sanıldığı Gibi Çalışmıyor: Ön-Kayıtlı İki Deney (Szegőfi, Altay & Heintz, 2026)

**Künye:** Ákos Szegőfi (Pittsburgh), Sacha Altay (Zürih), Christophe Heintz (CEU Viyana) — *British Journal of Social Psychology* 66(1): e70151; çevrimiçi 8 Kasım 2026; DOI 10.1111/bjso.70151; CC BY 4.0; PMID 43000938.

**ÖZET:** 
Ákos Szegőfi (Pittsburgh), Sacha Altay (Zürih) ve Christophe Heintz'in (CEU Viyana) *British Journal of Social Psychology*'de yayımlanan çalışması, dezenformasyon literatürünün en çok tekrarlanan ama en az test edilen iddiasını — 'selleme' (flooding) stratejisinin işe yaradığı iddiasını — laboratuvara sokuyor. Flooding, tek bir yalanı tekrarlamak değil; ortama birbiriyle ve gerçekle çelişen çok sayıda önerme boca ederek güvenilir bilginin **tanınmasını ve ona göre davranılmasını** engellemek. Kuramsal zincir: çelişkili içerik seli → belirsizlik ve bilgi yüklenmesi → **rasyonel dikkatsizlik** → konudan kopma ve eylemsizlik. Epistemik tetikteklik modeline göre aşırı yük saflık değil **çekilme** üretiyor.

Tasarım: OSF'te ön-kayıtlı iki vinyet deneyi, Prolific ABD örneklemi, N=2.607 (güneş kremi n=1.307; GDO n=1.300; d=0.20'de %95 güç). Katılımcılar X/Twitter görünümlü sahte akış görüyor: beş doğru, beş yanlış önerme; kontrol 1:1, deney 1:5. Kaynak ipuçları sabit (doğrular uzman, yanlışlar alakasız uzmanlık etiketiyle) — yani 'ideal' ortamda bile etki aranıyor. Bulgular: bilgi yüklenmesi her iki deneyde arttı (güneş kremi +0.515, p<.001; GDO +0.214, p=.018); doğru önermelerin doğruluk algısı güneş kreminde düştü (−0.216, p=.016), GDO'da anlamsız (−0.151, p=.062); güneş kreminde yanlış önermelerin algısı da yükseldi (+0.228, p=.008) ve truth-discernment −0.45 (p<.001) geriledi — sel, değerlendirmeleri 'yanlışa inanma'ya değil **'bilmiyorum'a** sıkıştırıyor. Tutumlar: güneş kreminde sel tutumu tersine olumluya kaydırdı (+0.138, p=.001), GDO'da iki tutum bozuldu (tüketim −0.167, çevre −0.192; p<.001). Moderasyon: GDO'ya önceden olumlu bakanlar doğru bilgiyi daha iyi ayırt ediyor (b=0.365), ama sel bunu aşındırıyor (−0.184, p=.012; çevre −0.199, p=.008).

Sınırlar açık: sabit kaynak ipuçları etkiyi hafife alıyor; 1:1 vs 1:5 oranı aşırı; konular partizan değil, oysa flooding en çok siyasi konularda kullanılıyor; tek seferlik tasarım rasyonel dikkatsizlik ve eylemsizliği test etmiyor. Politika çıkarımı az bulunur: **her yalanı tek tek doğrulamak sel ortamında işe yaramaz**, çünkü ortama bir içerik daha ekler ve yalan üretmek ucuzken doğrulama pahalıdır. Öneri: güvenilir sinyalleri çoğaltmak, geçmişi sağlam kaynakların görünürlüğünü artırmak, bilgi küratörlüğü yapan kurumları güçlendirmek.


**Türkiye notu:** Türkiye'de dezenformasyon tartışması ağırlıkla **tek bir yalanın** dolaşımı üzerine kurulu (seçim gecesi iddiaları, afet dönemi söylentileri). Selleme, farklı bir tehdit türü: tek tek çürütülemeyecek hacimde çelişkili iddia. Bu çalışmanın bulgusu, sellemeyi "her şeyi yalan söylemek" olarak anlayan politika yaklaşımını sınırlıyor: bilgi yüklenmesi artıyor ama doğru önermelerin değerlendirmesi her yerde çökmüyor, dolayısıyla etki **çekilme** (disengagement) üzerinden işliyor. Türkiye'de afet ve seçim dönemlerinde gözlenen "hiçbir şeye inanmama" hâli, bu mekanizmanın klinik olmayan karşılığı olabilir — test edilmemiş bir hipotez.

**Kanıt düzeyi:** Ön kayıtlı, N=2.607, Prolific ABD örneklemi, iki vinyet deneyi; güç analizi d=0,20 için %95. Tam metin: Wiley 403 (6.130 B, Cloudflare) → metadata tabanlı.

---

### 8. Aynı Eleştiri, Mizahla Verildiğinde Kutuplaşmayı Geri Çekiyor (Sleiman vd., 2026)

**Künye:** Yara Sleiman, Maria Grasso, Charles Pattie, Laura Serra, Carlo Hofer — *Political Studies*, OnlineFirst, ss. 1-24; 23 Ekim 2026; DOI 10.1177/00323217261496123; CC BY-NC 4.0.

**ÖZET:** 
Yara Sleiman, Maria Grasso, Charles Pattie, Laura Serra ve Carlo Hofer'ın *Political Studies* dergisinde 23 Ekim 2026'da çevrimiçi yayımlanan ön-kayıtlı anket deneyi, siyasi mizahın duygusal kutuplaşmayı her zaman artırdığı ya da azalttığı yönündeki iki rakip beklentiyi 2×3 faktöriyel tasarımla karşı karşıya getiriyor. Deltapoll sahasında (22-28 Şubat 2024) temsilî 2.011 Britanyalı yetişkine mesajın tonu (mizahi/mizahi değil) ve hedefi (iç-grup/dış-grup/siyaset-dışı kontrol) randomize ediliyor. İç- ve dış-grup, 0-10 ideolojik öz-konumlandırmaya göre tanımlanıyor; merkezdekiler (n=518) analiz dışı, analitik örneklem n=1.488. Uyaran seti, 'lefties'/'Tories' klişelerine dayanan sekiz hafif aşağılayıcı şaka ve her birinin aynı eleştiriyi koruyan ciddi eşdeğeri; ton farkı içerik farkına karışmıyor. Kutuplaşma duygu termometresi, sıfat değerlendirmesi ve sosyal mesafe maddeleriyle ölçülüyor.

Bulgular mizahın tek yönlü bir 'depolarizasyon aracı' olmadığını gösteriyor. Ciddi (mizahi olmayan) iç-grup eleştirisi sıfat temelli kutuplaşmayı 5,9 puan artırıyor (p=0.003; d=0.27): kendi grubuna yönelen eleştiri savunmacı kimlik tepkisini tetikliyor. Aynı eleştiri mizahla verildiğinde etki 4,4 puan geri çekiliyor (p=0.014); iç-grup × mizah etkileşimi negatif ve anlamlı (-0.070, p=0.006). Mizahın düzeltici etkisi (d=-0.33) karşı çıktığı etkiyle (d=0.27) başabaş: mizahi çerçeveleme kutuplaşmayı kontrol düzeyine geri döndürüyor. Dış-gruba yönelen mizah hiçbir kayma üretmiyor; baştan bir kimlik tehdidi yok. Mizahın genel ana etkisi yok; sosyal mesafede hiçbir koşulda etki çıkmıyor; etki tutumsal değerlendirmelerle sınırlı, davranışsal yatkınlıklara uzanmıyor. Ayrıştırma analizi hem dış-grup düşmanlığını (-0.078, p=0.010) hem iç-grup kayırmacılığını (-0.049, p=0.023) azaltıyor. Aracılık analizinde (Imai) mekanizma iki kanaldan işliyor: 'şakaydı' indirgemesi ve öfke/hayal kırıklığının azalması; kaygı kanalı ters işaretli, küçük ve anlamsız.

4,4 puanlık (≈0.20 SD) azalma, Voelkel vd. (2024) 25 depolarizasyon müdahalesinin ortalamasıyla (~5 puan) aynı mertebede. Yazarların uyarısı net: etki 'aktif tutum değişimi' değil 'nötrleştirme'; mizah ancak kaçınılmaz bir eleştirinin alımlanmasını yumuşatmak için değerli, tek başına müdahale değil. Sınırlılıklar: tek seferlik maruz kalma, metin uyaranı, hafif mizah (sert mizahın ters mekanizmayı tetikleyebileceği kabul ediliyor), Britanya'nın çok partili bağlamı ve kontrol kolunun üst-kimlik priming'i riski.


**Türkiye notu:** Türkiye'de siyasi mizah ağırlıkla **dış-gruba** yöneliyor; iktidar eleştirisini taşıyan televizyon ve sosyal medya mizahı, hedefi karşı kutup olan şakalardan oluşuyor. Çalışmanın bulgusu burada ters okunmalı: dış-gruba yönelen mizah hiçbir kayma üretmiyor (çünkü baştan bir kimlik tehdidi yok), asıl düzeltici etki **iç-gruba** yönelen mizahda. Yani Türkiye'de kutuplaşmayı azaltmak için mizahın "karşı tarafı" değil **"kendi tarafını"** hedeflemesi gerekiyor — politik olarak çok daha zor ve bu yüzden az denen bir hat. Tasarım ithali de mümkün: eşleştirilmiş uyaran (aynı eleştirinin mizahi ve ciddi versiyonu), KONDA/Türkiye Raporu panelleriyle n≈1.500–2.000'de düşük maliyetle tekrarlanabilir.

**Kanıt düzeyi:** Ön kayıtlı, temsilî örneklem (n=2.011, analitik n=1.488), tek seferlik maruz kalma, metin uyaranı. Tam metin: SAGE 403 (6.142 B) → metadata tabanlı.

---

### 9. Yankı Odalarının Kaldıracı Görüş Yakınlığı Değil, Tahammül (Huang vd., 2026)

**Künye:** Ting-Chun Huang (Peking University), Ning Ning Chung (SUSS) vd. — *Complexities* (MDPI) 2(4): 26; yayın 7 Kasım 2026; DOI 10.3390/complexities2040026; CC BY 4.0; 29 s. (early access).

**ÖZET:** 
**Tam metin okundu (29 sayfalık PDF, CC BY 4.0 altın açık erişim).** Huang, Chung ve Chew (Peking Üniversitesi / SUSS–CSH Vienna / NTU), yankı odalarını homofili ve "fikir ayrılığına tahammül" (τ) ekseninde ajan-tabanlı bir istatistiksel fizik modeliyle inceliyor.

Model (ABLTD): N = 400 düğümlü halka ağ, ortalama derece K = 8/16, G boyutlu ikili görüş vektörü (G = 3/9/27). Bağ işareti J_ij = sign(τ − 1/2 + S_i·S_j/2G) ile iki görüşün örtüşmesinden türer; yeni parametre τ, görüş ayrılığına rağmen dostane bağ kurma eşiğini kaydırır (τ = 1 tam tahammül, τ = 0 tam reddiye).

Üç bulgu. (1) Uzlaşma arzusu tek başına yankı odası üretmiyor: G = 3, K = 8 rejiminde nüfusun ~%60'ı karşıt görüşe maruz, ~%40'ı hiç maruz değil. (2) Asıl kaldıraç τ: τ > 0,5'te maruz kalmayanlar ~%40'tan ~%10'a iniyor ve kalan %90'ın teması tamamen dostane; τ < 0,5'te toplam maruziyet ılımlı düşerken niteliği çöküyor — temasın tümü düşmanca. Aşırı tahammülsüzlükte (τ < 0,2) yankı odaları nüfusun %60–80'ini yutuyor. (3) En büyük yankı odası düşük τ'da nüfusun %10–40'ı, yüksek τ'da %1'in altına iniyor.

Kavramsal ayrım en taşınabilir kısım: "fikir ayrılığını kabul" açık fikirlilik değil — açık fikirlilik görüş değişimini (homojenleşme) getirirken tahammül, görüş değişmeden bağın sürmesini sağlıyor. Metodolojik uyarı: ikili maruziyet ε ≈ 0,47 iken ağırlıklı ε_w ≈ 0,14; "herkesin bir karşıt komşusu var" gözlemi görüş çeşitliliğini abartabilir. Sınırlılık: hiç ampirik veri yok, τ tüm bireylerde homojen. Modelin en taşınabilir katkısı bu ayrım: yankı odasını küçültmenin yolu görüşleri yakınlaştırmak değil, ayrı görüşlüler arasında **dostane bağ kurabilmeyi** artırmak olabilir. Bunun ampirik karşılığı ölçülmemiş; "tahammül" henüz standart bir anket maddesi değil ve modelin tüm bireylere aynı τ değerini vermesi, gerçek ağlardaki dağılımı kaçırıyor.


**Türkiye notu:** Türkiye'de kutuplaşma literatürü ağırlıkla duygusal kutuplaşma (partizan sevgi/nefret) ve seçim ekseninde ölçülüyor. Bu model üçüncü bir değişken öneriyor: **fikir ayrılığına tahammül**. Ayrım politika açısından değerli — "kutuplaşma" ile "kutuplaşmanın nefretle mi nezaketle mi yaşandığı" aynı şey değil. Ancak kanıt düzeyi konusunda net olmak gerek: makalede tek bir ampirik veri yok, bulguların tamamı N=400 simülasyon. Türkiye tartışmasına **mekanizma düzeyinde** aktarılabilir, **kanıt düzeyinde** aktarılamaz.

**Kanıt düzeyi:** Simülasyon (ajan-tabanlı, ABLTD modeli); ampirik doğrulama yok, τ parametresi tüm bireylerde homojen. Tam metin: MDPI 200 döndü ama metin **0 karakter** (JS duvarı) 🆕 → engelli sayıldı, kayıt yayıncı özeti üzerinden.

---

## 🇹🇷 TÜRKİYE BAĞLAMI

### Araştırma kapasitesi: envanterin gösterdiği üç boşluk

Bu haftanın veri seti (750 doğrulama kuruluşu), Türkiye'nin araştırma altyapısı hakkında tek bir makaleden çıkarılabilecek en somut bulguyu veriyor: **kapasite var, çeşitlenme yok.** Dört kuruluşun dördü de aktif, metodolojik şeffaflıkları yüksek ve 2014–2021 arasında kurulmuşlar — yani 2015 sonrası küresel doğrulama dalgasının Türkiye ayağı kurulmuş, ama **2021'den sonra yeni kuruluş gelmemiş**. Küresel veride de benzer bir durgunluk var (2024: 5 yeni kuruluş, 2025: 3), ancak Türkiye'de taban zaten dar olduğu için durgunluk daha kritik.

Bu, çocuk dijital politikası açısından iki sonuç üretiyor. **Birincisi**, içerik müdahalesi kapasitesi (Bakanlığın açıkladığı 3.306 müdahale) ile bağımsız doğrulama kapasitesi (4 kuruluş) arasındaki asimetri, müdahale kararlarının denetlenebilirliğini sınırlıyor. **İkincisi**, yaş doğrulaması ve 15–18 rejimi gibi yeni yükümlülükler, platformların ve ailelerin başvuracağı **bağımsız bilgi kaynağı** ihtiyacını artırıyor; bu ihtiyacı karşılayacak kurumsal taban ise genişlemiyor.

### Yöntem ithali: üç taşınabilir tasarım

Türkiye'de çocuk ve genç odaklı dijital araştırma ağırlıkla anket ve içerik analizi ile yürüyor; deneysel ve ön-kayıtlı çalışma azlığı hem uluslararası görünürlüğü hem politika etkisini sınırlıyor. Bu haftaki üç tasarım düşük maliyetle taşınabilir:

1. **Eşleştirilmiş uyaran deneyi** (Sleiman vd.): aynı siyasi eleştirinin mizahi ve ciddi versiyonlarını randomize etmek. Panel altyapısı hazır; maliyet düşük; bulgu doğrudan medya okuryazarlığı politikasına bağlanıyor.
2. **LLM kimlik koşullaması deneyi** (Fitz & Saunders): yerel komplo iddialarını "parti atfı" ve "atıfsız" koşullarda sormak. API maliyeti bu ölçekte (135 bin konuşma) yüksek; ama 5.000 konuşmalık bir alt küme ile temel örüntü test edilebilir.
3. **Envanter çalışması** (Sánchez-Mayordomo vd.): Türkiye'deki medya okuryazarlığı ve doğrulama kuruluşlarının (STK, üniversite merkezleri, kamu programları) sistematik kodlanması. Veri seti şablonu açık erişimde; tek bir lisansüstü tezi ölçeğinde iş.

### Bir uyarı: "ölçüm" ile "denetim" aynı şey değil

Haftanın üç deneysel çalışması da aynı dersi veriyor: ölçüm tasarımı, bulguyu belirliyor. Fitz ve Saunders'ın OpenAI eleştirisi bunun en açık örneği — konu ve ton aynı anda değiştiğinde varyansın kaynağı izole edilemiyor. Türkiye'de çocuk dijital politikası için bu, "etki değerlendirmesi" yaparken **karşı-olgu** kurmanın zorunlu olduğu anlamına geliyor: yaş doğrulaması olmasaydı ne olurdu sorusuna cevap vermeyen bir değerlendirme, politikanın kendi başarısını ölçmez.

---
## 📖 OKUMA LİSTESİ

Haftanın 17 kaydının tamamı; ilk dokuzu bu sayıda derin okumayla işlendi.

| Zorluk | Makale | Konu | Öncelik |
|--------|--------|------|---------|
| 🟢 Kolay | **So vd. — AI 'slop' is a social judgement** (*Nat Hum Behav*, Comment) | Yapay zekâ içeriğinin tanımı; dedektör başarısızlığı; topluluk yargısı | ⭐⭐⭐ |
| 🟡 Orta | **Christou — Autoethnography & GenAI** (*The Qualitative Report*) | Nitel yazmada GenAI; epistemik özgünlük kaybı; verisimilitude paradoksu | ⭐⭐⭐ |
| 🔴 Zor | **Fitz & Saunders — LLM'ler ve komplo çürütme** (PsyArXiv, ön kayıtlı) | 135.845 konuşma; kimlik koşullaması; "çürüt ama onayla"; yönetişim eleştirisi | ⭐⭐⭐ |
| 🟢 Kolay | **Sánchez-Mayordomo vd. — 750 doğrulama kuruluşu** (*Data in Brief*) | Envanter; 131 ülke; Türkiye 4 kuruluş; hayatta kalma analizi imkânı | ⭐⭐⭐ |
| 🟡 Orta | **Sharma — Datafication meets democracy** (*Big Data & Society*) | Pencap etnografisi; epistemik güvensizlik; veri kararı yavaşlatıyor | ⭐⭐ |
| 🟡 Orta | **Szegőfi, Altay & Heintz — 'Flooding'** (*BJSP*) | Selleme stratejisinin ön-kayıtlı testi; rasyonel dikkatsizlik; çekilme | ⭐⭐⭐ |
| 🟡 Orta | **Sleiman vd. — Polarising punchlines** (*Political Studies*) | İç/dış-grup mizahı; duygusal kutuplaşma; eşleştirilmiş uyaran tasarımı | ⭐⭐⭐ |
| 🔴 Zor | **Huang vd. — Breaking Echo Chambers** (*Complexities*) | Ajan-tabanlı model; tahammül parametresi τ; maruziyet niteliği | ⭐⭐ |
| 🟡 Orta | **Miswadi vd. — Digital Communication Strategies** (*IJIT*) 🚩 | Medya okuryazarlığı literatür haritası; **dergi ele geçirilmiş** — kanıt olarak kullanılmaz | ⭐ (yalnız yayın etiği vakası) |
| 🟢 Kolay | **ALkharraz vd. — AI dezenformasyonu ve doğrulama niyeti** (*Frontiers in Communication*) | BAE, n=320; tehdit algısı aracılığı; eleştirel AI okuryazarlığı | ⭐⭐ |
| 🟢 Kolay | **Teixeira — UNICEF Innocenti katılım derlemesi** | 51 kaynak; kurumsal etki; Nepal ve Barra Mansa vakaları | ⭐⭐⭐ (KURATOR kesişimi) |
| 🟡 Orta | **Allen — Bandwagon or backlash?** (*JEaPP*) | Trump 2016 → Batı Avrupa aşırı sağı; ifade/damga ayrımı; ESS doğal deney | ⭐⭐ |
| 🔴 Zor | **Graf, Lenz & Adam — Keep the Peace?** (*Party Politics*) | Almanya Covid; cue-taking yok; partizan sıralanma; NEDV tasarımı | ⭐⭐ |
| 🟢 Kolay | **Packer & Van Bavel — 9 Findings on Political Partisans** (*The Power of Us*) | Derleme; 2 bulgu doğrulanabilir, 7'si ücretli duvarda | ⭐ |
| 🟢 Kolay | **Danka — Graph Theory for Visual Learners** (*The Palindrome*) | Çizge kuramı; 14 bölüm; öğretim materyali (araştırma değil) | ⭐⭐ (yöntem öğrenme) |
| 🟡 Orta | **Baral — From Chaos to Clarity** (*J. Library Management*) 🚩 | YouTube dezenformasyon videolarında duygu analizi; Crossref'te dergi kaydı yok | ⭐ |
| 🟢 Kolay | **MEDDMO/EDMO — Turkey and Cyprus in Online Narratives** | Türkiye–Kıbrıs çevrimiçi anlatılar; bölgesel gözlemevi raporu | ⭐⭐⭐ (Türkiye verisi) |

**Okuma önerisi:** Zaman kısıtlıysa sıra: (1) UNICEF Innocenti, (2) Data in Brief envanteri, (3) Sleiman vd., (4) Szegőfi vd. Bu dördü hem KURATOR gündemine doğrudan bağlanıyor hem de metodolojik olarak sağlam.

---

## 📚 KAYNAKÇA

1. ALkharraz, F., Abudraz, A. M. M., Tharwat, W. A. K., Abunamous, R. E. S., Musalam, A. M. A., Salem, O., Alghoul, I. & Naouss, M. (2026). Perceived Exposure to AI-Generated Misinformation During Crises and Information Verification Intentions: The Mediating Role of Perceived Threat and Critical AI Literacy. *Frontiers in Communication* 11. DOI 10.3389/fcomm.2026.2020314
2. Allen, T. J. (2025/2026). Bandwagon or backlash? Examining the impact of Trump's 2016 election on support for the West European far right. *Journal of Elections, Public Opinion and Parties* 36(4): 855-884. DOI 10.1080/17457289.2025.2547178
3. Baral, R. (2025). From Chaos to Clarity: Content Analysis of Viewer Sentiments Using YouTube Videos on Misinformation. *Journal of Library Management* (ISSN 2278-5523).
4. Christou, P. A. (2026). Autoethnography: Understandings, Evolution, and the Influence of GenAI. *The Qualitative Report* 31(8): 6519-6535. DOI 10.46743/2160-3715/2026.9211
5. Danka, T. (2026, 11 Kasım). Graph Theory for Visual Learners. *The Palindrome*.
6. Fitz, E. B. & Saunders, K. L. (2026). Political Ingroup and Outgroup Cues Condition How Large Language Models Refute Conspiracy Theories. PsyArXiv. DOI 10.31234/osf.io/4yexj_v1
7. Graf, F., Lenz, A. & Adam, C. (2026). Keep the Peace? The Early Politics of Covid-19 and the Limits of Partisan Influence on Public Opinion. *Party Politics* (online first). DOI 10.1177/13540688261487130
8. Huang, T.-C., Chung, N. N. vd. (2026). Breaking Echo Chambers Through Acceptance of Differing Opinions. *Complexities* 2(4): 26. DOI 10.3390/complexities2040026
9. MEDDMO/EDMO (2026, 11 Kasım). Turkey and Cyprus in Online Narratives. meddmo.eu
10. Miswadi, Fatimah & Andary, R. W. (2026). Digital Communication Strategies for Combating Misinformation and Strengthening Media Literacy Among Young Adults. *International Journal of Innovation and Thinking* 3(2): 1-15. DOI 10.71364/ijit.v3i2.106 🚩
11. Packer, D. & Van Bavel, J. (2026, 10 Kasım). Your Politics May Shape More Than You Think: 9 Findings on Political Partisans. *The Power of Us*.
12. Sánchez-Mayordomo, F., García-Alcaraz, T. & Ruipérez-Valiente, J. A. (2026). Fact-checking organizations worldwide: A dataset for structural and contextual analysis. *Data in Brief* 69: 113385. DOI 10.1016/j.dib.2026.113385
13. Sharma, A. D. (2026). Datafication meets democracy: epistemic distrust and data-driven campaigns in India. *Big Data & Society* 13(4). DOI 10.1177/20539517261492575
14. Sleiman, Y., Grasso, M., Pattie, C., Serra, L. & Hofer, C. (2026). Polarising punchlines: The influence of intergroup humour on affective political polarisation. *Political Studies* (OnlineFirst). DOI 10.1177/00323217261496123
15. So, R. J., Long, H., Kommers, C., Lee, M., Wenger, E., West, P., Duede, E., Holtzman, A. & Tan, C. (2026). AI 'slop' is a social judgement. *Nature Human Behaviour* (Comment). DOI 10.1038/s41562-026-02639-6
16. Szegőfi, Á., Altay, S. & Heintz, C. (2026). 'Flooding' using disinformation. *British Journal of Social Psychology* 66(1): e70151. DOI 10.1111/bjso.70151
17. Teixeira, C. (2026). Evidence Review of Adolescent and Youth Participation: Impact in Governance and Policymaking. UNICEF Innocenti Working Paper, Florence.

---

## 📌 YÖNTEM VE ERİŞİM NOTU

**Havuz:** Yedi `*_categorized.json` dosyası (10–14 Kasım) → 17 ham kayıt → başlık düzeyinde dedup → **17 benzersiz** (bu hafta örtüşme yok). 15 AKADEMİK ÖZEL, 2 KURATOR kesişimli (biri net KURATOR: UNICEF Innocenti).

**Erişim (Scrapling 0.4.7, 17 URL, 30 sn zaman aşımı, 5 eşzamanlı):** 9 engelli/metinsiz (%53).

| Yayıncı ailesi | n | Durum |
|---|---|---|
| SAGE | 3 | 403 / 6.142 B (Cloudflare) |
| Taylor & Francis | 1 | 403 / 6.174 B |
| Wiley | 1 | 403 / 6.130 B |
| Elsevier | 1 | 403 (captcha, 1,21 MB gövde) |
| ResearchGate | 1 | 403 / 23.573 B |
| OSF Preprints | 1 | 200 ama **3 karakter** (JS duvarı) |
| MDPI | 1 | 200 ama **0 karakter** (JS duvarı) 🆕 |
| Açık erişim (UNICEF, TQR, IJIT, Frontiers, Nature, Substack ×2, MEDDMO) | 8 | ✅ |

**Yöntem notu:** Eşik (%50) aşıldığı için kayıtların tamamı **metadata tabanlı** sınıflandırıldı: Crossref/OpenAlex künyesi + yayıncı özeti + varsa açık erişim ön baskısı. Özetler 250–300 kelime aralığında tutuldu ve programatik olarak ölçüldü. `blocked: true` bayrağı, çözümlenmiş yayıncı adresinin durumunu yansıtıyor; X/Twitter gönderilerinin kendisi ayrıca erişilebilir olabilir.

**Kapsam dışı bırakılanlar:** Hafta içinde `processed_links/` altında tek tek işlenmiş ve OKF hattı tarafından wiki'ye alınmış kayıtlar (ör. `2026-11-11_graph-theory`, `2026-11-11_turkey-and-cyprus`, `2026-11_evidence-review...`) bu sayıda yeniden özetlenmedi; yalnızca haftalık havuzda yer aldıkları için okuma listesine girdiler.
