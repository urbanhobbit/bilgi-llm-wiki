# AKADEMİK ÖZEL TARAMA — Haftalık Derleme
## 2026-10-31

**Tarih:** 31 Ekim 2026 | **Hafta:** 44/2026 (26 – 31 Ekim 2026 dilimi)
**Kapsam:** Telegram DM akışına bu pencerede **32 benzersiz kayıt** düştü; bunların **26'sı AKADEMİK ÖZEL** etiketli (10 kayıt çoklu etiketli: KURATOR 10, GENEL 19). Bu sayıda **9 çalışma** üç eksende ayrıntılı işlendi, kalan 23 kayıt Okuma Listesi ve Kaynakça'da konumlandırıldı.
**Önceki sayı:** 2026-10-24 (9 çalışma) — [Bulten_Havuzu/2026-10-24_akademik_ozel.md]
**Scrapling erişim testi:** 10 URL → **3 erişilebilir / 7 bloklu (%70 blok oranı)** → metadata tabanlı sınıflandırma modu. 403/Cloudflare: Wiley (3×), T&F, SAGE, OUP. 200 ile tam metin: `nature.com` (69.189 karakter), `digital-futures-for-children.net` (10.773), `adacio.eu` (2.366). Save the Children PDF'i 129 KB indi ama metin çıkarımı 170 karakterde kaldı → PDF erişilebilir, metin değil.

---

## YÖNETİCİ ÖZETİ

Bu haftanın dokuz çalışması, tek bir cümlenin etrafında üç ayrı yöne açılıyor: **yapay zekâ artık araştırmanın hem aracı hem nesnesi — ve ikisi aynı anda olduğunda kanıt üretimi ile kanıtın meşruiyeti birbirinden ayrışıyor.** Altı çalışma doğrudan bu ayrışmaya bakıyor; üçü ise çocukluk alanının kendi ampirik tabanını yeniden kuruyor.

**Metodoloji ekseninde tablo iki yüzlü.** Geiecke & Jaravel (*Review of Economic Studies*, kabul edilmiş) tek ajanlı, açık kaynaklı bir LLM görüşmeciyle nitel görüşmeyi binlerce kişiye ölçekliyor ve kör değerlendirmede **2,93/5** ile "ortalama insan uzman" düzeyine ulaşıyor; sesli modda yüz yüze insan görüşmesiyle başa baş (3,50 vs 3,53). Malmberg (*POQ*) ise aynı iyimserliğe konjoint deneyleri üzerinden fren koyuyor: demografik profili birebir eşleştirilmiş "silicon samples" bile birey düzeyinde en iyi modelde **F1 = 0,71**'de kalıyor, yani her üç görevden biri insanla uyuşmuyor — üstelik demografik ortak değişkenlerin seçimi biçimlendirme yönü insanlarda ve modellerde **sistematik olarak farklı**. Kohler vd.'nin ajanik tekrar üretim çalışması ise üçüncü bir yerde duruyor: 48 makalede hücrelerin **%52–72**'si yeniden üretilebiliyor ve sapmaların dörtte üçünden fazlası ajana değil, **makalenin yöntem belirsizliğine** atfedilebiliyor. Üç bulgu bir arada okunduğunda ortak payda şu: darboğaz model kapasitesi değil, **dokümantasyon ve ölçüm geçerliliği**.

**Etik ve teori ekseninde soru "kullanmalı mıyız"dan "hangi kullanım beyan edilebilir"e kayıyor.** Stuhler vd.'nin 300 sosyologla yaptığı anket, disiplinin aynı pratikte hem "kabul edilemez" hem "beyan bile gerekmez" diyebildiğini gösteriyor; en çarpıcı bulgu **%82,2'nin zorunlu beyan istemesi, ama başkalarının beyanına güvenin %22'de kalması**. Jayadeva & Livingstone'un 126 sayfalık raporu ise tartışmayı araştırma etiğinden çocuk haklarına taşıyor: kanıt, BM Ortak Bildirisi'nin önerilerini desteklemeye **zaten yeterli**; eksik olan önleyici mimari. Daly vd.'nin açık erişimli kitabı bu mimari tartışmasına hukuki bir omurga ekliyor: çocuklar "hak taşıyıcısı" değil **"hak yapıcı"**.

**Güncel tartışmalar ekseninde Türkiye verisi ilk kez bu kadar merkezde.** Saraç & Koç, TÜİK 2022 Çocuk Araştırması mikro verisiyle (n=10.210) akran zorbalığının ilk çok değişkenli ulusal modelini kuruyor: **%13,8**, ve en güçlü ilişki zayıf akademik performans (AOR 2,90). Kyriakides vd. okul ikliminde ustalık ve öğrenci sesinin performans ikliminden daha güvenilir bir kaldıraç olduğunu gösteriyor. Save the Children & Vodafone'un DWRI endeksi ise dokuz Avrupa ülkesinde bir çelişkiyi belgeliyor: **%73 dijital beceri, ama yalnızca dörtte bir öznel refah**.

Bu sayının ortak sonucu şu: **2026'da çocuk–dijital alanında kanıt üretimi hızlandı, ama kanıtın hangi soruya cevap verdiği netleşmedi.** Yaş doğrulama yasakları beceriyi değil yönetimi hedefliyor; akran zorbalığı aile gelirini değil engellilik ve akademik performansı işaret ediyor; LLM'ler nitel görüşmeyi ölçekliyor ama konjointte insanı temsil etmiyor. Üçü de aynı hatayı önlemek için var: **yanlış birimi hedeflemek**.

---

## 1) METODOLOJİ — SENTETİK YANIT, AJANİK TEKRAR VE DOKÜMANTASYON AÇIĞI

### Makale 1: Conversations at Scale: Robust AI-led Interviews

**Künye:** Friedrich Geiecke (LSE), Xavier Jaravel (LSE & CEPR), "Conversations at Scale: Robust AI-led Interviews", *The Review of Economic Studies* (kabul edilmiş makale), DOI 10.1093/restud/rdag114; metin sürümü 30 Eylül 2026, 51 sayfa. Önceki sürüm: SSRN 4974382 (2024).

**ÖZET:** Makale, nitel görüşmenin ölçeğini ve temsil gücünü tek ajanlı, açık kaynaklı bir LLM görüşmeci platformuyla artırmanın mümkün olup olmadığını soruyor ve cevabı dört ayrı uygulama alanında test ediyor. Platform mimarisi bilinçli olarak minimal: açık uçlu ana sorular ve bağlama duyarlı sonda üretimi, metin ve sesli mod, RAG yok, ince ayar yok. Görüşme tipik olarak 30–60 dakika sürüyor ve alfanümerik bir kodla sonlandırılıyor; yani sistem "sohbet" taklidi değil, sonlu bir araştırma protokolü yürütüyor. Kalite değerlendirmesi 20 transkriptin iki kör değerlendiriciye okutulmasıyla yapılmış (40 puan): AI görüşmesi ortalama **2,93/5** alıyor ve yazarların deyimiyle "ortalama insan uzman" düzeyine denk geliyor. Modalite sıralaması metin referansında AI sesli (3,93) > insan yüz yüze (3,51) > AI metin (2,98) > insan çevrimiçi metin (2,42); yüz yüze referansta insan yüz yüze (3,53) ile AI sesli (3,50) neredeyse eşitleniyor. Uygulama sonuçları ölçek iddiasını destekliyor: ABD'de hayatın anlamı araştırmasında (N=461, temsili) AI görüşmesi kişi başına 470 kelime üretmiş, açık uçlu anket 195 kelimede kalmış (%141 fark). Fransa 2024 erken seçiminde (N=383) kutuplaşmış seçmen gerekçeleri toplanmış, ancak örneklem temsili değil (Prolific tabanında sol eğilim %65, seçim günü %28). Sesli görüşmede (N=338, enflasyon) katılımcıların %54,73'ü insan yerine AI'ı tercih etmiş. Sınırlılıklar yazarlar tarafından açıkça yazılmış: uzman puanlarında heterojenlik yüksek (değerlendiriciler arası korelasyon **0,55**), yüz yüze görüşmenin yerini almıyor, tek ajanlı mimari hassas konularda riskli, Fransa örneği temsilî değil. Bir başka sınır, platformun ölçtüğü şeyin görüşme kalitesi değil görüşmenin metinsel çıktısı olması: ses tonu, duraklama ve beden dili gibi nitel verinin taşıyıcıları değerlendirmeye hiç girmiyor. Yazarların açık kaynak tercihi ise ayrı bir katkı — platform kurulabilir, denetlenebilir ve Türkçe dâhil yeni dillere uyarlanabilir.

