---
type: concept
title: 'Kullanıcı Simülasyonu ve Gizli Durum Hizalaması (HumanLM)'
description: 'LLM tabanlı kullanıcı simülatörlerinin yüzey taklidi (stil, emoji, kalıp) yerine psikolojik gizli durumlar (inanç, amaç, duygu, değer, tutum, iletişim) üzerinden eğitilmesi; Stanford HumanLM/Humanual hattı ve kamuoyu araştırmasına etkileri.'
tags:
- kavram
- yapay-zeka
- simulasyon
- sentetik-kullanici
- metodoloji
- kamuoyu-arastirmasi
timestamp: '2026-11-26T16:10:00Z'
created: '2026-11-26'
updated: '2026-11-26'
sources:
- raw/articles/2026-02-07_humanlm-simulating-users-state-alignment.md
related:
- concepts/sentetik-populasyonlar.md
- concepts/sentetik-odak-gruplari.md
- concepts/synthetic-media-ai-content.md
confidence: medium
---

# Kullanıcı Simülasyonu ve Gizli Durum Hizalaması (HumanLM)

## Tanım

**Kullanıcı simülatörü**, belirli bir kişinin (ya da kişi tipinin) bir uyarana — haber, politika, mesaj, ürün — nasıl yanıt vereceğini LLM ile tahmin eden sistemdir. Uygulama alanları: kamuoyu ve seçmen araştırması, mesaj/çerçeve testi, kullanıcı-merkezli ürün geliştirme, sosyal bilimde ön-test.

İki eğitim stratejisi ayırt edilir:

- **Yanıt taklidi (response imitation):** Modele kişinin geçmiş metinleri verilir, SFT ile o üslupta yazması öğretilir. Kopyalanan şey **yüzeydir**: emoji sıklığı, noktalama, kalıp ifadeler, jargon. Bağlam kaydığında ya da duygu ile tutum çeliştiğinde model savrulur.
- **Durum hizalaması (state alignment):** Model, yanıtı üretmeden önce kişinin **o andaki içsel durumunu** doğal dilde üretir; bu ara ürün, gerçek yanıtla uyumu üzerinden pekiştirmeli öğrenmeyle (GRPO) ödüllendirilir. Kopyalanan şey yüzey değil, **yüzeyi üreten mekanizmadır**.

## Altı durum boyutu ve psikolojik dayanakları

- **belief (inanç):** bilişsel hat, Belief–Desire–Intention çerçevesi (Rao & Georgeff) — neyin doğru olduğuna dair temel varsayım.
- **goal (amaç):** bilişsel hat, aynı çerçeve — bu bağlamda neyin elde edilmek istendiği.
- **value (değer):** normatif hat, konumlanma kuramı (Davies & Harré) — neyin önemsendiği.
- **stance (tutum):** normatif hat, aynı — somut bağlamdaki pozisyon.
- **emotion (duygu):** duygusal hat (Zajonc; Sander vd.) — kısa vadeli, bilginin nasıl işleneceğini değiştiren süreç.
- **communication (iletişim):** dilsel hat (Levelt) — yanıtın yapılandırılması: doğrudan/dolaylı, iddia/kanıt, cevap/soru.

Kritik ayrımlar: **değer ≠ tutum** (dürüstlüğü önemseyen biri çocuğa Noel Baba'nın var olduğunu söyleyebilir); **tutum ≠ duygu** (bir politikaya aynı ölçüde karşı çıkan iki kişiden biri öfkeli, diğeri kaygılı olabilir); **iletişim ≠ üslup** (doğrudan/dolaylı yanıt, iddia/kanıt, cevap/soru — yapı düzeyi).

## Kanıt tabanı (HumanLM, 2026)

Humanual kıyaslama seti: 6 veri seti, 26 bin kullanıcı, 216 bin yanıt (haber yorumu, kitap incelemesi, günlük hayat görüşü, politik blog, e-posta, LLM sohbeti). LLM-yargıç hizalama puanında en iyi alternatife göre **%16,3 göreli iyileşme**. 111 katılımcılı kör insan testinde en yüksek benzerlik puanı (6,5/10) ve kazanma oranı (%41,4); katılımcıların %68,6'sı yanıtları "en benzer/nearly identical" buldu. Kod, model ve veri açık kaynak.

## Sınırlılıklar ve eleştirel notlar

1. **Yargıç bağımlılığı:** Ana metrik, bir LLM yargıcının verdiği hizalama puanı. Yargıcın kendi normatif beklentileri ödül sinyaline sızar; insan değerlendirmesi ikincil.
2. **"Klonlama" retoriği:** Popüler anlatı "kişinin zihnini kopyalıyor" der; makalenin iddiası daha dar — *belirli bir bağlama verilecek yanıtın* psikolojik ara değişkenler üzerinden daha isabetli tahmini. Bu ayrım, hem abartılı beklentileri hem de abartılı korkuları düzeltir.
3. **Rıza ve mahremiyet:** Kamusal veriler anonimleştirilse de "bu kişinin düşünme biçimini modelledik" iddiası, bilgilendirilmiş rıza sınırını zorlar. Kullanıcı çalışmasında açık rıza alınmış, ancak kamuya açık metinlerle eğitilen simülatörlerde bu güvence yok.
4. **Kötüye kullanım yüzeyi:** Bir kişinin duygu/tutum matrisini öngörebilen model, mikro-hedefleme ve ikna için doğal bir altyapıdır. Bu, [[concepts/synthetic-media-ai-content.md]] ve [[concepts/ai-generated-disinformation.md]] hatlarındaki sentetik içerik riskiyle birleştiğinde ölçek etkisi yaratır.
5. **Temsil sorunu:** Eğitim verisi İngilizce ağırlıklı kamusal metinler (Reddit, blog, e-posta, MTurk). Türkiye gibi bağlamlarda deyim, ironi, siyasal kodlar ve sansür kaynaklı ölçülü ifade, modelin "durum" çıkarımını bozabilir.

## Wiki içindeki yeri

- [[concepts/sentetik-populasyonlar.md]] — ajan-tabanlı nüfus hattı; HumanLM bunun birey düzeyinde ve psikolojik değişkenlerle zenginleştirilmiş hâli.
- [[concepts/sentetik-odak-gruplari.md]] — Novelli vd. karar matrisindeki "G0 veriye dayanmayan personas" katmanının teknik olarak aşılmaya çalışılması; G1/G2 dayanak düzeyine doğru bir adım.
- [[concepts/ai-generated-disinformation.md]], [[concepts/synthetic-media-ai-content.md]] — manipülasyon ve sentetik içerik riskleri.
- Ham kayıt: [[raw/articles/2026-02-07_humanlm-simulating-users-state-alignment.md]]
