---
type: concept
title: Keşifsel–Doğrulayıcı Ayrımı (Exploratory–Confirmatory Distinction)
description: 'Araştırmanın hipotez üretme (keşifsel) ile önceden yazılmış hipotezi sınama (doğrulayıcı) modları arasındaki ayrım; ön kayıt, HARKing, sözde-doğrulayıcı bulgular ve yöntem araştırmalarında tekrarlanabilirlik.'
tags:
- kavram
- metodoloji
- metascience
- on-kayit
- tekrarlanabilirlik
timestamp: '2026-10-25T00:00:00Z'
created: 2026-10-25
updated: 2026-10-25
sources:
- raw/articles/2025-11-10_on-confirmatory-methodological-research-in-statist.md
confidence: medium
---

# Keşifsel–Doğrulayıcı Ayrımı (Exploratory–Confirmatory Distinction)

Bilimsel araştırma iki moda ayrılarak okunur: **keşifsel** (hipotez üreten, veriye bağlı, "postdiction") ve **doğrulayıcı** (önceden yazılmış, gerekçelendirilmiş, test edilebilir hipotezi sınayan, "prediction"). Ayrım, verinin kendisinden çok **araştırma sürecinin önceden ne kadar sabitlendiğiyle** ilgilidir: doğrulayıcı araştırmada hipotez, tasarım, veri seçimi ve analiz planı veri görülmeden önce yazılır; keşifsel araştırmada araştırmacının serbestlik dereceleri (researcher degrees of freedom) kasıtlı olarak açık bırakılır.

## Neden önemli

- **HARKing** (hypothesizing after results are known): keşifsel bir bulgunun ardından hipotezin geriye dönük yazılıp doğrulayıcı bulgu gibi sunulması. Sonuç, bulguya aşırı güven ve düşük tekrarlanabilirlik.
- **Ön kayıt (preregistration)**: hipotez, tasarım ve analiz planının veri toplanmadan kamuya kaydedilmesi; HARKing'i ve seçici raporlamayı görünür kılar. Klinik denemelerdeki tescil pratiğinin sosyal bilimlere uyarlanmış hâli (OSF bu iş için yaygın altyapı).
- **Sözde-doğrulayıcı bulgu (pseudo-confirmatory)**: doğrulayıcı olmayan bir sonucun doğrulayıcı araştırmanın ürünüymüş gibi sunulması. İki kaynağı var: baştan keşifsel olan çalışmanın süslenmesi ya da doğrulayıcı niyetle başlayıp sorgulanabilir araştırma pratiklerine sapılması (seçici raporlama, sonuç görüldükten sonra hipotez değiştirme).

## Yöntem araştırmalarında özel durum

İstatistik ve hesaplamalı alanlarda (ML, biyoinformatik) yayımlanan **ampirik yöntem araştırması** — yöntemlerin simüle ya da gerçek veriyle incelenmesi — neredeyse tamamen keşifseldir, ama sık sık doğrulayıcı gibi sunulur. Üç yapısal neden:

1. Yeni bir yöntem hakkında önceki ampirik kanıt olmadığı için doğrulayıcı bir güç/kesinlik hesabı yapılamaz.
2. Yöntemin yaratıcısı yantarsızdır: tercih, aşinalık ve yatırım, tasarımdan raporlamaya kadar her aşamayı biçimlendirir.
3. Yöntem yaratma süreci ile yayımlanan değerlendirme arasında **veri sızıntısı** vardır — aynı veri setleri ya da onlara dair ön bilgi hem geliştirmede hem değerlendirmede kullanılır.

Bu yüzden "yeni yöntemini aynı makalede değerlendiren" çalışmaların bulguları provizyonel sayılmalıdır. Çözüm önerileri: protokol + ön kayıt, veri seti/veri üretme mekanizması seçiminin gerekçelendirilmesi, körleme veya dış analist ile yantaraflığın azaltılması, duyarlılık analizleri, makalede araştırmanın türünün açıkça yazılması, dergilerde zorunlu yantaraflık beyanı ve kod-veri paylaşımı.

## Süreklilik, ikilik değil

Keşif ve doğrulama idealize edilmiş iki uçtur; tek bir çalışma her ikisini de içerebilir. Pratik kural (Drude vd. 2022): **doğrulayıcı olduğunu açıkça belirtmeyen araştırmayı keşifsel say** — bu, onu değersizleştirmek değil, farklı bir bilimsel amaca hizmet ettiğini kabul etmektir.

## İlgili Kavramlar

- [[concepts/siyaset-bilimi-metodolojisi.md|Siyaset Bilimi Metodolojisi]]
- [[concepts/olcum-araclari.md|Ölçüm Araçları]]
- [[concepts/yapay-zeka-destekli-gorusmeler.md|Yapay Zeka Destekli Görüşmeler (AI Interviewing)]]

## İlgili Kaynaklar

- [[raw/articles/2025-11-10_on-confirmatory-methodological-research-in-statist.md|On "Confirmatory" Methodological Research in Statistics and Related Fields (Lange vd., Statistics in Medicine 44, 2025)]] — 115 biyoistatistik makalesinin taraması: %87 yalnızca simülasyon, hiçbir makale kendi araştırmasını keşifsel/doğrulayıcı diye etiketlemiyor, %92 aynı makalede önerilen yöntemi değerlendiriyor.
