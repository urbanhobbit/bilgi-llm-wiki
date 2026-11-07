---
type: concept
title: Tavşan Deliği Etkisi (Rabbit Hole Effect)
description: '## Tanım Öneri algoritmasının kullanıcının etkileşim sinyallerini (izleme
  süresi, beğeni) kalıcı ilgi beyanı olarak okuması ve benzer içeriği giderek daha sık
  servis etmesi; kullanıcı kısa sürede daralan ve sertleşen bir içerik hattına hapsolur.'
tags:
- kavram
- algoritma
- platform-tasarimi
- ruh-sagligi
- dsa
timestamp: '2026-11-07T07:05:00Z'
created: '2026-11-07'
updated: '2026-11-07'
sources:
- raw/articles/2026-11-06_tiktok-for-you-feed-breaches-dsa-on-rabbit-holes.md
confidence: medium
---

# Tavşan Deliği Etkisi (Rabbit Hole Effect)

## Tanım

Öneri algoritması, kullanıcının **etkileşim sinyallerini** (izleme süresi, tekrar izleme, beğeni) kalıcı bir **ilgi beyanı** olarak okur ve aynı türden içeriği giderek daha sık servis eder. Kullanıcı birkaç dakika içinde hem **daralan** hem **sertleşen** bir içerik hattına girer: üzgünlük, izolasyon, beden imgesi ya da belirli bir siyasal pozisyon etrafında sürekli tekrar. "Tavşan deliği" (rabbit hole) metaforu bu **kademeli derinleşmeyi** anlatır — kullanıcı tek bir adımda uç içeriğe atılmaz, her adımda bir öncekine benzer ama biraz daha yoğun içerik görür.

## Filtre balonundan farkı

[[concepts/filtre-baloncuklari.md|Filtre balonu]] (filter bubble) ile sık karıştırılır; ayrım **yön** ve **derinlik**tir:

- **Filtre balonu:** kullanıcının dünya görüşü yelpazesi daralır — farklı bakış açıları görünmez olur. Statik bir yalıtım hâli.
- **Tavşan deliği:** daralma bir **yörünge**dir — algoritma kullanıcıyı her turda daha uç, daha zararlı ya da daha umutsuz içeriğe taşır. Zaman içinde **şiddetlenme** ve **kontrol kaybı** vardır; "ilgilenmiyorum" gibi geri bildirimler etkisiz kalabilir.

Bu yüzden tavşan deliği etkisi yalnızca bir maruziyet sorunu değil, **çıkarım (optimizasyon) hedefinin** kendisiyle ilgili bir tasarım sorunudur.

## DSA'daki yeri (6 Kasım 2026 ön bulgusu)

Avrupa Komisyonu, 6 Kasım 2026'da TikTok hakkında DSA kapsamındaki ön bulgularında tavşan deliği etkisini **iki ayrı yükümlülük** üzerinden ele aldı:

1. **Risk değerlendirmesi:** TikTok'un, öneri algoritmasının kullanıcıları tavşan deliklerine sokma riskini yeterince değerlendirmediği.
2. **Risk azaltma:** mevcut tedbirlerin (çeşitlendirilmiş öneriler, kullanıcı kontrolleri) **etkisiz** olduğu — "ilgilenmiyorum" düğmesi akışı değiştirmiyor, çünkü sistem izleme süresini kullanıcının açık tercihine üstün tutuyor.

Komisyon'un önerdiği düzeltme **içerik kaldırma değil, tasarım değişikliği**: açık tercihlere ağırlık verilmesi, izleme süresinin öneri göstergesi olmaktan çıkarılması, kullanıcı kontrollerinin işler hâle getirilmesi ve algoritmanın düzenli test edilmesi. Bu, [[concepts/yapay-zeka-yonetisimi.md|AI governance]] literatüründe **çıktı denetimi yerine süreç/optimizasyon denetimi** olarak tartışılan yaklaşımın somut bir örneği; [[concepts/platform-seffaflik.md|platform şeffaflığı]] ise bu denetimin ön koşulu (risk raporlarının ve algoritma testlerinin görünür olması).

## Zarar mekanizması ve kime dokunuyor

Ön bulguda sayılan zararlar: **üzüntü ve kaygı artışı, beden memnuniyetsizliği, düşük öz-saygı, mevcut yeme bozukluklarının ve ruhsal durumların kötüleşmesi.** Risk, kırılgan yetişkinlerde ve reşit olmayanlarda yoğunlaşıyor — bu yüzden kavram [[concepts/sosyal-medya-genclik.md|gençlerin sosyal medya kullanımı]] ve [[concepts/cocuk-haklari.md|çocuk hakları]] tartışmalarının kesişiminde duruyor: ergenlerde hem maruziyet süresi hem de kimlik oluşumu açısından etki daha büyük.

## Wiki'deki vaka kaydı

- [[raw/articles/2026-11-06_tiktok-for-you-feed-breaches-dsa-on-rabbit-holes.md|TikTok For You feed breaches DSA on rabbit holes (Avrupa Komisyonu, 6 Kasım 2026)]]

## Kanıt durumu ve sınırlılıklar

- Komisyon'un dosyası **kamuya açık değil**; tavşan deliğinin **ölçülen derinliği**, etkilenen kullanıcı sayısı veya etki büyüklüğü hiçbir kamu kaynağında **sayı** olarak verilmiyor.
- Şirketler mekanizmayı reddediyor: TikTok, bulguların "platform mimarisini çarpıttığını" savundu (6 Kasım 2026).
- Bağımsız kanıtlar daha çok **nitel ve doküman temelli**: ör. Amnesty International'ın TikTok araştırmaları çocukların depresif ve intihar düşüncesi içeren içerik hattına çekildiğini belgeliyor.
- Akademik literatürde algoritmik tavşan deliğinin **nedensel büyüklüğü** tartışmalıdır (platform verisine erişim olmadan panel verisiyle ölçmek zor). Bu sayfa kavramı ve düzenleyici tanımı kaydeder; etki büyüklüğü iddiası taşımaz.

## İlgili Varlıklar

- [[entities/european-commission.md|European Commission]]

## İlgili Kavramlar

- [[concepts/filtre-baloncuklari.md|Filtre Balonları (Filter Bubbles)]]
- [[concepts/platform-seffaflik.md|Platform Şeffaflığı]]
- [[concepts/yapay-zeka-yonetisimi.md|Yapay Zeka Yönetişimi]]
- [[concepts/sosyal-medya-genclik.md|Sosyal Medya ve Gençlik]]
- [[concepts/cocuk-haklari.md|Çocuk Hakları]]
- [[concepts/emotional-amplification-loops.md|Emotional Amplification Loops]]
