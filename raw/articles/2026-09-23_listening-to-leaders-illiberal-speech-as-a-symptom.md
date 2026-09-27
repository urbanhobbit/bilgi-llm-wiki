---
type: raw_article
title: 'Listening to Leaders: Illiberal Speech as a Symptom of Democratic Decline'
description: Bu makale, siyasi liderlerin resmi konuşmalarını demokratik gerilemenin
  erken ve bugüne kadar gözden kaçan bir semptomu olarak ele alıyor ve bunu ölçmek
  için Illiberal Speech Indicators (ISI) adlı yen...
resource: https://journals.sagepub.com/doi/10.1177/00104140261487983
tags:
- akademik
- high
timestamp: '2026-09-27T07:03:12Z'
source_file: 2026-09-27_listening-to-leaders-illiberal-speech.json
category: AKADEMİK ÖZEL
priority: high
roles:
- gap
- method
- result
published: '2026-09-23'
---

# Listening to Leaders: Illiberal Speech as a Symptom of Democratic Decline

**Author(s):** Seraphine F. Maerz (University of Melbourne), Dean G. Schafer (Mississippi State University), Carsten Q. Schneider (Central European University)

**Published:** 2026-09-23

**Source:** [https://journals.sagepub.com/doi/10.1177/00104140261487983](https://journals.sagepub.com/doi/10.1177/00104140261487983)

## Summary

Bu makale, siyasi liderlerin resmi konuşmalarını demokratik gerilemenin erken ve bugüne kadar gözden kaçan bir semptomu olarak ele alıyor ve bunu ölçmek için Illiberal Speech Indicators (ISI) adlı yeni bir gösterge seti geliştiriyor. Yazarlar (Seraphine F. Maerz – Melbourne, Dean G. Schafer – Mississippi State, Carsten Q. Schneider – CEU) kamu söylemini iki boyutta kavramsallaştırıyor: dışlayıcı-kapsayıcı (exclusive-inclusive) boyut, kimlik temelli dışlamayı ve azınlık haklarına/çoğulculuğa yönelik tavrı; güç yoğunlaşması-dağılımı (concentration-dispersion) boyutu ise yargı, medya, parlamento gibi yatay hesap verebilirlik kurumlarına yönelik saldırıyı ve otoriter yönetim arzusunu yakalıyor. Künye: Comparative Political Studies (SAGE), Online First, 23 Eylül 2026, DOI 10.1177/00104140261487983; CC-BY-NC.

Ampirik temel geniş: Global Populism Database ile LeaderSpeech korpusu birleştirilerek 409.570 paragrafa ayrılan konuşmalar, iki aşamalı bir makine öğrenmesi hattından geçiriliyor. Önce DeBERTa tabanlı konu-uygunluk filtreleri ilgisiz paragrafları eliyor, ardından ince ayarlı DeBERTa regresyon modelleri her paragrafı 0 (liberal) ile 10 (illiberal) arasında puanlıyor. Nihai puanlanmış korpus: 123 ülkede 452 liderin 1989-2024 arası konuşmaları; dışlayıcı-kapsayıcı boyutta 161.698, güç yoğunlaşması boyutunda 146.245 paragraf. Ölçüm, openai gpt-5.2 ve insan kodlayıcılarla doğrulanıyor; DeBERTa modelleri gpt-5.2'ye denk ya da biraz daha iyi performans gösteriyor (R² = 0,75 vs 0,76 ve 0,78 vs 0,71). Bu ölçüm aracı, puanları Bayesçi dinamik latent değişken modeliyle yıllara yayarak %95 güven aralıkları üretiyor ve klasik ortalama yerine 'high water mark' (yıl içindeki en yüksek %10 paragrafın ortalaması) kullanıyor: yazarlara göre bir lider bir kez kurumlara saldırdığında sonraki ılımlı söylem bunu telafi etmez.

Bulgular: illiberal söylemin baskın olduğu ülke-yılları, liberal söylemin baskın olduğu yıllara kıyasla V-Dem Electoral Democracy Index'te belirgin biçimde daha fazla düşüş yaşıyor. Dört dalgalı çapraz gecikmeli panel modelleri (CLPM) ilişkinin çift yönlü olduğunu gösteriyor: illiberal söylem gelecekteki demokratik erozyonu, demokratik erozyon da gelecekteki illiberal söylemi öngörüyor; yani kendi kendini besleyen bir geri bildirim döngüsü var. Yazarlar yine de nedensellik iddiasında temkinli: her illiberal konuşan lider demokratik çöküş yaşatmıyor, bu nedenle söylem bir 'risk sinyali' olarak okunmalı. Örnekler arasında Obama en liberal (2012'de en uç puanı 4,87), Trump hem seleflerinden hem halefinden belirgin biçimde daha illiberal, Biden ise seleflerinden daha yüksek puan alıyor; Bolsonaro, Orbán ve Erdoğan'ın yıllar içindeki illiberalleşme yörüngesi de vaka örnekleri olarak gösteriliyor.

