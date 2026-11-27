---
type: raw_article
title: 'HumanLM: Simulating Users with State Alignment Beats Response Imitation'
description: 'Stanford (Zou & Leskovec grupları) tarafından geliştirilen HumanLM, kullanıcı simülatörlerini yüzey taklidi yerine psikolojik "gizli durum" hizalamasıyla eğitiyor; Humanual kıyaslama seti (26 bin kullanıcı, 216 bin yanıt) üzerinde LLM-judge hizalama puanında %16,3 göreli iyileşme.'
resource: 'https://arxiv.org/abs/2603.03303'
tags:
- kurator
- yapay-zeka
- sentetik-kullanici
- simulasyon
- metodoloji
timestamp: '2026-11-26T16:05:00Z'
source_file: telegram_ad_hoc
category: AKADEMIK OZEL
priority: high
published: '2026-02-07'
---

# HumanLM: Simulating Users with State Alignment Beats Response Imitation

**Künye:** Shirley Wu*, Evelyn Choi*, Arpandeep Khatua*, Zhanghan Wang, Joy He-Yueya, Tharindu Cyril Weerasooriya, Wei Wei, Diyi Yang, Jure Leskovec, James Zou (eşit kıdemli danışmanlık). Stanford University · New York University · Accenture. arXiv:2603.03303v1 [cs.CL], 7 Şubat 2026. Proje: https://humanlm.stanford.edu/ · Kod: https://github.com/zou-group/humanlm · Veri/model: Hugging Face `snap-stanford/humanual-datasets`, `snap-stanford/humanlm-models`

## Problem
LLM tabanlı kullanıcı simülatörleri (user simulators) yaygın biçimde **yüzey taklidine** dayanıyor: yazım tarzı, emoji kullanımı, kalıp ifadeler, ünlem işaretleri. Bu simülatörler verilen bağlam değiştiğinde (ya da tutum/duygu düzeyinde bir çelişki doğduğunda) çöküyor; çünkü kullanıcının **neye inandığını, neyi amaçladığını, ne hissettiğini** modellemiyorlar. Sonuç, gerçek kullanıcı davranışını yansıtmayan ve insan-merkezli uygulamalarda (politika testi, mesaj testi, ürün geri bildirimi) genelleşmeyen yanıtlar.

## Yöntem
HumanLM, SFT'nin (supervised fine-tuning) tersine, yanıtı üretmeden **önce** kullanıcının o anki içsel durumunu doğal dilde üretiyor ve bu ara ürünü pekiştirmeli öğrenmeyle (GRPO) gerçek yanıta hizmet edecek şekilde ödüllendiriliyor. Durum boyutları (state dimensions) dört psikolojik hattan türetiliyor:

- **Bilişsel hat** (Belief–Desire–Intention çerçevesi): *belief* (neyin doğru olduğuna dair inanç) ve *goal* (ne elde edilmek istendiği).
- **Normatif hat** (konumlanma kuramı): *value* (neyin önemsendiği) ve *stance* (somut bağlamdaki pozisyon). Aynı değere sahip iki kişi farklı tutum alabilir.
- **Duygusal hat**: *emotion* (kısa vadeli süreç). Aynı tutuma sahip iki kişi birbirinden farklı duygular (öfke / kaygı) taşıyabilir.
- **Dilsel hat**: *communication* (yanıtın yapılandırılması: doğrudan/dolaylı, iddia/kanıt, cevap/soru).

Döngü dört adım: ① durum boyutları → ② gizli durumların üretilmesi (ör. "politikayla anlaşmıyor", "kurbanlara empati", "doğrudan eleştiriyor") → ③ bir LLM yargıcının bu gizli durumları gerçek yanıtla hizalama puanıyla ödüllendirmesi → ④ hizalanmış gizli durumlardan yanıtın sentezlenmesi. Eğitim sırasında gizli durumlar kullanılıyor; çıkarım sırasında model akıl yürütme izinde bunları kendisi üretiyor.

