# AKADEMİK ÖZEL TARAMA — Haftalık Derleme

**Tarih:** 2026-11-21
**Kapsam:** 16–21 Kasım 2026 (Pazartesi 16 Kasım sayısından sonraki kayıtlar)
**Havuz:** 33 benzersiz kayıt → **30 yeni**; bunların **27'si** AKADEMİK ÖZEL etiketli
**Hazırlayan:** KURATOR Araştırma Ekibi
**Önceki sayı:** `2026-11-14_akademik_ozel.md`

---

## 🧭 YÖNETİCİ ÖZETİ

Bu haftanın akademik akışı üçe ayrılıyor ve üçü de aynı sorunun etrafında dönüyor: **bilgi üretiminin altyapısı kimin elinde, nasıl doğrulanıyor ve ne kadar sağlam?**

**Birinci hat, araştırmanın kendisinin nesneleşmesi.** Bu hafta üç kayıt, yapay zekânın bilimsel pratiğin *içine* nasıl girdiğini ölçüyor. Matt Artz, *Anthropological Forum*'da "çok-ajanlı etnografi" (MAE) önerisiyle LLM ajanlarını araştırma yaşam döngüsünün tamamına yerleştiriyor ve epistemolojik merceği birinci sınıf tasarım parametresi yapıyor. Microsoft Research ekibi (Alsobay, Rothschild, Hofman, Goldstein), *CSCW*'de ön kayıtlı bir deneyle **1.475 katılımcı ve 281 canlı grup** üzerinde GPT-4o kolaylaştırıcının paylaşılan bilgi miktarını **Cohen's d = 0,61** düzeyinde artırdığını gösteriyor — üstelik insan kolaylaştırıcıdan belirgin biçimde daha iyi. Kousha ve Thelwall ise *Scientometrics*'te ChatGPT sonrası akademik İngilizcede **"delve"** teriminin Scopus makalelerinde 2022'de %0,07'den 2024'te %1,05'e (**+%1.360**) çıktığını, karşılaştırma terimi *investigate*'in yalnızca %8,9 arttığını gösteriyor.

**İkinci hat, meşruiyetin tarihsel ve bilişsel temeli.** Melinda Baldwin'in MIT Press monografisi, hakemliğin sandığımız kadar eski olmadığını — 19. yüzyıl başında ortaya çıktığını ve **"peer review" ile bilimsel meşruiyet arasındaki zorunlu bağın Soğuk Savaş'ta kurulduğunu** — arşiv çalışmasıyla gösteriyor. Cory Clark, "hayalet çoğunluk" (phantom majority) kavramıyla 500 milyonluk bir platformda %0,01'in **50.000 kişiye** denk gelmesinin kamuoyu algısını nasıl çarpıttığını modelliyor. Li, Grueneisen ve Tomasello ise sosyal kimliğin evrimsel olarak özgün biçiminin etnisite değil **ahlaki kimlik** olduğunu savunuyor.

**Üçüncü hat, platform ölçeğinde siyasal davranış.** Melito ve Zulianello, İtalya'nın Fratelli d'Italia partisi üzerinden popülist radikal sağın başarısını **partinin kendi anlatısı** üzerinden okuyor (21 parti temsilcisiyle derinlemesine görüşme). McWagner ve Kidd, duygusal kutuplaşma ile anti-demokratik tutumlar arasındaki ilişkinin **doğrusal olmadığını** ve iki partinin seçmenleri arasında asimetrik işlediğini gösteriyor. Malhotra ve **31 yazarlı** konsorsiyum, 2020 ABD seçimi boyunca **180 milyondan fazla** Facebook kullanıcısının arkadaşlıktan çıkarma davranışını günlük düzeyde izliyor — ancak bu kayıt **künye düzeyinde** kaldı, bulgular doğrulanamadı.

**Haftanın metodolojik dersi.** Bu sayıdaki 16 çözümlenmiş yayıncı adresinin **10'u (%62,5)** Scrapling'de engelli. En çarpıcı iki örnek: `osf.io` ve `mdpi.com` **HTTP 200** döndürüyor ama sırasıyla **3 karakter** ve **0 karakter** metin veriyor. Yani "200 = erişilebilir" varsayımı bu ortamda yanlış; her kayıtta `status`, gövde baytı ve metin uzunluğu birlikte okunmalı. Buna karşılık iki kaynak bu hafta açıldı: Boston Review (28.680 karakter) ve Harvard CEPR (13.626 karakter) artık tam metin veriyor — coğrafi/CDN bazlı engeller zamana göre değişiyor.

**KURATOR notu.** Bu hafta AKADEMİK ÖZEL havuzunda çocuk/genç kesişimi zayıf: 27 kaydın yalnızca üçü doğrudan çocuk veya gençlik verisi içeriyor (NEET derlemesi, genç akışları ön baskısı, telefon yasakları raporu). Bu üçü KURATOR sayısında işlendi; bu sayı akademik hattın kendi gündemini izliyor. Okuma listesinde öncelik sırası buna göre kuruldu.

---

## 🔬 METODOLOJİ

### 1. Multi-Agent Ethnography: Post-Conventional Anthropological Practice Through Human−AI Collaboration
**Yazar:** Matt Artz (Azimuth Labs; Aalborg Üniversitesi Techno-Anthropology Lab doktora çalışması kapsamında)
**Tarih:** 2026-02-08
**Yayın:** *Anthropological Forum* **36(2): 222–240** — hakemli, **kapalı erişim**, 72 kaynak
**DOI:** 10.1080/00664677.2026.2614501
**Erişim:** ❌ T&F Cloudflare (403 / 6.174 B). Künye Crossref, özet Semantic Scholar; teknik ayrıntılar yazarın kamusal araç dokümantasyonundan (GitHub/PyPI/mattartz.me) çapraz doğrulandı. **Tam metin okunmadı.**

**ÖZET:** Artz, antropolojide "çok-ajanlı etnografi" (MAE) adını verdiği bir araştırma pratiği öneriyor: LLM tabanlı ajanlar, araştırma yaşam döngüsünün tamamında — tasarım, saha, analiz ve yayın — dağıtık bir insan-AI ağı içinde **yapılandırılabilir işbirlikçiler** olarak konumlanıyor. Yazar bu öneriyi antropolojinin kendi yöntemsel yenilik geleneğine yerleştiriyor: çok-mekânlı (multi-sited) etnografiden çok-türlü (multi-species) etnografiye uzanan çizginin bir sonraki halkası. Kuramsal dayanak, AI'nın "siber takım arkadaşı" (cybernetic teammate) kapasitesi. Argümanın teknik kanıtı yazarın geliştirdiği **AI Anthropology Toolkit**: üç ajanı (kod kitabı üretimi, görüşme transkriptini anlamsal bölütleme, kodlama ve tematik analiz) sohbet üzerinden koordine eden bir MCP mimarisi. Araç doğrulanabilir durumda — GitHub deposu (`MattArtzAnthro/AI-Anthropology-Toolkit`, 27 yıldız, 7 çatal, son push 17 Kasım 2026), PyPI paketi (v3.11.1) ve MCP sunucusu (`ai-anthro-mcp`) kamuya açık. Makalenin en özgün yöntemsel hamlesi **epistemolojik merceği** birinci sınıf tasarım parametresi yapması: duruş (tasarım antropolojisi, yorumlayıcı, hesaplamalı, STS) kod kitabını ve analizi şekillendiriyor; `--distinct-codes` / `--overlapping-codes` bayrağı kodların birbirini dışlayıp dışlamadığına dair **yöntemsel kararı** açık hâle getiriyor. Yazarın kabul ettiği sınırlar arasında veri mahremiyeti, LLM çağrılarının **çevresel maliyeti** ve algoritmik yanlılık var; ancak tam metin kapalı olduğu için bu sınırların nasıl ele alındığı doğrulanamadı.

Kitabın alana yaptığı asıl çağrı, ajanı görünmez bir "yardımcı" olarak değil **belgelenmesi gereken bir araç** olarak ele almak: hangi model, hangi sürüm, hangi istem ve hangi mercekle çalıştığı yazılmadan yapılan bir analiz, etnografinin en temel talebi olan yöntemsel şeffaflığı karşılamıyor. Araç setinin sürüm geçmişi (V1 bağımsız Jupyter notebook'lar → V2 MCP ile orkestre edilen ajanlar → V3 web uygulaması, Zenodo'da arşivli) bu şeffaflığın nasıl kurulabileceğine dair somut bir örnek sunuyor.

