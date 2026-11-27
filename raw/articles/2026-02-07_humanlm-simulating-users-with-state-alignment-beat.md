---
type: raw_article
title: 'HumanLM: Simulating Users with State Alignment Beats Response Imitation'
description: 'Stanford, NYU ve Accenture ortaklığıyla yürütülen HumanLM çalışması
  (arXiv:2603.03303, 7 Şubat 2026), LLM tabanlı kullanıcı simülatörlerinin temel zayıflığını
  hedefliyor: mevcut simülatörler kullanıcı...'
resource: https://arxiv.org/abs/2603.03303
tags:
- akademik
- genel
- high
timestamp: '2026-11-27T06:00:20Z'
source_file: 2026-11-27_categorized.json
category: AKADEMİK ÖZEL; GENEL
priority: high
published: '2026-02-07'
---

# HumanLM: Simulating Users with State Alignment Beats Response Imitation

**Author(s):** Shirley Wu, Evelyn Choi, Arpandeep Khatua, Zhanghan Wang, Joy He-Yueya, Tharindu Cyril Weerasooriya, Wei Wei, Diyi Yang, Jure Leskovec, James Zou (Stanford / NYU / Accenture)

**Published:** 2026-02-07

**Source:** [https://arxiv.org/abs/2603.03303](https://arxiv.org/abs/2603.03303)

## Summary

Stanford, NYU ve Accenture ortaklığıyla yürütülen HumanLM çalışması (arXiv:2603.03303, 7 Şubat 2026), LLM tabanlı kullanıcı simülatörlerinin temel zayıflığını hedefliyor: mevcut simülatörler kullanıcıyı yüzey düzeyinde taklit ediyor (yazım tarzı, emoji, kalıp ifadeler) ve bağlam değiştiğinde çöküyor; çünkü kişinin neye inandığını, neyi amaçladığını ve ne hissettiğini modellemiyorlar. HumanLM, yanıtı üretmeden önce kullanıcının gizli durumunu doğal dilde üretiyor ve bu ara ürünü, gerçek yanıtla hizalanması üzerinden GRPO ile ödüllendiriyor. Durum boyutları dört hattan türetiliyor: bilişsel (belief, goal), normatif (value, stance), duygusal (emotion) ve dilsel (communication). Eğitimde gizli durumlar veriliyor; çıkarımda model bunları kendi akıl yürütme izinde üretiyor. Değerlendirme için altı veri setinden 26 bin kullanıcı ve 216 bin yanıttan oluşan Humanual kıyaslama seti kurulmuş. LLM-yargıç hizalama puanında en iyi alternatife göre ortalama %16,3 göreli iyileşme raporlanıyor. 111 katılımcılı kör insan testinde HumanLM 6,5/10 benzerlik puanıyla önde (Qwen3-8B 6,1; GRPO 5,9); en yüksek benzerlik kazanma oranı %41,4 ve katılımcıların %68,6'sı yanıtları "en benzer" ya da "neredeyse aynı" buluyor. Etik bölümünde kamusal veri setlerinin anonimleştirildiği, Mechanical Turk çalışanlarından açık rıza alındığı ve görev başına 9 dolar (yaklaşık 18 dolar/saat) ödendiği belirtiliyor. Kod, model ve veri setleri açık. Yazarlar iddianın "kişiyi klonlamak" değil, yanıt dağılımını psikolojik ara değişkenler üzerinden daha isabetli tahmin etmek olduğunu vurguluyor; ancak değerlendirmenin LLM yargıcına dayanması ve manipülasyon kapasitesi risk olarak duruyor.

## Key Points

- Yüzey taklidi yapan kullanıcı simülatörleri bağlam değişince çöküyor; HumanLM gizli psikolojik durumu hizalıyor.
- Dört durum hattı: belief/goal, value/stance, emotion, communication.
- Humanual kıyaslama seti: 26 bin kullanıcı, 216 bin yanıt; LLM-yargıç hizalamasında %16,3 göreli iyileşme.
- 111 kişilik kör testte 6,5/10 benzerlik ve %41,4 kazanma oranı; %68,6 'en benzer/neredeyse aynı' değerlendirmesi.
- Etik: anonimleştirme, açık rıza, adil ücret; açık kaynak model ve veri. Risk: mahremiyet, manipülasyon, yargıç yanlılığı.

## Turkey Context

HumanLM'in Türkiye açısından en kritik yanı, siyasi düşüncenin KVKK'da özel nitelikli kişisel veri sayılması. 6698 sayılı Kanun'un 6. maddesi kişilerin siyasi düşüncesini özel nitelikli veri olarak tanımlıyor ve işlenmesini kural olarak yasaklıyor; istisnalar açık rıza veya kanunda öngörülen hallerle sınırlı. Bir seçmenin inanç, tutum ve duygu matrisini modelleyen bir simülatör tanımı gereği bu veri türüne temas ediyor. Kamuya açık sosyal medya metinlerinden eğitilen modellerde "anonimleştirme" iddiası, yeniden kimliklendirme riski nedeniyle tek başına yeterli güvence değil. İkinci risk, sentetik kamuoyu araştırmalarının seçim dönemlerinde manipülatif kullanımı. Türkiye'de kamuoyu araştırmaları 298 sayılı Seçim Kanunu ve ilgili mevzuat çerçevesinde yayın sınırlamalarına tabi; ancak "sentetik seçmen" çıktılarının anket gibi sunulması bu düzenlemelerin kapsamına henüz açıkça girmiyor. Üçüncü risk, mikro-hedefleme: bir kişinin duygu ve tutum örüntüsünü öngörebilen simülatörler, siyasi iletişimde ikna ve hedefleme araçlarına dönüşebilir. Kurumsal düzlemde YÖK'ün bilimsel araştırma etiği çerçevesi, üniversite etik kurullarının bu tür çalışmalarda rıza ve veri koruma denetimini güçlendirmesini gerektiriyor; TÜBİTAK'ın açık bilim politikası ise model ve veri kartlarının (model card) yayınlanmasını teşvik etmeli. BTK ve 5651 sayılı Kanun platform verilerinin hukuka uygun kullanımını düzenlerken, DSA ile uyumlu bir dijital hizmetler çerçevesi sentetik içerik ve sentetik persona kullanımının etiketlenmesini zorunlu kılabilir. Önerimiz: (1) seçim dönemlerinde sentetik persona ile siyasi mesaj testinin açık etiketleme ve kayıt yükümlülüğüne bağlanması; (2) üniversite etik kurullarında siyasi veri içeren simülasyon çalışmaları için özel inceleme; (3) açık kaynak modellerin Türkçe üzerinde ayrımcılık ve yanlılık testlerinden geçirilmesi; (4) kamuoyu araştırma şirketlerinin sentetik örneklem kullandığında bunu yöntem notunda beyan etmesi. Aksi halde metodolojik kazanım, denetimsiz bir ikna altyapısına dönüşebilir.

---

## 🔗 İlgili Bağlantılar
### 🏛 İlgili Kurum/Kişiler
- [[entities/arxiv-org.md|Arxiv Org]]
