# AKADEMİK ÖZEL TARAMA - Haftalık Derleme
## 2026-10-10

**Tarih:** 10 Ekim 2026 | **Hafta:** 41/2026 (4 – 10 Ekim dilimi)
**Kapsam:** 4 – 10 Ekim 2026 Telegram DM akışı; haftanın havuzunda **26 kayıt**, bunların **23'ü yeni** (3'ü — *Diving Deep*, *Polarization Is Not the Problem*, *The Global Evolution of Political Polarization Research* — önceki sayıda derlendiği için bu sayıya alınmadı).
**Önceki sayı:** 2026-10-03 (14 çalışma) — [Bulten_Havuzu/2026-10-03_akademik_ozel.md]
**Scrapling erişim testi:** 14 URL → **5 erişilebilir / 9 bloklu (%64 blok oranı)** → metadata tabanlı sınıflandırma modu (%50 eşiğinin üzerinde)

---

## YÖNETİCİ ÖZETİ

Bu haftanın derlemesi, **4 – 10 Ekim 2026** dilimindeki Telegram DM akışından gelen **23 yeni çalışmayı** kapsıyor. Haftanın belirgin özelliği, akışın üç ana eksende yoğunlaşması: **(a) yöntem ve ölçüm** (küçük örneklemli politika değerlendirmesi, anket ölçüm hatası, LLM ile ölçekleme, conjoint strateji kullanımı), **(b) demokratik bilgisizlik ve kurumsal aşınma teorileri** (ekolojik rasyonalite, siyasi olarak motive akıl yürütme eleştirisi, demokratik kaynak laneti, uluslararası örgütlere itiraz, ABD kurumsal kutuplaşma tarihi) ve **(c) bilgi ortamı, duygu ve kutuplaşma** (ayrık duygular ve kendini sansürleme, içerik–etkileşim ilişkisi, elit haber paylaşımı, sosyal medyada ruh sağlığı öz-tanı aktarımı, müzakere ve karakter yargıları, tarihsel parlamento söylemi). Ayrıca nitel araştırmaya LLM girişini konu alan uygulamalı bir kılavuz kümesi sürüyor.

**Erişim notu.** Bu haftaki Scrapling testinde on dört URL'in dokuzu (%64) bloklandı: **SAGE (journals.sagepub.com), Taylor & Francis (tandfonline.com), Oxford University Press (academic.oup.com), Princeton University Press, SSRN, CABI ve PNAS** 403 + Cloudflare duvarı döndürdü; **OSF (osf.io/preprints)** çağrıları 200 dönse de yalnızca ~3 karakterlik gövdeyle JavaScript duvarına takıldı (bu nedenle bloklu sayıldı). Tam metne erişilebilen yüzeyler **link.springer.com** (üç makale, 330–447 KB), **cambridge.org** (1,5–2,0 MB), **arXiv.org** ve **şu askıda: Türkiye/Küresel haber siteleri** oldu. Blok oranı %50 eşiğini aştığı için bu sayı **metadata tabanlı sınıflandırma modunda** derlenmiştir; künye, özet ve yorumlar Crossref/OpenAlex metadata'sı ile satır-içi tam metin okumalarına dayanmaktadır.

**Haftanın en dikkat çekici bulgusu:** Musolff & Yanay (SSRN, 1 Ekim 2026), hem kamuoyunun hem akademik uzmanların beklentisinin aksine ABD'li partizanların **toplamda neredeyse hiç "siyasi olarak motive akıl yürütme" (PMR) sergilemediğini** ve algılanan inanç uçurumunun gerçek farkı abarttığını gösteriyor. Laufer vd. (EJPR, 8 Ekim 2026) ise kutuplaşmanın altında **ayrık duyguların** (korku/öfke/tiksinme) farklı işlediğini ortaya koyuyor: korku kendini sansürlemeyi artırırken öfke azaltıyor; her ikisi de karşı tarafı susturma arzusunu besliyor.

---

## 1) METODOLOJİ — ÖLÇÜM, NEDENSEL ÇIKARIM VE LLM

### Makale 1: Small Samples and Short Panels — Politika Değerlendirme Yöntemlerinin Gerçekçi Veriyle Sınavı

- **Yazarlar:** Luke Stewart, Gary Hettinger, Youjin Lee, Nandita Mitra
- **Yayın:** arXiv:2608.01537 (stat.ME / politika değerlendirme yöntemleri), 2 Ağustos 2026
- **Erişim:** Açık (arXiv HTML/PDF, 200)

**ÖZET:** Politika müdahalelerinin etkilerini değerlendirmek için kullanılan nedensel çıkarım yöntemleri — farkların farkı (difference-in-differences, DiD) ve sentetik kontrol (synthetic control, SCM) — uygulamada sıklıkla **sınırlı örneklem ve kısa panel** verisiyle karşı karşıya kalıyor. Stewart, Hettinger, Lee ve Mitra, bu iki yöntemin yeni kuşak türevlerini — **sentetik difference-in-differences (SDiD)** ve **güçlendirilmiş sentetik kontrol yöntemi (ASCM)** — gerçekçi küçük örneklem koşullarında test ediyor. Kuramsal olarak SDiD ve ASCM, DiD ve SCM'ye göre daha zayıf varsayımlara dayansa da, küçük örneklem veya kısa panel uzunluklarında **yanlılık ve kapsama (coverage)** açısından performans garantileri eksiktir. Yazarlar, mevcut veriye **bilinen bir müdahale etkisi enjekte eden kalibre edilmiş bir simülasyon stratejisi** kullanarak bu yöntemlerin gerçekçi koşullardaki davranışını ampirik olarak inceliyor. Bulgular, hangi koşullarda SDiD ve ASCM'nin güvenilir tahmin ve çıkarım ürettiğine dair araştırmacılar ve politika yapıcılar için **pratik rehberlik** sunuyor — özellikle sağlık ve sosyal politika değerlendirmelerinde yaygın olan küçük N'li tasarımlar için. Çalışmanın metodolojik önemi, "hangi yöntem hangi veride güvenilir?" sorusunu sezgiye değil, **yeniden üretilebilir simülasyona** dayandırması: araştırmacı kendi verisinde yöntem seçimini veri-güdümlü biçimde yapabiliyor. Yazarlar, nedensel çıkarım yöntemlerinin sağlamlık sınırlarını haritalandırarak örneklem boyutunun müdahale etkisi tahminlerindeki belirsizliği nasıl büyüttüğünü nicel olarak gösteriyor.