## Değerlendirme: Humanual kıyaslama seti
- **Ölçek:** 6 büyük veri seti, **26 bin kullanıcı**, **216 bin yanıt**. Alanlar: haber yorumları, kitap incelemeleri, günlük hayat görüşleri (r/AmItheAsshole tipi), politik blog yorumları, e-posta yanıtları, LLM asistanıyla sohbet.
- **Ana sonuç:** LLM-yargıç hizalama puanında en iyi alternatife göre ortalama **%16,3 göreli iyileşme**.
- **Canlı insan testi:** 111 katılımcı, üç simüle yanıt (Qwen3-8B-think, GRPO-think, HumanLM) arasında kör karşılaştırma. HumanLM ortalama benzerlik puanı **6,5/10** (Qwen 6,1 · GRPO 5,9); en yüksek benzerlik kazanma oranı **%41,4** (Qwen %30,6 · GRPO %27,9). Katılımcıların **%68,6'sı** HumanLM yanıtlarını "en benzer" ya da "neredeyse aynı" buldu.
- **Açık kaynak:** kod, modeller ve veri kümeleri yayınlandı.

## Araştırma etiği (yazarların beyanı)
Kamuya açık veri kümeleri anonimleştirildi (de-identification). Kullanıcı çalışmasında Amazon Mechanical Turk işçilerinden yazılı metinlerinin kamuya açık veri seti olarak yayınlanması için **açık rıza** alındı, kişisel tanımlayıcı bilgi vermemeleri istendi, görev başına 9 $ (ortalama ~18 $/saat) ödendi.

## Neden önemli: siyaset bilimi ve kamuoyu araştırması açısından
1. **Sentetik seçmen / sentetik kamuoyu iddiasının teknik temeli değişiyor.** Bugüne kadar "LLM'e persona yaz, o kişi gibi konuştur" katmanı (wiki'de [[concepts/sentetik-odak-gruplari.md]] içinde "veriye dayanmayan personas" olarak anılan G0 düzeyi) metodolojik olarak zayıftı. HumanLM, simülatörü gerçek kişinin kendi yanıtlarına *hizalayarak* kalibre ediyor — yani [[concepts/sentetik-populasyonlar.md]] hattındaki ajan-tabanlı nüfus mantığını birey düzeyinde, psikolojik durum değişkenleriyle birleştiriyor.
2. **Cevapların "değişmezliği" testi.** Yüzey taklidi yapan modeller bağlam değişince savrulur; durum hizalaması iddiası, aynı kullanıcının farklı uyaranlara verdiği yanıtların iç tutarlılığının korunması demek. Politika iletişimi ve mesaj testinde (framing deneyleri) bu, geçerliliğin asgari koşulu.
3. **İkinci dereceden riskler.** (a) *Mahremiyet ve rıza:* rıza ve anonimleştirme protokolü kamuya açık verilerde bile "bu kişinin düşünme biçimini modelledik" iddiasının hukuki-ahlaki sınırını tartışmaya açıyor. (b) *Manipülasyon kapasitesi:* bir kişinin duygu/tutum matrisini öngörebilen simülatör, ikna ve hedefleme araçlarına dönüşebilir — [[concepts/synthetic-media-ai-content.md]] ve [[concepts/ai-generated-disinformation.md]] hatlarıyla kesişir. (c) *Ölçüm yanlılığı:* değerlendirme bir LLM yargıcına dayanıyor; "hizalama puanı" yargıcın kendi normatif beklentilerinden bağımsız değil.
4. **Metodolojik ayrım:** Bu çalışma "kişiyi klonlamak" değil, kişinin **bağlama verdiği yanıtı** tahmin etmek. Popüler anlatı (X dizisi) "zekanı kopyalıyor" diyor; makale daha dar bir iddiada: bir yanıt dağılımının psikolojik ara değişkenler üzerinden daha isabetli tahmini.

---

## 🔗 İlgili Bağlantılar
### 🧠 İlgili Kavramlar
- [[concepts/olcum-araclari.md|Ölçüm Araçları (Polarization Measurement)]]
### 🏛 İlgili Kurum/Kişiler
- [[entities/arxiv-org.md|Arxiv Org]]
- [[entities/arxiv-org.md|arXiv]]
- [[entities/stanford-university.md|Stanford University]]