Sınırlılıklar açıkça belirtiliyor: analiz betimleyici ve keşifsel, demokratik düşüş ölçüsü tek yönlü (iyileşmeler sıfır kodlanıyor), normalizasyon mekanizması doğrudan test edilmiyor. Veri ve kod Harvard Dataverse'te kamuya açık.

## Key Points

- ISI (Illiberal Speech Indicators) iki boyutlu yeni bir olcum araci: dislayici-kapsayici degerler + guc yogunlasmasi-dagilimi; her paragraf 0 (liberal) - 5 (notr) - 10 (illiberal) olceginde puanlaniyor.
- Olcekleme: 123 ulkede 452 liderin 1989-2024 arasi konusmalari; 409.570 paragraftan filtre sonrasi 161.698 (EI) ve 146.245 (CD) paragraf; latent tahminler 120 ulkede 429 konusmaci-yili icin mevcut.
- Yontem: ince ayarli DeBERTa konu filtresi + DeBERTa regresyon skorlayicisi, gpt-5.2 ve insan kodlayicilarla dogrulama (R2 0,75 ve 0,78; gpt-5.2 0,76 ve 0,71); Bayesci dinamik latent degisken modeli ile %95 guven araliklari.
- Olcum tercihi 'high water mark' (yil icindeki en yuksek %10 paragrafin ortalamasi): illiberal bir ifade sonraki ilimli soylemle 'dengelenemez' kabul ediliyor.
- Bulgular: illiberal soylemin baskin oldugu ulke-yillarinda V-Dem EDI dususu belirgin bicimde daha buyuk; dort dalgali CLPM cift yonlu iliski (geri bildirim dongusu) gosteriyor; ancak illiberal konusan her lider cokus yasatmiyor - soylem bir RISK sinyali.
- Vaka ornekleri: Obama en liberal (EI maksimum 4,87), Trump belirgin illiberal, Biden seleflerinden yuksek; Bolsonaro, Orban ve Erdogan'in illiberallesme yorungeleri.
- Seffaflik: tam metin kaynagi Harvard Dataverse replikasyon paketi (doi:10.7910/DVN/TK7Y3V - paper.qmd + ek materyaller); toplu veri doi:10.7910/DVN/OHGRC3; ince ayarli modeller Hugging Face'te (MIT); interaktif pano validation.shinyapps.io/speeches/

## Turkey Context

Türkiye bu makalenin merkezi örneklerinden biri: yazarlar Erdoğan'ın iki on yılı aşan iktidarında söylemin erken dönemdeki görece liberal tonundan (askeri vesayetin gerilemesi, Kürt barış süreci) belirgin biçimde illiberal bir hatta kaydığını ve bunun hem dışlayıcı-kapsayıcı hem güç yoğunlaşması boyutunda izlendiğini gösteriyor; AKP'nin elit ve kitle düzeyindeki otoriterleşmesine dair literatüre (Selçuk; Schafer) atıf yapılıyor. ISI panosunda Türkiye verisi ülke seçicisinde mevcut, dolayısıyla Türkiye'ye özgü yıl bazlı söylem eğrileri ve paragraf düzeyinde örnek metinler doğrulanabilir durumda.

Türkiye açısından üç sonuç çıkıyor. Birincisi, ölçüm yaklaşımı yerel araştırmaya taşınabilir: TBMM tutanakları, resmi açıklamalar ve cumhurbaşkanlığı konuşmaları üzerinden aynı iki boyutlu kodlama şemasıyla Türkçe bir ISI uyarlaması kurulabilir; bu, RTÜK/BTK düzenlemeleri ve yargı-medya ilişkilerine dair tartışmaları söylem düzeyinde ampirik bir tabana oturtur. İkincisi, bulgu 'söylem önemsizdir' varsayımını çürütüyor: demokratik erozyonun ölçümünde yalnızca kurumsal göstergelere (V-Dem, Freedom House, World Bank) bakmak, sinyal niteliğindeki söylemsel kaymayı kaçırır; Türkiye'de sivil toplum ve medya izleme kuruluşları için bu, erken uyarı göstergesi olarak kullanılabilir. Üçüncüsü, geri bildirim döngüsü tezi Türkiye'deki kutuplaşma ve 'normalizasyon' tartışmasıyla örtüşüyor: illiberal dilin tekrarıyla kabul edilebilir söylem sınırının kayması, seçim dönemlerinde nefret söylemi ve azınlık karşıtı mobilizasyon riskini artırır. Akademik tarafta ise çalışma, metin madenciliği ve LLM doğrulamasını birleştiren metodolojik standart olarak TÜBİTAK ve üniversite projeleri için yol gösterici.

## 🏷 Retorik Roller

- 🔍 **Araştırma Boşluğu**
- 🧩 **Yöntem**
- 📊 **Bulgular**

---

## 🔗 İlgili Bağlantılar
### 🧠 İlgili Kavramlar
- [[concepts/demokratik-erozyon.md|Demokratik Erozyon]]
- [[concepts/olcum-araclari.md|Ölçüm Araçları (Polarization Measurement)]]
- [[concepts/populizm.md|Popülizm]]
### 🏛 İlgili Kurum/Kişiler
- [[entities/journals-sagepub-com.md|Journals Sagepub Com]]