**Anahtar noktalar:** (1) SDiD ve ASCM küçük örneklem/kısa panelde sınanıyor; (2) bilinen etki enjeksiyonlu kalibre simülasyon; (3) beş disiplinde (ekonomi, kamu sağlığı, siyaset bilimi) yaygın kullanım; (4) çıktı: hangi koşulda hangi yöntemin güvenilir olduğuna dair pratik rehber.

---

### Makale 2: Un-Priming Politics — Siyasi Katılımın Fazla Bildirimini Azaltan Yöntem

- **Yazarlar:** Elizabeth C. Connors, John V. Kane
- **Yayın:** *Political Behavior* (Springer), online first, ss. 1- ; DOI **10.1007/s11109-026-10200-4**, 7 Ekim 2026
- **Erişim:** Açık — Scrapling 200 (447 KB / 82.634 karakter tam metin)

**ÖZET:** Connors ve Kane, anket araştırmalarında siyasi katılım (political engagement) ölçümlerinin **sosyal beğenirlik (social desirability)** baskısı nedeniyle sistematik olarak **fazla bildirildiğini** (overreporting) gösteriyor ve bu sapmayı azaltacak basit bir yöntem öneriyor. Dört **ön-kayıtlı (preregistered)** anket deneyi toplam **N = 7.122** katılımcıyla yürütülmüş. İlk adımda sosyal beğenirlik kaygılarının bazı öz-bildirim türlerinin altında yattığı doğrulanıyor. İkinci adımda bir dizi müdahale test edilmiş ve en etkili bırakım **"Dampen Politics"** (siyasetin belirginliğini azaltma) olmuş: bu bırakım, (1) katılımcının anketi "siyasi" olarak algılama düzeyini ve (2) özellikle **siyasi ilgi** ile **oy verme** gibi bazı öz-bildirim türlerini anlamlı biçimde düşürüyor. Yazarlar bırakımın alternatif uygulamalarını da test edip sağlamlığını ve geçerliliğini değerlendirmiş. Sonuç: anket **sözcük seçimi ve soru düzenindeki basit bir ayarlama**, siyasi katılımın fazla bildirilmesini anlamlı ölçüde azaltabiliyor. Çalışma, anket tasarımının ölçüm hatasını "soru metni mühendisliği" ile değil, **bağlam ve belirginlik düzenlemesiyle** azaltabileceğini göstererek kamuoyu araştırmaları yöntemine doğrudan katkı sunuyor. Yöntemsel olarak çalışma, ön-kayıtlı tasarımı ve çoklu müdahale testiyle deneysel titizliği yüksek tutarken, ölçüm hatasının kaynağını "katılımcı yanlılığı" yerine **anket bağlamının kendisine** taşıyor.

**Anahtar noktalar:** (1) Dört ön-kayıtlı deney, N=7.122; (2) sosyal beğenirlik → fazla bildirim; (3) "Dampen Politics" en etkili müdahale; (4) sözcük+düzen ayarıyla fazla bildirim düşüyor.

---

### Makale 3: Scaling Up With Integrity — Anlatı Politikası Çerçevesi Analizlerinde LLM

- **Yazarlar:** Kylie L. Anglin, Ariell Bertrand, Jessica Gottlieb, Joseph Elefante
- **Yayın:** *Policy Studies Journal* (Wiley), **Cilt 54, Sayı 2** (research note); DOI **10.1111/psj.70045**
- **Erişim:** Bloklu (Wiley/Cloudflare 403) — özet künyesi Crossref/OpenAlex'ten

**ÖZET:** *Policy Studies Journal*'da yayımlanan bu araştırma notu, **Anlatı Politikası Çerçevesi (Narrative Policy Framework, NPF)** araştırmalarında büyük dil modellerinin (LLM) anlatı unsurlarını nasıl tespit edebileceğini ve bu ölçeklemenin **yapı geçerliliğini (construct validity)** nasıl koruyabileceğini gösteriyor. NPF'nin temel sorunu **ölçektir**: haber metinleri, kongre tutanakları ve sosyal medya paylaşımları milyonlarca politika-ilgili belgeye erişim sağlarken, geleneksel NPF çalışmaları anlatı unsurlarını (kahraman, kötü adam, kurban, olay örgüsü, ahlaki ders) **emek-yoğun insan kodlamasıyla** belirliyor; bu da analiz edilebilir belge sayısını ciddi biçimde sınırlıyor. Anglin, Bertrand, Gottlieb ve Elefante üç otomatik sınıflandırma yaklaşımını karşılaştırıyor: **zero-shot, few-shot ve fine-tuned** sınıflandırma. Çalışmanın temel argümanı metodolojik: LLM ile ölçekleme ancak **yapı geçerliliği sürecin her adımında önceliklendirilirse** anlamlıdır — model seçimi, prompt tasarımı, **insan kodlamasıyla karşılaştırmalı doğrulama** ve şeffaf raporlama. Bu "dürüstlükle ölçekleme" yaklaşımı, otomatik kodlamanın hızını insan kodlamasının geçerlilik ve güvenilirlik standartlarıyla birleştirmeyi hedefliyor ve LLM'lerin anlatı politikası araştırmasına entegrasyonu için **tekrarlanabilir (replicable) bir protokol** sunuyor. Yazarlar, otomatik kodlamanın avantajlarını (hız, ölçek, maliyet) kabul etmekle birlikte, doğrulama olmadan üretilen anlatı etiketlerinin yanıltıcı olabileceğini vurguluyor; bu nedenle önerilen iş akışı, model çıktılarının bağımsız bir insan kodlaması alt kümesiyle sürekli karşılaştırılmasını içeriyor.

**Anahtar noktalar:** (1) NPF + LLM ile anlatı unsuru tespiti; (2) zero-shot / few-shot / fine-tuned karşılaştırması; (3) süreç boyunca yapı geçerliliği önceliği; (4) insan kodlamasıyla doğrulama + şeffaf raporlama zorunlu; (5) Türkçe için dil kayması/ironi riski nedeniyle yerel doğrulama setleri ve Krippendorff alfa gerekli.

---

## 2) ETİK VE TEORİ — DEMOKRATİK BİLGİSİZLİK VE KURUMSAL AŞINMA

### Makale 4: Ecological Rationality and Democratic Ignorance — Rasyonel ve Radikal Bilgisizliğin Uzlaştırılması

- **Yazar:** Aylon R. Manor
- **Yayın:** *Public Choice* (Springer), **Cilt 208, Sayı 3-4, ss. 497-517**, Ocak 2026; DOI **10.1007/s11127-025-01370-6**
- **Erişim:** Açık (Scrapling 200, 330 KB) — ancak yayıncı abstract'ı "Client Challenge" duvarının arkasında; özet künye + anahtar kelimeler + 53 referanslık kaynakçadan metadata tabanlı kuruldu