**TÜRKİYE BAĞLAMI:** Türkiye'de nitel araştırma altyapısı — özellikle saha erişimi kısıtlı alanlarda (göç, çocuk koruma, cezaevi, sağlık) — uzun süredir aynı darboğazla çalışıyor: az sayıda araştırmacı, çok miktarda metin, sınırlı kodlama kapasitesi. MAE'nin Türkiye'de iki somut karşılığı var. **Birincisi, çocuk katılımı araştırmaları:** görüşme transkriptlerinin bölütlenmesi ve tematik kodlanması, çocuklarla yapılan çalışmalarda etik açıdan en hassas aşama; ajan destekli kodlama, insan kodlayıcıya **denetlenebilir** bir ön katman sağlarsa hem süre hem tutarlılık kazanılır, ama çocuk verisinin bulut LLM'e gönderilmesi KVKK açısından sorunlu. Yerel/on-prem model zorunlu hâle geliyor. **İkincisi, yöntem eğitimi:** Türkiye'de lisansüstü nitel yöntem eğitimi çoğu programda tek dönemlik; ajan destekli araçlar bu boşluğu kapatabilir ya da kodlama kararlarının **gerekçesini görünmez** kılarak derinleştirebilir. Belirleyici olan, Artz'ın vurguladığı gibi, merceğin açıkça tanımlanması: ajanın hangi epistemolojik konumdan kodladığı yazılmazsa, çıktı tekrarlanabilir olmaktan çıkar. Türkiye'de TÜBİTAK 1001 kapsamında bir "yerel LLM + nitel analiz" projesi bu boşluğa doğrudan oturur.

**Metodolojik Değerlendirme:** Kuramsal katkı güçlü, ampirik katkı zayıf: makale yeni veri sunmuyor, bir araç ve bir çerçeve öneriyor. Araç doğrulanabilir (kod, paket, sürüm geçmişi açık), ancak ajan çıktılarının insan kodlamasıyla karşılaştırmalı doğruluğu (inter-coder reliability) raporlanmış değil. Tam metin kapalı olduğu için yöntem bölümü ve vaka verisi okunamadı — bu kayıt **çerçeve düzeyinde** değerlendirilmeli.
**Öncelik:** high  |  **Eylem:** akademik_only

### 2. Bringing Everyone to the Table: An Experimental Study of LLM-Facilitated Group Decision Making
**Yazarlar:** Mohammed Alsobay, David M. Rothschild, Jake M. Hofman, Daniel G. Goldstein (Microsoft Research)
**Tarih:** 2026-09-23
**Yayın:** *Proceedings of the ACM on Human-Computer Interaction* **10(6), CSCW059**, Ekim 2026, 36 sayfa, 80 kaynak — hakemli, **CC BY 4.0**; açık sürüm arXiv:2508.08242v2
**DOI:** 10.1145/3816907
**Erişim:** ❌ ACM DL 403 / 6.066 B. Tam metin arXiv PDF'inden okundu; tüm sayılar birincil metinden doğrulandı.

**ÖZET:** Çalışma, LLM'lerin grup karar süreçlerinde kolaylaştırıcı olarak insan kolaylaştırıcıdan daha iyi çalışıp çalışamayacağını ön kayıtlı ve randomize bir deneyle sınıyor. Tasarım: **1.475 katılımcı, 281 canlı grup**, koşul başına 70 geçerli grup, beş kişilik gruplar (insan kolaylaştırıcı koşulunda altı). Görev, klasik bir **"hidden profile"** problemi: dört şehir arasından en iyisini seçmek; bilgi parçaları üyeler arasında dağıtılmış durumda ve doğru karar ancak paylaşılmayan bilginin masaya gelmesiyle mümkün. Dört koşul: (a) kolaylaştırma yok, (b) bir kerelik "bilgi paylaşın" mesajı, (c) insan kolaylaştırıcı, (d) **LLM (GPT-4o) kolaylaştırıcı**. Ana bulgu: LLM kolaylaştırma, paylaşılan bilgi miktarını kolaylaştırmasız koşula göre **2,9 bilgi artırıyor** (t(138) = 3,58; p < 0,001; **Cohen's d = 0,61**); tek seferlik mesaja göre 1,58 (p = 0,021), insan kolaylaştırıcıya göre 2,47 (p < 0,001). Ne tek seferlik mesaj ne de insan kolaylaştırıcı, kontrol koşuluna göre anlamlı fark üretiyor (p = 0,066 / 0,31). Mekanizma "herkesi masaya getirmek": LLM kolaylaştırma **minimum** katkıyı artırıyor (Δ = 0,41 bilgi, p = 0,003) ama maksimumu değiştirmiyor — yani zaten aktif olanları değil, hiç katkı vermeyenleri yukarı çekiyor. Herkesin en az bir bilgi paylaştığı grup oranı LLM koşulunda **%61**, kontrol koşulunda %39. Nedeni davranışta: insan kolaylaştırıcı mesajlarının **%25**'inde belirli bir üyeye doğrudan seslenirken, LLM mesajlarının **%68**'inde sesleniyor. Tartışma uzamıyor (mesaj sayısı koşullar arasında farklı değil, p = 0,71) ama **bilgi yoğunluğu** artıyor (Δ = 0,067, p = 0,002) ve bilgi şehirler arasında daha dengeli yayılıyor (Gini Δ = −0,05, p = 0,017).

Yazarların altını çizdiği nokta, etkinin bir "yapay zekâ sihri" değil **kolaylaştırma davranışının** sonucu olması: LLM her turda üyelere tek tek seslendiği için sessiz üyenin bilgisi masaya geliyor. Aynı davranışı eğitimli bir insan kolaylaştırıcı da sergileyebilir; ama çalışmadaki insan kolaylaştırıcılar bunu yapmıyor.

**TÜRKİYE BAĞLAMI:** Bu bulgu Türkiye'de iki alanda doğrudan uygulanabilir. **Birincisi, katılımcı bütçeleme ve kentsel karar süreçleri:** Türkiye'de mahalle ölçeğindeki katılımcı mekanizmalar (kent konseyleri, imar katılım toplantıları, üniversite-şehir işbirlikleri) sürekli aynı sorunla karşılaşıyor — en sessiz üyenin bilgisi masaya gelmiyor, karar en yüksek sesli azınlığın çerçevesine göre kuruluyor. LLM kolaylaştırıcının "minimum katkıyı" artırması tam bu sorunun çözümü. **İkincisi, kamu istişareleri:** 3 Aralık'ta kapanan EU KIDS Act istişaresi gibi süreçlerde binlerce yorumun tematik olarak dengelenmesi gerekiyor; aynı mantık (herkesi masaya getirme) burada da işler. Ancak iki uyarı var. Birincisi, çalışma **yetişkin, çevrim içi, Prolific örneklemi**; Türkiye'de düşük dijital okuryazarlıklı gruplarda LLM'in "herkese seslenme" davranışı otoriter bir ton olarak okunabilir. İkincisi, kolaylaştırıcının **kim olduğu** siyasi bir soru: belediyenin atadığı bir LLM kolaylaştırıcı, katılımcılar tarafından tarafsız kabul edilir mi? Bu, Türkiye'de yapılması gereken asıl deney.

**Metodolojik Değerlendirme:** Ön kayıtlı, randomize, yeterli güçte (70 grup/koşul), mekanizma analizi ayrıntılı, kod ve veri açık. Sınırlar: tek görev türü (hidden profile), tek model (GPT-4o), tek dil/örneklem (İngilizce, Prolific), kısa vadeli laboratuvar etkisi. "LLM kolaylaştırıcı daha iyi" sonucu, **insan kolaylaştırıcıların eğitimsiz** olduğu bir karşılaştırmaya dayanıyor — eğitimli kolaylaştırıcıyla fark kapanabilir.
**Öncelik:** high  |  **Eylem:** akademik_only

### 3. How much are LLMs changing the language of academic papers after ChatGPT? A multi-database and full text analysis
**Yazarlar:** Kayvan Kousha (Wolverhampton Üniversitesi, Statistical Cybermetrics and Research Evaluation Group), Mike Thelwall (Sheffield Üniversitesi)
**Tarih:** 2026-04-03
**Yayın:** *Scientometrics* (Springer), açık erişim CC BY 4.0, 27 kaynak; ön baskı arXiv:2509.09596
**DOI:** 10.1007/s11192-026-05601-5
**Erişim:** ✅ Tam metin (383.344 B / 56.013 karakter)

