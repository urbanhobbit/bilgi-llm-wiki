---
type: concept
title: Yapay Zeka Destekli Görüşmeler (AI Interviewing)
description: 'LLM tabanlı sistemlerin nitel görüşmeyi ölçeklendirmek için kullanılması; maruz kalma, özgüllük ve alaka üzerinden veri kalitesi, yerel açık ağırlıklı modeller ve görüşmeci etkisi.'
tags:
- kavram
- yapay-zeka
- nitel-yontem
- arastirma-yontemleri
timestamp: '2026-10-25T00:00:00Z'
created: 2026-10-25
updated: 2026-10-25
sources:
- raw/articles/2026-10-20_can-ai-interview-comparing-ai-led-to-human-led-cha.md
confidence: medium
---

# Yapay Zeka Destekli Görüşmeler (AI Interviewing)

Yapay zeka destekli görüşme, açık uçlu sorular soran ve yanıta göre bağlama duyarlı takip sorusu (sonda) üreten bir dil modelinin, nitel görüşmeyi insan görüşmeci olmadan yürütmesidir. Temel iddia, sosyal bilimin bilinen bir açmazını (Lazarsfeld 1944) kapatmaktır: anketin genişliği ile nitel görüşmenin derinliği arasındaki mesafe. Anket 1.000+ kişiye ulaşırken derinlemesine görüşme genellikle 20-40 kişide kalır; maliyet bu sınırın asıl nedeni olduğu için, görüşmenin marjinal maliyetini düşürmek örneklemi büyütmenin yolu olarak görülür.

## Kalite ölçütleri (Small & Calarco 2022)

Yapay zeka görüşmecinin değeri, insan görüşmeciyle **aynı ölçütlerde** karşılaştırılmadan iddia edilemez:

| Ölçüt | Ne ölçer | Ölçüm tuzağı |
|---|---|---|
| **Maruz kalma (exposure)** | Görüşmeye ayrılan zaman ve üretilen malzeme | Karakter sayısı derinlik değil uzunluk ölçer; uzun yanıt zengin yanıt demek değildir |
| **Özgüllük (specificity)** | Somut, deneyime dayalı ayrıntı düzeyi (1-5) | Kodlayıcılar arası güvenilirlik genellikle eşiğin hemen altında kalır; "fark saptanamadı" ≠ "fark yok" |
| **Alaka (relevance)** | Yanıtın soruyla ilgisi (1-5) | Puanlar tavana yığılır, varyans kalmaz, ayrım gücü düşer |

## Tasarım tercihleri

- **Yerel ve açık ağırlıklı model**: Ticari API'ye veri göndermek (a) gizlilik, (b) GDPR/KVKK uyumu, (c) yeniden üretilebilirlik açısından üç ayrı sorun üretir — API modelleri habersiz güncellenir, sürümden çıkarılır ve sistem istemleri açık değildir. Yerel model bu üç sorunu birlikte çözer; karşılığında tam açık model bulmak zordur (temel modelin eğitim verisi çoğu zaman belgelenmemiştir).
- **Özerklik kısıtı**: Modelin serbestçe yeni soru üretmesi yerine, yalnızca araştırmacının teorik ve etik olarak gerekçelendirdiği ana sorulara sonda üretmesi. Bu, kılavuza sadakati korur ama görüşmenin keşif kapasitesini sınırlar.
- **Görüşmeci etkisi**: İnsan görüşmecinin özellikleri veriyi nasıl sistematik olarak biçimlendiriyorsa, modelin eğitim verisi de biçimlendirir. Eğitim verisi belgelenmemişse bu etki tespit edilemez.

## Kanıt durumu

İlk doğrudan randomize karşılaştırma (Guven vd. 2026, N=41, eşzamanlı chat görüşmesi), 7B'lik yerel bir modelin eğitimli uzman olmayan insan görüşmeciyle kıyasla **birim zamanda belirgin biçimde daha fazla malzeme** topladığını, alaka açısından eşdeğer olduğunu, özgüllükte ise saptanabilir bir fark üretmediğini gösteriyor — ancak özgüllükte yarım puanlık bir insan üstünlüğü dışlanamıyor. Önemli sınır: karşılaştırma uzman görüşmeciye değil, büyük ölçekli projelerde kılavuzla eğitilen saha asistanına karşı; chat formatı sözlü ipuçlarını ortadan kaldırdığı için insan görüşmeciyi dezavantajlıyor. Sonuç, "yapay zeka görüşmeci uzmanın yerini alır" değil, "büyük-N nitel veri toplamada uygulanabilir" iddiasıdır.

## İlgili Kavramlar

- [[concepts/siyaset-bilimi-metodolojisi.md|Siyaset Bilimi Metodolojisi]]
- [[concepts/olcum-araclari.md|Ölçüm Araçları]]
- [[concepts/sentetik-populasyonlar.md|Sentetik Popülasyonlar]]
- [[concepts/yapay-zeka-yonetisimi.md|Yapay Zeka Yönetişimi]]

## İlgili Kaynaklar

- [[raw/articles/2026-10-06_conversations-at-scale-robust-ai-led-interviews.md|Conversations at Scale: Robust AI-led Interviews]] — ölçek sıçraması: N=461 (hayatın anlamı), 793 (zihinsel modeller), 338 (sesli görüşme); 20 transkriptte uzman puanı 2,93/5, sesli mod 3,93 ile yüz yüze insan uzmanı (3,51) geçiyor; tek ajanlı açık kaynak platform ve dört uygulama alanı.
- [[raw/articles/2026-10-20_can-ai-interview-comparing-ai-led-to-human-led-cha.md|Can AI interview? Comparing AI-led to Human-led Chat Interviews]] — 7B'lik yerel açık ağırlıklı modelle yürütülen ilk doğrudan randomize karşılaştırma (N=41); maruz kalma, özgüllük ve alaka üzerinden veri kalitesi.