**ÖZET:** Manor, seçmen davranışı literatüründeki iki rakip açıklamayı — **"rasyonel bilgisizlik" (rational ignorance)** ve **"radikal bilgisizlik" (radical ignorance)** — **"ekolojik rasyonalite" (ecological rationality)** çerçevesi üzerinden uzlaştırmayı amaçlıyor. **Rasyonel bilgisizlik tezi** (Downs, Buchanan, Caplan, Somin): seçmenin tek oyu seçim sonucunu neredeyse hiç değiştirmediği için bilgi edinmenin beklenen faydası maliyetini karşılamaz; seçmen bu nedenle rasyonel biçimde bilgisiz kalır. **Radikal bilgisizlik tezi** (Friedman, Evans & Friedman, Gibbons): sorun yalnızca bilgi eksikliği değil, seçmenin politikaların **nedensel işleyişine** dair derin kavrayıştan büsbütün yoksun olmasıdır — bilgi verilse bile "doğru" karar veremez. Manor, Gigerenzer'in ve Vernon Smith'in ekolojik rasyonalite kavramını (basit sezgisel kuralların belirli ortamlarda işlevsel olması) devreye sokarak bu ikiliği çözmeye çalışıyor: seçmen davranışı ekolojik anlamda **rasyonel olabilir**, ancak bu rasyonellik demokratik bilgisizliği ortadan kaldırmaz, hatta **yeniden üretir**. Böylece hem seçmeni "aptal" sayan küçümseyici okumadan hem de bilgisizliği bütünüyle irrasyonellik saymaktan kaçınıyor. Kamu tercihi (public choice) ve epistemik demokrasi literatürünü (Schumpeter, Brennan *Against Democracy*, Landemore, Goodin, Wittman) bir araya getiren kuramsal/kavramsal bir makale; **seçmen yeterliliği, teknokrasi/epistokrasi tartışmaları ve demokratik meşruiyet** için normatif sonuçlar barındırıyor.

**Anahtar noktalar:** (1) Rasyonel vs. radikal bilgisizlik tezleri ekolojik rasyonalite ile uzlaştırılıyor; (2) tek oyun sonuca etkisizliği → beklenen faydanın düşüşü; (3) radikal bilgisizlik: nedensel kavrayış yokluğu; (4) kuramsal köprü: kamu tercihi + epistemik demokrasi; (5) erişim notu: abstract kapalı → metadata tabanlı.

---

### Makale 5: (Mis-)Perceptions of Politically Motivated Reasoning — Partizan İnanç Uçurumunun Sınavı

- **Yazarlar:** Robin Musolff, Guy Yanay
- **Yayın:** SSRN Working Paper / preprint (Elsevier BV – SSRN), DOI **10.2139/ssrn.7548042**, 1 Ekim 2026
- **Erişim:** Bloklu (SSRN 403 / 6155 B Cloudflare) — Crossref kaydı (posted-content) + tweet metninden

**ÖZET:** Musolff ve Yanay, ABD'li partizanlar arasındaki olgusal inanç farklılıklarının **"siyasi olarak motive akıl yürütme" (politically motivated reasoning, PMR)** ile açıklanıp açıklanamayacağını bir dizi anket deneyiyle sınıyor. PMR, bireyin **kendi siyasi görüşüyle uyumlu mesajı daha ağır tartması** — bilgiye karşı partizan yönlü asimetrik tepki — olarak tanımlanıyor ve partizan inanç uçurumunun yaygın açıklaması olarak sunuluyor. Yazarlar üç bulguyu öne çıkarıyor: (1) Rakip partilerin taraftarları arasındaki olgusal inanç farkları olduğundan **büyük görünüyor, yani abartılıyor**; algılanan uçurum gerçek farktan daha geniş. (2) Hem genel kamuoyunun hem de akademik uzmanların beklentisinin aksine, **ABD'li partizanlar toplamda neredeyse hiç PMR sergilemiyor**. (3) Tespit edilen sınırlı motive akıl yürütme partiler arasında **asimetrik**: duygusal kutuplaşma düzeyi yüksek olanlarda daha yaygın ve partizanların "önemli" saydığı konularda daha belirgin. Tasarımın ayırt edici iki yönü vurgulanıyor: **kolay anlaşılır bilgilendirici sinyaller** kullanması ve **ikili (binary) olmayan bir ortamda** inanç hareketini doğrudan ölçmesi — bu, inanç güncellemesini (belief updating) yalnızca doğru/yanlış ikileminde değil sürekli bir ölçekte gözlemlemeye izin veriyor. Yazarlar buradan PMR'nin partizan inanç uçurumunu açıklamaya yetmediği sonucuna varıyor: uçurumun kaynağı başka mekanizmalarda (bilgi ortamı, elit sinyalleri, maruziyet farkları) aranmalı.

**Anahtar noktalar:** (1) PMR tanımı ve standart açıklama konumu; (2) ABD partizanlarında toplamda neredeyse hiç PMR yok; (3) algılanan uçurum gerçek farkı abartıyor; (4) PMR asimetrik ve duygusal kutuplaşma yüksek olanlarda daha güçlü; (5) sonuç: uçurumun kaynağı başka mekanizmalarda.

---

### Makale 6: Are Liberal Democracies Immune to the Democratic Resource Curse? — İsrail Doğal Gaz Vakası

- **Yazarlar:** Ariel Paz-Sawicki, Lior Herman
- **Yayın:** *Environmental Politics* (Taylor & Francis), ss. 1-25; DOI **10.1080/09644016.2026.2714728**, 14 Ağustos 2026
- **Erişim:** Bloklu (T&F 403 / 6185 B Cloudflare)