**ÖZET:** Kousha ve Thelwall, ChatGPT sonrası akademik yazımdaki dil değişimini on iki "LLM ile ilişkili" terim üzerinden ölçüyor. Veri iki katmanlı: altı veritabanında (Scopus, Web of Science, PubMed, PMC, Dimensions, OpenAlex) 2015–2024 arası başlık/özet/anahtar kelime düzeyi, ayrıca **2,4 milyondan fazla PMC açık erişim tam metni** (2021 – Temmuz 2025) için frekans, birlikte geçiş ve korelasyon analizi. Sonuç net ve büyüklük olarak çarpıcı: Scopus makalelerinde **"delve"** 2022'de %0,07'den 2024'te %1,05'e çıkıyor (**+%1.360**), karşılaştırma terimi *investigate* ise yalnızca %8,9 artıyor. Diğer artışlar: **underscore +%1.062** (*highlight* +%86), **intricate +%727** (*complex* +%18), **meticulous +%611**, showcase +%395, bolster +%361, pivotal +%308, heighten +%273, unveil +%235, nuanced +%210. Tam metin katmanında etki daha da büyük: underscore'ı altı veya daha fazla kez kullanan makale oranı **%10.000'den fazla** artıyor, intricate +%5.400, meticulous +%2.800. "Delve" ise gövdede seyrek kalıyor (makale başına en çok ~5 kez) — yani **özet dostu** bir terim: "This study delves into...". Birlikte geçiş analizi aynı olguyu doğruluyor: 2024'te delve içeren 37.534 PMC makalesinin **%59,3'ü** underscore da içeriyor; underscore–pivotal korelasyonu 2022'de 0,032 iken 2024'te 0,449'a çıkıyor. Disiplin kırılımı da anlamlı: STEM'de artış çoğu alanda %3.000'i aşarken sosyal bilimler ve beşeri bilimlerde çoğunlukla %500'ün altında kalıyor. Yazarlar bulguların **nedensel kanıt sağlamadığını** ve LLM üretimi, LLM ile düzenleme ve genel yazım stili benimsenmesi arasında ayrım yapamadıklarını açıkça yazıyor; ayrıca LLM destekli yazımın dil bariyerini azaltan **olumlu** bir gelişme olabileceğini de not ediyorlar.

Yazarların metodolojik özeni, bulguyu bir "sahtekârlık" iddiasından ayırıyor: frekans artışı nedensel kanıt değil, bir **iz**. Ama izin kendisi önemli — aynı dönemde kontrol terimlerinin artışı tek haneli, LLM terimlerininki dört haneli; bu asimetri, dil değişiminin kaynağını başka bir yerde aramayı zorlaştırıyor. Özet ile gövde arasındaki fark da öğretici: "delve" özet dostu, "underscore" gövde dostu.

**TÜRKİYE BAĞLAMI:** Bu bulgu Türkiye için iki yönlü okunmalı ve ikincisi daha önemli. **Birincisi, akademik değerlendirme:** Türkiye'de doçentlik ve akademik teşvik kriterleri ağırlıkla **yayın sayısı ve dergi indeksi** üzerine kurulu; metnin nasıl üretildiğine dair hiçbir sinyal yok. Bu çalışma, üretim biçiminin ölçülebilir bir iz bıraktığını gösteriyor — yani "LLM ile yazıldı mı" sorusu teknik olarak yanıtlanabilir hâle geliyor. Türkiye'de bunun bir **denetim** aracı olarak kullanılması riskli: ana dili İngilizce olmayan yazarlar LLM'i çeviri ve düzeltme için daha çok kullandığı için, dilsel iz **etnik/dilsel bir işaret** hâline gelebilir ve akademik eşitsizliği derinleştirebilir. **İkincisi, olumlu okuma:** çalışmanın kendi notu — LLM destekli yazımın dil bariyerini azaltması — Türkiye'deki araştırmacılar için somut bir kazanç. YÖK ve TÜBİTAK'ın politikası bu iki okumayı ayırmalı: üretim aracının kullanımı ile bilimsel içeriğin sorumluluğu aynı şey değil. Kurumsal düzeyde yapılabilecek en sağlıklı hamle, LLM kullanımının **beyan edilmesini** zorunlu kılmak (yöntem bölümünde), dilsel izi denetim aracı yapmamak.

**Metodolojik Değerlendirme:** Kapsam olağanüstü geniş (6 veritabanı + 2,4 milyon tam metin), ölçüm şeffaf. Sınırlar yazarlar tarafından açıkça listelenmiş: yalnızca 12 terim, ağırlıkla meta veri analizi, İngilizce terimler, çevrilmiş özetlerin etkisi belirsiz, anlamsal düzeyde analiz yok. En önemli sınır: **nedensellik yok**. İz, üretim mi düzenleme mi stilin yayılması mı — ayrıştırılamıyor. Yine de alanın "LLM akademik yazımı değiştirdi mi" sorusuna verdiği en sağlam ampirik yanıt.
**Öncelik:** high  |  **Eylem:** akademik_only

---

## ⚖️ ETİK / TEORİ

### 4. In Referees We Trust? How Peer Review Became a Mark of Scientific Legitimacy
**Yazar:** Melinda Baldwin (AIP Endowed Professor in History of Natural Sciences, University of Maryland)
**Tarih:** 2026-10-13
**Yayın:** The MIT Press, bilim tarihi monografisi, 244 sayfa (metin 1–178, notlar 181–224, indeks 225–244), 14 bölüm — **CC BY-NC-ND 4.0 açık erişim**
**DOI:** 10.7551/mitpress/15937.001.0001
**Erişim:** ❌ MIT Press Cloudflare (403 / 6.365 B). Kayıt Crossref JATS özeti (3 paragraf) + tam içindekiler + yayıncı/üniversite haber kaydı üzerinden kuruldu. **Gövde okunmadı.**

**ÖZET:** Baldwin, hakemliğin (refereeing) ve "peer review"un tarihsel olarak ne kadar **genç** olduğunu arşiv çalışmasıyla gösteriyor. Kitabın tezi iki aşamalı. Birincisi, yayılma tezi: ilk hakemlik sistemleri **19. yüzyıl başında bilimsel derneklere bağlı dergilerde** ortaya çıktı ve Britanya'dan ABD'ye yayıldı; ama sistem **hemen benimsenmedi** — birçok kurum hakemliği bilinçli olarak atladı ve bundan dolayı daha az güvenilir sayılmadı. Bölüm başlıkları bu yayılmayı kronolojik olarak izliyor: "The European Origins of the Referee", "Across the Atlantic: Refereeing Comes to the Early Twentieth-Century US", "'Not Pleasant Work': The Expansion of Refereeing After World War II", "From Refereeing to Peer Review", "'Abolish th[e]..." başlıklı tartışma bölümü. İkinci ve asıl tez, meşruiyet bağının kurulması: **Soğuk Savaş** döneminde federal hibe dağıtımı siyasi sorgulama konusu olunca, bilim insanları "akran değerlendirmesi olmadan hibe dağıtmak bilimin çekirdek ilkesini ihlal eder" argümanını kurdular. Baldwin'in gösterdiği şey, bu cümlenin bir **betimleme** değil bir **savunma hamlesi** olduğu: "peer review" bu argümanla opsiyonel bir editoryal süreçten bilimin zorunlu temeli hâline geldi. Yani bugün sorgulanamaz saydığımız bağ, hayli yakın tarihli bir kurumsal-politik inşa. Kitap açık erişim (CC BY-NC-ND) ve MIT Press'in açık monografi programı kapsamında ücretsiz indirilebiliyor — bu, tezin kendi konusuyla ironik biçimde uyumlu: bilimsel meşruiyetin maliyetsiz dolaşımı.

Kitabın en pratik katkısı, hakemliğin **ne olmadığını** göstermesi: ne evrensel, ne eski, ne de bilimsel meşruiyetin tek kaynağı. Bu, "hakemlik kutsaldır" ile "hakemlik işe yaramaz" kutuplarının ikisini birden reddetmeyi mümkün kılıyor; soru artık "hakemlik var mı" değil, "hangi işlevi görüyor ve o işlevi hangi koşulda görüyor". Baldwin ayrıca dergi editörlüğünün tarihsel olarak hakemlikten **daha merkezi** olduğunu hatırlatıyor — bugünkü "hakem otoritesi" anlayışının ne kadar yeni olduğunu gösteren bir ayrıntı.

