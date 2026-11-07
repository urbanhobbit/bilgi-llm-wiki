# AKADEMİK ÖZEL TARAMA — Haftalık Derleme
## 7 Kasım 2026

**Kapsam:** 1–7 Kasım 2026 dilimi · 63 benzersiz kayıt (62 AKADEMİK ÖZEL etiketli, 4 KURATOR kesişimli)
**Hazırlayan:** KURATOR Araştırma Ekibi
**Yöntem:** Telegram link akışı → günlük `*_categorized.json` dosyaları → haftalık havuz (başlık düzeyinde dedup) → 9 makale derin okuma, 11 makale okuma listesi

---

## 📋 YÖNETİCİ ÖZETİ

Bu haftanın akademik akışı tek bir sorunun etrafında toplandı: **yapay zekâ, sosyal bilim araştırmasının hangi aşamalarına girebilir — ve girdiğinde neyi sessizce değiştirir?** Dokuz makalenin beşi doğrudan bu soruya bakıyor, ama birbirinden çok farklı yerlerden: bir müdahalenin etkisini ön-kayıttan tahmin etmek (Vivalt), anket katılımcısının kendisinin yapay zekâ kullanması (Goetze), anket maddesini katılımcının kendi önceliğinden üretmek (Velez & Ewig), sosyolojik bir kuramı LLM'e uygulatmak (Schroeder vd. + Lundberg), ve sahadaki etik kırılganlık (Soyata).

Haftanın en sert yöntemsel bulgusu **Goetze'nin vaka raporundan** geliyor: 259 katılımcılı bir anket çalışmasında yapay zekâ şüphesi analitik örneklemi **29 kişiye** indiriyor — kaybın %70'i tek bir yoruma dayanıyor ve beş kişilik uzman paneli belirsizliği azaltmıyor. Bu, "katılımcı yapay zekâ kullanımı" tartışmasını bir etik not olmaktan çıkarıp saha çalışmasının kaderi hâline getiriyor.

İkinci sert bulgu **kuramsal**: Schroeder, Thelwall ve Thomas'ın Collins uygulamasına Lundberg'in itirazı, LLM'in kuramı uygulamakla kalmayıp **değiştirdiğini** gösteriyor. Collins'in "yapısal sıkışma" mekanizması ChatGPT özetinde kayboluyor, yerine genel bir dışsalcı önerme geçiyor ve o önerme üzerine kurulan tahminler artık Collins'in kuramından türetilmiş sayılamıyor. Bu, Türkiye'de Batılı kaynakların özetleri üzerinden dolaşan kuram zincirine eklenen yeni ve çok daha hızlı bir halka.

Üçüncü hat **Türkiye'ye doğrudan bağlanıyor**. Soyata'nın Koç Üniversitesi'ndeki bir yıllık saha çalışmasına dayanan makalesi, erişimin izin belgesiyle değil **güven, ihtiyat ve itibar riski** etrafında kurulan ilişkisel-ahlaki değerlendirmelerle üretildiğini gösteriyor; "bunu yazma" talepleri veri kaybı değil, sınırın kanıtı. Ajzenman, Aksoy ve Pickard ise 53 ülkede 260.000+ katılımcıyla, popülist yönetim altında 18–25 yaşını geçiren kuşakların sıfır toplamlı dünya görüşünü kalıcı olarak benimsediğini buluyor — ve Türkiye, bulgunun büyüklüğünü anlatmak için kullanılan ölçeğin üst ucunda duruyor.

**Bu hafta yeni olan ne?** Pazartesi KURATOR bülteni (2 Kasım) QJE/JAMA okul telefon kanıtını ve 1 Kasım yürürlüğünü işlemişti. Bu derleme o iki hattı tekrar etmiyor; onun yerine hafta içinde gelen **yöntem** ve **kuram** kayıtlarını derinleştiriyor.

**Erişim durumu:** Scrapling testinde 12 yayıncı URL'sinden 7'si engelli (%58) — OUP/QJE, Taylor & Francis, SAGE (×2), Elsevier, CEPR/VoxEU 403; CUP 500. Tam metin alınabilenler: Nature Reviews Psychology (66,8 bin karakter), CE International (17,2 bin), arXiv (4,6 bin), IPC Sabancı (4,1 bin). Bu nedenle özetler yayıncı özeti + Crossref/OpenAlex künyesi + doğrulanabilen ölçüde tam metin üzerine kuruldu; hangi kaydın hangi düzeyde doğrulandığı her makalenin **Erişim** satırında ayrıca belirtildi.

---

## 🔬 METODOLOJİ

### 1. Yapay Zekâ Ekonominin Tedavi Etkilerini Önceden Tahmin Edebilir mi? (Vivalt, 2026)

**Künye:** Eva Vivalt, "Can Artificial Intelligence Forecast Treatment Effects in Economics?", arXiv:2610.38883 [econ.GN], v1, 28 Ekim 2026 · DOI 10.48550/arXiv.2610.38883 · ön baskı, hakemsiz
**Erişim:** ✅ arXiv 200, tam metin özet düzeyinde okundu (4.644 karakter)
**URL:** https://arxiv.org/abs/2610.38883

**ÖZET:** Eva Vivalt'ın ön baskısı, üretken yapay zekânın sosyal bilimlerde henüz kurumsallaşmamış bir işi yapıp yapamayacağını soruyor: bir müdahalenin etkisini, sonucu görmeden, yalnızca ön-kayıt metninden tahmin etmek. Tasarım bu literatürün en kolay eleştirisine — veri sızıntısına — doğrudan cevap veriyor. Sonuçları ilk kez 2026'da açıklanmış, AEA RCT Registry ve OSF'te ön-kayıtlı çalışmalar seçiliyor; tahmin istemleri ise bilgi kesme tarihi bu yayınlardan önce olan modellere yöneltiliyor, yani modelin cevabı görmüş olması mümkün değil. İlk aşamada modeller ön-kayıt ve ön-analiz planlarından tahmin edilebilir tedavi etkisi soruları çıkarıyor; ikinci aşamada bu sorulara sayısal tahmin veriliyor. Örneklem 39 makaleden 889 tedavi etkisi, tarama sonrası 33 makaleden 673 etki. En iyi modelde medyan mutlak tahmin hatası 0,054 standart sapma, ortalama mutlak hata 0,093 SD, MSE 0,0218. Bu, iki naif referansın — "etki sıfırdır" ve "etki o dönemin diğer makalelerinin ortalamasıdır" — belirgin biçimde önünde. Vivalt sonucu ihtiyatla çerçeveliyor: tahminlerin politika ve araştırma kararlarını bilgilendirmede değerli olabileceği yönünde ciddi bir alan var. Sınırlar açık: ön baskı hakemsiz; modeller yalnızca ön-kayıt metnini görüyor, saha koşulları ve uygulama sadakati verilmiyor; yayımlanmış literatürle eğitilen modeller yayın yanlılığını devralıyor. Yine de çalışma "etki tahmini"ni bağımsız bir araştırma sorusu olarak kuruyor ve ölçülebilir bir performans eşiği tanımlıyor. Metodolojik olarak en değerli yanı soru üretimini tahminden ayırması: bu ayrım, insan uzmanların soru yazmasına bağlı kalan önceki tahmin platformlarının ölçek sınırını aşmanın yolunu gösteriyor. Çalışmanın göstermediği şey ise kritik: bir tahminin doğru çıkması, o müdahalenin başka bir bağlamda da aynı etkiyi üreteceği anlamına gelmiyor. Vivalt'ın ölçtüğü şey açıklayıcı güç — uygulama kararı için gereken dış geçerlilik değil. Yine de bu, saha bütçesi ayrılmadan önce hangi müdahalelerin umut vaat ettiğini görmenin en ucuz yolu olarak duruyor.

