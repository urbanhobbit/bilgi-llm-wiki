---
type: concept
title: Negatif Bilgi Yanlılığı (Negativity Bias in News)
description: İnsanların olumsuz bilgiye olumluya kıyasla daha fazla dikkat ve tepki vermesi; haber seçiminde bireysel (trait) ve durumsal (state) bileşenleri, algoritmik kişiselleştirmeyle etkileşimi.
tags:
- kavram
- haber-tuketimi
- algoritma
- duygu
- siyasal-iletisim
timestamp: '2026-11-14T00:00:00Z'
created: '2026-11-14'
updated: '2026-11-14'
sources:
- raw/articles/2025-11-01_negativity-biases-online-the-interplay-of-individual.md
related:
- duygusal-kutuplasma
- emotional-amplification-loops
- filtre-baloncuklari
confidence: medium
---

# Negatif Bilgi Yanlılığı (Negativity Bias in News)

## Tanım

İnsanlar olumsuz bilgiye olumluya kıyasla **daha fazla dikkat, daha güçlü fizyolojik tepki ve daha iyi hatırlama** gösteriyor. Psikoloji, sinirbilim, ekonomi ve siyasal iletişimde geniş biçimde belgelenmiş; evrimsel bir kökene işaret ediyor (tehditten kaçınma). Haber bağlamında iki ayrı olguya ayrılıyor: **arz** (haber içeriği ortalama olarak negatife eğik) ve **talep** (okuyucu negatif başlığı daha sık seçiyor).

## Neden önemli

- **Dezenformasyon ve yanlış bilgi:** negatif çerçeveler daha hızlı yayılıyor; düzeltme (correction) negatif inançlarda daha zor tutuyor.
- **Seçici maruz kalma / filtre baloncukları:** algoritmalar geçmiş seçimleri taklit ettiğinde yanlılık **içeri gömülü** hale geliyor.
- **Haberden kaçınma (news avoidance):** aşırı negatiflik izleyiciyi siyasetten uzaklaştırabiliyor — yani yanlılık hem çekiyor hem itiyor.

## Ölçüm yaklaşımları

| Yöntem | Ne ölçer | Örnek |
|---|---|---|
| IAPS fotoğraf tepkileri | laboratuvar, psikofizyolojik | Soroka vd. (2019) |
| NBNS (anket tabanlı başlık seçimi) | 5 başlık görevi; 3 yıl arayla tekrar test | Bachleda vd. (2020) |
| Sözlük tabanlı duygu (LSD) | haber metni/başlığı net duygu skoru | Young & Soroka (2012); Noh & Soroka (2025) |
| Dijital iz (impression/read) | gerçek uygulamada seçim davranışı | Noh & Soroka (2025) |

## Trait mi, state mi? (kanıt çekirdeği)

Noh & Soroka (2025), SmartNews'te **25.171 kullanıcı / 113 milyon gösterim / 4,5 milyon tekil haber** üzerinden 6 ayı (Temmuz–Aralık 2023) inceliyor. Bootstrap ANCOVA ile açıklanan varyans:

| Model | Bağımlı değişken | User ID (trait) | Tarih (state) | Feed duygusu |
|---|---|---|---|---|
| 1 | Göreli NS okuma | **%3,97** | %0,72 | %0,35 |
| 2 | NS okuma | **%9,71** | %1,67 | %58,61 |
| 3 | NS gösterim (feed) | **%12,32** | %1,55 | — |

Yorum: haber **seçiminde** kalıcı bireysel fark **küçük ama gerçek** (~%4); haber **akışında** (feed) daha büyük (~%12). Yani kullanıcının negatiflik eğilimi yalnızca ne okuduğuna değil, **ona ne gösterildiğine** de gömülü. Panel testi (NSfeed_w ~ NSfeed_{w-1} + göreli NSreads_{w-1}): 0,074*** ve 0,011*** (N = 238.608, R² = 0,031).

## Tanımlayıcı bulgular

- Kullanıcıların **%7'sinden azının** feed'i net pozitif; okumalarda bu oran **%15,5**.
- Ortalama NS okuma **−0,048**, NS geçme (pass) **−0,044** → okunan içerik, gösterilenden **biraz daha negatif**.
- Ama göreli ölçümde (okuma − feed) değerlerin **~%40'ı pozitif** → kullanıcılar zaman zaman feed'lerinden **daha olumlu** içerik de seçiyor.

## Sınırlılıklar

Tek platform (SmartNews), tek 6 aylık pencere, konu bazlı ayrıştırma yok, sözlük tabanlı duygu ölçümü, kota örneklemi (temsili değil). Etki **büyüklükleri** platformdan platforma değişebilir; yönün değişmesi beklenmiyor.

## Vault'taki ilgili kayıtlar

- [[raw/articles/2025-11-01_negativity-biases-online-the-interplay-of-individual.md|Noh & Soroka (2025), Journal of Media Psychology]] — çekirdek ampirik kayıt.
- [[raw/articles/2026-10-22_avoiding-the-worst-leaders-is-more-important-than-.md|Lider seçiminde negatiflik asimetrisi]] — negatif bilgi yanlılığının siyasal sonucu.
- [[concepts/duygusal-kutuplasma.md|Duygusal Kutuplaşma]], [[concepts/emotional-amplification-loops.md|Emotional Amplification Loops]], [[concepts/filtre-baloncuklari.md|Filtre Baloncukları]]