**Anahtar noktalar:**
- Tek ajanlı, açık kaynaklı LLM görüşmeci; RAG yok, ince ayar yok, 30–60 dk sonlu protokol.
- Kör değerlendirme: 40 puan üzerinden ortalama 2,93/5 (s.e. 0,167) — "ortalama insan uzman" düzeyi.
- Sesli AI, yüz yüze insan görüşmesiyle başa baş (3,50 vs 3,53).
- Ölçek etkisi somut: AI 470 kelime/kişi, açık uçlu anket 195 kelime (+%141).
- Nitel → nicel döngü: 35 anlatı, 300 kişilik kapalı uçlu ankette test edilmiş; negatif tarife zincirine katılım %87,04.
- Değerlendiriciler arası korelasyon 0,55 — kalite iddiası heterojen.

**Türkiye notu:** Türkiye için en pratik başlık maliyet ve saha erişimi. Nitel görüşme burada ağırlıkla yüz yüze, tek tek ve pahalı yapılıyor; aynı bütçeyle yüzlerce kişiye ulaşmak araştırma şirketleri ve üniversite ekipleri için oyunu değiştirir. Platform açık kaynak olduğu için Türkçe promptla kurmak teknik olarak zahmetsiz; asıl sınav Türkçe görüşme kalitesi. Yazılı Türkçede modeller akıcı, ama sonda üretiminde klişeye ve resmî dile kaçma eğilimi var; "doğal sohbet" hissi İngilizceye göre daha zayıf kalabilir ve bunun ölçülmesi gerekir, varsayılmaması. İkinci fırsat kutuplaşmış seçmen gerekçelerinin toplanması: Türkiye'de seçmen davranışının "neden" katmanı anketlerle neredeyse hiç toplanmıyor; nitel ölçek bu boşluğu kapatabilir, ama Fransa örneğindeki temsil sorunu Türkiye'de daha da sert olur.

**Erişim:** `restud.com` üzerinden özet ve künye; **tam metin alınamadı**, DOI Crossref'te "pending publication".

---

### Makale 2: Read the Paper, Write the Code — Agentic Reproduction of Social-Science Results

**Künye:** Benjamin Kohler, David Zollikofer, Alexander Hoyle, Elliott Ash, Johanna Einsiedler (ETH Zurich), "Read the Paper, Write the Code: Agentic Reproduction of Social-Science Results", arXiv:2604.21965v2 (v1: 23 Nisan 2026; güncel sürüm Ekim 2026), DOI 10.48550/arXiv.2604.21965. Hakemsiz ön baskı.