**Anahtar noktalar:**
- Sızıntı kontrolü tasarımın merkezinde: model kesme tarihi < yayın tarihi.
- 673–889 etki üzerinde medyan hata 0,054 SD; "sıfır etki" ve "dönem ortalaması" referanslarından iyi.
- Soru üretimi ile tahmin ayrı aşamalar — ölçeklenebilirliğin koşulu.
- Aynı yazarın adı geçen The Agency Fund "Prediction League" yarışmasının bilimsel dayanaklarından biri.

**Türkiye notu:** Türkiye'de politika değerlendirmesi pahalı ve seyrek; bir müfredat reformunun veya sosyal yardım kademelendirmesinin etkisini ölçmek için RCT kurmak yıllar alıyor. Ön-kayıt metni varsa etkinin makul doğrulukla önceden tahmin edilebilmesi, "önce pilot, sonra ölçüm" döngüsünü hızlandırabilir. Asıl boşluk şurada: bu modeller ağırlıklı İngilizce literatürle eğitiliyor, Türkiye'deki etki büyüklükleri ve uygulama kalitesi farklı olduğu için tahminler sistematik kayabilir. Gerçek katkı, aynı yöntemi Türkiye'de sonuçlanmış programlarla sınamak olur.

---

### 2. Katılımcılar da Yapay Zekâ Kullanıyor: 259 Kişilik Örneklem 29'a Nasıl Düştü? (Goetze, 2026)

**Künye:** Julia Goetze, "And now what? An experiential case report of participant AI use in survey research", *Research Methods in Applied Linguistics* 5(3), 100392, Aralık 2026 (online-first 3 Kasım 2026) · DOI 10.1016/j.rmal.2026.100392 · Elsevier, abonelikli
**Erişim:** ⛔ ScienceDirect 403 (Cloudflare); özet + bölüm başlıkları üzerinden okundu
**URL:** https://www.sciencedirect.com/science/article/abs/pii/S2772766126000984

**ÖZET:** Julia Goetze'nin deneyimsel vaka raporu, anket araştırmalarında yapay zekâ tartışmasının ihmal edilen tarafına bakıyor: yazarlar, hakemler ve editörler değil, katılımcılar. Yazarın ACTFL hibesiyle yürüttüğü karma yöntemli ankette — ABD'deki Almanca öğretmenleri ve program yöneticilerinin eleştirel, adalet odaklı müfredat geliştirmeye ilişkin inançları — üç açık uçlu sorunun yanıtlarında yapay zekâ kullanımı şüphesi doğuyor. Şüphe analitik örneklemi 259 katılımcıdan 29'a indiriyor: 180 kişi yapay zekâ şüphesiyle, 50 kişi eksik veya İngilizce olmayan veri ve uygunluk kriteri nedeniyle dışlanıyor. Yani veri kaybının yaklaşık %70'i tek bir yoruma dayanıyor. Yazar belirsizlik altında verdiği kararları belgeliyor: çok aşamalı tarama, veri işaretleme ve beş kişilik uzman değerlendirici paneli. Kendi ifadesiyle değerlendiriciler birbirinden belirgin biçimde farklılaşıyor; bağımsız insan yargısı eklemek şüpheyi çözmüyor, belirsizliği azaltmıyor. Rapor üç yapısal sorunu görünür kılıyor: yanıtın kime ait olduğunun belirlenememesi, katılımcı yapay zekâ kullanımının veri kalitesi ve geçerliliğe etkisi, ve araştırmacının kendi eleme kararlarının çalışma geçerliliğine etkisi. Goetze vakayı model olarak sunmuyor; alanın kanıta dayalı, saha çapında kılavuzlara ihtiyacı olduğunu söylüyor. Raporun en değerli yanı şeffaflığı: dışlama gerekçeleri, panelin işleyişi ve tarama adımları raporun parçası, böylece başka bir araştırmacı aynı veriyle farklı sonuca varıp varamayacağını görebiliyor. Raporun aktarılabilir dersi, şüphenin kendisinden çok şüpheyle ne yapıldığı: aynı veri seti, farklı bir eşik ve farklı bir dışlama kuralıyla tamamen farklı bir örnekleme ve dolayısıyla farklı sonuçlara götürebilirdi. Goetze bu nedenle şeffaflığı bir erdem olarak değil, geçerliliğin ön koşulu olarak sunuyor. Raporda eksik kalan şey ise nicel bir eşik: hangi sinyal kombinasyonunun yapay zekâ sayılacağına dair ölçüt verilmiyor, bu da bulguların başka sahalara aktarılmasını zorlaştırıyor.

**Anahtar noktalar:**
- 259 → 29 katılımcı; kaybın %70'i "AI şüphesi" yorumundan.
- Beş uzmanlı panel belirsizliği çözmedi — şüphe sinyalleri kesin kanıt değil.
- Yazarlık atfı (authorship) teknik olarak çözülemiyor; sorun etik değil yöntemsel.
- Çağrı: önleyici strateji ve saha çapında kılavuz; mevcut öneriler "en iyi uygulama" iddiası taşımıyor.

**Türkiye notu:** Türkiye'de akademik anket örneklemleri çoğu zaman 100–300 kişi. Goetze'nin yaşadığı ölçekte bir kayıp (259'dan 29'a) burada çoğu saha çalışmasını tamamen bitirir; yani "AI şüphesi varsa ne yapılır" sorusu bir yöntem tercihi değil, çalışmanın kaderi. Bu nedenle şüphe eşiği, tarama prosedürü ve dışlama gerekçeleri veri toplanmadan önce — ön-kayıtta ya da en azından yöntem notunda — tanımlanmalı. İkinci risk ölçüm hatası: açık uçlu sorular kutuplaşma, hoşgörü ve çocuk hakları gibi hassas konularda sık kullanılıyor; katılımcıların ChatGPT'ye yazdırdığı yanıtlar homojen ve olumlu tonda geldiği için varyansı yapay biçimde düşürebiliyor. Üçüncüsü, kurumsal: Türkiye'de etik kurulların ve dergilerin bu konuda yazılı bir standardı yok, karar tamamen araştırmacının kişisel yargısına kalıyor.