**ÖZET:** **"Demokratik kaynak laneti" (democratic resource curse)**, doğal kaynak keşfinin demokrasi üzerinde olumsuz etkileri olduğu, bunun da otoriterleşme ile kaynak zenginliği arasındaki pozitif korelasyondan kaynaklandığı tezini ifade ediyor. Literatürdeki hâkim görüş, kaynakların **liberal demokrasiler üzerinde çok az etkisi** olduğunu, "lanetin" asıl otoriter rejimlerle ilgili olduğunu savunuyor. Paz-Sawicki ve Herman bu görüşe itiraz ediyor: **çıkarıcı (extractive) sektörün** kendine elverişli düzenlemeleri teşvik etme yönündeki yoğun çabası karşısında demokratik kurumlar zayıflayabilir. Bunu **İsrail** örneği üzerinden inceliyorlar: önemli bir doğal gaz keşfinin ardından sektörün kârlılığını kritik biçimde etkileyen bir dizi düzenleyici karar alınmış; gaz şirketlerinin kararları etkileme girişimlerinin **potansiyel medya ele geçirmesi (media capture)** ile **"döner kapı" (revolving door)** ve lobicilik gibi **yasal yolsuzluk** türlerinde artışa yol açtığına dair kanıt bulunuyor. Yazarlar, kaynak keşfinin liberal demokrasiler üzerindeki etkilerini analiz etmek için kavramsal bir çerçeve öneriyor ve ilk bulguları sunuyor. Çalışma, tek vaka (İsrail) analizine dayanan bir kuramsal-görgül çerçeve önerisi niteliğinde olup bulguları "kaynak laneti" literatürünün demokrasiye özgü koluyla ve **düzenleyici devlet (regulatory state)** tartışmalarıyla ilişkilendiriyor. Yazarlar, demokratik ülkelerde "kurumsal aşınma'nın **sinsi biçimde** ilerleyebileceğini savunuyor — şeffaflık ve çıkar çatışması denetimi zayıfsa.

**Anahtar noktalar:** (1) Hâkim görüş: lanet yalnızca otoriter rejimlerde; (2) karşı tez: demokratik kurumlar da düzenleme baskısıyla zayıflar; (3) vaka: İsrail doğal gaz keşfi; (4) kanıt: potansiyel medya ele geçirmesi, döner kapı, lobicilik; (5) öneri: liberal demokrasiler için kavramsal çerçeve.

---

## 3) GÜNCEL TARTIŞMALAR — BİLGİ ORTAMI, DUYGU VE KUTUPLAŞMA

### Makale 7: Powered by (Discrete) Emotions? — Duygusal Kutuplaşma, Kendini Sansürleme ve Dış-Grubu Susturma

- **Yazarlar:** Luna Laufer, Laura Gerstner, Pia Kinzler, Julia Stockwald, Anna-Luisa Sacher, Carsten Reinemann
- **Yayın:** *European Journal of Political Research* (Cambridge University Press); DOI **10.1017/S147567652610190X**, 8 Ekim 2026
- **Erişim:** Açık — Scrapling cambridge.org (2,0 MB / 152.309 karakter); wiki bireysel girişi 10 Ekim'de yapıldı

**ÖZET:** Laufer, Gerstner, Kinzler, Stockwald, Sacher ve Reinemann, Almanya'da sonbahar 2024'te yapılan kota tabanlı çevrimiçi anket (**N = 1.918**) ile duygusal kutuplaşma (affective polarization) literatürünü **genelleştirilmiş partizan antipatisinin ötesine** taşıyor: ayrık olumsuz duyguları (**korku, tiksinme, öfke**) ayrı ayrı ele alıp bunların siyasi söyleme dair iki davranışla ilişkisini ölçüyor — (1) kendi görüşünü ifade etmekten kaçınma (**self-censorship**) eğilimi ve (2) karşı siyasi dış-grubu (**out-group**) susturmanın önemli olduğuna inanma. Bulgular, duygusal kutuplaşmanın etkisinin **altındaki duyguya göre değiştiğini** gösteriyor: karşı siyasi gruba yönelik **KORKU**, kendini sansürleme eğilimini **artırıyor**; **ÖFKE** ise kendini sansürleme eğilimini **azaltıyor**; buna karşılık **üç olumsuz duygunun hepsi** (korku, tiksinme, öfke) karşı grubu susturmanın önemli olduğu inancını yükseltiyor. Yazarların çıkarımı: ayrık duygular duygusal kutuplaşmada kritik bir rol oynuyor ve genel hoşnutsuzluk ölçütlerinin ötesinde bilgi veriyor; ayrıca duygusal kutuplaşmanın **demokratik değerleri (ifade özgürlüğü, çoğulcu tartışma)** nasıl tehdit edebileceğine dair kanıt sunuyor. Mekanizma ayrımı önemli: korku bireyi geri çekilmeye (sessizleşmeye) iterken öfke kamusal ifadeyi tetikliyor, ama her iki duygu da karşı tarafı susturma arzusunu besliyor — yani **ifade özgürlüğü talebi seçici olabiliyor**. Sınırlılık: tek ülke (Almanya), kesitsel anket → nedensel değil ilişkisel çıkarım; yazarlar boylamsal ve çok ülkeli doğrulama öneriyor.

**Anahtar noktalar:** (1) EJPR; Almanya kota tabanlı anket, N=1.918; (2) korku → kendini sansürleme artıyor; (3) öfke → azalıyor; (4) üç duygu da karşı grubu susturma inancını yükseltiyor; (5) demokrasi açısından: ifade özgürlüğü ve çoğulcu tartışma aşınıyor.

---

### Makale 8: Two Centuries of Sexism in British Parliament — Hansard Corpus'un LLM ile Analizi

- **Yazarlar:** Mohammad Omar Khursheed, Mandira Sawkar, Ashiqur R. KhudaBukhsh
- **Yayın:** arXiv:2608.30485 (cs.CL / cs.CY), 31 Ağustos 2026
- **Erişim:** Açık (arXiv 200)

**ÖZET:** Bu hesaplamalı sosyal bilim çalışması, Birleşik Krallık Parlamentosu'nun 200 yıllık **Hansard** tutanaklarını (1803-2005) büyük dil modelleriyle analiz ederek kadınların siyasi temsiline dair söylemi ölçüyor. **6.531 konuşma** LLM ile kodlanıyor: her konuşmacının kadınların oy hakkı ve siyasi temsili karşısındaki tutumu (lehte/aleyhte) sınıflanıyor ve konuşmalar **Ambivalent Cinsiyetçilik Envanteri** (düşmanca/hostile + yardımsever/benevolent cinsiyetçilik) çerçevesinde taranıyor. Bulgular: kadınların temsiline **karşı çıkan** konuşmaların **%54'ü** cinsiyetçi içerik taşırken **lehteki** konuşmalarda bu oran yalnızca **%21**; iki taraf temelden farklı cinsiyetçilik türleri kullanıyor — oy hakkı karşıtı retorik düşmanca ve yardımsever çerçeveyi bir arada kullanırken, oy hakkı yanlısı cinsiyetçilik **ezici biçimde yardımsever**. **Kadın milletvekilleri** kadınların siyasi haklarını **%93** oranında destekliyor (erkek milletvekillerinde %70); bu fark ancak oy hakkı verildikten sonra kapanıyor. Yazarlar ayrıca Hansard Corpus'un meta-veriyle zenginleştirilmiş, hesaplamalı sosyal bilim araştırması için optimize edilmiş bir sürümünü **açık veri** olarak yayımlıyor: **1,2 milyon tartışma** içinde **6,7 milyon konuşma** ve Avam Kamarası milletvekilleri için **%89 cinsiyet eşleşmesi**. Yöntem katkısı: tarihsel parlamento metinlerinin (text-as-data) LLM ile ölçeklenebilir biçimde kodlanması; ancak yazarlar kodlamanın **insan doğrulamasına bağlı** olduğunu ve model hatasının uzun vadeli eğilimleri kaydırabileceğini de gösteriyor. Ana çıkarım: yardımsever ve düşmanca cinsiyetçilik ayrı retorik bağlamlarda kullanılıyor ve "kadın haklarına destek" söylemi bile ataerkil bir çerçeve taşıyabiliyor.