**TÜRKİYE BAĞLAMI:** Türkiye'de hakemlik sistemi son on beş yılda hızla kurumsallaştı ama aynı meşruiyet sorusuyla yüzleşmedi. Üç nokta. **Birincisi, tarihsel paralellik:** Baldwin'in anlattığı süreç — hibe/atama kararlarının siyasi sorgulamaya açılması, ardından "hakemlik olmadan olmaz" argümanının kurulması — Türkiye'de doçentlik ve akademik teşvik sisteminde farklı bir biçimde tekrarlanıyor: hakemlik bir **kalite güvencesi** olarak değil, bir **belge** olarak işliyor. ÜAK/doçentlik dosyalarında hakemlik sayısı ölçülüyor, kalitesi ölçülmüyor. **İkincisi, dergi ekosistemi:** Türkiye'de çok sayıda dergi "hakemli" etiketi taşıyor ama hakem sürecinin belgelenmesi (kaç hakem, ne kadar süre, ret oranı, itiraz mekanizması) kamuya açık değil. Baldwin'in monografisi bu şeffaflık eksikliğinin tarihsel olarak **normal** olduğunu hatırlatıyor — ve tam bu yüzden sorgulanabilir olduğunu. **Üçüncüsü, açık erişim:** kitabın kendisi CC BY-NC-ND ile ücretsiz; Türkiye'de kamu fonlu araştırmaların (TÜBİTAK, BAP) açık erişim zorunluluğu hâlâ gevşek. Meşruiyet tartışması Türkiye'de erişim tartışmasıyla birlikte yürütülmeli: kapalı bir hakemlik sistemi ile açık bir yayın sistemi bir arada tutarlı değil.

**Metodolojik Değerlendirme:** Arşiv temelli tarih çalışması; nicel kanıt üretmiyor, süreç izi sürüyor. Gövde okunamadığı için bölüm bazlı argümanlar, vaka anlatıları ve arşiv kaynakları doğrulanmadı; kayıt **tez düzeyinde** tutuldu. Yayıncı özetinin üç paragrafı ve tam içindekiler, argümanın iskeletini güvenilir biçimde veriyor.
**Öncelik:** medium  |  **Eylem:** akademik_only

### 5. Fear, Conformity, and Phantom Majorities
**Yazar:** Cory J. Clark (New College of Florida)
**Tarih:** 2026-09-19
**Yayın:** PsyArXiv ön baskısı, CC BY 4.0, 8 sayfa; *On Political Order and The Future of Democracy* derlemesinde bölüm olarak yayımlanacak
**DOI:** 10.31234/osf.io/uw25s
**Erişim:** ✅ Tam metin (OSF PDF, 602 KB, 8 sayfa) — ResearchGate bağlantısı 403 verdi

**ÖZET:** Clark, sosyal medyanın kamuoyu algısını nasıl çarpıttığına dair **"hayalet çoğunluk"** (phantom majority) kavramını öneriyor: göreli payı küçük ama mutlak sayısı büyük bir grubun, insan zihninde olduğundan çok daha temsili ve sosyal olarak güçlü bir çoğunluk gibi deneyimlenmesi. Kavramın çekirdeği ölçek aritmetiği: 10.000 kişilik bir ağda %0,01 **bir kişiye** denk gelir ve kimse ciddiye almaz; 500 milyonluk X'te aynı %0,01 **50.000 kişiye** denk gelir ve akışta bir kalabalık gibi görünür. Clark bunu iki psikolojik yolla modelliyor. **Dış-grup yolu:** insanlar dış gruplarının uçluğunu, homojenliğini ve düşmanlığını sistematik olarak abartıyor (Ahler & Sood 2018; Lees & Cikara 2020/2021; Levendusky & Malhotra 2016); More in Common/YouGov saha çalışmasında hem Demokratlar hem Cumhuriyetçiler dış gruplarındaki uç görüşlü oranı oldukça yüksek tahmin ediyor. **İç-grup yolu:** iç grubun da olduğundan uç algılanması (daha zayıf ama gerçek) ortalama üyeyi "konsensüsün dışında" hissettiriyor; sonuç **öz-sansür** (Sutherland & Gibson 2024; akademisyenler üzerine Clark vd. 2025, *Perspectives on Psychological Science* 20(5):941–957; FIRE 2024 fakülte anketi), **tercih tahrifi** (Kuran 1995) ve sahici uyum. İki yol birleşince kendini gerçekleştiren bir kehanet kuruluyor: hayalet çoğunluk pozisyonları popülerleşiyor ve zamanla **gerçek** hâle geliyor. Clark'ın kendi kanıt sınırı dürüst: dış-grup maruziyetinin **inanç** kutuplaşmasına yol açtığına dair kanıt daha zayıf; Bail vd. (2018) karşıt görüşlere rastgele maruz bırakılanların daha uçlaştığını buluyor ama etki Cumhuriyetçilerde daha büyük.

Clark'ın önerdiği müdahale de bu çerçeveden çıkıyor: insanlara "karşı taraf sandığın kadar uç değil" demek tek başına yetmiyor; asıl hedef **payda** — platformun gösterdiği sayıların ne anlama geldiğini görünür kılmak. Bu, medya okuryazarlığını soyut bir çağrı olmaktan çıkarıp **ölçek aritmetiği** öğretmeye indirgiyor: "%0,01 ne demek, kaç kişi eder, o sayı neyi temsil eder".

**TÜRKİYE BAĞLAMI:** "Hayalet çoğunluk" Türkiye'nin dijital kamusal alanını açıklamak için alışılmadık derecede verimli bir kavram — ve üç nedenle. **Birincisi, ölçek:** Türkiye'de X kullanıcı tabanı seçmen tabanının çok küçük bir bölümü; buna karşılık siyasi gündem neredeyse tamamen bu platformdaki etkileşim sayıları üzerinden kuruluyor. %0,01'lik bir grubun 5.000-10.000 kişilik görünürlüğü, televizyon ve gazete gündemine "kamuoyu böyle düşünüyor" olarak aktarılıyor. **İkincisi, iç-grup yolu ve öz-sansür:** Türkiye'de araştırmacılar, gazeteciler ve öğretmenler üzerine yapılan (ve yapılamayan) çalışmaların en sık bulgusu, kişinin kendi çevresinde "herkesin böyle düşündüğü" algısı ile ifade ettiği görüş arasındaki fark. Clark'ın çerçevesi bu farkı bireysel cesaret sorunu olmaktan çıkarıp **algısal bir yanılgı** olarak modelliyor — ki bu, müdahale tasarımı açısından çok daha umut verici. **Üçüncüsü, ölçüm:** Türkiye'de "sessiz çoğunluk" söylemi sık kullanılıyor ama hiçbir zaman hayalet çoğunluk çerçevesiyle **ölçülmedi**. Yapılabilir bir çalışma: katılımcılara kendi görüşlerinin yaygınlığını tahmin ettirmek, sonra gerçek dağılımla karşılaştırmak. Bu, düşük maliyetli ve yüksek etkili bir anket tasarımı.

**Metodolojik Değerlendirme:** Kavramsal/sentez makalesi, yeni veri yok; iddia mevcut literatürün yeniden çerçevelenmesine dayanıyor. Güçlü tarafı: mekanizmayı iki yola ayırıp her birinin kanıt düzeyini ayrı ayrı tartışması. Zayıf tarafı: "hayalet çoğunluk" henüz doğrudan ölçülmüş bir yapı değil — önerilen ölçüm (algılanan yaygınlık vs. gerçek yaygınlık) yapılmamış. Kitap bölümü olarak yayımlanacak; hakemsiz ön baskı.
**Öncelik:** high  |  **Eylem:** both

### 6. Evolutionary foundations of social identity
**Yazarlar:** Leon Li (Leipzig University), Sebastian Grueneisen (Leipzig University), Michael Tomasello (Duke University)
**Tarih:** 2026-11-10
**Yayın:** *Philosophical Transactions of the Royal Society B* **381(1962), makale 20250157** — CC BY 4.0; PMCID PMC13750410; PMID 43007818
**DOI:** 10.1098/rstb.2025.0157
**Erişim:** ❌ Royal Society 403 / 6.283 B. Kayıt Crossref + PubMed Central künyesi + özet düzeyinde; tam metin okunmadı.