---

### 3. Anket Maddesini Katılımcının Kendi Önceliğinden Üretmek (Velez & Ewig, 2026)

**Künye:** Yamil Velez, Alec Ewig, "Retrieval-Augmented Surveys for Measuring Political Representation", *Political Analysis* (CUP), ss. 1–16, 3 Kasım 2026 · DOI 10.1017/pan.2026.10064 · CC BY açık erişim
**Erişim:** ⚠️ CUP 500 + 8,9 bin karakter (kısmi); künye ve bulgular doğrulandı
**URL:** https://www.cambridge.org/core/journals/political-analysis/article/retrievalaugmented-surveys/2D43DFC0765382818BD8D402C905175B

**ÖZET:** Velez ve Ewig'in *Political Analysis* makalesi, klasik temsil ölçümünün en bilinen kısıtını hedefliyor: anket maddeleri araştırmacının seçtiği sabit bir konu listesine bağlıdır, yani seçmenin gerçekten önemsediği ama ankette sorulmamış bir konu ya "temsil edilmiş" sayılır ya da hiç görünmez. Önerilen yöntem dört adımda işliyor. Birincisi, Kongre faturaları gibi kurumsal bir metin tabanı kısa ve nötr özetlere çevriliyor. İkincisi, katılımcı kendi cümlesiyle en önemsediği tek konuyu yazıyor ve kısa bir netleştirme adımında kapsam ile yön onaylanıyor. Üçüncüsü, gömme modeliyle katılımcının önceliğine en yakın üç komşu politika seçilip kişiye özel anket maddesi üretiliyor. Dördüncüsü, bu maddelere destek ölçülüyor ve LLM ile "bu politika kişinin derdini karşılıyor mu" kodlaması yapılıyor. Doğrulama dört metrikle yapılıyor: yüz geçerliliğinde (n=2.000 ABD yetişkini) en yakın komşu politika için %69 "büyük ölçüde/tamamen karşılıyor", %91 en az "kısmen"; el kodlaması denetiminde LLM insan kodlayıcılarla %83,6 uyuşuyor; panel kararlılığında üç hafta sonra en yüksek destek düzeyini koruma %82; tailored conjoint'te en büyük etki yine komşu politikada. Kongre uygulamasında önceliğini beyan edenlerin %77'sinin en az bir karşılayan faturası var, ama yalnız %12'si Genel Kurul'a ulaşmış; eşleşmelerin %84'ü komisyonda duruyor. Yorum: dışlanma "gündeme hiç girmeme" biçiminde değil, komisyon aşamasında tıkanma biçiminde işliyor. Sınır: örneklemin %15'i hiçbir öncelik beyan etmiyor ve bu grup düşük gelirli, düşük eğitimli, daha az oy kullanan kesim. Yöntemin asıl sınırı örneklem değil kapsam: yalnızca ABD Kongresi ve İngilizce metinlerle çalışılmış, parti programı ya da belediye bütçesi gibi alanlarda test edilmemiş. Yine de katkı yöntemsel: sabit madde varsayımını görünür kılıyor ve seçmenin neyi önemsediği sorusunu araştırmacının listesinden katılımcının kendi cümlesine taşıyor.

**Anahtar noktalar:**
- Sabit madde yerine katılımcıya özel madde; gömme + LLM kodlama birlikte.
- Kongre'de kapsanma %77, ilerleme %12; tıkanma komisyonda.
- Katılımcıların %15'i susuyor — temsilin "üçüncü yüzü" ölçüm dışında kalıyor.
- Yöntem modüler: belediye bütçesi, parti programı, kural koyma alanlarına taşınabilir (henüz test edilmedi).

**Türkiye notu:** Türkiye'de temsil ölçümü neredeyse tamamen sabit madde mantığıyla yapılıyor: seçmen-milletvekili görüş uyumu, parti programı-seçmen önceliği karşılaştırması, ara sıra "hangi sorun önemli" anketleri. TBMM verisi bu yöntem için elverişli — kanun teklifleri, komisyon gündemleri ve tutanaklar açık; yani "kapsanma" ve "ilerleme" ölçülebilir. Türkiye'deki ampirik boşluk tam burada: hangi seçmen önceliğinin gündeme girdiği, hangisinin komisyonda öldüğü sistematik olarak ölçülmüyor. Makalenin "tıkanma komisyonda" bulgusu, özellikle muhalefet partilerinin tekliflerinde test edilebilir güçlü bir hipotez. Metodolojik uyarı da var: Türkiye'de anketler "hangi parti" ekseni üzerine kurulduğu için seçmenin kendi önceliği hiç sorulmuyor; bu yöntem o boşluğu doldurmanın en ucuz yolunu gösteriyor.

---

## 🧭 ETİK VE TEORİ

### 4. Türkiye'de Elit Etnografyası: Erişim Bir Ahlak Ekonomisidir (Soyata, 2026)

**Künye:** Sezai Doruk Soyata (Koç Üniversitesi), "Gatekeeping, Rapport, and Ethical Vulnerability: Elite Ethnography on Sensitive Topics in Turkey", *International Journal of Qualitative Methods* 25 (2026) · DOI 10.1177/16094069261455129 · CC BY-NC 4.0 · 66 kaynak
**Erişim:** ⛔ SAGE 403 (Cloudflare, 6.127 bayt); yayıncı özeti ve künye üzerinden okundu
**URL:** https://doi.org/10.1177/16094069261455129

**ÖZET:** Soyata'nın makalesi, otoriter ve eşitsiz bir bağlamda elitlerle yapılan etnografyada erişimin nasıl üretildiğini ve araştırmacının bu süreçte nasıl kırılganlaştığını soruyor. Dayanak, Türkiye'de muhafazakâr iş elitleriyle bir yıl süren saha çalışması. Temel argüman net: erişim resmî izin, kurumsal aidiyet veya görüşmeci becerisiyle açıklanamaz; erişim güven, ihtiyat ve itibar riski etrafında kurulan ilişkisel-ahlaki değerlendirmelerle üretilir. Kiminle görüşülebileceği, neyin sorulabileceği ve neyin söylenemez kalacağı bu değerlendirmelerle belirlenir. Yazı üç kavramsal katkı sunuyor. Birincisi, kapı bekçiliği bir "erişim ahlak ekonomisi" olarak tanımlanıyor: tanıştırmalar, referanslar, geciktirmeler ve reddetmeler, araştırmacının konumsal güvenliği hakkında verilen yargılardır; kapı bekçisi izin veren değil, araştırmacının riskini fiyatlayan aktördür. İkincisi, rapport bir görünürlük ve anlam siyaseti olarak okunuyor: ton, tempo, geri çekilme ve yönetilen yakınlıkla kalibre edilir; sessizlik, tıkanan etkileşim ve "yumuşatma" talepleri başarısızlık değil, kabul edilebilir sorgunun sınırlarının kanıtıdır. Üçüncüsü, etik kırılganlık: araştırmacının konumu ihtiyari güvene bağlı kaldığı için süreklilik kazanmaz, erişim prosedürel olarak güvenceye alınmış değil sürekli müzakere edilen bir şeydir. Sonuç: siyaseten hassas ve liberal olmayan bağlamlarda kalitatif araştırma, etik kurul onayıyla çözülen bir mesele değil, saha boyunca yeniden kurulan bir ilişki rejimidir. Sınır: tek araştırmacı, tek saha, tek elit grubu; iddia istatistiksel değil analitik genelleme düzeyinde. Makalenin göstermediği şey, bu ilişkisel-ahlaki rejimin bilgi üretimini nicelik olarak nasıl biçimlendirdiği: hangi soruların hiç sorulamadığı, hangi vakaların örneklemden düştüğü ölçülmüyor. Bu, tek saha çalışmasının kaçınılmaz sınırı; ama yöntem bölümüne yazıldığında başka araştırmacılar için karşılaştırılabilir bir taban oluşturuyor. Türkiye'de benzer saha çalışmalarının yöntem eklerinde böyle bir erişim günlüğü tutması, alanın en hızlı iyileşebileceği yer. Bu aynı zamanda lisansüstü tez danışmanlığında en çok atlanan aktarım noktası.