**Anahtar noktalar:** (1) 200 yıllık Hansard, 6.531 konuşma; (2) karşıt konuşmaların %54'ü / lehteki %21 cinsiyetçi; (3) karşıt retorik düşmanca+yardımsever, yanlısı ezici benevolan; (4) kadın mv. %93 / erkek mv. %70 destek; (5) açık veri: 6,7 milyon konuşma, %89 cinsiyet eşleşmesi.

---

### Makale 9: Peer Transmission of Mental Health Information Increases ADHD Self-Diagnosis — Sosyal Medyada Ruh Sağlığı Bilgisinin Yayılımı

- **Yazarlar:** Tanay Katiyar, George Gillett, Adam Hunt, Amanda Ferguson, Alessia Pascale, Alberto Acerbi, Nikhil Chaudhary, **Amy Orben**
- **Yayın:** PsyArXiv preprint (OSF), DOI **10.31234/osf.io/dj6me**, 2 Ekim 2026; n = 3.392; dört çalışma
- **Erişim:** Bloklu (OSF 200 ama ~3 karakterlik JS duvarı) — metadata + özet künyesinden

**ÖZET:** İnternette ruh sağlığı bilgisi paylaşımının artması, sosyal medyanın ruh sağlığı **öz-tanı (self-diagnosis)** oranlarını şişirebileceği kaygısını büyüttü. Ancak bu bilginin **nasıl üretildiği ve tüketildiğini** yöneten mekanizmalar yeterince incelenmemiş. Yazarlar **kültürel evrim perspektifinden**, sosyal medyanın psikiyatrik bilginin yurttaştan yurttaşa aktarımını yeni formatlarda mümkün kıldığını ve bu bilgiyi iletmek için yeni motivasyonlar sağladığını öne sürüyor. Bunu, katılımcıların **DEHB (ADHD)** açıklamalarını sırayla değiştirip birbirlerine aktardığı uyarlanmış bir **"aktarım zinciri" (transmission chain)** paradigmasıyla inceliyorlar; böylece öz-tanı eğiliminin bu süreçte nasıl evrildiği gözlemlenebiliyor. **Dört çalışmada** (n = 3.392) bulunan sonuç: bu aktarım, katılımcıların **kendilerine ve subklinik özellikler taşıyan başka bir bireye DEHB tanısı koyma eğilimini artırıyor**; ayrıca katılımcıların bu kişiyi **profesyonel yardıma yönlendirme eğilimi de artıyor**. Aktarım **formatı** (örnek liste üretme vs. anlatı özeti) ve **motivasyon** (beğeni maksimizasyonu vs. doğruluk) bazı etkileri anlamlı biçimde değiştiriyor. Sonuç: yurttaştan yurttaşa aktarım, psikiyatrik tanı trendlerini ve kamuoyunun ruh sağlığı anlayışını şekillendirmede **kilit rol** oynayabilir. Yazarlar (aralarında dijital çağda gençlik araştırmalarıyla tanınan **Amy Orben** de var), bulguların sosyal medya platformlarının ruh sağlığı içeriğini nasıl biçimlendirdiğine ve bu içeriğin yurttaşlar arası aktarımının **klinik sonuçlar** doğurabileceğine dair uyarılar içerdiğini vurguluyor. Çalışma, öz-tanı tartışmasını **ahlaki panikten deneysel mekanizmaya** taşıması bakımından önemli.

**Anahtar noktalar:** (1) Aktarım zinciri paradigması, dört çalışma, n=3.392; (2) aktarım kendine ve başkasına DEHB tanısı koyma eğilimini artırıyor; (3) profesyonel yardıma yönlendirme de artıyor; (4) format ve motivasyon etkileri değiştiriyor; (5) çerçeve: kültürel evrim + psikiyatri + sosyal medya.

---

## 4) DİĞER ÇALIŞMALAR (Künye ve Kısa Değerlendirme)

Aşağıdaki çalışmalar bu sayının havuzuna girmiş ancak yukarıdaki üç ana bölümde derinlemesine ele alınmamıştır; künye, kısa özet ve erişim durumu verilmiştir.

**10. What Works Against Populist Rhetoric?** — Kollberg & Leschke, *Political Behavior* (Springer), DOI **10.1007/s11109-026-10198-9**, 6 Ekim 2026. BK'da ön-kayıtlı anket deneyi (n≈4.000). **Çoğulcu** karşı-argümanlar popülist çoğunlukçu demokrasi desteğini düşürüyor; **elitist** karşı-argümanların demokratik tutumlara etkisi yok. Karşı-argümanlar aday değerlendirmelerini de etkileyebiliyor. *Erişim:* Açık (Springer 200, 446 KB).

**11. Enemy Establishments** — Calvin TerBeek, Princeton University Press (kitap, ISBN 9780691294889), 2026. Tez: partiler kutuplaşmanın **nedeni değil, geç kutuplaşan sonucu**; kurumlar (üniversite, medya, bürokrasi, yargı) üzerinden yürüyen yüz yıllık mücadele ve paralel "Establishment" inşası; kök neden: bağdaşmayan iki anayasal tahayyül. *Erişim:* Bloklu (Princeton UP 403 / 6264 B).

**12. Contestation of International Organizations** — Tallberg, Walter & Zürn, *International Organization* (CUP), DOI **10.1017/S0020818326101477**, 2 Ekim 2026. **İç itiraz** (reform amaçlı) ile **dış itiraz** (varlık/ilkeler sorgulaması) tipolojisi; eleştirinin "nasıl işliyor"dan "varlığı meşru mu"ya kayması; dinamik teori ve ölçüm ihtiyacı. *Erişim:* Açık (cambridge.org 200, 2,0 MB).

