---
type: raw_article
title: 'One Sentence at a Time: A Quantitative History of Rationality in Economic
  Thought'
description: 'İktisat düşünce tarihinde nicel yöntemlerin nasıl kullanılabileceğini
  somut bir uygulamayla gösteren, hakemli yöntem makalesi. Künye: Delcey, Goutsmedt
  & Truc, The European Journal of the History of E...'
resource: https://hal.science/hal-05431080
tags:
- kurator
- medium
timestamp: '2026-10-27T07:58:19Z'
source_file: 2026-09-25_one-sentence-at-a-time-quantitative-history-rationality.json
category: KURATOR
priority: medium
roles:
- gap
- method
- result
- limitation
published: '2026-09-25'
---

# One Sentence at a Time: A Quantitative History of Rationality in Economic Thought

**Author(s):** Thomas Delcey (Université de Bourgogne), Aurélien Goutsmedt (UC Louvain, ISPOLE / ICHEC Brussels), Alexandre Truc (Université Côte d'Azur)

**Published:** 2026-09-25

**Source:** [https://hal.science/hal-05431080](https://hal.science/hal-05431080)

## Summary

İktisat düşünce tarihinde nicel yöntemlerin nasıl kullanılabileceğini somut bir uygulamayla gösteren, hakemli yöntem makalesi. Künye: Delcey, Goutsmedt & Truc, The European Journal of the History of Economic Thought 33(4), 835–887; DOI 10.1080/09672567.2026.2698470 (Crossref: online 25 Eylül 2026). Açık erişimli okunan sürüm SocArXiv ön baskısı v3 (11 Haziran 2026 derlemesi, 53 sayfa).

Soru ve iddia: "rational/rasyonalite" kavramının 20. yüzyıldaki anlam ve kullanım dönüşümü, gözetimsiz (unsupervised) nicel yöntemlerle — büyük dil modeli tabanlı anlamsal analiz + bibliyometri + ağ analizi — izlenebilir mi? Yazarlar bunu hem bir yöntem gösterimi hem de yöntem tartışması olarak kuruyor: nicel analiz, önceden tanımlanmış kategorileri dayatmadığı için şimdiciliği (presentism) azaltır, ama tek başına anlam üretmez; küme etiketleri ancak yakın okuma ve ikincil literatürle birlikte anlam kazanır.

Veri: 1900–2009 arası İngilizce 259.165 iktisat makalesi (tam metin) + atıf verisi — yazarlara göre alan için kurulmuş en büyük İngilizce korpus. Tam metin kaynakları JSTOR (ana kaynak), Scopus ile belirlenen Elsevier makaleleri ve ISTEX; atıf verisi Web of Science. Korpus 61 milyondan fazla cümleye ayrılıp Sentence-BERT ile vektörleştirilmiş; her yıl için "temsilci vektör" (representative vector) hesaplanmış ve buna en yakın cümlelerin ilk %1'i ile makalelerin ilk %10'u alt-korpus olarak alınmış.

Yöntem: (1) Metin tarafında onar yıllık dilimlerde HDBSCAN ile cümle kümeleri çıkarılıp yıllar arası kosinüs benzerliğiyle birleştirilmiş → 17 "zamanlararası anlamsal küme" (intertemporal semantic cluster). (2) Atıf tarafında 1960'tan başlayan, 8 yıllık örtüşen 43 pencerede bibliyografik eşleşme (bibliographic coupling) ağları kurulmuş ve Leiden topluluk algılamasıyla "bibliyometrik topluluklar" elde edilmiş; ardışık pencerelerde düğüm örtüşmesiyle "zamanlararası topluluklar" tanımlanmış. İki yaklaşım birbirini sağlama olarak kullanılıyor: metin anlamı, atıf ise etki ve dolaşım kanallarını gösteriyor.

Ana bulgular: "Rational/rationality" kullanımı savaş sonrasında düzenli artıyor; "rational" 1980'lerde, "rationality" 1990'larda tepe yapıyor. 1980'lerde en sık ikili ifade "rational expectations" ve diğer ikili ifadelerden 15 kat daha sık; rasyonel beklentiler 1960'larda veride hiç görünmüyor, 1980'lerde cümlelerin ~%30'una ulaşıyor (Muth 1961 → Lucas/Sargent aktarımı). "Rasyonalitenin toplumsal boyutu" sanıldığı gibi Soğuk Savaş sonrası değil, 1930'larda "rationalisation" (Brady 1932) tartışmalarıyla zaten belirgin. Sınırlı rasyonalite (bounded rationality) kavramı Simon'ın 1950'lerdeki formülasyonuna rağmen ancak 1990'larda yaygınlaşıyor; Simon'ın "Rationality & its Limits" kümesi 1950'lerde cümlelerin %5,76'sından 1990'larda %9,56'sına çıkıyor.

Simon vs. Kahneman–Tversky: Simon kavramsal olarak merkezî ama bibliyometrik olarak istikrarlı topluluk kuramamış — etkisi küçük, kısa ömürlü ve dağınık topluluklarda (cl_165, cl_123, cl_179, cl_258) kalmış, sonra post-Keynesyen/kurumsalci/heterodoks alanlara savrulmuş. Kahneman–Tversky (1979) ise 1978–1985 ağında kendi otonom kümesini (cl_391) kurmuş; 1980'e gelindiğinde K&T yıllık atıfta Simon (1955)'i geçmiş, 1985'te prospect theory Simon'ın ömür boyu atıf tepesini aşmış. 2000'lerde üç davranışsal iktisat topluluğu ağın ~%30'unu oluşturuyor. İlginç bulgu: Simon'a atıflar en yüksek düzeye "yeni" davranışsal iktisadın yükselişi sırasında çıkıyor — yazarlar bunu üç rakip yorumla sunuyor (gerçek canlanma / seçici sahiplenme / hegemoniyaya karşı retorik başvuru) ve verinin "sahiplenme"ye daha yakın durduğunu söylüyor.

Sınırlılıklar (yazarların kendi beyanı): OCR formül ve tabloları iyi işlemediği için biçimsel modeller anlamsal analizde zayıf görünüyor; atıf verisi 1960 öncesi için anlamlı değil; korpus kitap içermiyor; İngilizce ve ABD dergilerine yanlılık var; yöntem bir kavramın kökenini izlemekte zayıf (rasyonel beklentilerin 1960'larda görünmemesi bunun örneği); 259 bin makaleyi kuran veri ve kod, JSTOR lisansı nedeniyle paylaşılamıyor — paylaşılan şey kümeleri üreten kod.

Açık araç: küme ve toplulukları göstergeleriyle gezmeye izin veren açık kaynak uygulama — Zenodo 10.5281/zenodo.20558669 (DataCite ile doğrulandı) ve canlı Posit Connect sürümü; replikasyon dosyaları Zenodo 10.5281/zenodo.20641721.

## Key Points

- Künye: Delcey, T., Goutsmedt, A. & Truc, A. (2026), 'One sentence at a time: a quantitative history of rationality in economic thought', European Journal of the History of Economic Thought 33(4), 835–887; DOI 10.1080/09672567.2026.2698470; Crossref: online 25 Eylül 2026, yayıncı Informa (Taylor & Francis).
- Okunan sürüm: SocArXiv ön baskısı v3 ('paper_v3.pdf', 53 sayfa, derleme 11 Haziran 2026) — HAL kaydı hal-05431080 (v1/v2) Anubis bot koruması nedeniyle doğrudan indirilemedi, PDF OSF/SocArXiv üzerinden alındı ve tam metin okundu.
- Ölçek: 259.165 İngilizce iktisat makalesi (1900–2009), tam metin + atıf verisi; 61 milyondan fazla cümle Sentence-BERT ile vektörleştirilmiş. Kaynaklar: JSTOR, Scopus/Elsevier, ISTEX; atıf: Web of Science. Yazarlara göre alanın en büyük İngilizce korpusu.
- Yöntem-1 (metin): yıllık temsilci vektörlere en yakın cümlelerin %1'i + makalelerin %10'u; onar yıllık dilimlerde HDBSCAN, sonra kosinüs benzerliğiyle birleştirme → 17 zamanlararası anlamsal küme.
- Yöntem-2 (atıf): 1960–2009 arası 8 yıllık örtüşen 43 bibliyografik eşleşme ağı, Leiden topluluk algılaması; ardışık pencerelerde düğüm örtüşmesiyle 'zamanlararası bibliyometrik topluluk'. İki yöntem birbirinin sağlaması olarak kullanılıyor.
- Zamanlama bulgusu: rasyonel beklentiler 1960'larda metinde de ağda da görünmüyor; 1970'lerden sonra merkezîleşiyor ve 1980'lerde cümlelerin ~%30'una ulaşıyor. 'Rational expectations' 1980'lerde en sık ikili ifade ve diğerlerinden 15 kat sık.
- Kavram tarihi bulgusu: rasyonalitenin 'toplumsal' boyutu 1930'larda 'rationalisation' tartışmalarıyla zaten güçlü (Brady 1932: 'neredeyse hiçbir terim bu kadar tartışma yaratmadı'); kamu ekonomisi toplulukları 1960–70'lerde ağın beşte birinden fazlasını kaplıyor.
- Sınırlı rasyonalite gecikmesi: Simon'ın kavramı 1950'lerde var, ama 'bounded rationality' 1970'lerde kümenin ayırt edici sözcüğü, 1990'larda 'boundedly rational agents' / 'procedural rationality' ile merkezîleşiyor. 'Rationality & its Limits' kümesi: %5,76 (1950'ler) → %7,85 (1980'ler) → %9,56 (1990'lar, tepe).
- Simon vs. K&T: Simon kavramsal olarak etkili ama bibliyometrik olarak istikrarsız (cl_165, cl_123, cl_179, cl_258; sonra post-Keynesyen/kurumsalci kümelerde dağınık); Kahneman–Tversky 1978–1985'te otonom küme (cl_391) kuruyor, 1980'de yıllık atıfta Simon'ı, 1985'te Simon'ın ömür boyu tepesini geçiyor.
- Davranışsal iktisadın ağırlığı: 1981–1988 penceresinde 'Behavioral Economics: Risk & Uncertainty' ağın ~%5'i; 2000'lerde üç davranışsal topluluk ağın ~%30'u. Yeni davranışsal iktisadın yükselişi Simon atıflarını da zirveye taşıyor — yazarlar bunu 'sahiplenme' (appropriation) olarak yorumlamaya daha yakın.
- Finans bulgusu: rasyonalite finansa önce kurumsal finans (yatırım kararı, Modigliani–Miller) üzerinden girdi; varlık fiyatlamada davranışsal finans çıkana kadar örtük varsayım olarak kaldı. 1970'lerin ortasından itibaren finans ile rasyonel beklentiler yakınlaşıyor (Grossman–Stiglitz 1980 iki tarafta da merkezî).
- Şeffaflık: küme/topluluk göstergelerini (TF-IDF, merkeze en yakın cümleler ve makaleler, en çok atıf alan referanslar, topluluk 'kökleri ve varışları') gezmeye izin veren açık kaynak uygulama — Zenodo 10.5281/zenodo.20558669 + canlı Posit Connect sürümü; replikasyon: Zenodo 10.5281/zenodo.20641721 (ikisi de DataCite'te doğrulandı).
- Sınırlılık: korpus verisi ve kodu JSTOR lisansı nedeniyle paylaşılamıyor; atıf verisi 1960 öncesi için sessiz; kitaplar korpusta yok; İngilizce/ABD yanlılığı; yöntem köken izlemede zayıf (yazarların kendi uyarısı).

## Turkey Context

Türkiye açısından bu makalenin değeri, tekil bir bulgudan çok aktarılabilir bir yöntem paketi olması: 100+ yıllık, yüz binlerce metinlik bir korpusta kavram dönüşümünü ölçmek. Türkiye'de iktisat düşünce tarihi hâlâ ağırlıkla metin okuması ve kurum tarihçiliği üzerinden yürüyor; DergiPark'ta 2000 sonrası için çok geniş, 1950–1990 arası için ise dağınık ama erişilebilir bir Türkçe iktisat dergisi birikimi var. Aynı boru hattı (yıllık temsilci vektör + dilimlenmiş kümeleme + bibliyografik eşleşme) Türkçe için BERTurk tabanlı cümle gömmeleriyle kurulabilir; asıl darboğaz yöntem değil, 1960–1990 arası Türkçe süreli yayınların OCR kalitesi ve atıf verisinin yokluğu — yazarların formül/tablo uyarısı Türkçe gazete ve dergi taramalarında daha da sert geçerli.

KURATOR açısından asıl transfer edilebilir kısım 'sahiplenme' bulgusu: bir kavramın kurucusu (Simon) kavramsal olarak merkezî kalırken, onu popülerleştiren program (Kahneman–Tversky) hem atıf hem topluluk yapısı olarak alanı ele geçiriyor; kurucu figür sonradan retorik bir çıpa işlevi görüyor. Dezenformasyon ve kutuplaşma literatüründe aynı desen tekrar ediyor: kavramı ilk formüle eden isimler (ör. 'filter bubble' → Pariser) atıf ekonomisinde programı kuran kurumların/ekollerin gerisinde kalıyor. Bu, KURATOR'ün 'kim kurucu, kim taşıyıcı' ayrımını nicel olarak test etmesine yarayacak bir şablon.

Bir de madde: 259 bin makaleyi kuran korpusun kendisi paylaşılamıyor (JSTOR lisansı). Bu, açık bilim açısından önemli bir uyarı — Türkiye'de TR Dizin/DergiPark açık lisanslı olduğu için aynı ölçekte bir Türkçe korpus gerçekten paylaşılabilir; yani yöntemsel olarak geriden gelen alan, veri açıklığında öne geçme şansına sahip.

## 🏷 Retorik Roller

- 🔍 **Araştırma Boşluğu**
- 🧩 **Yöntem**
- 📊 **Bulgular**
- ⚠️ **Sınırlılıklar**

---

## 🔗 İlgili Bağlantılar
### 🧠 İlgili Kavramlar
- [[concepts/metin-madenciligi.md|Metin Madenciliği ve Hesaplamalı Metin Analizi]] — yıllık temsilci vektör + HDBSCAN kümeleme + bibliyografik eşleşme; metin madenciliği boru hattının en ayrıntılı anlatıldığı kaynak.
- [[concepts/siyaset-bilimi-metodolojisi.md|Siyaset Bilimi Metodolojisi]] — gözetimsiz yöntemlerin şimdiciliği (presentism) azaltma gerekçesi ve küme etiketlerinin yakın okumayla doğrulanması, sosyal bilimlerde araştırma yöntemleri tartışmasına doğrudan taşınabilir.
### 🏛 İlgili Kurum/Kişiler
- [[entities/hal-science.md|HAL Open Archive (hal.science)]] — gönderinin bağlantı hedefi (hal-05431080); Anubis duvarı nedeniyle tam metin oradan indirilemedi.
- [[entities/osf-io.md|OSF Preprints (SocArXiv)]] — tam metnin okunduğu sürüm: SocArXiv ön baskısı 10.31235/osf.io/38na2 (paper_v3.pdf, 53 sayfa).

