---
type: raw_article
title: Data-Driven Economic Agent-Based Models
description: Pangallo ve del Rio-Chanona'nın bu manifesto-review'ı, iktisadi ajan-temelli
  modellerin (ABM) veriyle kurduğu ilişkiyi sınıflandırıp 'veri-güdümlü ABM' diye
  bir kategori kuruyor. Yazarların ölçütü iki...
resource: https://arxiv.org/abs/2412.16591
tags:
- kurator
- akademik
- medium
timestamp: '2026-11-02T05:07:58Z'
source_file: 2024-12-21_data-driven-economic-abm.json
category: KURATOR; AKADEMİK ÖZEL
priority: medium
roles:
- method
- result
- limitation
published: '2024-12-21'
---

# Data-Driven Economic Agent-Based Models

**Author(s):** Marco Pangallo, R. Maria del Rio-Chanona

**Published:** 2024-12-21

**Source:** [https://arxiv.org/abs/2412.16591](https://arxiv.org/abs/2412.16591)

## Summary

Pangallo ve del Rio-Chanona'nın bu manifesto-review'ı, iktisadi ajan-temelli modellerin (ABM) veriyle kurduğu ilişkiyi sınıflandırıp 'veri-güdümlü ABM' diye bir kategori kuruyor. Yazarların ölçütü iki boyutlu: modelin ajan düzeyindeki nicelikleri (başlangıç koşulları, ajan nitelikleri) gerçek mikro-veriden mi alınıyor, ve modelin dinamikleri ampirik zaman serilerini mi izliyor? Yalnızca parametre kalibre eden ya da zaman-bağımsız özet istatistiklere uyan modeller 'az veri-güdümlü'; ajan düzeyinde veri alıp zaman serisini izleyenler 'en çok veri-güdümlü'. Bu ayrımla yazarlar, 2015 öncesi makro ABM'lerin çoğunu (stilize olguları ve özet istatistikleri eşleştiren, ajan niceliklerini teorik dağılımlardan örnekleyen modeller) kategorinin dışında bırakıyor ve son on yılda üç yöntem hattının olgunlaştığını gösteriyor: parametre kalibrasyonu, başlatma (initialization) ve veri asimilasyonu. Başarı öyküleri bölümü iddiayı somutlaştırıyor: Geanakoplos vd. (2012) konut balonu karşı-olgusalında faiz artışının değil kredi/değer sınırının işe yaradığını, Hallegatte (2008) Katrina'da dolaylı etkinin doğrudan etkinin %50'si olduğunu, Pichler vd. (2022) Birleşik Krallık 2020 ikinci çeyrek tahmininde çoğu kurumu geçtiğini, Poledna vd. (2023) Avusturya ekonomisini bire bir ölçekte modelleyip VAR ve DSGE ile yarıştığını gösteriyor. Yazarların önerisi net: stilize olgular ABM için artık asgari eşik olmalı, doğrulama örneklem-dışı tahmine taşınmalı. Manifesto, alanın yönünü de belirliyor: 'ad-hoc' eleştirisi — genel bir sınırlı-rasyonalite çerçevesi yok; çözüm olarak deney, psikoloji ve LLM tabanlı davranış kuralları öneriliyor. Yazarlar bunu bir araştırma gündemi olarak sunuyor, kesin bir sonuç olarak değil.

## Key Points

- Künye: arXiv:2412.16591 [econ.GN], v1 21 Aralık 2024 (tek sürüm; arXiv API 'updated' alanı 2026-11-02 gösteriyor ama gönderim geçmişinde yalnızca v1 var — bu metadata tazelemesi, yeni sürüm değil). Yazarlar Marco Pangallo ve R. Maria del Rio-Chanona. Metin kitap bölümü formatında: Borsos vd. (2024) çalışmasına 'in this volume' diye atıf yapılıyor (muhtemelen SFI Press 'The Economy as an Evolving Complex System IV'); hakemli dergi DOI'si yok, arXiv dışı yayın künyesi doğrulanamadı.
- Tanım/ölçüt: bir ABM, ajan düzeyindeki niceliklerin (xi,t değişkenleri veya ai nitelikleri) en az biri tüm ajanlar için veriden elde ediliyorsa ya da model en az bir ampirik zaman serisini izliyorsa 'veri-güdümlü' sayılıyor. Sınıflandırma iki eksenli: (dikey) zaman serisini mi yoksa yalnızca özet istatistikleri mi eşleştiriyor; (yatay) veriden alınan nicelikler modele mi yoksa ajana mı özgü. En veri-güdümlü çeyrek: hem ajan düzeyinde veri hem zaman serisi takibi.
- Tarihsel teşhis: 2015 öncesi makro ABM'ler stilize olguları ve özet istatistikleri (değişkenler arası korelasyonlar, firma büyüklüğü dağılımının kuyruk üsleri) eşleştiriyor, ajan niceliklerini teorik dağılımlardan örnekliyordu — bu yüzden yazarların ölçütünde 'veri-güdümlü' sayılmıyorlar. Veri-güdümlü modeller son on yılda ortaya çıktı.
- Üç yöntem hattı: (1) parametre kalibrasyonu (bir on yıldan uzun süredir gelişiyor), (2) başlatma/initialization (ajan niceliklerinin gerçek mikro-veriden atanması), (3) veri asimilasyonu (modelin zaman içinde gelen veriyle güncellenmesi) — son ikisi ABM için oldukça yeni ve büyük ölçekli modellerde tüm mikro-değişkenleri ayarlamak hâlâ açık problem; sinir ağı vekil modelleri (Grattarola vd. 2021; Casert vd. 2024; Cozzi vd. 2024) burada önerilen yol.
- Konut piyasası: Geanakoplos vd. (2012) 2008 krizi öncesi balonu Washington D.C. 1997-2009 verisiyle ve uygulanan gerçek politikalarla yeniden üretti; sonuç — faiz artışı balonu durdurmazdı, kredi/değer (LTV) sınırı çok daha etkili olurdu. Model birkaç merkez bankası tarafından kullanıldı/genişletildi.
- İşgücü piyasası: Axtell vd. (2019) ampirik işgücü akış ağlarının (heavy-tailed) aynı boş kadro oranında işsizliği artırdığını ve Beveridge eğrisini yukarı kaydırdığını gösteriyor; del Rio-Chanona vd. (2021) otomasyon riski yüksek bazı mesleklerde değil, geçiş yolu az olan mesleklerde işsizliğin daha çok arttığını ve denge varsayımının terk edilmesinin Beveridge eğrisinin saat yönünün tersine döngüsünü yeniden ürettiğini gösteriyor.
- Afetler ve pandemi: Hallegatte (2008) Katrina sonrası Louisiana'da girdi-çıktı ağını gerçek veriyle başlatıp dolaylı etkinin doğrudan etkinin ~%50'si olduğunu buldu. Pichler vd. (2022) Birleşik Krallık için 2020 ikinci çeyrek daralma tahminini veriler açıklanmadan yaptı ve çoğu kamu/özel kurumun tahmininden daha isabetli çıktı. Pangallo vd. (2023) New York metropolünde 500.000 kişilik sentetik popülasyonla salgın-ekonomi modelini birleştirdi: yüksek gelirlilerin daha az işsiz kalıp daha çok tüketim kıstığı 'Covid resesyonu' olgusunu yeniden üretti ve karşı-olgusal olarak kapanma ile gönüllü davranış değişikliğinin benzer ekonomik sonuç verdiğini gösterdi ('ekonomiye zararı virüs veriyor, kapanma değil').
- Makro: bilinen ilk veri-güdümlü makro ABM Bergmann (1974) — girdi-çıktı ağı gerçek veriden başlatılmış, 1967-1970 ABD makro istatistiklerini eşleştiriyor. En etkili güncel örnek Poledna vd. (2023): Avusturya ekonomisi bire bir ölçekte modellenmiş ve tahmin performansı VAR ve DSGE modelleriyle yarışıyor.
- Doğrulama önerisi: stilize olgular artık 'asgari eşik'; mümkün olduğunda örneklem-dışı tahminle doğrulama (ilk yıllarda kalibre edip sonraki yılları tahmin etme) ya da en azından örneklem içi zaman serisi eşleştirmesi. Yazarlar bunun için ince taneli veri ve ileri istatistiksel yöntem gerektiğini, önceliğin bu olduğunu söylüyor.
- Açık sorun — 'ad-hoc' eleştirisi: genel bir sınırlı-rasyonalite çerçevesi yok (Harstad ve Selten 2013), bu yüzden ABM'ler keyfî varsayım ve serbest parametre yığını olmakla eleştiriliyor. İki çözüm: kritik olmayan varsayımları veriyle değiştirmek (ör. hareketlilik için cep telefonu verisi, davranış değişikliği için tek parametre) ve hangi varsayımın modeli gerçekten iyileştirdiğini tahmin performansıyla test edip gereksiz olanı atmak.
- Tweet bağlamı ve iddia kontrolü: Alex Imas (Google DeepMind, AGI Economics direktörü; Chicago Booth'ta izinli) Andrey Fradkin'in 'SFI ajan-temelli modelleme gündemi iktisatta büyük bir başarısızlıktı, bunun tarihi yazılmalı' eleştirisine yanıt veriyor: 'ABM'ler tarihsel olarak veriye götürülmedi, ama bu değişiyor' diyerek bu makaleyi 'boşluğu kapatan çalışma' olarak sunuyor. Doğrulama: makale tam olarak bunu yapıyor ama bir *manifesto-review* olarak — yeni bir model değil, alanın durumunu sınıflandıran ve örnekleri derleyen bir çerçeve; yani 'boşluk kapanıyor' iddiası tek bir makaleyle değil, yazarların derlediği 15 yıllık bir literatürle destekleniyor. Imas'ın çerçevesi abartılı değil, ama makaleyi 'yeni köprü' değil 'alanın bilançosu' olarak okumak gerekiyor.
- Sınırlılık: yazarlar kendi konumlarını 'manifesto' olarak tanımlıyor — bu bir taraf tutan derleme; başarısız/yanlış ABM örnekleri sistematik olarak sayılmıyor, dolayısıyla seçilim yanlılığı riski var. Ayrıca veri erişimi (istatistik kurumları, özel sektör verisi) ve hesaplama maliyeti, önerilen doğrulama standardının önündeki pratik engeller olarak kabul ediliyor.

## Turkey Context

Türkiye'de iktisat politikası modelleri neredeyse tamamen denge geleneğinde: TCMB'nin ve Hazine'nin çalışma tezgâhında DSGE ve VAR hâkim, ABM ise marjinal bir merak olarak duruyor. Bu makale, o tercihin maliyetini somutlaştırıyor: ajan-temelli modellerin politika değeri, tam da veri-güdümlü hâle geldiklerinde ortaya çıkıyor — yani modelin mikro başlangıç koşulları gerçek veriden atandığında ve çıktılar zaman serisini izlediğinde. Türkiye bu iki koşul açısından ilginç bir vaka: mikro-veri var (TÜİK'in hanehalkı işgücü anketi, Hanehalkı Bütçe Araştırması, firma düzeyinde TÜİK Yapısal İş İstatistikleri, SGK kayıtları, TOBB sanayi veri tabanı) ama araştırmacı erişimi ağır kısıtlı ve mikro-veri setleri arasında eşleştirme yapmak için kurum içi protokol gerekiyor — yazarların 'başlatma zaman alıyor, devlet ve istatistik ofisleri veri erişimini kolaylaştırmalı' tespiti Türkiye için birebir geçerli. İkinci uygulama alanı afet ekonomisi: Hallegatte'in girdi-çıktı ağıyla dolaylı etkiyi ölçme yöntemi, 2023 Kahramanmaraş depremlerinin bölgesel ve ulusal ekonomik yayılımını modellemek için doğal bir çerçeve; Türkiye'de bu tür bir veri-güdümlü ABM'nin yapılmamış olması, tam olarak mikro-veri erişimi ve sektörel ağ verisinin (girdi-çıktı tabloları yıllık ve gecikmeli) sınırlılığıyla ilgili. Üçüncü nokta işgücü: otomasyon ve yapay zekâ etkisini meslek düzeyinde tartışırken Türkiye'de kullanılan yaklaşım genellikle görev-içeriği endekslerinin meslek paylarıyla ağırlıklandırılması; del Rio-Chanona vd.'nin gösterdiği gibi 'geçiş yolu az olan meslekler daha çok işsizlik üretir' içgörüsü ancak işgücü akış ağlarıyla modellendiğinde görünür hâle geliyor. Dördüncüsü, yazının açık bıraktığı 'ad-hoc' sorunu Türkiye'de daha keskin: kayıt dışı ekonominin büyüklüğü ve hanehalkı davranışının yüksek varyansı, davranış kurallarını veriyle disipline etmeyi zorunlu kılıyor. Son olarak siyasi iktisat: 'ekonomiye zararı virüs veriyor, kapanma değil' bulgusu, Türkiye'nin 2020 kapanma dönemindeki tartışmasına (kapanma mı, davranış mı?) doğrudan uygulanabilir bir karşı-olgusal çerçeve sunuyor.

## 🏷 Retorik Roller

- 🧩 **Yöntem**
- 📊 **Bulgular**
- ⚠️ **Sınırlılıklar**

---

## 🔗 İlgili Bağlantılar
### 🏛 İlgili Kurum/Kişiler
- [[entities/arxiv-org.md|Arxiv Org]]