**ÖZET:** Bu ön baskı, sosyal bilimlerdeki tekrarlanabilirlik tartışmasını ajan sistemlerine taşıyor ve soruyu alışılmadık biçimde keskinleştiriyor: bir makalenin **kodunu hiç görmeden**, yalnızca yöntem anlatımı ve özgün veriyle sonuçlar yeniden üretilebilir mi? Yazarlar bunun için üç aşamalı bir hat kuruyor: çıkarım (makaleden yapılandırılmış yöntem tarifi ve sayıları maskelenmiş tablo şablonları), yeniden uygulama (ajan her tablo için sandbox'ta Python betiği yazıp çalıştırıyor) ve değerlendirme (hücre hücre deterministik karşılaştırma ve hata atfı). Kritik tasarım tercihi **bilgi izolasyonu**: ajan orijinal kodu, sonuçları ve makalenin tam metnini hiç görmüyor; böylece sonuçları ezberleyip koda gömme yolu kapanıyor. Deney 48 insan doğrulamalı makale üzerinde, 4 ajan iskeleti (Claude Code, Codex CLI, OpenCode, SWE-Agent) × 4 model (GPT-5.4, GPT-5.3 Codex, Opus 4.6, GLM-5) ile yürütülüyor. Sonuçlar şaşırtıcı ölçüde iyi: ajanlar makalelerin **%92–100**'ünde, tabloların %82–97'sinde, hücrelerin **%52–72**'sinde kullanılabilir sonuç üretiyor; katsayılarda tamamlama %82, standart hatalarda %80; işaret uyumu %78–91 (pozitif tahmin baseline'ı %68). Asıl bulgu hata atfında: sapmaların **dörtte üçünden fazlası** belirli bir kaynağa bağlanabiliyor ve en büyük pay **"original error"** — yani makalenin yöntem anlatımı, altındaki kodu yeniden üretmeye yetecek kesinlikte değil. İkinci sırada eksik veri, üçüncüde çıkarım hattı hatası; **ajan hatası ancak dördüncü sırada** ve güçlü ajanlarda belirgin biçimde küçülüyor. Yazarların formülasyonu darboğazın model kapasitesi değil **dokümantasyon** olduğu yönünde: parti kodlamasının nasıl yapıldığı ya da hangi F-istatistiğinin kullanıldığı yazılmadığında ajanlar farklı varsayımlara itiliyor. Sağlamlık testlerinde tekrar koşularda tabloların %80'inden fazlasında not farkı en fazla bir kademe, ama katsayı düzeyinde gürültü yüksek; eğitim verisi sızması testinde kesim öncesi/sonrası makaleler arasında anlamlı fark yok. Kod ve veri paylaşımı olmadan bu bulgu bile doğrulanamaz.

**Anahtar noktalar:**
- Kod görmeden, yalnızca yöntem + veriyle sonuç üretilebilir mi? — büyük ölçüde evet.
- 48 makale, 4 iskelet × 4 model; hücre tamamlama %52–72, katsayı tamamlama %82.
- En büyük hata kaynağı ajan değil: makalenin yöntem belirsizliği ("original error").
- En iyi kombinasyon OpenCode + GPT-5.4, aynı zamanda en pahalısı (~7,5 USD/makale).
- Öneri: kod "ne yapıldı"nın, makale "neden yapıldı"nın otoritesi; uyum otomatik denetlenmeli.

**Türkiye notu:** Türkiye'de sosyal bilim yayıncılığının en kronik sorunu tam da makalenin bulduğu yerde: yöntem bölümü, altındaki analizi başkasının yeniden kurabileceği ayrıntıda yazılmıyor. Veri setinin kaynağı, değişken kodlaması, örneklem filtreleri ve tahmin yöntemi çoğu zaman tek paragrafta geçiştiriliyor; kod ve veri paylaşımı istisna. Bu, TR Dizin ve ulusal dergilerde "tekrarlanabilirlik" bir yayın ölçütü olmadığı için kurumsal olarak da ödüllendirilmiyor. Makalenin çerçevesi burada bir kalite ölçütü öneriyor: bir hakemin, makalenin yöntem metninden analizi yeniden kurabilmesi. Türkiye'de bunun en hızlı uygulama alanı lisansüstü tezler ve TÜBİTAK destekli projeler — ikisinde de veri ve kod beyanı zaten istenebilir durumda, sadece istenmiyor.

**Erişim:** arXiv **200**, tam metin ve özet erişilebilir; kod GitHub'da.

---

### Makale 3: Investigating the Utility of LLM-Based "Silicon Samples" in Political Science Conjoint Experiments

**Künye:** Alice Malmberg (Johns Hopkins University, SNF Agora Institute), *Public Opinion Quarterly* (OUP), research note, 29 Ekim 2026 (online first), DOI 10.1093/poq/nfag069. Kapalı erişim; çoğaltım verisi Harvard Dataverse'te açık (CC0, doi 10.7910/DVN/2LVYOO).

**ÖZET:** Malmberg, zorunlu seçimli (forced-choice) konjoint deneylerinde LLM ile üretilmiş yanıtlayıcıların — yazının deyimiyle "silicon samples" — insan yanıtlayıcıların yerini alıp alamayacağını sistematik olarak test ediyor. Tasarım doğrudan bir eşleştirmeye dayanıyor: üç model (GPT-4o-Mini, Llama 3.2, Magistral-small-2506) için canlı bir konjoint örneklemindeki her yanıtlayıcının demografik profili (partizanlık, ideoloji, ırk, cinsiyet, yaş kategorisi, eyalet) birebir verilerek sentetik karşılıkları üretiliyor; ardından iki grup aynı profil setlerini ve aynı öznitelik düzeylerini görüyor. Konjoint ABD eyaletleri arasında taşınma tercihini altı öznitelikle modelliyor: kürtaj politikası, LGBTQ hakları, silah politikası, geçim maliyeti, suç oranı ve devlet okulu kalitesi. Her model için 15 tekrar × 2.000 görev = 30.000 görev üretiliyor; sıcaklık hem ortak (0 / 0,5 / 1) hem modele özgü değerlerde test ediliyor. Bulgu net ve olumsuz: naif biçimde üretilen silicon samples konjoint görevlerinde insan kararlarını simüle etmeye yetmiyor. Bireysel düzeyde insan–sentetik seçim uyumu (F1) GPT-4o-Mini'de **0,62–0,70**, Magistral-small-2506'da **0,63–0,71**, Llama 3.2'de **0,41–0,48**. Yani en iyi modelde bile yaklaşık her üç görevden biri insanla uyuşmuyor; Llama'da yarıdan fazlası. Daha önemlisi, demografik ortak değişkenlerin seçimleri biçimlendirme tarzı insanlarla modeller arasında **sistematik olarak** farklılaşıyor: aynı profil insan yanıtlayıcıda bir yönde hareket üretirken modelde başka, hatta ters yönde etki üretiyor. Yazının iki katkısı buradan çıkıyor: konjoint bağlamında LLM yanıtlayıcı performansına dair betimsel bir referans tabanı kurmak ve naif silicon samples'ın demografik özellikler üzerinden insan seçimlerini çıkaramayacağını göstermek. Sonuç, "LLM'lerle anket simülasyonu" literatürünün en hızlı büyüyen iddiasına doğrudan sınır çekiyor: sentetik yanıtlayıcı profil düzeyinde ortalamaları yaklaşık tutturabilse bile birey düzeyinde ve ortak değişken etkilerinde insanı temsil etmiyor. Bu, sentetik örneklem kullanacak her konjoint için bir ön test şartı demek.

**Anahtar noktalar:**
- Tasarım: her insan yanıtlayıcının demografik profili modele birebir verilerek sentetik karşılığı üretiliyor.
- Ölçek: 3 model × 15 tekrar × 2.000 görev = 30.000 görev; sıcaklık hem ortak hem modele özgü.
- F1: 0,62–0,70 (GPT-4o-Mini), 0,63–0,71 (Magistral), 0,41–0,48 (Llama 3.2) — her üç görevden biri uyumsuz.
- Kritik bulgu: ortak değişken etkilerinin yönü insanlarda ve modellerde sistematik olarak farklı.
- Dürüst sınırlılık: GPT-4o-Mini ve Magistral yayım sırasında emekliye ayrılmış; üretim betikleri verilmiyor, birebir tekrar mümkün değil.
- Açık bilim: tüm R kodları ve çıktı csv'leri Dataverse'te CC0.

**Türkiye notu:** Türkiye'de anket maliyetleri ve saha erişimi hızla kötüleşirken "LLM ile sentetik yanıtlayıcı" fikri hem akademik hem ticari anket sektöründe cazip bir kısayol olarak dolaşıma girdi; Malmberg'in notu bu kısayolun en sık kullanıldığı yerden, konjoint deneylerinden ampirik bir fren getiriyor. Türkiye açısından ilk sonuç doğrudan: aynı demografik etiketler (genç, muhafazakâr, İstanbullu, üniversite mezunu) verildiğinde LLM'lerin bu etiketleri insanlarla aynı yönde işlememesi, "sentetik seçmen" üreten çalışmaların geçerliliğini ciddi biçimde sarsar. İkinci sonuç daha incelikli: model etiketleri *ortalamada* yakalasa bile, Türkiye'de siyasal davranışın en belirleyici değişkenleri (dindarlık, etnik kimlik, hemşehrilik ağları) konjoint tasarımlarına nadiren giriyor; girmediğinde modelin "temsil" iddiası ölçülemez hale geliyor.

**Erişim:** **403 (OUP/Cloudflare, 6.171 B)**; değerlendirme Crossref tam özeti ve açık çoğaltım paketi üzerinden.

---

## 2) ETİK VE TEORİ — HAK, BEYAN VE ÖNLEYİCİ MİMARİ

### Makale 4: Artificial intelligence and children's rights — a narrative review of the evidence

**Künye:** Smera Jayadeva & Sonia Livingstone (LSE Media and Communications; Digital Futures for Children centre / 5Rights Foundation), "Artificial intelligence and children's rights: a narrative review of the evidence", Ağustos 2026, 126 s.; LSE Research Online eprint 140815 (depo: 27 Ağustos 2026), DFC yayını 30 Ağustos 2026. CC BY-NC 4.0.

**ÖZET:** Jayadeva ve Livingstone'un 126 sayfalık raporu, 2025'te ITU + BM Çocuk Hakları Komitesi + UNICEF eş-liderliğinde kabul edilen "Yapay Zekâ ve Çocuk Hakları Ortak Bildirisi"nin 11 temasını ampirik kanıtla eşleştiriyor. Tür açıkça belirtilmiş: **anlatı (narrative) derlemesi**, sistematik derleme değil; yazarlar Grant & Booth (2009) tanımına yaslanıyor ve eksiksizlik iddiası taşımıyor. Omurga, DFC'nin 300'den fazla kaynağı eleştirel notlarla barındıran Küresel Araştırma Veritabanı; anahtar sözcük taramalarıyla genişletilmiş (Mayıs–Ağustos 2026, yalnızca İngilizce). Raporun varlık nedeni tam olarak bu: Ortak Bildiri ampirik iddialarını kanıtla desteklemiyor ve iyi uygulama örneği göstermiyor. Temel sonuç cümlesi şu: mevcut kanıt, Bildiri'nin önerilerini desteklemeye **bugün zaten yeterli**; eksik olan kanıt değil, **önleyici mimari**. En güçlü vurgu, çocuğun AI'ı kullanıp kullanmamasından bağımsız hasar: eğitim, sağlık, sosyal hizmet, sosyal yardım ve yargı kurumları AI'ı işleyişlerine gömüyor, dolayısıyla hiç AI kullanmayan çocuk da etkileniyor. Kullanım verileri: UNICEF'in 10 orta gelirli ülke anketinde çocukların %50'ye kadarı AI kullanıyor ve ebeveynlerinden üç kat fazla olasılıkla AI kullanıcısı; Avrupa'da 9–16 yaş grubunun dörtte üçü GenAI kullanıyor; ABD'de 2023 sonunda ChatGPT'den haberdar gençlerin yaklaşık beşte biri onu okul işleri için denemiş. Hasar kanıtı dört eksende yineleniyor: ırk, toplumsal cinsiyet, yaş ve gelir temelli ayrımcılık; nudification ve akran/yetişkin siber zorbalığında erişim kolaylığı; çocuk görüntü ve biyometrik verisinin eğitim verisine dönüşmesi; companion/chatbot tasarımının bağımlılık ve manipülasyon üretmesi. Kurumsal hasar: Birleşik Krallık ve Hollanda'da sosyal hizmette otomatik profilleme, Gazze'de AI destekli hedeflemenin çocuk ölümleriyle sonuçlanması. İyi uygulama kanıtı zayıf ama var: risk temelli değerlendirme, CRIA, HRDD, anlamlı çocuk katılımı. Raporun en büyük boşluğu, iyi uygulama örneklerinin etki büyüklüğü bildirmemesi.

**Anahtar noktalar:**
- Yöntem: anlatı derlemesi, sistematik değil; Mayıs–Ağustos 2026, yalnızca İngilizce, ağırlıklı Küresel Kuzey.
- Ana tez: kanıt yeterli; sorun yönetişimin tepkisel olması, önleyici olmaması.
- Kullanım: orta gelirli 10 ülkede %50'ye kadar; Avrupa 9–16'da dörtte üçü.
- Hasar: ayrımcılık, nudification, biyometrik veri, companion bağımlılığı, sosyal hizmette profilleme.
- Boşluk: çerçeveler "yetişkin varsayılanına" düşüyor; yaş doğrulama ya mahremiyet ihlali ya atlatılabilir.
- Politika: CRIA ve HRDD sistem çocuğa ulaşmadan önce; katılım mekanizma + kaynak + denetim gerektiriyor.

**Türkiye notu:** Türkiye bu haritada "çerçeve var, uygulama yok" kutusunda. Kapsamlı bir yapay zekâ yasası hâlâ yok: Yapay Zekâ Kanunu Teklifi (Esas No. 2/2234) 25 Haziran 2024'te TBMM'ye sunuldu ve 2026 ortası itibarıyla komisyonda bekliyor; AB Yapay Zekâ Tüzüğü'nün risk temelli yapısını alıyor ama yüksek riskli kullanım listesini ikincil düzenlemeye bırakıyor, bağımsız otorite ve sandbox öngörmüyor. 1 Kasım'da yürürlüğe giren sosyal ağ yönetmeliği bu boşluğu kısmen dolduruyor; ama yalnızca sosyal medya tarafında. Raporun en uygulanabilir önerisi olan CRIA, Türkiye'de yasa beklemeden idari usulle (kamu ihalesi şartnamesi, etik kurul, veri işleme envanteri) devreye alınabilir. En kritik boşluk eğitimde: devamsızlık tahmini, rehberlik yönlendirmesi ve sınav analitiği gibi sistemlerin kamuya açık bir envanteri dahi yok — envanter olmadan etki değerlendirmesi de olamaz.

**Erişim:** **200 (549 KB / 10.773 karakter)**, DFC sayfası üzerinden; tam rapor PDF'i LSE Research Online'da.

---

### Makale 5: Is it Okay to Use Generative AI in Sociological Research?

**Künye:** Oscar Stuhler (Northwestern), Dustin S. Stoltz (Lehigh), AJ Alvero (Cornell), Marshall A. Taylor (CREST/ENSAE), "Is it Okay to Use Generative AI in Sociological Research?", SocArXiv preprint v1, 28 Ekim 2026, DOI 10.31235/osf.io/y6vtp_v1; *Sociological Science* dergisinde yayına kabul edildi (forthcoming). Açık erişim; çoğaltım osf.io/fpjzn, veri Harvard Dataverse doi 10.7910/DVN/HNK0SO.

**ÖZET:** Yazarlar, sosyologların üretken yapay zekânın hangi araştırma pratiklerinde kabul edilebilir olduğunu ölçen bir anketin sonuçlarını sunuyor. Örneklem, son beş yılda Web of Science'ta taranan 50 sosyoloji dergisinde yayın yapmış yazarlardan rastgele seçilen 3.425 kişi; Nisan–Haziran 2026'da davet edilenlerden 300'ü yanıt veriyor (%8,7), bunların 259'u kendini sosyolog olarak tanımlıyor. Katılımcılara araştırma sürecinin dört aşamasında (literatür/fikir, veri toplama ve analiz, yazma, hakemlik) 19 senaryo sunuluyor ve her biri için "kabul edilemez", "sonuçlarda beyan edilirse kabul edilebilir" ya da "beyan gerekmeksizin kabul edilebilir" seçenekleri isteniyor. Temel bulgu disiplinin belirgin biçimde bölünmüş olması: aynı pratik, katılımcıların kayda değer bir bölümü için hiç kabul edilemezken benzer büyüklükte başka bir bölüm için beyan bile gerektirmiyor. Makale için taslak plan üretmek %40 için kabul edilemezken %34 için beyansız kabul edilebilir; hakem raporlarını özetleyip revizyon stratejisi geliştirmek %37 için kabul edilemezken %40 için beyansız meşru. Yine de topyekûn red yok: sosyologların yalnızca %5'i tüm kullanımları kabul edilemez buluyor. Görece uzlaşı literatür aramada (%66 beyansız kabul), görselleştirme kodu yazmada (%82 kümülatif kabul) ve metin cilalamada (%49 kabul) görülüyor; buna karşılık ilk taslağı makineden istemek (%61 ret), başkasının makalesini modele yapıştırmak (%76 karşı) ve görüşmeleri katılımcıya bildirmeden chatbotla yapmak geniş biçimde reddediliyor. Kabul eğilimi nicel çalışanlarda (0,69 standart sapma), anadili İngilizce olmayanlarda (0,31 sd) ve erkeklerde daha yüksek. En çarpıcı politika bulgusu: %82,2 zorunlu GenAI beyanı istiyor, ama başkalarının beyanına güven yalnızca **%22** — yani beyan kurumu kendi içinde kırılgan. Yazarlar bu ikilemi, kullanım geniş ölçüde onaylanmadığı için beyanı gizleme teşvikinin doğması olarak okuyor; beyan kurumu kullanımın meşruiyetine bağlı. Bu yüzden zorunlu beyan tek başına yeterli değil.

**Anahtar noktalar:**
- 3.425 davet, 300 yanıt (%8,7); 19 senaryo, üç kategorili kabul ölçeği.
- Bölünme: aynı pratik hem "kabul edilemez" hem "beyansız kabul" olabiliyor; topyekûn ret yalnızca %5.
- Uzlaşı: literatür arama (%66 beyansız), görselleştirme kodu (%82), metin cilalama (%49).
- Ret: ilk taslak (%61), başkasının makalesini yapıştırma (%76), beyansız chatbot görüşmesi.
- Yordayıcılar: nicelciler +0,69 sd, anadili İngilizce olmayanlar +0,31 sd.
- Politika ikilemi: %82,2 zorunlu beyan isterken beyana güven %22.

**Türkiye notu:** Türkiye'de sosyoloji camiası bu tartışmanın tam ortasında ama veriyle desteklenen bir zemin yok. YÖK Akademik ve TR Dizin üzerinden yürüyen yayın baskısı, doçentlik ve akademik teşvik kriterlerinde "yayın sayısı" ağırlığını korurken üretken yapay zekâ en görünmez yerden — dil düzeltme, literatür taraması, özet çıkarma — rutin iş akışına giriyor. Makalenin en doğrudan Türkiye'ye bakan bulgusu, anadili İngilizce olmayan araştırmacıların GenAI'yi tüm aşamalarda belirgin biçimde daha kabul edilebilir bulması (0,31 sd): Türkiye'de İngilizce yayın zorunluluğu, uluslararası dergilerde yayın baskısı ve çeviri maliyeti, GenAI'yi bir "eşitleyici" olarak konumlandırıyor. Ama aynı bulgu bir riski de işaret ediyor: kabul eğilimi en yüksek grup, aynı zamanda beyan denetiminin en zayıf olduğu grup. Türkiye'de dergilerin GenAI beyanı şartı neredeyse hiç yok; bu, makalenin işaret ettiği "beyanı gizleme teşviki"nin en saf biçimde oluşacağı ortam.

**Erişim:** **200 (OSF preprint)**, tam metin açık.

---

### Makale 6: The Rights of Children and Youth in the Climate Crisis — Action and Litigation

**Künye:** Aoife Daly, Florencia Paz Landeira, Liesl Muller, *The Rights of Children and Youth in the Climate Crisis: Action and Litigation*, Routledge (Taylor & Francis), Londra, 1. baskı, 240 s., 8 bölüm, CC BY 4.0 (ERC fonlu), eBook ISBN 9781003298557, DOI 10.4324/9781003298557.

**ÖZET:** Kitap, iklim krizini bir çocuk hakları krizi olarak kuruyor ve çocukları "hak taşıyıcısı" değil **"hak yapıcı"** (rights-makers) olarak konumlandırıyor. Temel tez şu: çocuklar ve gençler yalnızca iklim politikalarından etkilenen mağdurlar değil, hukuki ve siyasi normları herkes için yeniden biçimlendiren aktörler; yazarlar bunu **"postpaternalist dönem"** olarak adlandırıyor. Sekiz bölüm boyunca sav üç katmanda örülüyor. İkinci bölüm sağlıklı çevre hakkının uluslararası hukuktaki hızlı gelişimini, Sürdürülebilir Kalkınma Amaçları ile UNFCCC metinlerinin çocuk haklarına yetersiz atfını ve çocuklar–gelecek nesiller bağlantısını inceliyor. Üçüncü bölüm CRC'nin ilgili maddelerini (sağlık, yaşam ve gelişim, eğitim, oyun, çocuğun yüksek yararı) ve özellikle Genel Yorum No. 26'yı çözümlüyor; m.12 (dinlenilme hakkı) üzerinden çocukların "iklim mağduru"ndan "çevresel hak savunucusu"na geçişini tartışıyor. Dördüncü bölüm çocukların siyasi failliğine kuramsal arka plan sunuyor ve **tokenizmi** (temsili katılım gösterisi) ayrı bir bariyer olarak açıyor. Beşinci bölüm yönetişim tarafında: ulusal ve yerel iklim meclisleri, danışma konseyleri, UNFCCC süreçleri ve GC26 hazırlığı — bu yeniliklerin çocukların sesini gerçekten güçlendirdiğini mi yoksa gücü yeniden mi dağıttığını soruyor. Altıncı ve yedinci bölümler **Youth Climate Justice veritabanındaki 81 iklim davasını** çocuk katılımı perspektifinden inceliyor; dava yolunun katılımın yeni bir biçimi olduğu ve kazanımların yalnızca davacı çocuklara değil genel olarak insan haklarına yayıldığı sonucuna varıyor. Kitabın katkısı ampirik olmaktan çok kavramsal-hukuki: çocuk haklarını koruma diliyle değil **norm üretme** diliyle yeniden yazıyor. Kitabın sınırı, dava yolunun uzun vadeli etkisini ölçmemesi: 81 davanın kaçının norm değişikliğiyle sonuçlandığı, kaçının yalnızca kamuoyu baskısı ürettiği ayrıştırılmıyor; ayrıca Küresel Güney'den dava örnekleri veritabanında seyrek, oysa iklim mağduriyetinin en ağır yaşandığı coğrafyalar tam oralar. Bu da dava temelli iklim stratejisinin ölçülebilir bir başarı tanımına ihtiyaç duyduğunu gösteriyor.

**Anahtar noktalar:**
- Tez: iklim krizi çocuk hakları krizidir; çocuklar "hak yapıcı"dır, "postpaternalist dönem".
- Yapı: sağlıklı çevre hakkı → CRC + GC26 → siyasi faillik/tokenizm → yönetişim → 81 dava.
- Görgül çekirdek: Youth Climate Justice veritabanı, 81 dava, CRC m.12 perspektifi.
- Tokenizm ayrı bir bariyer: katılım gösterisi ile karar yetkisi ayrı şeyler.
- Yazarlar: Daly (çocuk hakları hukuku), Paz Landeira (childhood studies), Muller (iklim hukuku).
- Sınır: tam metin bu ortamdan alınamadı; bulgular bölüm özetleri üzerinden.

**Türkiye notu:** Türkiye iklim krizinin etkilerini (orman yangınları, kuraklık, sıcak dalgaları, sel) yoğun yaşıyor ama bu etkiler hâlâ çocuk hakları diliyle değil, afet yönetimi ve enerji politikası diliyle çerçeveleniyor. Kitabın en verimli kavramı "postpaternalizm": çocukları korunacak nesne olarak gören vesayetçi yaklaşımın, onları hak öznesi ve hak yapıcı olarak gören yaklaşıma bırakması. Türkiye'de çocuk katılımı mimarisi (İl Çocuk Hakları Komiteleri, okul meclisleri, çocuk danışma süreçleri) büyük ölçüde danışma niteliğinde kalıyor; karar alma yetkisi devredilmiyor — kitabın tokenizm uyarısı tam buraya oturuyor. İkinci bağlantı dava yolu: Türkiye'de iklim davaları henüz çocuk hakları çerçevesinde kurulmuş değil; 81 davalık veritabanında Türkiye kaynaklı bir dava görünmüyor, bu da hem bir boşluk hem bir fırsat.

**Erişim:** **T&F kitap sayfası erişilemedi** (Cloudflare); bölüm düzeyindeki bulgular yayıncı bölüm özetlerinden (8 bölümün 7'si) doğrulandı, 7. bölüm özeti alınamadı.

---

## 3) GÜNCEL TARTIŞMALAR — ÇOCUKLUĞUN AMPİRİK TABANI

### Makale 7: Peer Victimisation Among School-Age Children in Türkiye

**Künye:** Melike Saraç & İsmet Koç (Hacettepe Üniversitesi Nüfus Etütleri Enstitüsü), "Peer Victimisation Among School-Age Children in Türkiye: A Blockwise Regression Analysis of the 2022 Child Survey", *Child Abuse Review* 35(6), Wiley, DOI 10.1002/car.70182 (online 27 Ekim 2026, baskı Kasım 2026). 35 kaynak, 0 atıf.

**ÖZET:** Makale, Türkiye'de 6–17 yaş çocuklarda akran zorbalığına maruz kalmanın yaygınlığını ve bağımsız ilişkili özelliklerini TÜİK'in 2022 Çocuk Araştırması mikro verisiyle inceliyor. Veri seti n = **10.210** çocuk; altı zorbalık türü tek bir genel göstergeye birleştirilmiş ve bu göstergenin ulusal tahmini (**%13,8**) yeniden üretilmiş. Analiz, hane düzeyinde küme-dayanıklı standart hatalarla ve nüfus ağırlıklı **blok blok (blockwise) lojistik regresyon** ile yürütülüyor: değişken grupları sırayla modele eklenerek hangi ilişkinin diğerlerini kontrol ettikten sonra ayakta kaldığı izleniyor. Tanımlayıcı bulgular çarpıcı: zorbalık, engellilik bildirimi olan çocuklarda **%32,4**, akademik performansı zayıf olanlarda **%25,4**, yakın arkadaşı olmayanlarda **%23,5**, kronik hastalığı olanlarda **%20,6**. Düzeltilmiş modelde bağımsız kalan faktörler: engellilik (AOR = **1,92**; %95 GA 1,27–2,92), zayıf akademik performans (AOR = **2,90**; 2,25–3,74), kronik hastalık (AOR = 1,43), yüksek göreli VKİ (AOR = 1,44), kız olmak (AOR = 1,19), küçük hane (2–3 kişi, AOR = 1,34) ve eğlence amaçlı ekran süresi (haftalık saat başına AOR = 1,014). Beklenmedik bulgu **aile yapısı ve gelir yeterliliği** ile ilişkilerin düzeltmeden sonra belirgin biçimde zayıflaması: yani yaygın anlatının aksine, bu veri setinde zorbalık daha çok çocuğun bireysel/klinik ve okul–akran özellikleriyle ilişkili, hanenin sosyoekonomik konumuyla değil. Yazarların çerçevesi de bunu vurguluyor: çok alanlı (multidomain) ulusal temsili kanıt nadir. Sınırlar ağır: makalenin tam metni okunamadı (Wiley Cloudflare; Unpaywall'da OA kopya yok, OpenAlex'te kayıt henüz yok), tüm sayılar Crossref tam özetinden alındı, zorbalık tür tanımları ve model uyumu doğrulanamadı, kesitsel tasarım nedensellik vermiyor. Bu, Türkiye'de zorbalık literatürünün en büyük eksikliğini de gösteriyor: TÜİK araştırması dört yılda bir tekrarlandığı için aynı çocuklar izlenemiyor ve nedensellik yönü hiçbir zaman sınanamıyor.

**Anahtar noktalar:**
- TÜİK 2022 Çocuk Araştırması, n=10.210, 6–17 yaş; ulusal yaygınlık %13,8 yeniden üretildi.
- Yöntem: küme-dayanıklı SE + nüfus ağırlıklı blok blok lojistik regresyon.
- Yaygınlıklar: engellilik %32,4 · zayıf akademik performans %25,4 · yakın arkadaşı yok %23,5 · kronik hastalık %20,6.
- AOR'lar: zayıf performans 2,90 · engellilik 1,92 · yüksek VKİ 1,44 · kronik hastalık 1,43 · kız 1,19 · küçük hane 1,34.
- Aile yapısı ve gelir yeterliliği düzeltme sonrası çöküyor — politika hedefi değişmeli.
- Ekran süresi küçük (%1,4/saat-hafta) ama bağımsız; doz-yanıt için boylamsal veri şart.

**Türkiye notu:** Bu, KURATOR açısından dönemin en kullanışlı Türkiye kayıtlarından biri: TÜİK'in 2022 Çocuk Araştırması mikro verisi bilinen kadarıyla ilk kez çok değişkenli bir zorbalık modelinde kullanılıyor ve ulusal %13,8 tahminini bağımsız olarak yeniden üretiyor — yani artık "TÜİK diyor ki" cümlesinin arkasında yöntemi denetlenebilir bir akademik referans var. Politika açısından en çarpıcı sonuç, aile yapısı ve gelir yeterliliği değişkenlerinin düzeltme sonrası çökmesi. Türkiye'de akran zorbalığı kamuoyunda ve Meclis çalışmalarında sık sık yoksulluk ve aile parçalanması çerçevesine oturtuluyor; bu veri, müdahale tasarımının hedefini değiştiriyor: engelli çocuklar, akademik olarak zorlananlar, kronik hastalığı olanlar ve sosyal ağı zayıf olanlar. Bir uyarı: kesitsel tasarım nedeniyle "zayıf performans zorbaliğa yol açıyor" demek mümkün değil; ters yön de aynı derecede makul.

**Erişim:** **403 (Wiley/Cloudflare, 6.127 B)**; değerlendirme Crossref tam özeti üzerinden.

---

### Makale 8: Does school climate matter? Mastery, performance and student voice climate

**Künye:** Leonidas Kyriakides, Demos Michael, Seaneen Sloan, Gabriela Martinez Sainz, Jennifer Symonds, Dympna Devine, "Does school climate matter? The impact of mastery, performance and student voice climate on promoting school effectiveness", *British Educational Research Journal* (BERA/Wiley), erken görünüm, e-locator berj.70296, hibrit açık erişim (CC BY-NC-ND 4.0), DOI 10.1002/berj.70296.

**ÖZET:** Çalışma, okul ikliminin okul etkililiğine etkisini İrlanda'nın ulusal boylamsal ilköğretim araştırması **Children's School Lives (CSL)** paneli üzerinden modelliyor ve öğrenci sesini (student voice) ayrı bir iklim boyutu olarak kuruyor. Dört bileşen ayrılıyor: ustalık (mastery) öğrenme iklimi, performans öğrenme iklimi, öğrenci sesi desteği ve çocukların ses pratikleri. Her ölçüm noktasında yaklaşık 1500 öğrenci var; okul etkililiği, öğrenci arka plan özellikleri kontrol edildikten sonra okulun okuma ve matematik başarısına yaptığı katkı olarak tanımlanıyor. İklim yapıları öğretmen bildirimleriyle ölçülüyor; yapı geçerliliği ve zaman içinde ölçme değişmezliği ayrıca sınanıyor. Yöntem zinciri üç aşamalı: önce çok düzeyli modelleme ile okullar her dalgada etkili/etkisiz olarak sınıflanıyor, ardından dalgalar arasındaki statü değişimi (iyileşme, durağanlık, gerileme) modelleniyor, son aşamada diskriminant fonksiyon analizi hangi iklim bileşeninin bu değişimi yordadığını test ediyor. Bulgular net bir ayrım veriyor: ustalık öğrenme iklimi, öğrenci sesi desteği ve çocukların ses pratikleri hem dönemler hem dersler arasında okul etkililiğindeki değişimi anlamlı biçimde yordamış. Performans öğrenme ikliminin etkisi ise tutarsız; yazarlar bunu performans iklimi kavramsallaştırmasındaki belirsizliğe bağlıyor ve kavramın netleştirilmesi gerektiğini söylüyor. Politika çevirisi açık: okul gelişimi için ustalık iklimini ve öğrenci sesini güçlendiren okul düzeyi müdahaleler, rekabetçi performans baskısından daha güvenilir bir kaldıraç. Sınırlılık tarafında iklimin öğretmen bildirimine dayanması, tek ülke paneline bağlı kalınması ve öğrenci sesinin kurumsal olarak ne kadar bağlayıcı olduğunun ölçülmemesi öne çıkıyor. Bir başka sınır, okul etkililiğinin yalnızca okuma ve matematik başarısıyla tanımlanması: sosyal-duygusal çıktılar, öğrenci refahı ve devam oranı modelin dışında; oysa öğrenci sesinin en güçlü etkisi tam da bu çıktılarda görülebilir ve mevcut tasarım bunu göremez. Öğrenci sesinin okul etkililiğine katkısı bu yüzden olduğundan küçük görünüyor olabilir.

**Anahtar noktalar:**
- Dört iklim bileşeni ayrı: ustalık, performans, öğrenci sesi desteği, çocukların ses pratikleri.
- Ustalık + öğrenci sesi, okul etkililiğindeki değişimi dönemler ve dersler arası yordamış.
- Performans iklimi etkisi tutarsız — sorun kavramsallaştırmada.
- Yöntem: CSL paneli (~1500/dalga), çok düzeyli modelleme + diskriminant fonksiyon analizi, ölçme değişmezliği sınanmış.
- Politika: ustalık ve öğrenci sesi, sınav baskısından daha güvenilir kaldıraç.
- Sınır: öğretmen bildirimi, tek ülke, sesin bağlayıcılığı ölçülmemiş.

**Türkiye notu:** Türkiye'de okul etkililiği tartışması hâlâ büyük ölçüde sınav başarısı, LGS/YKS yerleştirmeleri ve okul türleri arasındaki fark üzerinden yürüyor; iklim ve öğrenci katılımı çoğunlukla "disiplin" ve "motivasyon" başlıkları altında, ölçülmeden konuşuluyor. Bu çalışmanın en kullanışlı yanı, iklimi tek bir ölçek olarak değil birbirine zıt iki öğrenme iklimi ile iki katılım boyutu olarak ayırması. Türkiye'de okul iklimi ölçümleri çoğunlukla öğrenci algısına dayanıyor; CSL'nin öğretmen bildirimine dayanması bir sınır ama aynı zamanda bir yöntem alternatifi. Asıl politika dersi şu: Türkiye'de okul meclisleri ve İl Çocuk Hakları Komiteleri danışma niteliğinde kaldığı sürece "öğrenci sesi" bir iklim bileşeni olarak ölçülemez; ölçülmediği için de etkisi tartışılamaz.

**Erişim:** **403 (Wiley/Cloudflare, 6.130 B)**; CC BY-NC-ND işaretli olmasına rağmen bot duvarı nedeniyle tam metin alınamadı.

---

### Makale 9: Connected Childhood — The State of Digital Wellbeing and Resilience for Children and Young People in Europe (2026)

**Künye:** Viraj Rajdev, Caroline Paskell, Maya Bozhikova, Diana Vasileva, Rosie Castle (Ipsos); Jeffrey DeMarco, Daniela Ritz (Save the Children UK), *Connected Childhood: The State of Digital Wellbeing and Resilience for Children and Young People in Europe (2026)*, Save the Children UK & Vodafone Foundation, 71 s. + 7 s. Türkçe yönetici özeti, rapor kodu SCUK-VF-Connected-Childhood-2026.

**ÖZET:** Save the Children UK ve Vodafone Vakfı'nın Ipsos ile yürüttüğü ilk **Dijital Refah ve Dayanıklılık Endeksi (DWRI)** çalışması, dokuz Avrupa ülkesinde (Arnavutluk, Almanya, Yunanistan, Hollanda, Portekiz, Romanya, İspanya, Türkiye, Birleşik Krallık) 13–18 yaş arası **7.755** çocuk ve gençle Aralık 2025 – Ocak 2026'da yapılan anketi raporluyor. Endeks, SMILE çerçevesinin beş alanını (Security, Management, Identity, Literacy, Empathy) 0–100 ölçeğinde birleştiriyor; erişim (Enablement) ve öznel iyi oluş (Digital Wellbeing) endeksin dışında tutuluyor. Temel bulgu bir çelişki: katılımcıların **%73'ü** endekste "iyi" veya "yüksek" puan alırken yalnızca **dörtte biri** çevrimiçi ortamda kendini iyi ve dengede hissediyor. En güçlü alanlar güvenlik (%67) ve kimlik (%66); en zayıf alan açık ara **yönetim (%33, "yüksek" yalnızca %2)** — ekran süresi, bildirim yönetimi ve çevrimdışı denge kurmada çocukların üçte ikisi etkili bir stratejiye sahip değil. Dijital okuryazarlık %55'te kalıyor; algoritma farkındalığı ve bilgi doğrulama zayıf halka. Rapor, refahı çocukların kişisel sorumluluğuna bırakmanın yanlış olduğunu savunuyor: platform tasarımı (sonsuz kaydırma, bildirim mimarisi) ve yapısal eşitsizlikler belirleyici. Gıda güvensizliği, engellilik, düzenli kaygı-depresyon ve heteroseksüel olmayan kimlik bildiren gruplar her alanda sistematik olarak daha düşük puan alıyor: çevrimdışı dezavantaj çevrimiçine taşınıyor ve bazı durumlarda büyüyor. Türkiye endekste ikinci en yüksek "iyi+yüksek" orana (**%78**) ve %15 "yüksek" puana sahip; ama öznel refahta **%22** ile dokuz ülke ortalamasının (%27) altında ve yönetim alanında %38. Rapor altı öneriyle kapanıyor: tasarıma gömülü güvenlik, müfredata dijital refah, ruh sağlığı hizmetlerinin uyarlanması, öğretmen/ebeveyn kapasitesi, kapsayıcılık, endeksin düzenli ölçümü. Raporun kendi sınırı, endeksin kesitsel olması: aynı çocukların zaman içinde izlenmesiyle hangi alanın refahı sürüklediği hâlâ bilinmiyor. Panel tasarımı, önerilerin maliyetini de ölçebilir hale getirir.

**Anahtar noktalar:**
- 7.755 çocuk, 13–18, dokuz ülke; kota örneklemesi; Türkiye n=1.000.
- Çelişki: %73 endeks "iyi+yüksek", ama yalnızca ~dörtte biri öznel refah bildiriyor.
- En zayıf alan yönetim: %33 "iyi+yüksek", %2 "yüksek" — dokuz ülkenin tamamında.
- Eşitsizlik: engellilikte "yüksek" %7 vs %16; kaygı-depresyonda %7 vs %12.
- Türkiye: %78 endeks (2.), %15 yüksek (2.), ama öznel refah %22 (ortalama %27), yönetim %38.
- Türkiye çevrimdışı kaybı en yüksek ülke; "hiçbir şeyi kaçırmıyorum" diyenler yalnızca %5 (Arnavutluk %33).
- Sınır: kesitsel, öz bildirim, panel tabanlı örneklem; nedensellik yok.

**Türkiye notu:** Türkiye bu endekste ilk bakışta "iyi" görünüyor: %78 iyi+yüksek puanla dokuz ülke içinde ikinci. Ama raporun asıl mesajı tam bu tablonun yanıltıcılığında: aynı çocukların yalnızca %22'si çevrimiçi yaşamında kendini iyi hissediyor ve yönetim alanında iyi+yüksek oranı %38'de kalıyor. Yani Türkiye'de gençler dijital olarak **becerikli ama iyi değil**. Bu ayrım, 1 Kasım'da yürürlüğe giren yönetmeliğin hedefini de netleştiriyor: yasak, beceri eksikliğine değil **yönetim** eksikliğine denk geliyor — ve bu, tasarım rejiminin (sonsuz kaydırma yasağı, bildirim mimarisi, ebeveyn araçları) neden gerekli olduğunun en somut kanıtı. İkinci bulgu kültürel: Türkiye "çevrimdışıyken hiçbir şeyi kaçırmıyorum" diyenlerin oranının en düşük olduğu ülke (%5). Bu, bağlı kalma normunun akran grubunda ne kadar güçlü olduğunu gösteriyor ve bireysel "ekran süresi" müdahalelerinin neden burada zayıf kalacağını açıklıyor.

**Erişim:** **PDF 200 (129 KB)**, metin çıkarımı 170 karakterde kaldı; sayılar raporun Türkçe yönetici özeti ve anahtar gösterge tabloları üzerinden doğrulandı.

---

## OKUMA LİSTESİ

Bu haftanın havuzunda ayrıntılı işlenen 9 çalışmanın dışında kalan 23 kayıt. Öncelik sütunu, kaydın kendi `priority` etiketini yansıtır; "Konum" sütunu bu sayıda nasıl kullanıldığını gösterir.

| Zorluk | Makale | Konu | Öncelik | Konum |
|---|---|---|---|---|
| Yüksek | On "Confirmatory" Methodological Research in Statistics and Related Fields (*Statistics in Medicine*, 10.1002/sim.70303) | Doğrulayıcı metodolojik araştırmanın tanımı ve hakemlik standardı | high | Metodoloji tartışması — Makale 2 ve 3'ün doğal tamamlayıcısı |
| Orta | Paid to Post: Mapping the Political Influencer Industry (CDT) | Siyasi etkileyici endüstrisi, şeffaflık ve platform kuralları | high | 26 Ekim sayısında işlendi; tekrar edilmedi |
| Orta | Understanding Harness Engineering (techNmak, 48 s.) | Ajan mühendisliği pratiği; kendi kendine yayımlanmış el kitabı | medium | Arka plan — hakemsiz, doğrulanmadı |
| Yüksek | Propaganda as infrastructure: the Pravda network (*JITP*, 10.1080/19331681.2026.2747171) | Propagandanın altyapı olarak yeniden kavramsallaştırılması; 5M+ makale | high | KURATOR sayısında işlendi (bölüm 6) |
| Orta | Political, Ideological and Affective Gender Polarisation among Young People (YOPO, Helsinki) | Gençlerde cinsiyet kutuplaşması; Finlandiya–Macaristan | high | KURATOR bölüm 6; proje vitrini, ampirik bulgu yok |
| Orta | Political Noise and Disinformation in Southeast Asia (*IJTMS*, 10.66074/C5B8K6X3V) | SEA'da dezenformasyonun demokratik etkisi, sistematik derleme | medium | Bölgesel karşılaştırma için başvuru kaynağı |
| Yüksek | One Sentence at a Time: A Quantitative History of Rationality in Economic Thought (*EJHET*, 10.1080/09672567.2026.2698470) | İktisadi düşüncede "rasyonalite"nin nicel tarihi | medium | Teori tarihi — ayrı okuma önerilir |
| Orta | Six questions about political polarization (Gelman blog, 27.10.2026) | Kutuplaşma ölçümünün kavramsal sorunları | high | Blog; hakemsiz — ölçüm tartışması için |
| Düşük | Emotions as global low-dimensional brain flow patterns (Neural Flows) | Duyguların beyin ağ dinamikleriyle modellenmesi | low | Kapsam dışı — kitap tanıtımı |
| Orta | Theorizing the Democratic Crisis: Alexander Symposium (*Cultural Sociology*, 10.1177/17499755261484198) | Frontlash/backlash kuramı etrafında demokrasi tartışması | medium | Teori — kutuplaşma literatürüne köprü |
| Yüksek | Competitive autocracy goes online: the Turkish case (*Democratization*, 10.1080/13510347.2026.2733598) | 2022 dezenformasyon yasası; 16.000 kullanıcı, 1,1M gönderi | high | KURATOR bölüm 6; asimetrik risk |
| Yüksek | A Framework for Attribution of Information Influence Operations (ADAC.io D1.1) | IIO atfetmesinde usul, kanıt kategorileri, güven dili | high | Yöntem referansı — KURATOR'da anıldı |
| Orta | YSocial v4.0.0 (Scadrial) sürüm notu | Açık kaynak sosyal simülasyon platformu | medium | Araç — denenmeye değer |
| Orta | The Factory of Discord (EDMO Blog, 29.10.2026) | Yabancı aktörlerin Avrupa'da toplumsal huzursuzluğu sömürmesi | medium | Güncel — KURATOR haber bölümüne aday |
| Düşük | Agent-Based Modeling: Worlds Within Worlds (SFI) | Ajan tabanlı modellemeye interaktif giriş | low | Öğretim materyali |
| Orta | Cognitive Warfare: A Democratic Defence (KAS, 2 cilt, 439 s.) | Bilişsel savaş ve demokratik savunma; ülke özetleri | medium | Politika referansı — Türkiye bölümü ayrıca okunmalı |
| Yüksek | Manufacturing the Great Replacement (Dysinfluence) | Örtülü anti-Müslüman/anti-göçmen reklam kampanyası | high | Açık web araştırması — yöntem örneği |
| Orta | Ideas, institutions, and field theory (*RUCP*, 10.26851/rucp.35.13) | Alan kuramı ve kurumsalcılık | medium | Teori |
| Yüksek | Forecasting Social Science: Evidence from 100 Projects (NBER WP 34493) | Sosyal bilimde tahmin turnuvası; 100 proje | high | Metodoloji — Makale 3 ile birlikte okunmalı |
| Yüksek | The Economics of Intelligence (DeepMind Institute) | AGI'nin ekonomik dönüşüm koşulları | high | Politika denemesi — hakemsiz |
| Yüksek | Time-Varying Relationships Between "Sentiment" of U.S. Public Opinion and News Media (*IJPOR*, 10.1093/ijpor/edaf052) | Kamuoyu duygu durumu ile haber medyası arasındaki dinamik ilişki | high | Ölçüm — zamanla değişen katsayılar |
| Yüksek | Large language models for computational social science (*Nature Human Behaviour*, 10.1038/s41562-026-02539-9) | LLM'lerin dört rolü: nesne, asistan, ortak, değerlendirici | high | Bu sayının çerçeve metni — Makale 1–3'ün şemsiyesi |

---

## KAYNAKÇA VE ERİŞİM NOTU

### Ayrıntılı işlenen 9 çalışma

1. **Geiecke, F. & Jaravel, X.** (2026). Conversations at Scale: Robust AI-led Interviews. *The Review of Economic Studies* (kabul). DOI 10.1093/restud/rdag114. — Erişim: `restud.com`, tam metin alınamadı.
2. **Kohler, B., Zollikofer, D., Hoyle, A., Ash, E. & Einsiedler, J.** (2026). Read the Paper, Write the Code: Agentic Reproduction of Social-Science Results. arXiv:2604.21965v2. DOI 10.48550/arXiv.2604.21965. — Erişim: **200**, açık.
3. **Malmberg, A.** (2026). Investigating the Utility of LLM-Based "Silicon Samples" in Political Science Conjoint Experiments. *Public Opinion Quarterly*, nfag069. DOI 10.1093/poq/nfag069. — Erişim: **403**, özet Crossref; veri CC0.
4. **Jayadeva, S. & Livingstone, S.** (2026). Artificial intelligence and children's rights: a narrative review of the evidence. LSE DFC & 5Rights, 126 s. — Erişim: **200** (10.773 karakter).
5. **Stuhler, O., Stoltz, D. S., Alvero, A. J. & Taylor, M. A.** (2026). Is it Okay to Use Generative AI in Sociological Research? SocArXiv v1. DOI 10.31235/osf.io/y6vtp_v1. — Erişim: **200**, açık.
6. **Daly, A., Paz Landeira, F. & Muller, L.** (2026). *The Rights of Children and Youth in the Climate Crisis*. Routledge, 240 s. DOI 10.4324/9781003298557. — Erişim: kitap sayfası engelli, bölüm özetleri.
7. **Saraç, M. & Koç, İ.** (2026). Peer Victimisation Among School-Age Children in Türkiye. *Child Abuse Review* 35(6). DOI 10.1002/car.70182. — Erişim: **403**, özet Crossref.
8. **Kyriakides, L. vd.** (2026). Does school climate matter? *BERJ*, berj.70296. DOI 10.1002/berj.70296. — Erişim: **403**, özet Crossref.
9. **Rajdev, V. vd.** (2026). *Connected Childhood* (DWRI 2026). Save the Children UK & Vodafone Foundation, 71 s. — Erişim: PDF 200, metin çıkarımı sınırlı.

### Yöntem notu

- Havuz: 26–31 Ekim arasındaki 11 `*_categorized*.json` dosyası (26 kayıt) + pencerede üretilmiş 26 per-link JSON dosyası (29 kayıt) birleştirildi; `title[:70]` üzerinden tekilleştirildi → **32 benzersiz kayıt**. Günlük dosyalar örtüştüğü için URL yerine başlık üzerinden tekilleştirme yapıldı (X paylaşımlarında `original_url` değişiyor, çözümlenen yayıncı aynı).
- Sınıflandırma: 13 kayıt bot korumalı; %70 blok oranı nedeniyle metadata (Crossref/OpenAlex/Unpaywall) tabanlı mod. Hiçbir sayı doğrulanmamış bir kaynaktan alınmadı; tam metin okunamayan her başlıkta bu durum ilgili künyede yazılı.
- Bu sayıda işlenmeyen ama izlenmesi gereken başlık: *Paid to Post* (CDT) 26 Ekim sayısında ayrıntılı işlendi, tekrardan kaçınmak için Okuma Listesi'nde bırakıldı.

---

*Hafta 44/2026 · 9 çalışma ayrıntılı, 23 kayıt konumlandırılmış · 10 URL'lik Scrapling testi (%70 blok) · Metodoloji: blok blok regresyon, konjoint simülasyonu, ajanik tekrar üretim, panel analizi, kota örneklemli anket*