**Anahtar noktalar:**
- Erişim prosedürel değil ilişkisel-ahlaki: güven + ihtiyat + itibar riski.
- Kapı bekçisi bir "risk sigortacısı"; referans veren kişi itibarını rehin veriyor.
- Sessizlik ve "bunu yazma" talepleri veri kaybı değil, sınırın kanıtı.
- Etik kurul onayı erişimi garanti etmiyor — etik saha boyunca süren pratik.

**Türkiye notu:** Türkiye'de saha araştırması yapan herkesin bildiği ama yöntem bölümüne yazmadığı şeyi bu makale kavramsallaştırıyor. Muhafazakâr iş elitleriyle çalışırken erişim, kurumsal ilişkilerden çok tanışıklık zincirlerine bağlı; zincir kopunca saha da bitiyor. Bu, genç araştırmacılar için görünmez bir kariyer riski: erişimi olan araştırmacı yöntem bölümünde bunu yazmadığı için, erişimi olmayan araştırmacı kendi başarısızlığını kişisel yetersizlik olarak okuyor. İkinci katkı, lisansüstü eğitimde "söylenemez olan"ın nasıl öğretileceği: sessizliği veri kaybı olarak kodlayan tez kılavuzları, aslında sahanın en bilgilendirici kısmını çöpe atmayı öğretiyor.

---

### 5. Yapay Zekâ Sosyolojik Kuramı Operasyonelleştirebilir mi? Bir Kuram-Değiştirme Vakası (Schroeder vd. & Lundberg, 2026)

**Künye:** Ralph Schroeder, Mike Thelwall, Arthur Thomas, *Theory and Society* 55, makale 67 (27 Temmuz 2026) + Henrik Lundberg yorumu, 55, makale 89 (9 Ekim 2026) · DOI 10.1007/s11186-026-09738-3 · her ikisi CC BY 4.0
**Erişim:** ✅ Springer 200, tam metin ve yorum okundu
**URL:** https://doi.org/10.1007/s11186-026-09738-3

**ÖZET:** *Theory and Society*'nin yayımladığı makale ve ona yazılan yorum, "yapay zekâ sosyolojik kuramı operasyonelleştirebilir mi" sorusunu somut bir vakada tartışıyor. Schroeder, Thelwall ve Thomas, Randall Collins'in *The Sociology of Philosophies* kitabındaki öğretmen-öğrenci soyağaçlarını 20. yüzyıl ortasından bugüne uzatıyor; OpenAlex, Scopus, PhilPapers gibi bibliometrik taban çizgileri kuruyor ve üç LLM'e Collins'in ilkelerini uygulayarak hangi öğrencilerin gelecekte "eminent" olacağını tahmin ettiriyor. Bulgu iki katmanlı. Bibliometrik sıralamalar birbirinden çarpıcı biçimde ayrışıyor: OpenAlex'te en çok atıf alan Rorty diğer listelerin hiçbirinde yok. LLM'ler kuramsız verildiğinde yalnızca ünlü kamusal entelektüelleri (Sartre, Foucault, Butler, Žižek) sıralıyor ve Collins'in çekirdek tanımına uymuyor; kuram verildiğinde Chalmers, Nussbaum ve Williamson öne çıkıyor; aynı soru Haziran 2026'da ChatGPT 5.5'e sorulduğunda cevaplar tamamen değişiyor. Lundberg'in itirazı keskin: makale, Claude'un ürettiği ve Collins'in bizzat onayladığı beş ilkeli özeti değil, ChatGPT'nin yedi ilkeli özetini kullanıyor; bu özette Collins'in **yapısal sıkışma** mekanizması kayboluyor ve yerine "kültürel/tarihsel bağlamla rezonans" gibi genel bir dışsalcı önerme geçiyor. Lundberg ayrıca atfın yanlış sayfalara gittiğini gösteriyor. Sonuç: tahminler artık Collins'in kuramından türetilmiş sayılamaz, çünkü model kuramı uygulamakla kalmayıp değiştirmiş oluyor. Yazarlar yöntemi "kısmen yeniden üretilebilir" olarak sunuyor; İngilizce ve dergi yanlılığı, kitap atıflarının sayılamaması ve LLM'lerin kara kutu davranışı genellenebilirliği sınırlıyor. Yazarların kendi kabul ettiği sınırlar da öğretici: kitap atıflarının büyük ölçüde sayılamaması, İngilizce ve dergi yanlılığı, modellerin sürüme göre farklı cevap vermesi. Bu, tek bir LLM çıktısının kuramın uygulanışı olarak sunulmasının neden riskli olduğunu gösteriyor. Makalenin asıl katkısı bu yüzden bir tahmin değil, bir uyarı: kuramı özetleten her araştırma, özetin kuramı koruyup korumadığını ayrıca denetlemek zorunda. Bu denetimin nasıl yapılacağı ise henüz yöntem kitaplarında yazmıyor.

**Anahtar noktalar:**
- Bibliometrik listeler birbiriyle uyuşmuyor; "ün" ölçümü araca bağlı.
- LLM kuramı uygulamıyor, özet üzerinden dönüştürüyor.
- Collins'in onayladığı özet ile analizde kullanılan özet farklı — yeniden üretilebilirlik sorunu.
- Yöntemsel ders: LLM çıktısını "kuramın uygulanışı" saymadan önce özetin kendisi denetlenmeli.

