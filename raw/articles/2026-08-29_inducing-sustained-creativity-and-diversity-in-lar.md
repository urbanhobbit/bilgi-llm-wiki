---
type: raw_article
title: Inducing Sustained Creativity and Diversity in Large Language Models
description: 'Queenie Luo, Gary King, Michael Puett ve Michael D. Smith''in 29 Ağustos
  2026 tarihli çalışma makalesi (Harvard; IRB25-0151). Sorun tanımı: sosyal bilimde
  her proje bir ''arama görevi'' (search quest) il...'
resource: https://gking.harvard.edu/files/Inducing-Sustained-Creativity-LLM.pdf
tags:
- kurator
- high
timestamp: '2026-10-23T16:27:03Z'
source_file: 2026-10-23_gary-king-ai-better-worse-talk-and-quest-paper.json
category: KURATOR
priority: high
roles:
- gap
- method
- result
- limitation
published: '2026-08-29'
---

# Inducing Sustained Creativity and Diversity in Large Language Models

**Author(s):** Queenie Luo, Gary King, Michael Puett, Michael D. Smith

**Published:** 2026-08-29

**Source:** [https://gking.harvard.edu/files/Inducing-Sustained-Creativity-LLM.pdf](https://gking.harvard.edu/files/Inducing-Sustained-Creativity-LLM.pdf)

## Summary

Queenie Luo, Gary King, Michael Puett ve Michael D. Smith'in 29 Ağustos 2026 tarihli çalışma makalesi (Harvard; IRB25-0151). Sorun tanımı: sosyal bilimde her proje bir 'arama görevi' (search quest) ile başlar — araştırma konusu, nitel vaka, oyun ağacı ilkelleri, anket sorusu, politika yan etkisi seçimi — ve bu görevde kullanıcı olası cevapların tüm arama uzayını anlamadan karar veremez. Mevcut LLM'ler bunu yapamıyor: kod çözme (decoding) yöntemleri 'doğru cevap' için optimize edildiği için modal (en yaygın) cevapları döndürüyor, ısrar edildiğinde kendini tekrar ediyor ve herkese aynı cevabı vererek bilimde homojenleşme riski yaratıyor; üstelik modeller olgusal kıyaslamalarda güçlendikçe dağılım daha da sivrilip kuyruk bilgisi daha çok göz ardı ediliyor — yani sorun kötüleşiyor. Yazarlar 'Recoding-Decoding' (RD) adını verdikleri, yeniden eğitim ya da ince ayar gerektirmeyen bir kod çözme düzeni öneriyor: her cümle üretiminde isteme rastgele bir 'priming' ifadesi (en yaygın 2.000 İngilizce isimden seçilip '**Related to NOUN**' kalıbına yerleştiriliyor) ve her yeni cümlenin başına rastgele bir 'saptırıcı' (diverting) token ekleniyor; bu, LLM'lerin konum yanlılığından yararlanarak modeli modal yoldan uzaklaştırıp kuyruk bölgelerine yönlendiriyor. Değerlendirme: (1) dünya tarihi muharebe alanları — aynı istem 1.000 kez; olağan kod çözme (OD) yalnızca 19 benzersiz muharebe alanı üretirken (hepsi Avrupa ve Amerika, en ünlü örnekler) RD 1.157 benzersiz alan üretiyor (Doğu/Güney Asya, Rusya, Orta Doğu, Afrika, Avustralya dahil); ilgililik 0,98'e 1,00, olgusal doğruluk 0,98'e 1,00 ve OD'nin RD'ye eklediği tek bir alan yok. (2) Oyun kuramı: üç istem (caydırıcılık, pazarlık, sinyalleşme) için RD yaklaşık 2,8 kat daha fazla literatürde dayanağı olan benzersiz fikir üretiyor; ilgililik 1,000'e 0,987, literatür dayanağı %100,0'a %99,9; RD'nin ürettiği yapısal eklentiler (Okinawa'da ABD üssü, Afrika uranyum imtiyazı, Hürmüz Boğazı ablukası) mevcut literatürde karşılığı olan gerçek genişletmeler. (3) Araştırma fikri üretimi: 2017–2025 arası önde gelen dergilerden 50 replikasyon paketi (medyan 52 atıf), 50 istem × 50 koşu (Gemini-3.1-pro); RD her eşik değerinde (0,55–0,95) OD'yi geçiyor, ilgililik 0,997'ye 0,974. (4) Yüksek riskli politika: 50 gerçek bağlam, beş alan (askeri ihtimal planlaması, çatışma arabuluculuğu, Yüksek Mahkeme argümanları, yasama stratejisi/herestetik manevralar, kamuoyu araştırması segmentleri); RD'nin küme sayısı koşu sayısıyla büyümeye devam ederken OD doyuma ulaşıyor. (5) Sağlamlık: dört LLM (Deepseek-3, GPT-3.5, GPT-5.1, Gemini-3.1-pro) ve dört ek baseline (sohbet geçmişi, tek istem ifadesi, çoklu istem ifadeleri, sıcaklık 1.6) karşısında RD üstün; 500 geniş konu ve 1.000 koşuluk uzun ufuklu görsel değerlendirme testleri de aynı yönde. Katkı: 'çeşitlilik' ölçütünü sözcüksel tekrardan (n-gram, entropi) kavramsal ayrışmaya taşıyor ve arama görevini optimizasyon hedefi olarak tanımlıyor. Sınır: yöntem yine de bir kod çözme müdahalesi; 'yaratıcılık' LLM yargıçları ve kümeleme eşikleriyle ölçülüyor, insan değerlendirmesi sınırlı. Yöntem, hesaplamalı sosyal bilim (computational social science) ile LLM araştırmalarının kesişiminde duruyor: araştırma yöntemleri açısından katkısı, konu seçimini kişisel sezgiye bırakmak yerine ölçülebilir bir arama uzayı taramasına çevirmesi ve 'çeşitlilik' ölçütünü sözcüksel tekrardan kavramsal ayrışmaya taşıması.

## Key Points

- Yöntem: Recoding-Decoding (RD) — yeniden eğitim gerektirmeyen kod çözme müdahalesi; rastgele priming ifadesi + her cümlenin başına rastgele saptırıcı token, konum yanlılığından yararlanıyor.
- Amaç: LLM'in kuyruk bilgisini (konvansiyonel olmayan, heterodoks bilgi) açığa çıkarmak; hedef 'sürdürülebilir çeşitlilik' — koşu sayısı arttıkça tekrar değil yeni bölge.
- Muharebe alanları testi: OD 19 benzersiz alan (yalnızca Avrupa/Amerika), RD 1.157 benzersiz alan; ilgililik 0,98/1,00, olgusal doğruluk 0,98/1,00.
- Oyun kuramı testi: RD ~2,8 kat daha fazla literatürde dayanağı olan benzersiz fikir; örnekler Okinawa üssü (yeni oyuncu), Afrika uranyum imtiyazı (pazarlıkta ikinci boyut), Hürmüz ablukası (yeni eylem).
- Araştırma fikri testi: 50 replikasyon paketi × 50 koşu (Gemini-3.1-pro); RD tüm kümeleme eşiklerinde (0,55–0,95) OD'yi geçiyor.
- Yüksek riskli politika testi: 50 gerçek bağlamda (askeri planlama, arabuluculuk, Yüksek Mahkeme, yasama stratejisi, kamuoyu) RD doyuma ulaşmıyor, OD ulaşıyor.
- Sağlamlık: 4 LLM + 4 baseline (sohbet geçmişi, tek/çoklu istem ifadesi, sıcaklık 1.6) karşısında üstün; 500 geniş konu ve 1.000 koşuluk uzun ufuk testleri.
- Teşhis: modeller olgusal kıyaslamalarda güçlendikçe cevap dağılımı sivrilip kuyruk bilgisi daha çok göz ardı ediliyor — yani homojenleşme sorunu model geliştikçe büyüyor.

## Turkey Context

Türkiye'de sosyal bilim araştırmasının en kronik sorunu konu seçiminin dar bir 'moda' kümesine sıkışması; RD gibi bir kod çözme müdahalesi, aynı istemle herkesin aynı beş fikri alması yerine arama uzayının haritasını çıkarmayı mümkün kılıyor ve bunu model değiştirmeden, yalnızca istem/cümle düzeyinde yapıyor — Türkiye'de erişilebilir modeller (GPT, Gemini, açık kaynak Deepseek türevleri) için pratik. İkincisi dil: yöntem İngilizce isim listesi ve İngilizce kalıpla çalışıyor; Türkçe istemlerde priming/saptırıcı token dağarcığının Türkçeye uyarlanması ve etkisinin ayrıca sınanması gerekir, aksi halde çeşitlilik artışı İngilizce metinlerde kalır. Üçüncüsü teşvik: TÜBİTAK ve üniversite proje çağrılarında konu tekrarlarının artması hakem havuzunu da yoruyor; araştırma ofislerinin (proje geliştirme birimleri) RD benzeri araçlarla 'konu uzayı taraması' yapması, aynı konuya yığılmayı azaltabilir. Dördüncüsü yöntem eğitimi: lisansüstü yöntem derslerinde 'tek istem → beş fikir' pratiği yerine arama uzayı taraması öğretilmeli; ayrıca fikirlerin literatürde dayanağı olup olmadığı ayrıca kontrol edilmeli (makale bunu ayrı bir ajanla yapıyor). Beşincisi yönetişim: bu tür bir müdahale, 'AI aynı cevabı veriyor' eleştirisine teknik bir yanıt; ancak kurumsal düzeyde kullanılırsa farklı kurumların aynı RD parametreleriyle yine aynı uzaya yakınsama riski var — parametrelerin kamuya açık ama rastgeleleştirilmiş olması önemli.

## 🏷 Retorik Roller

- 🔍 **Araştırma Boşluğu**
- 🧩 **Yöntem**
- 📊 **Bulgular**
- ⚠️ **Sınırlılıklar**

---

## 🔗 İlgili Bağlantılar
### 🧠 İlgili Kavramlar
- [[concepts/siyaset-bilimi-metodolojisi.md|Siyaset Bilimi Metodolojisi]]
### 🏛 İlgili Kurum/Kişiler
- [[entities/gking-harvard-edu.md|Gary King (gking.harvard.edu)]]
### 📄 İlgili Makaleler
- [[raw/articles/2026-10-06_when-ai-makes-each-of-us-better-all-of-us-worse-an.md|When AI Makes Each of Us Better & All of Us Worse (Harvard AI Research Seminar)]]
- [[raw/articles/2026-10-22_ai-article-reviews-dominate-human-peer-reviews-at-.md|AI Article Reviews Dominate Human Peer Reviews at Their Best]]