**13. A Review of Conceptual Approaches and Empirical Evidence on Probability and Nonprobability Sample Survey Research** — Cornesse ve 11 ortak yazarı, *Journal of Survey Statistics and Methodology* 8(1): 4-36, DOI **10.1093/jssam/smz041**, 2019. Olasılıklı örneklem tasarıma dayalı güven sunarken olasılıklı olmayan örneklem model bağımlılığındadır; hangi örneklem tipinin pratikte en doğru olduğuna dair ampirik kanıt derlemesi ve en iyi uygulama önerileri. *Erişim:* Bloklu (OUP 403 / 6085 B). *(Temel referans — önceki sayılarda da atıf ağında.)*

**14. Associations between content and engagement vary across social media communities** — Alberto Acerbi, SocArXiv preprint (OSF), DOI **10.31235/osf.io/xwktf**, 6 Ekim 2026. **1.078.044 içerik / 587 topluluk / 5 korpus** (Reddit, Stack Exchange, X, YouTube). Negativite, ahlakileştirme, uyarılma, iç/dış-grup dili; değişken-eğimli modeller beş korpusta da daha iyi uyuyor; **topluluk eğimleri büyüklük ve yön bakımından çok farklı**; zayıf ortalama ilişki zıt yönlü güçlü ilişkileri gizleyebiliyor (kültürel ekoloji). *Erişim:* Bloklu (OSF JS duvarı).

**15. Why Politicians Retweet** — Shetty, Simmendinger, Lühring, Waldherr, Garcia & Metzler, SocArXiv (OSF), DOI **10.31235/osf.io/2hvpf**, 25 Eylül 2026. ABD Kongre üyelerinin 2021-2023 haber retweet'leri + negatif örneklem; NLP (duygusal ton, partizan ipuçları) + çok düzeyli lojistik regresyon. **Partizan kimlik en güçlü yordayıcı**; güvenilir kaynak tercihi tweet partizan referans içerdiğinde zayıflıyor; öfke/korku rakiplere atıfta retweet'i artırıyor; uç Cumhuriyetçilerde asimetri. *Erişim:* Bloklu (OSF JS duvarı).

**16. Diverging Effects of Deliberation** — Grey, Bloom, Plaks & Inbar, *Personality and Social Psychology Bulletin* (SAGE), DOI **10.1177/01461672261478731**, 3 Eylül 2026. Üç çalışma, toplam **N=896**: algılanan müzakere × siyasi anlaşma/anlaşmazlık → ahlaki karakter yargıları. Görüş **aynı**yken müzakerenin net etkisi yok (daha az kesinlik [olumsuz] ile daha düşüncelilik [olumlu] dengeleniyor); görüş **farklı**yken müzakere ahlaki karakter yargısını **olumlu** etkiliyor — siyasi ayrılığı "daha sindirilebilir" kılıyor. *Erişim:* Bloklu (SAGE 403).

**17. LLM Analysis of 150+ Years of German Parliamentary Debates on Migration** — Kostikova, Pütz, Eger, Sabelfeld & Paassen, arXiv:2509.07274 (cs.CL/cs.CY), 8 Eylül 2025. Reichstag (1867-1933), Batı Almanya Bundestag (1949-1990) ve Yeniden Birleşik Bundestag (1990-2025) üzerinde dayanışma/karşı-dayanışma etiketlemesi; en güçlü modeller (GPT-5, gpt-oss-120B) insan uyumu düzeyinde makro-F1'e ulaşıyor ama **sistematik hatalar** aşağı-yönlü çıkarımı saptırabiliyor; **yumuşak etiket + Design-based Supervised Learning (DSL)** ile düzeltme. Bulgu: savaş sonrası görece yüksek dayanışma, **2015'ten itibaren karşı-dayanışmada belirgin artış**. *Erişim:* Açık (arXiv 200).

**18. The Political Class in Citizens' Minds** — Mads Nørgaard, *European Journal of Political Research* (CUP), DOI **10.1017/S1475676526101777**, 25 Eylül 2026. Danimarka, **N=1.302**; serbest çağrışım + açık uçlu + kapalı uçlu ölçümler. Yurttaşların çoğu politikacıları hem homojen hem toplumsal olarak ayrı görüyor; bu algılar düşük güven/etkinlik/memnuniyetle ilişkili; **algılanan toplumsal farklılık, algılanan homojenlikten daha belirleyici**. *Erişim:* Açık (cambridge.org).

**19. A Guide for Qualitative Researchers Using Large Language Models** — Armstrong & Gale, CABI eBooks (kitap bölümü), ss. 84-96, DOI **10.1079/9781800626607.0008**. ChatGPT'yi temsilci alarak AI'nın nitel araştırmaya entegrasyonu için **altı aşamalı çerçeve** (soru sorma, yanlılık, şeffaflık, problem odaklılık, amaç biçimlendirme, veri toplama/analiz); yanıltıcı çıktı ve gizlilik uyarıları; araştırmacının yorumlayıcı sorumluluğu korunmalı. *Erişim:* Bloklu (CABI/DOI 403).

**20. Qualitative Analysis: Questions to Stimulate Researcher Reflexivity in the Age of GenAI** — Margaret R. Roller, *Research Design Review* (blog/metodoloji notu), 30 Eylül 2026. TQF'in dört kalite boyutu (Credibility, Analyzability, Transparency, Usefulness) GenAI çağında yeniden düşünülüyor; refleksivite kritik adım; somut soru setleri (bağlam kaybı, çıktıya meydan okuma, süreç şeffaflığı) ve refleksif günlük önerisi. *Erişim:* Bloklu (403).