**Türkiye notu:** Türkiye'de sosyal bilimlerde LLM kullanımı hızla yaygınlaşıyor ama neredeyse tamamen verimlilik ekseninde tartışılıyor: literatür taraması, özet çıkarma, kod yazma, çeviri. Bu makale-ve-yorum çiftinin asıl değeri kuramsal kayma uyarısı. Bir kuramı LLM'e özetletip o özetle analiz yaptığınızda model kuramı uygulamıyor, sessizce başka bir kurama dönüştürüyor; Lundberg'in gösterdiği mekanizma bunu net ortaya koyuyor — sayıya çevrilmesi zor, sezgiye aykırı kavram düşüyor, yerine herkesin kabul edeceği ama kuramsal olarak boş bir önerme geliyor. Bu risk Türkiye'de daha yüksek: Türkçe sosyal bilim literatüründe kuramlar sıklıkla Batılı kaynaklardan alınan ikincil özetler üzerinden dolaşıma giriyor ve LLM bu özet zincirine çok daha hızlı bir halka ekliyor. Pratik öneri: tez ve makale yöntem bölümlerinde hangi modelin, hangi sürümün, hangi dilde ve hangi özet üzerinden kullanıldığı yazılmalı.

---

### 6. Empati Tek Kişinin Becerisi Değil: Çift Süreci Çerçevesi (Genzer & Perry, 2026)

**Künye:** Shir Genzer, Anat Perry, "Empathy as a dyadic process", *Nature Reviews Psychology*, ss. 1–16, çevrimiçi 14 Ekim 2026 · DOI 10.1038/s44159-026-00624-4 · abonelikli
**Erişim:** ✅ nature.com 200, tam metin (66,8 bin karakter)
**URL:** https://www.nature.com/articles/s44159-026-00624-4

**ÖZET:** *Nature Reviews Psychology*'de yayımlanan derleme, empati araştırmasının yerleşik odağını tersine çeviriyor: empati, empati kuran kişinin özelliği ya da performansı olarak değil, iki partnerin karşılıklı olarak kurduğu süregiden bir süreç olarak kavramsallaştırılıyor. Yazarlar empatik etkileşimi üç unsurlu bir yapı olarak tanımlıyor: bir empati kuran, bir alıcı ve ikisinin birlikte kurduğu, olumlu duygulanım rezonansı ve birliktelik üretebilen ortak deneyim. Empatinin bilişsel, duygusal ve motivasyonel bileşenleri bu çift merceğinden tek tek ele alınıyor: her bileşenin hem veren hem alan tarafında nasıl tezahür ettiği ve partnerlerin karşılıklı ipuçlarının bu bileşenler üzerinden birbirini nasıl etkilediği gösteriliyor. Bu, empatiyi tek yönlü bir algılama-hissetme-yanıt verme akışından, iki tarafın sürekli birbirini kalibre ettiği döngüsel bir etkileşime taşıyor. Derleme alanın üç yapısal boşluğunu işaret ediyor: çalışmaların neredeyse tamamının yabancı çiftlerle yürütülmesi ve ebeveyn-çocuk, romantik partner, arkadaşlık gibi ilişkilerde çift düzeyinde mekanizmaların test edilmemesi; empatinin ağırlıkla olumsuz duygular üzerinden ölçülmesi ve olumlu ya da karışık değerlikte işleyişin bilinmemesi; kesitsel ve tek oturumluk tasarımların ilişki gelişimi boyunca değişimi görememesi. Kuramsal katkı, empati açığını bireysel beceri eksikliği olarak değil etkileşimin ortak ürünü olarak okumayı mümkün kılıyor; bu da empati temelli müdahalelerin tasarımını tek kişiden ilişkiye kaydırmayı gerektiriyor. Derleme yeni ampirik veri üretmiyor; katkısı çerçeve ve araştırma gündemidir. Derlemenin sınırı, çerçevenin ampirik olarak sınanmamış olması: çift düzeyinde mekanizmalar öneriliyor ama hangi bileşenin hangi koşulda belirleyici olduğuna dair veri sunulmuyor. Bu, alanı yeni bir tasarım gündemine açıyor: aynı çifti zaman içinde izleyen, alıcının sinyallerini ölçen ve olumlu duyguları da kapsayan çalışmalar. Kuramsal olarak ise empati müdahalelerinin neden bu kadar sık başarısız olduğuna inandırıcı bir açıklama getiriyor.

**Anahtar noktalar:**
- Empati üç unsurlu ve döngüsel: veren + alan + ortak deneyim.
- Alan yabancı çiftlerle çalışıyor; aile ve yakın ilişki bağlamı boş.
- Olumsuz duygu yanlılığı: empati neredeyse hep acı üzerinden ölçülüyor.
- Müdahale yüzeyi birey değil, ilişkinin kendisi.

**Türkiye notu:** Türkiye'de kutuplaşma tartışması neredeyse tamamen duygusal kutuplaşma üzerinden yürüyor ve çözüm önerileri düzenli olarak empathy'e başvuruyor: STK diyalog programları, gençlik depolarizasyon atölyeleri, medya okuryazarlığı müfredatı. Bu derlemenin en kullanışlı katkısı, o önerilerin sessiz varsayımını bozması: empatiyi empati kuranın becerisi olarak kurgulayan müdahaleler etkiyi tek tarafta arıyor; oysa çift çerçevesi sonucun alıcının ipuçları ve iki taraf arasındaki karşılıklı kalibrasyondan doğduğunu söylüyor. İki bloklu yüksek kimlikleşmiş bir yapıda bu ayrım kritik: karşı tarafa empathy gösterme çağrısı, alıcı tarafında "yine üstten bakıyorlar" tepkisi ürettiğinde müdahale ters etki yapıyor. Aile içi uygulama açısından da önemli — ebeveyn-çocuk empathy çalışmaları alanın en büyük boşluğu, yani "çocuğunla empati kur" tavsiyesinin ampirik temeli sanıldığından çok daha zayıf.

---

## 🌍 GÜNCEL TARTIŞMALAR

### 7. Popülizm ve Komplo Teorileri: İlişki Popülizmde mi, Radikal Sağda mı? (Sawyer, 2026)

**Künye:** Patrick S. Sawyer (Centro de Estudos Sociais, Coimbra), "Populism and conspiracy theories: A cross-national analysis", *Electoral Studies* 104, 103173, Aralık 2026 (çevrimiçi 27 Ekim 2026) · DOI 10.1016/j.electstud.2026.103173 · CC BY 4.0
**Erişim:** ⛔ ScienceDirect 403; yayıncı özeti (223 kelime) + Crossref künyesi
**URL:** https://www.sciencedirect.com/science/article/pii/S0261379426001319