**ÖZET:** Li, Grueneisen ve Tomasello, sosyal kimlik teorisinin en temel sorusunu — insan psikolojisi neden bu kadar "grup kafalı" evrimleşti — evrimsel bir açıklamayla yanıtlıyor. Tezleri şu: sosyal kimliğin evrimsel olarak **özgün biçimi** ırk, etnisite, milliyet veya sınıf değil, kişinin kendi kültürel grubunun **"iyi/kooperatif bir üyesi"** olarak kendini görmesi, yani **ahlaki kimlik**. Irk ve etnisite insanlık tarihinin büyük bölümünde ayırt edici değildi (komşu gruplar fizyonomi ve ten rengi bakımından belirgin biçimde farklılaşmıyordu); milliyet ise çok daha yeni. Klasik sosyal kimlik teorisi (Tajfel) gruplara bağlanmanın **yakınsal** motivasyonlarını (olumlu benlik, farklılaşma, anlam, aidiyet) iyi betimliyor ama bu eğilimin neden evrimleştiğini açıklamıyor; yazarların katkısı bu boşlukta. İki aşamalı bir doğa tarihi öneriyorlar. **Birinci aşama (~2 milyon yıl önce):** büyük avı tek başına elde edemeyen erken insanlar işbirlikçi yiyecek aramaya geçti; bireysel "tavşan" yerine ortak "geyik" tercihi, bireysel failliğin "biz" düzeyine ölçeklendiği ortak faillik kapasitesini üretti. **İkinci aşama (~130 bin yıl önce, Geç Pleistosen):** nüfus ve grup boyutu büyüdü, gruplar arası kaynak rekabeti keskinleşti ve büyük bantlarda herkes birbirini tanımadığı için "kim bizden" sorusu ortaya çıktı; sosyal kimlik, kolektif failliği sürdüren grup düzeyinde bir **öz-düzenleme sistemi** olarak evrildi. Ontogenetik kanıt tablosu ikna edici: 3 yaşında ortak taahhütler, norm ihlaline itiraz ve paylaşma; 4-5 yaşında minimal grup paradigmasında keyfi ölçütlerle bile iç-grup kayırmacılığı; 5 yaşında kültürel ortak zemin beklentisi ve başkalarının ihlallerine tepki.

Yazarların en tartışmalı iddiası, etnik ve ulusal kimliklerin **türevsel** olduğu: bunlar ahlaki kimlik sisteminin üzerine sonradan eklenen, tarihsel olarak genç katmanlar. İddia doğruysa kimlik çatışmalarının çözümü "farklılıkları tanımak" değil, **ahlaki kimliğin ortak zeminini** yeniden kurmak olur — çok kültürlülük politikalarının tam tersi bir yön.

**TÜRKİYE BAĞLAMI:** Bu makale, Türkiye'de kimlik tartışmasının neden sürekli "etnisite" eksenine sıkıştığını açıklamaya yardım ediyor. Yazarların tezi, ahlaki kimliğin etnik kimlikten **önce** geldiğini söylüyor — yani insan zihni önce "iyi/kooperatif üye mi" sorusuna bakıyor, sonra "hangi gruptan" sorusuna. Türkiye'de saha gözlemleri bu sıralamayla uyumlu: hemşerilik, mahalle dayanışması, esnaf ahlakı, "sözünün eri olma" gibi kodlar etnik kimliği aşan bir güven üretiyor; tersine, ahlaki ihlal (sözünde durmama, haksız kazanç, torpil) kimlik sınırlarını hızla harekete geçiriyor. İkinci ve daha kritik nokta **çocukluk**: makalenin ontogenetik tablosu, iç-grup kayırmacılığının **4-5 yaşında** ve keyfi ölçütlerle bile ortaya çıktığını gösteriyor. Bu, erken çocukluk eğitiminde "farklılıklara saygı" programlarının neden geç kaldığını açıklıyor: müdahale, kayırmacılık zaten kurulduktan sonra başlıyor. Türkiye'de okul öncesi müfredatında (MEB 2024 programı) ahlaki kimlik ve ortak faillik ekseni neredeyse yok; program ağırlıkla "değerler eğitimi" başlığı altında davranış öğretiyor. Üçüncüsü, **kuramsal uyarı**: makale yeni veri sunmuyor ve kendisi "deneysel sınama gerekli" diyor. Türkiye'de bu hipotezi sınamak için en doğal saha, çok dilli/çok kimlikli sınıflar — ve orada asıl soru, ahlaki kimlik ile etnik kimliğin hangi yaşta ve hangi koşulda birbirine bağlandığı.

**Metodolojik Değerlendirme:** Kuramsal sentez; "This article has no additional data" notu var. Güçlü tarafı: iki aşamalı evrimsel model ve gelişim psikolojisi kanıtının tablo hâlinde birleştirilmesi. Zayıf tarafı: hipotez doğrudan test edilmemiş; etnisitenin "tarihsel olarak ayırt edici olmadığı" iddiası tartışmalı (bazı arkeolojik/genetik bulgular aksi yönde okunabilir). Tam metin okunmadı.
**Öncelik:** medium  |  **Eylem:** akademik_only

---

## 🔥 GÜNCEL TARTIŞMALAR

### 7. The Winning Formula of the Populist Radical Right: Insider Narratives and the Making of a Representative Claim
**Yazarlar:** Francesco Melito; Mattia Zulianello
**Tarih:** 2026-11-06
**Yayın:** *Government and Opposition* (Cambridge University Press), 2026, cilt 61, makale no e40, ss. 1–21 — RESEARCH ARTICLE, **açık erişim CC BY 4.0**
**DOI:** 10.1017/gov.2026.10064
**Erişim:** ✅ Tam metin (1.500.571 B / 90.966 karakter)

**ÖZET:** Melito ve Zulianello, popülist radikal sağın (PRR) seçim başarısı literatüründeki yapısal bir kör noktayı hedef alıyor: bugüne kadar neredeyse tüm çalışmalar başarıyı **"dışarıdan"** — seçmen talebi, ekonomik kırılganlık, medya ortamı, parti rekabeti gibi aktörün kendi anlatısının dışındaki faktörler — açıklamış; PRR partilerinin kendi başarılarını nasıl yorumladığını sistematik olarak incelememiştir. Yazarlar bu boşluğu, çağdaş PRR başarısının paradigmatik örneği saydıkları İtalya'nın **Fratelli d'Italia (FdI)** partisi üzerinden dolduruyor. Yöntem: Eylül 2023 – Şubat 2024 arasında **21 parti temsilcisiyle** yarı yapılandırılmış derinlemesine görüşme; kartopu örneklemeyle teorik doygunluğa ulaşma. Analiz, temsil iddiası (representative claim) literatürüne dayanıyor: bir partinin "halkı temsil ettiğini" söylemesi bir betimleme değil, bir **iddia üretme** edimidir. Yazarların bulduğu formül üç bileşenli: (1) **dışsallaştırma** — partinin yükselişi kendi stratejisinin değil, rakiplerin başarısızlığının ve "sistemin" çöküşünün sonucu olarak anlatılıyor; (2) **içeride olma anlatısı** — partinin sistemin dışında değil, "gerçek merkezinde" olduğu iddiası; yani anti-sistem söylemi ile hükümet olma kapasitesi aynı anda kuruluyor; (3) **normalizasyon** — radikal talepler, "sorumlu yönetim" diline çevrilerek taşınabilir hâle getiriliyor. Bu üçlünün işlevi, PRR'nin klasik açmazını çözmek: protesto partisi olarak kalırsa iktidara gelemiyor, iktidara gelirse protesto tabanını kaybediyor. FdI anlatısı bu açmazı, başarıyı "kaçınılmaz" ve "zaten orada olan" bir şey gibi sunarak aşıyor.

Yazarların en güçlü ampirik hamlesi, partinin söylemini "başarı sonrası" değil **iktidara yürüyüş** döneminde toplaması: Eylül 2023 – Şubat 2024, yani FdI hükümette ama anlatı hâlâ kuruluyor. Bu zamanlama, formülün iktidarda kalma değil **iktidara gelme** anlatısı olduğunu gösteriyor. Aynı formülün iktidarda nasıl değiştiği makalenin kapsamı dışında — ve bu, alanın bir sonraki sorusu. Görüşmelerin parti içi hiyerarşiyi ne ölçüde yansıttığı da ayrı bir sınır.