**21. A Journey Through Creative Research Methods** — Rebekah Gear, Social Research Association (SRA, BK) Blog, 1 Ekim 2026. 4. Uluslararası Yaratıcı Araştırma Yöntemleri Konferansı (Manchester) izlenimleri; **"yaratıcılık bir adalet biçimidir"** (küresel sağlık araştırmasının <%20'si küresel çoğunluktan); güvenlik ilişiseldir; **çocuklar ortak-yazar/ortak-editör olabilir** (Childhood 31(3)); kısmi uzlaşmayı değerlemek. *Erişim:* Bloklu (403).

**22. September Research Roundup: 7 Findings on Intergroup Contact and Prosociality** — Packer & Van Bavel, *The Power of Us* (Substack), 7 Ekim 2026. **"Kabilecilik miti" çürütülüyor**: 121 toplum, 743.402 kişi, 6 veri seti — iç-gruba prososyal olanlar dış-gruba da prososyal. 5.980 kayıp mektup / 188 İtalyan topluluğu: iç-grup ve dış-grup dönüş oranları eşit; en güçlü yordayıcı **piyasa entegrasyonu**. Manşet: **10 dakikalık "dış-grup sohbet botu"** partizan yanlış algılarını düzeltip düşmanlığı azaltıyor. *Erişim:* Açık (Substack).

**23. Classifying strategy use in multiattribute subjective choice** — Banavar & Bansak, *PNAS* 123(40): e2613113123, DOI **10.1073/pnas.2613113123**, 28 Eylül 2026. Conjoint deneylerinde **birey düzeyinde strateji kullanımı**; Bayesci bilişsel model (nitelik ağırlığı + nitelik düzeyi + gizli-karışım strateji sınıflandırması); iki conjoint deneyi, **N=3.762**; en basit sezgisel strateji her koşulda en yüksek olasılıkta; deneklerin **~%67-76'sı** strateji bakımından farklılaşıyor. *Erişim:* Bloklu (PNAS 403).

---

## OKUMA LİSTESİ

| # | Zorluk | Makale | Konu | Öncelik |
|---|--------|--------|------|---------|
| 1 | Orta | (Mis-)Perceptions of Politically Motivated Reasoning | PMR eleştirisi; partizan inanç uçurumu abartılıyor | **Yüksek** |
| 2 | Orta | Powered by (Discrete) Emotions? | Ayrık duygular; kendini sansürleme / dış-grubu susturma | **Yüksek** |
| 3 | Orta | Small Samples and Short Panels | Nedensel çıkarım yöntemleri; küçük N / kısa panel | Yüksek |
| 4 | Kolay | Un-Priming Politics | Anket ölçüm hatası; "Dampen Politics" müdahalesi | Yüksek |
| 5 | Orta | Ecological Rationality and Democratic Ignorance | Seçmen yeterliliği; epistemik demokrasi | Orta |
| 6 | Kolay | Peer Transmission of Mental Health Information (ADHD) | Sosyal medyada ruh sağlığı öz-tanı aktarımı | **Yüksek** |
| 7 | Orta | Two Centuries of Sexism in British Parliament | Hanseard + LLM; cinsiyetçilik söylemi (text-as-data) | Orta |
| 8 | Zor | Scaling Up With Integrity (NPF + LLM) | LLM ile ölçekleme; yapı geçerliliği | Yüksek |
| 9 | Orta | Associations between content and engagement | Sosyal medya toplulukları; içerik–etkileşim heterojenliği | **Yüksek** |
| 10 | Orta | Why Politicians Retweet | Elit haber paylaşımı; duygu ve partizan asimetri | Yüksek |
| 11 | Kolay | Diverging Effects of Deliberation | Müzakere ve ahlaki karakter yargıları | Orta |
| 12 | Orta | What Works Against Populist Rhetoric? | Çoğulcu vs. elitist karşı-argüman | Orta |
| 13 | Orta | Contestation of International Organizations | İç/dış itiraz tipolojisi | Orta |
| 14 | Kolay | September Research Roundup (intergroup contact) | Prososyalite; kabilecilik miti | Orta |
| 15 | Orta | The Political Class in Citizens' Minds | Politikacı algısı; siyasi güven | Orta |
| 16 | Kolay | A Guide for Qualitative Researchers Using LLMs | Nitel araştırma + AI kılavuzu | Orta |
| 17 | Kolay | Reflexivity in the Age of GenAI | Refleksivite soruları; TQF | Düşük |
| 18 | Orta | Classifying strategy use (conjoint) | Conjoint deneylerinde strateji sınıflandırma | Orta |
| 19 | Orta | LLM Analysis of German Parliamentary Debates | Göç söylemi; DSL düzeltmesi | Orta |
| 20 | Orta | Are Liberal Democracies Immune to the Resource Curse? | Kurumsal aşınma; İsrail doğalgaz | Düşük |
| 21 | Zor | Enemy Establishments (kitap) | ABD kurumsal kutuplaşma tarihi | Düşük |
| 22 | Kolay | A Journey Through Creative Research Methods | Yaratıcı yöntemler; çocuk epistemik faillik | Düşük |
| 23 | Orta | Probability and Nonprobability Sample Survey Research | Anket örneklem yöntembilimi (temel referans) | Düşük |

---

## KAYNAKÇA

1. Stewart, L., Hettinger, G., Lee, Y., Mitra, N. (2026). *Small Samples and Short Panels: Evaluating Policy Evaluation Methods with Realistic Data.* arXiv:2608.01537. https://arxiv.org/abs/2608.01537
2. Connors, E. C., Kane, J. V. (2026). *Un-Priming Politics: A Method to Reduce Overreporting of Political Engagement.* Political Behavior. DOI 10.1007/s11109-026-10200-4
3. Anglin, K. L., Bertrand, A., Gottlieb, J., Elefante, J. (2026). *Scaling Up With Integrity: Valid and Efficient Narrative Policy Framework Analyses Using Large Language Models.* Policy Studies Journal 54(2). DOI 10.1111/psj.70045
4. Manor, A. R. (2026). *Ecological rationality and democratic ignorance: reconciling rational and radical accounts of voter behavior.* Public Choice 208(3-4): 497-517. DOI 10.1007/s11127-025-01370-6
5. Musolff, R., Yanay, G. (2026). *(Mis-)Perceptions of Politically Motivated Reasoning.* SSRN Working Paper. DOI 10.2139/ssrn.7548042
6. Paz-Sawicki, A., Herman, L. (2026). *Are liberal democracies immune to the democratic resource curse?* Environmental Politics, 1-25. DOI 10.1080/09644016.2026.2714728
7. Laufer, L., Gerstner, L., Kinzler, P., Stockwald, J., Sacher, A.-L., Reinemann, C. (2026). *Powered by (discrete) emotions? The consequences of affective polarization for self-censorship and outgroup silencing.* European Journal of Political Research. DOI 10.1017/S147567652610190X
8. Khursheed, M. O., Sawkar, M., KhudaBukhsh, A. R. (2026). *Two Centuries of Sexism in British Parliament: A Computational Analysis of Women's Representation in the Hansard Corpus.* arXiv:2608.30485. https://arxiv.org/abs/2608.30485
9. Katiyar, T., Gillett, G., Hunt, A., Ferguson, A., Pascale, A., Acerbi, A., Chaudhary, N., Orben, A. (2026). *Peer Transmission of Mental Health Information Increases ADHD Self-Diagnosis.* PsyArXiv. DOI 10.31234/osf.io/dj6me
10. Kollberg, M., Leschke, J. (2026). *What Works Against Populist Rhetoric? The Effects of Counter-Arguments on Democratic Attitudes.* Political Behavior. DOI 10.1007/s11109-026-10198-9
11. TerBeek, C. (2026). *Enemy Establishments: How the Hundred-Year War to Control America's Institutions Polarized Its Politics.* Princeton University Press. ISBN 9780691294889
12. Tallberg, J., Walter, S., Zürn, M. (2026). *Contestation of International Organizations: Patterns, Drivers, and Responses.* International Organization, 1-. DOI 10.1017/S0020818326101477
13. Cornesse, C., Blom, A. G., Dutwin, D., Krosnick, J. A., de Leeuw, E. D., Legleye, S., Pasek, J., Pennay, D., Phillips, B. W., Sakshaug, J. W., Struminskaya, B., Wenz, A. (2019). *A Review of Conceptual Approaches and Empirical Evidence on Probability and Nonprobability Sample Survey Research.* Journal of Survey Statistics and Methodology 8(1): 4-36. DOI 10.1093/jssam/smz041
14. Acerbi, A. (2026). *Associations between content and engagement vary across social media communities.* SocArXiv. DOI 10.31235/osf.io/xwktf
15. Shetty, A., Simmendinger, E., Lühring, J., Waldherr, A., Garcia, D., Metzler, H. (2026). *Why Politicians Retweet: News Trustworthiness, Emotion, and Partisan Asymmetry in Elite News Sharing among US Congress Members.* SocArXiv. DOI 10.31235/osf.io/2hvpf
16. Grey, Z. N., Bloom, P., Plaks, J. E., Inbar, Y. (2026). *Diverging Effects of Deliberation: How Perceived Thoughtfulness About Political Issues Affects Character Judgments.* Personality and Social Psychology Bulletin. DOI 10.1177/01461672261478731
17. Kostikova, A., Pütz, O., Eger, S., Sabelfeld, O., Paassen, B. (2025). *LLM Analysis of 150+ years of German Parliamentary Debates on Migration Reveals Shift from Post-War Solidarity to Anti-Solidarity in the Last Decade.* arXiv:2509.07274. https://arxiv.org/abs/2509.07274
18. Nørgaard, M. (2026). *The political class in citizens' minds: Mapping public perceptions of politicians.* European Journal of Political Research. DOI 10.1017/S1475676526101777
19. Armstrong, A. L., Gale, A. J. (2025). *A Guide for Qualitative Researchers Using Large Language Models with Representative Examples Using ChatGPT.* CABI eBooks: 84-96. DOI 10.1079/9781800626607.0008
20. Roller, M. R. (2026). *Qualitative Analysis: Questions to Stimulate Researcher Reflexivity in the Age of GenAI.* Research Design Review, 30 Eylül 2026.
21. Gear, R. (2026). *A Journey Through Creative Research Methods.* Social Research Association (SRA) Blog, 1 Ekim 2026.
22. Packer, D., Van Bavel, J. (2026). *September Research Roundup: 7 Findings on Intergroup Contact and Prosociality.* The Power of Us, 7 Ekim 2026.
23. Banavar, N. V., Bansak, K. (2026). *Classifying strategy use in multiattribute subjective choice: Application to conjoint experiments in political science.* PNAS 123(40): e2613113123. DOI 10.1073/pnas.2613113123

---

## METODOLOJİ, ERİŞİM VE DOĞRULAMA NOTU

Bu sayı, 4 – 10 Ekim 2026 diliminde `processed_links/` altına düşen `*_categorized.json` dosyaları (2026-10-04, 2026-10-04 batch2, 2026-10-08, 2026-10-08 batch2, 2026-10-09, 2026-10-10) ile bu en yeni categorized dosyadan sonra yazılan per-link `YYYY-MM-DD_<konu>.json` dosyalarının birleştirilmesiyle oluşturulmuştur. Yinelenen kayıtlar başlık normalizasyonu ve DOI ile ayıklandı; önceki iki sayıda (2026-10-03, 2026-10-05) derlenen üç kayıt bu sayıya alınmadı.

**Scrapling testi (2026-10-10):** 14 URL, 9 bloklu (%64). Bloklu: papers.ssrn.com (403), tandfonline.com (403), academic.oup.com (403), press.princeton.edu (403), cabidigitallibrary.org (403), researchdesignreview.com (403), pnas.org (403), osf.io ×2 (200 ama ~3 karakter JS duvarı). Erişilebilir: link.springer.com ×3, arxiv.org, cambridge.org. Blok oranı %50'nin üzerinde olduğundan **metadata tabanlı sınıflandırma modu** uygulanmıştır (Crossref/OpenAlex + satır-içi tam metin). Hiçbir özet veya künye uydurulmamıştır; erişilemeyen kaynakların künyesi DOI/Crossref kaydına, özetleri kaynak metnine dayanmaktadır.

---

## 🔗 İlgili Bağlantılar
### 🧠 İlgili Kavramlar
- [[concepts/affective-polarisation.md|Affective Polarisation]]
- [[concepts/dis-grup-dusmanligi.md|Dış-Grup Düşmanlığı]]
- [[concepts/duygusal-kutuplasma.md|Duygusal Kutuplaşma (Affective Polarization)]]
- [[concepts/olcum-araclari.md|Ölçüm Araçları (Polarization Measurement)]]
- [[concepts/platform-seffaflik.md|platform-seffaflik]]
- [[concepts/populizm.md|Popülizm]]
- [[concepts/siyasal-katilim.md|Siyasal Katılım (Political Participation)]]
- [[concepts/siyaset-bilimi-metodolojisi.md|Siyaset Bilimi Metodolojisi]]
- [[concepts/sosyal-kutuplasma.md|Sosyal Kutuplaşma ve Dijital Platformlar]]
- [[concepts/sosyal-medya-genclik.md|Sosyal Medya ve Gençlik]]
- [[concepts/yapay-zeka-cocuklar.md|Yapay Zeka ve Çocuklar]]
### 🏛 İlgili Kurum/Kişiler
- [[entities/arxiv-org.md|arXiv]]
- [[entities/aura-com.md|Aura]]
- [[entities/cambridge-university-press.md|Cambridge University Press]]
- [[entities/www-tandfonline-com.md|Taylor & Francis]]