**ÖZET:** Sawyer, popülist ve radikal sağ partilere destek ile komplo teorisi inançları arasındaki ilişkiyi Avrupa ölçeğinde ilk kez sistematik biçimde ayrıştırıyor. Soru üç katmanlı: komplo inançları popülist seçmen tabanında ne kadar yaygın; bu inanç popülizmin ince ideolojisine mi yoksa ona eşlik eden kalın ideolojilere mi ait; ve seçimlerde popülist adaylara oy vermeyle ilişkili mi? Literatürde popülist dünya görüşü ile komplocu inançlar arasında bir yakınsama tespit edilmiş, ama çalışmaların çoğu tek ülkeye odaklandığı için karşılaştırmalı örüntü görülmemiş. Sawyer iki çalışmayla bu boşluğu kapatıyor. Birinci çalışma, Voices of Central Europe veri setiyle 9 Orta Avrupa ülkesinde parti ailesi kontrol edildiğinde komplo inançlarının hem popülist hem radikal sağ partilere destekle güçlü biçimde ilişkili olduğunu, en güçlü yordayıcının radikal sağ ideoloji olduğunu gösteriyor. İkinci çalışma, European Social Survey'nin 24 ülkelik verisiyle benzer ilişkileri gizil popülist tutumlar ve otoriterlik düzeyinde, ayrıca kendini popülist veya radikal sağ bir partiye yakın hissetme ve son seçimde o partiyi oylamayla kuruyor. Sonuç: komplo inançları popülist aday desteğini artırıyor ama ilişki belirgin biçimde sağa yatık; yani komplo inançları popülizmin kendisinden çok ona eşlik eden radikal sağ ideolojiyle taşınıyor. Bu, popülizmin bağımsız bir komplo üretici çerçeve olmadığı yorumunu destekliyor. Sınır: kesitsel veri yön belirsizliğini çözmüyor; örneklem büyüklükleri ve katsayılar yalnızca özetten doğrulanabildi. Pratik sonuç, komplo anlatılarıyla mücadelede hedefin popülizm değil radikal sağ ideolojik paket olması gerektiği; ama yazı bunun nasıl yapılacağına dair bir müdahale önerisi sunmuyor. Bir başka sınır: iki veri seti de 2010'lar sonrası popülist dalgayı kapsıyor, dolayısıyla bulgu popülizmin her yerde aynı işlediği iddiasını desteklemiyor. Türkiye gibi yüksek komplo inancına sahip ama karşılaştırmalı veri setlerinin dışında kalan ülkeler için bu, hem boşluk hem davet.

**Anahtar noktalar:**
- İki bağımsız veri seti (9 Orta Avrupa ülkesi + ESS 24 ülke).
- En güçlü yordayıcı popülizm değil, radikal sağ ideoloji.
- Kesitsel tasarım: komplo inancı mı desteği üretiyor, destek mi inancı?
- Kamu iletişimi için sonuç: komplo anlatılarıyla mücadele "popülizm" değil "radikal sağ" hedefli olmalı.

**Türkiye notu:** Makale Türkiye için hem çok yakın hem tam olarak kapsam dışı — ikisi de öğretici. Yakın, çünkü komplo anlatıları siyasal mobilizasyonun rutin yakıtı ve iktidar-muhalefet bloklarının ikisinde de dolaşımda. Kapsam dışı, çünkü iki veri seti de Türkiye'yi içermiyor: ESS Türkiye'yi kapsamıyor, Voices of Central Europe Orta Avrupa ile sınırlı. Yani "Avrupa karşılaştırmalı" kanıtın tam ortasında, komplo inancı yüksek ve popülist-otoriter bir iktidar bloğuna sahip bir ülkeye denk gelen bir boşluk var. Aktarılabilir bulgu şu: komplo inançları popülizmin ince ideolojisine değil, eşlik eden kalın ideolojiye yükleniyor. Türkiye'de bu, komplo anlatılarını "halkın refleksi" olarak çerçeveleyen popülist okumayı zayıflatıyor ve mücadelenin adresini ideolojik pakete kaydırıyor.

---

### 8. Dezenformasyona Maruz Kalma Sistematik Olarak Eksik Ölçülüyor (Dahlke vd., 2026)

**Künye:** Ross Dahlke, Ryan C. Moore, Danya Adib-Azpeitia, Johan Ugander, Jeffrey T. Hancock, "Multi-Platform Referrers of Misinformation...", *Political Communication* 43(6), 851–887 (çevrimiçi 9 Haziran 2026, basılı sayı 2 Kasım 2026) · DOI 10.1080/10584609.2026.2679492
**Erişim:** ⛔ Taylor & Francis 403 (6.174 bayt); künye + özet + tablo değerleri ikincil doğrulama
**URL:** https://doi.org/10.1080/10584609.2026.2679492

**ÖZET:** Dahlke, Moore, Adib-Azpeitia, Ugander ve Hancock, sosyal medyanın dezenformasyona maruz bırakma etkisini ölçen literatürün sistematik bir kör noktasını gösteriyor: çalışmaların neredeyse tamamı "doğrudan yönlendirici" paradigmasıyla çalışıyor, yani yalnızca sosyal medya ziyaretinden hemen sonra gelen dezenformasyon ziyaretlerini sayıyor. Yazarlar buna "gömülü yönlendirici" paradigmasını karşı koyuyor: platformlar insanları aracı siteler üzerinden ve platformdan ayrıldıktan sonra süren bilgi arama davranışını tetikleyerek de dezenformasyona götürebilir. Bu paradigmayı karşı-olgusal simülasyonla işletiyorlar: YouGov Pulse paneliyle toplanan gerçek tarama verisinden (N = 1.240 kişi, ~21 milyon sayfa ziyareti, 395.936 oturum) her birey için geçiş matrisleri kurup, bir platforma girmek üzere olan yolu o platformun yok olduğu varsayımıyla saptırıyor ve sahte yolu sonuna kadar simüle ediyorlar. Sonuç net: doğrudan paradigma sosyal medyanın rolünü sistematik olarak küçümsüyor; gömülü paradigmayla etkiler 1,5 ila 15 kat daha büyük. Facebook'u kaldırmak tüm dezenformasyon ziyaretlerini %9,25 değil %14,07 azaltıyor; Twitter'da fark çarpıcı: %2,17'ye karşı %12,27. Etkiler ideolojik tipe göre değişiyor: Facebook liberal dezenformasyonda %58,56, Reddit ideolojik olmayan dezenformasyonda %18,22 (doğrudan ölçüm %0,20). İkinci ana bulgu: platform kaldırmanın yüksek kaliteli haber üzerindeki etkisi dezenformasyondan çok daha büyük (Facebook'ta her 1 dezenformasyon ziyaretine karşı 73,3 kaliteli haber ziyareti). Sınır: Markov/IIA varsayımları, uygulama içi akışların görünmemesi, panelin kendini seçme yanlılığı. Yazarların beyan ettiği sınırlar da önemli: sosyal medya dışı kullanıma ikame modellenmiyor, bu da etki büyüklüklerinin muhtemelen altında tahmin edildiği anlamına geliyor; uygulama içi akışlar hiç görünmüyor. Yani gerçek etki ölçülenden daha büyük olabilir; bu politika mesajını güçlendiriyor ama platform kapatma önerisinin maliyet hesabını ağırlaştırıyor. Ölçüm altyapısı olmayan ülkeler için asıl ders yöntemsel: tek adımlı sorular yapısal olarak yanlış.