**TÜRKİYE BAĞLAMI:** Bu makale Türkiye'yi doğrudan incelemiyor ama Türkiye'deki parti anlatısı tartışmasına üç somut katkı yapıyor. **Birincisi, yöntem:** Türkiye'de parti elitleriyle derinlemesine görüşme yapmak — özellikle iktidar partisi ve büyük muhalefet söz konusu olduğunda — erişim ve güven açısından zor; ama Melito-Zulianello tasarımı (21 temsilci, kartopu, teorik doygunluk) Türkiye'de de uygulanabilir ve bu alanda ciddi bir boşluk var. **İkincisi, "temsil iddiası" kavramı:** Türkiye'de siyasi partilerin "milleti temsil etme" söylemi sürekli ama bu söylemin **nasıl kurulduğu** akademik olarak incelenmiyor. Dışsallaştırma-İçeride olma-Normalizasyon üçlüsü, Türkiye'de iktidar partisinin "beka" söylemiyle, muhalefetin "gerçek temsil" söylemiyle nasıl çalıştığını karşılaştırmalı okumak için hazır bir şablon. **Üçüncüsü, uyarı:** FdI'nin İtalya'ya özgü koşulları (kısa hükümet ömrü, merkez-sağın çöküşü, Meloni'nin kişisel konumu) Türkiye'ye taşınamaz. Türkiye'de parti sistemi daha uzun süreli bir iktidar yapısı üretiyor; "içeride olma" anlatısı burada radikal sağ için değil, **iktidarın kendisi** için kuruluyor. Bu fark, karşılaştırmalı çalışmanın asıl sorusu olmalı: normalizasyon kimin için gerekli?

**Metodolojik Değerlendirme:** Nitel, tek vaka, 21 görüşme; açık erişim ve şeffaf yöntem. Sınırlar: tek ülke, tek parti, görüşmelerin parti içi muhalif sesleri kapsamaması muhtemel (kartopu örnekleme), anlatı analizinin kodlama güvenilirliği raporlanmamış. Bulgu "neden başarılı oldular" sorusuna değil "başarıyı nasıl anlatıyorlar" sorusuna yanıt veriyor — yazarlar bunu baştan kabul ediyor.
**Öncelik:** medium  |  **Eylem:** akademik_only

### 8. Affective polarization and anti-democratic attitudes: a complex relationship
**Yazarlar:** Kyle McWagner; William Kidd
**Tarih:** 2025-10-08
**Yayın:** *Journal of Elections, Public Opinion and Parties* (Routledge / T&F), 2026, cilt 36, sayı 4, ss. 997–1017 — RESEARCH ARTICLE, kapalı erişim
**DOI:** 10.1080/17457289.2025.2558780
**Erişim:** ❌ T&F Cloudflare (403). Kayıt yayıncı özeti + Crossref künyesi üzerinden; örneklem büyüklükleri, katsayılar ve model spesifikasyonları doğrulanmadı.

**ÖZET:** McWagner ve Kidd, duygusal kutuplaşma (affective polarization) ile anti-demokratik tutumlar arasındaki ilişkinin literatürde varsayıldığı gibi **doğrusal** ve partizan kimlikten **bağımsız** olmadığını gösteriyor. Kamuya açık ABD anketleri ile kendi yürüttükleri özgün bir Lucid anketini birlikte kullanarak iki temel varsayımı sınıyorlar: ilişkinin fonksiyonel biçiminin doğrusal olduğu ve her iki partinin seçmenleri arasında aynı şekilde işlediği. Bulgular her iki varsayımın da güçlü biçimde reddedildiğini ortaya koyuyor. Birincisi, ilişki **monotonik değil**: duygusal kutuplaşma düzeyi düşük ve yüksek olan katılımcılarda anti-demokratik tutum eğilimi farklı yönlerde hareket ediyor; yani "ne kadar kutuplaşmışsa o kadar anti-demokratik" cümlesi veriyle uyuşmuyor. İkincisi, ilişki **asimetrik**: aynı düzeyde duygusal kutuplaşma, iki partinin seçmenlerinde aynı anti-demokratik tutum düzeyine karşılık gelmiyor. Bu iki bulgu birlikte, alanın en sık kullanılan ölçüm stratejisini sorunlu hâle getiriyor: duygusal kutuplaşmayı tek bir doğrusal gösterge olarak modele koymak, heterojen bir ilişkiyi ortalamaya indirgiyor. Yazarların çıkarımı, kutuplaşma-anti-demokratik tutum bağının **partizan kimliğin kendisinden** değil, kimliğin nasıl düzenlendiğinden geçtiği yönünde. Bu, "kutuplaşma demokrasiyi yıkar" tezinin koşullu olduğunu, hatta bazı aralıklarda ters yönde çalışabileceğini ima ediyor.

Yazarların önerdiği düzeltme, ölçümü tek bir doğrusal endeksten çıkarıp **eşik ve asimetri** temelli bir modele geçmek: duygusal kutuplaşmanın hangi aralığında anti-demokratik tutumun arttığı, hangi aralığında sabit kaldığı ayrı ayrı test edilmeli. Bu, hem karşılaştırmalı siyaset çalışmaları hem platform verisiyle yapılan analizler için önemli: kutuplaşma endeksini tek başına bir "demokrasi riski" göstergesi saymak, verinin taşıyamayacağı bir yük. Bu, özellikle Türkiye gibi tek eksenli okumaya yatkın bağlamlarda kritik: simetri varsayımı çökerse, "kutuplaşma arttı" cümlesi hangi tarafın hangi davranışını anlattığını kaybeder.

**TÜRKİYE BAĞLAMI:** Türkiye'de kutuplaşma literatürü büyük ölçüde **tek bir eksende** (iktidar-muhalefet) ve tek bir doğrusal varsayımla çalışıyor: seçmen ne kadar kutuplaşmışsa demokrasiye o kadar az destek veriyor. Bu makale o varsayımı iki yerden kırıyor. **Birincisi, doğrusallık:** Türkiye'de "aşırı kutuplaşmış" seçmen ile "az kutuplaşmış" seçmenin demokrasiye desteği aynı yönde hareket etmiyor olabilir; özellikle yüksek kutuplaşma düzeyinde demokrasiye desteğin **araçsal** olarak arttığı (kendi tarafın kazanması için demokrasi gerekli) bir aralık mümkün. Bu, Türkiye'de yapılan anketlerde hiç test edilmedi. **İkincisi, asimetri:** Türkiye'de kutuplaşmanın partizan dağılımı simetrik değil — iktidar ve muhalefet seçmenlerinin kutuplaşma düzeyi, yoğunluğu ve nesnesi farklı. Aynı düzeyde "duygusal mesafe" iki tarafta aynı anti-demokratik tutuma karşılık gelmiyorsa, Türkiye'deki anket temelli yorumların önemli bir kısmı yanlış bir simetri varsayımına dayanıyor demektir. **Üçüncüsü, ölçüm:** Türkiye'de duygusal kutuplaşma çoğunlukla tek bir "thermometer" sorusuyla ölçülüyor; ABD literatürü çok maddeli ölçekler kullanıyor. Bu, karşılaştırmayı zorlaştırıyor ve etki büyüklüklerini şişirebiliyor. Türkiye'de yapılacak bir çalışmanın ilk işi ölçümü standardize etmek olmalı.

**Metodolojik Değerlendirme:** İki veri kaynağının (mevcut anketler + özgün Lucid anketi) birleştirilmesi güçlü. Ancak tam metin okunamadı: örneklem büyüklükleri, katsayılar, "doğru oy" benzeri ölçümlerin operasyonelleştirilmesi ve sağlamlık testleri doğrulanmadı. ABD iki partili sistem bağlamı, Asimetri bulgusunun genellenebilirliğini sınırlıyor. Kayıt **özet düzeyinde** tutuldu.
**Öncelik:** medium  |  **Eylem:** akademik_only

### 9. Political Unfriending on Facebook: Evidence from over 180 Million Users
**Yazarlar:** Neil Malhotra, Jaime Settle, Magdalena Wojcieszak, Olivier Bergeron-Boutin, Fang Guo, Annie Franco, Amac Herdagdelen, Winter Mason, Hunt Allcott, Pablo Barberá, Taylor Brown, Adriana Crespo-Tenorio, Deen Freelon, Matthew Gentzkow, Sandra González-Bailión, Andrew Guess, Shanto Iyengar, Young Mie Kim, David Lazer, Devra Moehler, Brendan Nyhan, Jennifer Pan, Carlos Velasco Rivera, Daniel Thomas, Emily Thorson, Rebekah Tromble, Arjun Wilkins, Beixian Xiong, Chad Kiewiet de Jonge, Natalie Jomini Stroud, Joshua Tucker (31 yazar; 2020 Facebook/Instagram Seçim Çalışması konsorsiyumu)
**Tarih:** 2026-11-13
**Yayın:** *The Journal of Politics* (University of Chicago Press), early access, çevrimiçi 13 Kasım 2026; cilt/sayı/sayfa atanmamış; ISSN 0022-3816 — kapalı erişim
**DOI:** 10.1086/744929
**Erişim:** ❌ journals.uchicago.edu 403 / 6.120 B. **Özet dahi okunamadı.** Kayıt künye + kapsam düzeyinde tutuldu; hiçbir sayısal sonuç üretilmedi.

**ÖZET:** Bu kayıt, bir bulgu özeti değil bir **kapsam ve altyapı notu** olarak okunmalı — çünkü makalenin kendisine erişilemedi ve yayıncı özeti de alınamadı. Elimizde doğrulanabilir olan şey künye ve kapsam: 2020 ABD başkanlık seçimi döneminde **180 milyondan fazla** Facebook kullanıcısının arkadaşlıktan çıkarma (unfriending) davranışı **günlük** düzeyde izleniyor; amaç platform üzerindeki **siyasi homofili** örüntüsünü platformun kendi davranış verisiyle ölçmek. Makale, 2020 Facebook/Instagram Seçim Çalışması konsorsiyumunun bir kolu; aynı ekip daha önce aynı veri altyapısıyla güvenilmez kaynaklara maruziyet ve ideolojik ayrışma üzerine yayın yaptı. **31 yazarlı** bir konsorsiyum olması, alanın ölçek sorununa verdiği kurumsal yanıtı gösteriyor: platform verisiyle çalışmak artık tek araştırmacının işi değil, müzakere edilmiş bir veri erişim rejimi ve çok yazarlı bir yönetişim gerektiriyor. Yöntemin potansiyeli büyük: arkadaşlıktan çıkarma, siyasi hoşgörüsüzlüğün **davranışsal** göstergesi ve öz bildirime dayanmıyor. Ama bu sayıda KURATOR'un söyleyebileceği tek şey şu: 180 milyon kullanıcı ölçeğinde günlük unfriending verisi var, sonuçlar doğrulanmadı. Bu dürüstlük notu, kaydın kendisinden daha önemli — çünkü alanın bir kısmı yayıncı özetine bile erişemeden bu tür makalelere atıf yapıyor.

Yöntemin potansiyeli de burada: arkadaşlıktan çıkarma, siyasi hoşgörüsüzlüğün **davranışsal** göstergesi ve öz bildirime dayanmıyor; insanlar ankette "karşı görüşten arkadaşım var" derken platformda o bağı koparıyor olabilir. Bu tür veri, kutuplaşma literatürünün en zayıf halkasını (öz bildirim yanlılığı) doğrudan hedefliyor ve "ağ homofilisi" ile "siyasi hoşgörüsüzlük" arasındaki ayrımı görünür kılıyor. Aynı veri mahremiyet açısından da alanın en hassas malzemesi: 180 milyon kullanıcının günlük ilişki kesme davranışı, kimin kimi çıkardığını göstermese bile siyasi homofilinin ölçülebilir olduğunu kanıtlıyor.

**TÜRKİYE BAĞLAMI:** Bu kayıt Türkiye için **yöntemsel** bir ders taşıyor, bulgusal değil. Türkiye'de siyasi kutuplaşma tartışması neredeyse tamamen anket verisiyle yürüyor; oysa "siyasi homofili" (insanların siyasi olarak benzer kişilerle bağ kurması) en iyi **davranışsal** veriyle ölçülür. Türkiye'de bu veri iki yerde duruyor: platformların kendisinde (erişim yok) ve **kullanıcıların kendi hesap geçmişinde** (veri bağışı ile mümkün). 18 Kasım'da işlediğimiz TikTok akış bağışı çalışması bu yöntemin gençlik ayağını gösteriyor; aynı protokol Türkiye'de **arkadaşlık ağı** için kurulabilir: katılımcılar hangi içeriği paylaştıklarını, kiminle etkileşime girdiklerini ve seçim döneminde kaç kişiyi çıkardıklarını bağışlar. KVKK açısından kritik nokta, üçüncü kişilerin (arkadaş listesindeki diğer kişilerin) verisinin işlenmesi — bu, açık rıza ile çözülemez, anonimleştirme ve yerel işleme şart. İkinci ders **kurumsal**: 31 yazarlı konsorsiyum modeli, Türkiye'de platform verisine erişimin tek yolunun **kurumsal işbirliği** olduğunu gösteriyor. Üçüncü ders **şeffaflık**: bu kaydı "180 milyon kullanıcı üzerinde yapılan çalışma kutuplaşmayı kanıtladı" diye aktaran bir haber, doğrulanmamış bir çerçeveyi dolaşıma sokar. KURATOR bu tuzağı bilinçli olarak reddediyor.

**Metodolojik Değerlendirme:** Künye ve kapsam dışında hiçbir şey doğrulanmadı: özet okunamadı, Crossref'te abstract yok, OpenAlex kaydı closed, Semantic Scholar DOI'yi tanımıyor, repository kopyası yok. Bu kayıt **atıf yapılabilir ama alıntı yapılamaz** durumda; okuma listesinde düşük öncelikli, kaynakçada "erişilemedi" notuyla yer alıyor.
**Öncelik:** low  |  **Eylem:** akademik_only

---

## 📎 EK OKUMA — BU HAFTA İZLENEN DİĞER KAYITLAR

| Kayıt | Künye | Not |
|-------|-------|-----|
| Being good to look good: Self-reported moral character predicts moral double standards | Dong, Kupfer, Yuan & van Prooijen, *British Journal of Psychology* 114(1):244–261, DOI 10.1111/bjop.12608 | 34.323 kişilik 25 ülkeli ESS paneli + üç deney; kendini ahlaklı görenlerin başkalarını sert, kendini hoşgörülü yargılaması itibar kaygısıyla güçleniyor. **Haftanın "ahlaki panik" tartışmasıyla doğrudan kesişiyor.** 403. |
| Neighborhood Democracy: The Politicization of School Boards | Arnzen & Jacobsen, *AERA Open* 12, DOI 10.1177/23328584261448159 | Okul kurullarını "mahalle demokrasisi" olarak kavramsallaştırıyor; ulusallaşma, merkezileşme, kutuplaşma ve azalan güven. 403. |
| Hostility, Population Sorting, and Backwardness (Red Army, WWII) | Ochsner, *Review of Economics and Statistics*, DOI 10.1162/REST.a.1874 | 74 günlük temas hattı üzerinden mekânsal RD: ~%12 nispi nüfus kaybı, bugüne ~%25 gerileme. 403. |
| Citizen-produced political text (CPPT): research note | Koc-Michalska, Gelovani, Haraldsson & Kalsnes, *JITP*, DOI 10.1080/19331681.2026.2758236 | 2014–2022 arası **2.785** makale; pencere 2022'de bittiği için LLM sonrası dönem kapsam dışı. 403. |
| Cognitive grounding improves LLM simulation of collective human behavior | Zhu & Heydari, *Nature Computational Science*, DOI 10.1038/s43588-026-01080-z | Beer Game, 231 oturum, yedi LLM: karar kurallarını isteme nitel olarak koymak yörünge uyumunu iyileştiriyor. Kapalı. |
| Group cross-pressures and correct voting in American elections | Sleiman, *Electoral Studies* 105:103196, DOI 10.1016/j.electstud.2026.103196 | ANES 2008–2024; çapraz baskılar "doğru oy" üzerinde ciddi ceza yaratıyor, siyasi bilgiyle açıklanmıyor. JS duvarı. |
| Dealing with misinformation in times of crises (pharma) | Zeaiter, Steils & Calciu, *Journal of Consumer Marketing*, DOI 10.1108/JCM-03-2026-9074 | 6 ilaç şirketinin 6.466 tweet'i; bilim temelli iletişim daha yüksek etkileşim, "boosting" baskın. Kapalı. |
| Misinformation and hoaxes in disaster and crisis communication | Rudianto vd., *Cogent Arts & Humanities* 13(1):2759373, DOI 10.1080/23311983.2026.2759373 | 592 Scopus belgesi (2007–2026), yıllık bileşik büyüme %28,5; "kamu güveni" anahtar kelime ağında görünmüyor. |
| Ethical and Socially Aware English-Norwegian Hate Speech Detection | Hashmi & Yayilgan, *MAKE* 8(9):292, DOI 10.3390/make8090292 | 14.008 örnek iki dilli veri seti; altı aşamalı etik tasarım çerçevesi. MDPI 200/0 karakter. |
| 2026 Election Conspiracies Haven't Breached the Vermeule Threshold | Gelman, blog, 15.11.2026 | "Vermeule eşiği": çılgın bir komplo teorisinin kravatlı saygın kişilerce savunulabilir hâle geldiği düzey. |
| A framework for navigating the choice between AI or traditional research | Bilow & Campbell, *Quirk's* (hakemsiz) | RISE modeli: Routine, Interpretation, Strategy, Engagement. Sektör yazısı. |
| Deep Learning and Social-Context Approaches for Fake News Detection | Dattatray vd., *IJSRET* 12(5), DOI 10.5281/zenodo.24220335 | ⚠️ **Dört sayfalık derleme, deney yok.** Kanıt olarak kullanılmadı. |
| Agent Reach (CLI) | Reid vd., GitHub v1.6.1, MIT | Ajanlara giriş duvarlı platformlara erişim; Hermes Agent README'de anılıyor. Konu dışı — yalnızca araç notu. |

---

## 📖 OKUMA LİSTESİ

| Zorluk | Makale | Konu | Öncelik |
|--------|--------|------|---------|
| ★★☆ | Bringing Everyone to the Table (Alsobay vd.) | LLM kolaylaştırıcı, grup kararı, d = 0,61 | **1 — bu hafta oku** |
| ★★☆ | How much are LLMs changing the language of academic papers (Kousha & Thelwall) | Akademik dilde LLM izi, +%1.360 | **2 — bu hafta oku** |
| ★☆☆ | Fear, Conformity, and Phantom Majorities (Clark) | Algılanan çoğunluk, öz-sansür | **3 — kısa, 8 sayfa** |
| ★★★ | The Winning Formula of the Populist Radical Right (Melito & Zulianello) | Temsil iddiası, PRR anlatısı | 4 — açık erişim |
| ★★★ | In Referees We Trust? (Baldwin) | Hakemliğin tarihi ve meşruiyeti | 5 — kitap, seçici okuma |
| ★★☆ | Multi-Agent Ethnography (Artz) | LLM ajanlarıyla nitel araştırma | 6 — çerçeve düzeyinde |
| ★★★ | Evolutionary foundations of social identity (Li vd.) | Ahlaki kimlik, ortak faillik | 7 — kuramsal |
| ★★☆ | Affective polarization and anti-democratic attitudes (McWagner & Kidd) | Kutuplaşma-anti-demokrasi ilişkisi | 8 — özet düzeyinde |
| ★★★ | Political Unfriending on Facebook (Malhotra vd.) | 180M kullanıcı, siyasi homofili | 9 — **erişilemedi, künye** |
| ★☆☆ | Being good to look good (Dong vd.) | Ahlaki çifte standart | Ek — tema desteği |

---

## 📚 KAYNAKÇA VE ERİŞİM NOTU

**Tam metin erişilen kayıtlar (5):** Artz — kısmi (araç dokümantasyonu); Alsobay vd. — arXiv PDF; Kousha & Thelwall — 56.013 karakter; Clark — OSF PDF; Melito & Zulianello — 90.966 karakter.

**Metadata tabanlı kayıtlar (8):** Baldwin (Crossref JATS özeti + içindekiler), Li vd. (Crossref + PMC), McWagner & Kidd (yayıncı özeti), Malhotra vd. (**özet yok**), Arnzen & Jacobsen, Ochsner, Koc-Michalska vd., Zeaiter vd., Hashmi & Yayilgan, Dong vd., Rudianto vd.

**Scrapling erişim tablosu (bu sayı, 10 adres):**

| Adres | HTTP | Gövde | Metin | Sonuç |
|-------|------|-------|-------|-------|
| doi.org/10.1080/00664677.2026.2614501 | 403 | 6.174 B | 58 kr | ❌ T&F |
| doi.org/10.1145/3816907 | 403 | 6.066 B | 58 kr | ❌ ACM |
| doi.org/10.1086/744929 | 403 | 6.120 B | 58 kr | ❌ UChicago |
| doi.org/10.3390/make8090292 | 200 | 2.279 B | 0 kr | ❌ JS duvarı |
| doi.org/10.1098/rstb.2025.0157 | 403 | 6.283 B | 58 kr | ❌ Royal Society |
| doi.org/10.1017/gov.2026.10064 | 200 | 1.500.571 B | 90.966 kr | ✅ CUP tam metin |
| doi.org/10.1177/23328584261448159 | 403 | 6.127 B | 58 kr | ❌ SAGE |
| doi.org/10.1007/s11192-026-05601-5 | 200 | 383.344 B | 56.013 kr | ✅ Springer tam metin |
| doi.org/10.1162/REST.a.1874 | 403 | 6.365 B | 58 kr | ❌ MIT Press |
| doi.org/10.1111/bjop.12608 | 403 | 6.162 B | 58 kr | ❌ Wiley |

**Engel oranı: 8/10 = %80** (KURATOR sayısındaki 16 adreslik geniş testte 10/16 = %62,5). Her iki oran da %50 eşiğinin üzerinde olduğu için sınıflandırma **metadata tabanlı** yürütüldü. Yeni gözlem: `mitpress` (10.1162) 403/6.365 B ile engelli aileye katıldı; `mdpi` 200 ama 0 karakter döndürmeye devam ediyor (geçen haftaki bulgu doğrulandı).

**Bu sayıda yer almayan kayıtlar ve gerekçeleri:** (1) *Deep Learning and Social-Context Approaches for Fake News Detection* — dört sayfalık, deneyi olmayan derleme; yalnızca ek okuma tablosunda uyarı notuyla anıldı. (2) *Agent Reach* — konu dışı (ajan altyapısı). (3) *A framework for navigating the choice between AI or traditional research* — hakemsiz sektör yazısı; yalnızca tabloda. (4) Gelman blog yazısı — akademik kayıt değil, kavram notu olarak tabloda. (5) Telefon yasakları raporu, NEET derlemesi, genç akışları ön baskısı, toksik içerik saha deneyi — çocuk/genç kesişimi nedeniyle **KURATOR sayısında** işlendi, burada tekrarlanmadı.

---

## 🔗 İlgili Bağlantılar
### 🧠 İlgili Kavramlar
- [[concepts/affective-polarisation.md|Affective Polarisation]]
- [[concepts/cocuk-veri-gizliligi.md|Çocuk Veri Gizliliği]]
- [[concepts/dijital-okuryazarlik.md|Dijital Okuryazarlık]]
- [[concepts/dijital-vatandaslik-egitimi-erken.md|Erken Çocukluk Dijital Vatandaşlık Eğitimi (0-8 Yaş)]]
- [[concepts/dis-grup-dusmanligi.md|Dış-Grup Düşmanlığı]]
- [[concepts/duygusal-kutuplasma.md|Duygusal Kutuplaşma (Affective Polarization)]]
- [[concepts/komplo-inanclari.md|Komplo İnançları]]
- [[concepts/olcum-araclari.md|Ölçüm Araçları (Polarization Measurement)]]
- [[concepts/platform-economy-misinformation.md|Platform Economy and Misinformation (Platform Ekonomisi ve Dezenformasyon)]]
- [[concepts/platform-seffaflik.md|platform-seffaflik]]
- [[concepts/populizm.md|Popülizm]]
- [[concepts/protesto-ve-toplumsal-hareketler.md|Protesto ve Toplumsal Hareketler]]
- [[concepts/sosyal-kutuplasma.md|Sosyal Kutuplaşma ve Dijital Platformlar]]
- [[concepts/sosyal-medya-genclik.md|Sosyal Medya ve Gençlik]]
- [[concepts/sosyal-medya-yasagi-tartismasi.md|Sosyal Medya Yasağı Tartışması]]
- [[concepts/yapay-zeka-cocuklar.md|Yapay Zeka ve Çocuklar]]
### 🏛 İlgili Kurum/Kişiler
- [[entities/ai-anthropology-toolkit.md|AI Anthropology Toolkit]]
- [[entities/arxiv-org.md|arXiv]]
- [[entities/boston-review.md|Boston Review]]
- [[entities/cambridge-university-press.md|Cambridge University Press]]
- [[entities/cepr-harvard.md|Harvard CEPR]]
- [[entities/cory-j-clark.md|Cory J. Clark]]
- [[entities/duke-university.md|Duke University]]
- [[entities/electoral-studies.md|Electoral Studies]]
- [[entities/ijsret.md|IJSRET]]
- [[entities/journal-of-politics.md|The Journal of Politics]]
- [[entities/kayvan-kousha.md|Kayvan Kousha]]
- [[entities/leipzig-university.md|Leipzig University]]
- [[entities/matt-artz.md|Matt Artz]]
- [[entities/melinda-baldwin.md|Melinda Baldwin]]
- [[entities/michael-tomasello.md|Michael Tomasello]]
- [[entities/mike-thelwall.md|Mike Thelwall]]
- [[entities/mit-press.md|MIT Press]]
- [[entities/nature-computational-science.md|Nature Computational Science]]
- [[entities/neil-malhotra.md|Neil Malhotra]]
- [[entities/prolific.md|Prolific]]
- [[entities/review-of-economics-and-statistics.md|Review of Economics and Statistics]]
- [[entities/routledge.md|Routledge]]
- [[entities/university-of-maryland.md|University of Maryland]]
- [[entities/yougov.md|YouGov]]
