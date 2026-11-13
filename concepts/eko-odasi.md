---
type: concept
title: Yankı Odası (Echo Chamber)
description: Aynı görüşü paylaşan bireylerin karşıt görüşlere maruz kalmadan kapalı bir iletişim ağı içinde kalması; homofili, seçici maruziyet ve algoritmik filtrelemenin ortak ürünü.
tags:
- kutuplasma
- sosyal-medya
- dezenformasyon
- kavram
timestamp: '2026-11-13T00:00:00Z'
created: '2026-11-13'
updated: '2026-11-13'
sources:
- raw/articles/2026-11-07_breaking-echo-chambers-through-acceptance-of-diffe.md
confidence: medium
---

# Yankı Odası (Echo Chamber)

## Tanım
Yankı odası, bireylerin ağırlıklı olarak kendi görüşlerini **pekiştiren** enformasyon ve görüşlere maruz kaldığı, alternatif perspektiflere erişimin kısıtlandığı kapalı iletişim ortamıdır. Kavramı siyaset bilimine **Cass Sunstein** (*Republic.com*, 2001) kazandırdı; tanım gereği iki bileşen içerir: (1) yerel görüş homojenliği, (2) karşıt görüşe **maruziyetin** yokluğu. Bu iki bileşenden hangisinin ölçüldüğü, literatürdeki en büyük kavramsal karışıklık kaynağıdır.

## Birbirine Karışan Dört Şey
1. **Yankı odası:** grubun kendi içinde homojen olması *ve* dışarıdan kopuk olması.
2. **Filtre balonları (filter bubbles):** algoritmik kişiselleştirmenin ürettiği bilgi izolasyonu — mekanizma düzeyinde açıklama, yankı odasının kendisi değil. Ayrı kavram: [[concepts/filtre-baloncuklari.md|Filtre Balonları]].
3. **Pozitif bağlı grup:** yalnızca dostane ilişkilerle bağlanmış küme. **Dostane bağ, görüş anlaşması demek değildir** — yüksek tahammül rejiminde dostane grup içinde görüş çeşitliliği olabilir. Bu ayrım, ampirik çalışmalarda sık yapılan bir hatayı önler.
4. **Benzer düşünen grup (like-minded group):** tüm konularda çoğunlukla aynı görüşü paylaşanların bağlantılı kümesi — yankı odasından daha geniş, daha zayıf bir ölçüt.

## Mekanizmalar
- **Homofili:** benzer görüşlülerin birbirine bağlanma eğilimi; ağ topolojisi üzerinden yankı odası üretir.
- **Seçici maruziyet:** bireyin kendi görüşünü doğrulayan içeriği aktif olarak araması.
- **Algoritmik filtreleme:** etkileşim odaklı sıralamanın (engagement-based ranking) homojenliği pekiştirmesi.
- **Uzlaşma arzusu (consensus-seeking):** grubun içinde anlaşmaya varma isteği; kısa vadede uyumu artırır, uzun vadede karşıt görüş maruziyetini düşürür.
- **Ayrılığa tahammülsüzlük:** fikir ayrılığının ilişkiyi düşmanca hale getirmesi — karşıt görüşe "maruz kalmak" varsa bile bunun **çatışma** kanalından gerçekleşmesi.

## Kırma Stratejileri (literatürde test edilenler)
- **Ayrılığı kabulü artırmak (τ):** görüşleri yakınlaştırmadan, ayrı görüşlüler arasında dostane bağ kurulmasına izin vermek. Model sonuçları: maruziyetin toplamı artar ve **niteliği düşmancadan dostaneye** kayar.
- **İnatçı ajanlar / arabulucular (stubborn agents):** gruplar arası bilgi akışını sağlayarak uzlaşmayı hızlandırma.
- **Düzenleyici müdahaleler:** platform tasarımı, şeffaflık, sıralama denetimi.
- **Karşıt görüşe rastgele maruz bırakma (random exposure) ve haber diyeti müdahaleleri:** etkisi en çok tartışılan grup.

## Kanıt Tabamı (Wiki)
- [[raw/articles/2026-11-07_breaking-echo-chambers-through-acceptance-of-diffe.md|Huang, Chung & Chew (2026), *Complexities* 2(4):26]] — ABLTD simülasyonu; τ (ayrılığı kabul) düştükçe yankı odaları nüfusun %60–80'ine yayılıyor, τ yükseldikçe en büyük yankı odası %1'in altına iniyor. **Simülasyon kanıtı, ampirik değil.**
- [[raw/articles/2026-10-12_polarization-and-echo-chambers-in-reddit-s-politic.md|Reddit siyasi tartışmalarında kutuplaşma ve yankı odaları (2026)]] — ampirik platform verisi.
- [[raw/articles/2026-08-28_from-echo-chambers-to-cross-boundary-diffusion-a-m.md|Yankı odalarından sınır-ötesi yayılıma (2026)]] — yankı odası çerçevesinin sınırları.
- [[raw/articles/2026-09-29_the-disappearance-of-political-moderates-online-ho.md|Ilımlıların çevrimiçi kayboluşu (2026)]] — ılımlıların çekilmesiyle oluşan görünürlük yanlılığı.
- [[raw/articles/2025-08-23_unfollowing-hyperpartisan-social-media-influencers.md|Aşırı partizan etkileyicileri takibi bırakmak (2025)]] — müdahale deneyi.
- [[raw/articles/2026-06-26_depolarization-toolkit-an-agentic-ai-framework.md|Depolarizasyon araç kutusu (2026)]] — ajan-tabanlı yapay zekâ müdahaleleri.

## İlgili Kavramlar
- [[concepts/sosyal-kutuplasma.md|Sosyal Kutuplaşma]]
- [[concepts/dezenformasyon.md|Dezenformasyon]]
- [[concepts/yanlis-kutuplasma.md|Yanlış Kutuplaşma]]
- [[concepts/affective-polarisation.md|Affective Polarisation]]

## Ölçüm Uyarısı (metodolojik)
"Karşıt görüşe maruz kalma" iki farklı şeyi gösterebilir: (a) kişinin **en az bir** karşıt komşusu olması (ikili maruziyet), (b) karşıt görüşlerin kişinin bağlantılarının **ne kadarı** olduğu (ağırlıklı maruziyet). Huang vd. (2026) bu ikisinin çok ayrıştığını gösteriyor (ikili ≈0.47 iken ağırlıklı ≈0.14) ve maruziyetin **işaretini** (dostane/düşmanca) ölçmenin zorunlu olduğunu savunuyor. Türkiye'de X/Twitter etkileşimini "cross-cutting exposure" sayan ölçümler bu ayrımı yapmadığı için yanıltıcı olabilir.

## Türkiye'ye Aktarım Notu
Türkiye'de yankı odası tartışması çoğunlukla **içerik/kanal** düzeyinde yürüyor (partizan TV, gazete, X ekosistemi). Bu kavram çerçevesi, ölçümü üç eksene ayırmayı öneriyor: (1) ağ homojenliği, (2) karşıt görüş maruziyetinin varlığı, (3) maruziyetin niteliği. Üçüncüsü Türkiye için kritik: kutuplaşmış kamusal tartışmada karşıt görüş çoğu zaman **alıntılanma, ifşa ve kavga** kanalıyla dolaşıma giriyor; bu, modelin "düşük τ" rejimine denk düşer ve yankı odasını küçültmediği gibi derinleştirir.