**Anahtar noktalar:**
- Doğrudan referrer paradigması etkiyi 1,5–15 kat küçültüyor.
- Twitter'da fark beş katın üzerinde (%2,17 → %12,27).
- Platformlar aynı zamanda kaliteli haber kanalı; kaldırma oranı 73,3:1.
- Politika çıkarımı: "hangi platformu kaldırmak neyi değiştirir" sorusu yeniden çerçevelenmeli.

**Türkiye notu:** Türkiye'de dezenformasyon araştırması ağırlıkla anket ve içerik analiziyle yapılıyor; tarayıcı düzeyinde panel verisi neredeyse yok. Bu makale, Türkiye'de yapılabilecek en değerli çalışmanın ne olduğunu gösteriyor: platform içi akış değil, platformdan ayrıldıktan sonraki geçişler. Türkiye'de WhatsApp'ın yaygınlığı düşünüldüğünde, "gömülü yönlendirici" etkisinin ölçülmesi özellikle kritik, çünkü kapalı gruplarda dolaşan içerik tarayıcı verisinde hiç görünmüyor. İkinci aktarım politika düzeyinde: Türkiye'de platform kapatma tartışmaları neredeyse her zaman dezenformasyon ekseninde yürüyor; bu makale, kapatmanın kaliteli haber erişimini çok daha büyük oranda kesebileceğini hatırlatıyor. Üçüncüsü yöntemsel: Türkiye'deki akademik anketlerde "haberi nereden gördünüz" sorusu neredeyse her zaman tek adımlı soruluyor; bu çalışma tek adımlı sorunun yapısal olarak yanlış olduğunu gösteriyor.

---

### 9. Popülist Yönetim Altında Yetişmek: Sıfır Toplamlı İnancın Kuşak İzi (Ajzenman, Aksoy & Pickard, 2026)

**Künye:** Nicolas Ajzenman (McGill/J-PAL), Cevat Giray Aksoy (EBRD/KCL), Harry Pickard (Newcastle), VoxEU/CEPR kolonu, 6 Kasım 2026; altındaki çalışma: SSRN WP 7438339
**Erişim:** ⛔ cepr.org 403 (6.237 bayt); kolon metni ve atıf verileri ikincil kaynaklardan doğrulandı
**URL:** https://cepr.org/voxeu/columns/coming-age-under-populists-zero-sum-legacy-populist-rule

**ÖZET:** Ajzenman, Aksoy ve Pickard'ın VoxEU kolonu, popülist yönetim altında yetişenlerin dünyayı sıfır toplamlı görmeyi öğrendiğini ve bu izin yirmi yıl kaldığını gösteriyor. Soru şu: sıfır toplamlı inançlar popülizmin nedeni olarak biliniyordu, sonucu da olabilir mi? Popülist liderler uzun süre iktidarda kaldığında, biçimlendirici yıllarını 18–25 yaş arasında bu ortamda geçiren kuşaklar etkileniyor mu? Tasarım geniş: Funke vd. (2023) popülist lider sınıflandırması, World Values Survey ve ISSP ile 53 ülkede 260.000'den fazla katılımcı. Her kişi için 18–25 yaş arasının yüzde kaçının popülist hükümet altında geçtiği hesaplanıyor; kimlik stratejisi aynı ülke ve yılda görüşülen ama farklı yıllarda doğmuş kişileri karşılaştırıyor. Bulgular: tam maruziyet ile hiç maruziyet arasında sıfır toplamlı düşünmede +0,09 puan fark var — ABD-Türkiye farkının beşte biri. Algılanan sınıf çatışması da aynı yönde ve 26 yaşında ~0,2 puana çıkıyor, kırklı yaşların ortasına kadar saptanabiliyor. Zamanlama testi kritik: doğum öncesi, çocukluk, ergenlik veya 25 sonrası maruziyette benzer ilişki yok. Etki ekonomik koşullar, demokrasi düzeyi ve lider özellikleri kontrol edildiğinde sürüyor. Mekanizma anlatı ve güven: popülist iktidarda iktidar partisinin anti-elitist söylemi 1 standart sapmadan fazla yükseliyor; BM Genel Kurulu'ndaki 11.000'den fazla konuşma LLM ile puanlandığında sıfır toplamlı çerçeveleme +0,67 SS; bu kuşaklarda bilim insanlarına güven −0,3 SS. Sandığa yansımada maruz kalan kuşaklar popülist partilere olduğu gibi daha fazla oy vermiyor, ama büyüdükleri popülizmin yönündeki uçlara kayıyorlar. Sınır: kolon hakemsiz; sınıflandırma sonuçları doğrudan belirliyor. Kolonun politik sonucu net ama rahatsız edici: büyüme izi silmiyor, dolayısıyla ekonomik iyileşme tek başına kuşak etkisini geri almıyor; hedef kurum güvenilirliği ve gençlik okuryazarlığı olmalı. Yazının göstermediği şey ise mekanizmanın birey düzeyinde nasıl işlediği — okulda mı, medyada mı, aile içinde mi öğreniliyor, veri bunu ayırmıyor. Bu boşluk, Türkiye gibi tek iktidar döneminde birden fazla kuşak yetiştirmiş ülkeler için doğrudan bir araştırma gündemi.

**Anahtar noktalar:**
- 53 ülke, 260.000+ katılımcı; 18–25 yaş maruziyeti ölçülüyor.
- Zamanlama testi nedenselliği destekliyor: yalnız 18–25 aralığında etki var.
- Etki ekonomik krizden değil, söylemden ve büyüme yıllarından geliyor.
- Kurumsal kısıt (mahkeme, parlamento) etkiyi güçlendiriyor — ilginç yön.

**Türkiye notu:** Türkiye bu makalede iki şekilde merkezi. Ölçek olarak: ABD ile Türkiye arasındaki sıfır toplamlı inanç farkı, bulgunun büyüklüğünü anlatmak için kullanılıyor — yani Türkiye ölçeğin üst ucunda. Tasarım olarak: 2000'lerin başından itibaren tek bir iktidar altında biçimlendirici yıllarını geçirmiş birden fazla kuşak var ve WVS/ISSP Türkiye dalgaları mevcut. Yapılabilecek test üç adım: doğum kohortlarını 18–25 yaş maruziyetine göre ayırmak, aynı dalga içinde kohortları karşılaştırmak ve sıfır toplamlı ölçek ile kurumlara ve bilime güven arasındaki bağı test etmek. Kritik uyarı: sonuç, Türkiye'nin popülist lider sınıflandırmasında nasıl kodlandığına doğrudan bağlı; Funke vd. bilinçli olarak yüksek eşik kullandığı için Türkiye'nin kodlanması hassas bir tercih. Yine de çocuk ve gençlik politikası açısından doğrudan sonuç var: sıfır toplamlı dünya görüşü okulda öğretilen bir "değer" değil, kurumsal ortamın yan ürünü.

---

## 📖 OKUMA LİSTESİ

| Zorluk | Makale | Konu | Öncelik |
|---|---|---|---|
| ●●● | Vivalt — AI Forecast Treatment Effects (arXiv) | Etki tahmini, sızıntı kontrolü | Yüksek |
| ●●○ | Goetze — Participant AI use in surveys (RMAL) | Anket yöntemi, veri kaybı | Yüksek |
| ●●● | Velez & Ewig — Retrieval-Augmented Surveys (PA) | Temsil ölçümü, LLM kodlama | Orta |
| ●●○ | Soyata — Elite Ethnography in Turkey (IJQM) | Etik, erişim, saha | Yüksek |
| ●●● | Schroeder vd. + Lundberg — Collins/LLM (T&S) | Kuram operasyonelleştirme | Yüksek |
| ●●○ | Genzer & Perry — Empathy as dyadic process (NRP) | Sosyal psikoloji, çift süreci | Orta |
| ●●○ | Sawyer — Populism & conspiracy (Electoral Studies) | Karşılaştırmalı siyaset | Orta |
| ●●● | Dahlke vd. — Multi-platform referrers (Pol Comm) | Dezenformasyon ölçümü | Yüksek |
| ●●○ | Ajzenman, Aksoy & Pickard — Populist legacy (VoxEU) | Kuşak etkisi, sıfır toplamlı inanç | Yüksek |
| ●○○ | Allcott vd. — School Phone Bans (QJE) | Eğitim politikası | Yüksek* |
| ●●○ | Özkaya & Monrad — Youth anger norms (JYS) | Gençlik, duygusal sermaye | Orta |
| ●●○ | Wu & Goh — Intergenerational AI health misinfo (Health Comm) | Kuşak, görsel çerçeveleme | Orta |
| ●●○ | Briones — Climate misinformation in Türkiye (IPC) | Türkiye, iklim dezenformasyonu | Orta |
| ●○○ | Willingham — Critical Thinking (AFT) | Eğitim, bilişsel bilim | Orta |
| ●●○ | Na vd. — Behavioral Profiles for LLM Simulation (arXiv) | Simülasyon, dış-dağılım | Orta |
| ●●○ | Moses & Hartzbech — AI Emotion Metrics (QRCA) | Nitel yöntem, duygu ölçümü | Düşük |
| ●●○ | Young & de-Wit — Affective Polarization Within Parties (Pol Psych) | Parti içi kutuplaşma | Düşük |
| ●●○ | Wichgers vd. — Survey measurement accuracy (PA) | Ölçüm hatası | Düşük |

\* QJE çalışması 2 Kasım KURATOR bülteninde derinlemesine işlendi; burada yalnızca bütünlük için listeleniyor.

---

## 📚 KAYNAKÇA

1. Vivalt, E. (2026-10-28). "Can Artificial Intelligence Forecast Treatment Effects in Economics?" arXiv:2610.38883. https://arxiv.org/abs/2610.38883
2. Goetze, J. (2026-11-03). "And now what? An experiential case report of participant AI use in survey research." *Research Methods in Applied Linguistics* 5(3), 100392. https://doi.org/10.1016/j.rmal.2026.100392
3. Velez, Y. & Ewig, A. (2026-11-03). "Retrieval-Augmented Surveys for Measuring Political Representation." *Political Analysis*, 1–16. https://doi.org/10.1017/pan.2026.10064
4. Soyata, S. D. (2026). "Gatekeeping, Rapport, and Ethical Vulnerability: Elite Ethnography on Sensitive Topics in Turkey." *IJQM* 25. https://doi.org/10.1177/16094069261455129
5. Schroeder, R., Thelwall, M. & Thomas, A. (2026-07-27). "Can AI operationalise sociological theory?" *Theory and Society* 55:67. https://doi.org/10.1007/s11186-026-09738-3
6. Lundberg, H. (2026-10-09). Yorum: "On summarising and reshaping Collins." *Theory and Society* 55:89.
7. Genzer, S. & Perry, A. (2026-10-14). "Empathy as a dyadic process." *Nature Reviews Psychology*, 1–16. https://doi.org/10.1038/s44159-026-00624-4
8. Sawyer, P. S. (2026-10-27). "Populism and conspiracy theories: A cross-national analysis." *Electoral Studies* 104:103173. https://doi.org/10.1016/j.electstud.2026.103173
9. Dahlke, R., Moore, R. C., Adib-Azpeitia, D., Ugander, J. & Hancock, J. T. (2026). "Multi-Platform Referrers of Misinformation." *Political Communication* 43(6), 851–887. https://doi.org/10.1080/10584609.2026.2679492
10. Ajzenman, N., Aksoy, C. G. & Pickard, H. (2026-11-06). "Coming of age under populists: the zero-sum legacy of populist rule." VoxEU/CEPR. https://cepr.org/voxeu/columns/coming-age-under-populists-zero-sum-legacy-populist-rule
11. Allcott, H., Baron, J., Dee, T., Duckworth, A. L., Gentzkow, M. & Jacob, B. (2026-10-30). "The Effects of School Phone Bans: National Evidence from Lockable Pouches." *QJE*, qjag050. https://doi.org/10.1093/qje/qjag050
12. Özkaya, B. & Monrad, M. (2026-11-03). "Youth anger norms and emotional capital across social fields." *Journal of Youth Studies*, 1–18. https://doi.org/10.1080/13676261.2026.2757654
13. Wu, Q. & Goh, D. H.-L. (2026-11-03). "Intergenerational Perspectives on AI-Generated Health Misinformation." *Health Communication*, 1–11. https://doi.org/10.1080/10410236.2026.2757113
14. Briones, F. (2026-11). "Beyond climate denial: misinformation on climate extremes and policies in Türkiye." IPC–Mercator Analysis. https://ipc.sabanciuniv.edu/en/publications
15. Willingham, D. T. (2007). "Critical Thinking: Why Is It So Hard to Teach?" *American Educator* 31(2), 8–19. https://www.aft.org/ae/summer2007/willingham
16. Na, Zhu, Cross & Bakker (2026). "Designing Behavioral Profiles for Language Model Simulation..." arXiv:2611.00661. https://arxiv.org/abs/2611.00661
17. Moses & Hartzbech (2026-10-20). "AI-Driven Emotion Metrics in Qualitative Research." *QRCA Views*. https://www.qrcaviews.org/2026/10/20/
18. Young & de-Wit (2026). "Affective Polarization Within Parties." *Political Psychology* 46(1), 49–69. https://doi.org/10.1111/pops.12973
19. Wichgers vd. (2026). "How accurate are survey measurements of objective phenomena?" *Political Analysis*.
20. Velez, Y. (2026-10). "Filedrawer: AI-generated research reports for unpublished studies." https://filedrawer.org/

---

*Bu derleme 7 Kasım 2026, 14:00 itibarıyla 1–7 Kasım 2026 dilimindeki 63 benzersiz kayıttan üretildi. Özetlerde yayıncı özeti, Crossref/OpenAlex künyesi ve erişilebilen tam metin birlikte kullanıldı; erişim engeli olan kayıtlarda özetin ötesinde iddia üretilmedi.*
