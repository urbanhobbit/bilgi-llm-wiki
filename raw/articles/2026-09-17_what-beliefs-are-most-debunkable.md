---
type: raw_article
title: What beliefs are most debunkable?
description: Bu çalışma, yapay zekâ ile ikna edilen inançların hangilerinin daha kolay
  "çürütülebilir" (debunkable) olduğunu ve bunun neden kaynaklandığını doğrudan test
  ediyor. Esther Boissin, Thomas H. Costello,...
resource: https://osf.io/preprints/psyarxiv/xe72y_v1
tags:
- kurator
- high
timestamp: '2026-09-28T17:15:59Z'
source_file: 2026-09-17_what-beliefs-are-most-debunkable.json
category: KURATOR
priority: high
roles:
- gap
- method
- result
published: '2026-09-17'
---

# What beliefs are most debunkable?

**Author(s):** Esther Boissin (Cornell University), Thomas H. Costello (Carnegie Mellon University), David G. Rand (Cornell / MIT Sloan), Gordon Pennycook (Cornell / University of Regina)

**Published:** 2026-09-17

**Source:** [https://osf.io/preprints/psyarxiv/xe72y_v1](https://osf.io/preprints/psyarxiv/xe72y_v1)

## Summary

Bu çalışma, yapay zekâ ile ikna edilen inançların hangilerinin daha kolay "çürütülebilir" (debunkable) olduğunu ve bunun neden kaynaklandığını doğrudan test ediyor. Esther Boissin, Thomas H. Costello, David G. Rand ve Gordon Pennycook, üç çalışmadan havuzlanan 3.341 ABD'li yetişkinin kendi bildirdikleri komplo inançları ve diğer epistemik olarak şüpheli inançları üzerine GPT-4 ile üç turluk, kanıt sunmaya yönlendirilmiş diyaloglarını (toplam 10.020 model mesajı) analiz ediyor. Her inanç, katılımcıdan bağımsız olarak – model tarafından – iki eksende kodlanıyor: içerik alanı (komplo %32, diğer %18, paranormal/dogaüstü %18, sözde-bilimsel %12, din %12, siyaset %8) ve kanıtsal statü (desteklenen, yanlışlanamaz, araştırılmamış, zayıf karşı-kanıt, güçlü karşı-kanıt).

Bulgular net: Güven düzeyi her alanda düşüyor (komplo koşulu −12,60; epistemik inanç koşulu −6,35 puan, 0–100 ölçeğinde), ama değişimin büyüklüğü içerik alanına değil kanıtsal statüye bağlı. Karşı-kanıta açık olan inançlarda – karşı-kanıt güçlü, zayıf ya da henüz araştırılmamış olsa bile – düşüş belirgin; yanlışlanamayan ve kanıtlarla desteklenen inançlarda ise küçük kalıyor. Kanıtsal statü ve alan birlikte modele girdiğinde alanın etkisi anlamsızlaşırken (p = .057) kanıtsal statü anlamlı kalıyor; yani bir inancın revize edilebilirliğini belirleyen, konusu değil, kanıtın onu çürütüp çürütemeyeceği. Model, daha çok karşı-kanıt bulunan inançlara karşı ilk yanıtında daha fazla çelişen kanıt üretiyor ve bu "kalibrasyon" gradyanın yaklaşık beşte birine aracılık ediyor (indirekt etki komplo koşulunda −0,44; epistemik inanç koşulunda −0,54). Uzunluk değil içerik belirleyici: yanıt uzunluğu inanç değişimini öngörmüyor.

Yazarlar sonucu kanıta dayalı ikna hesabının kanıtı olarak okuyor: Diyalogdan "kanıtı" çıkarmak etkiyi büyük ölçüde siliyor (Costello, Pennycook & Rand 2026),"ne söylendiği" kaynağın insan ya da AI olmasından bağımsız işliyor (Boissin vd. 2025). Sınırlılık olarak tasarımın korelasyonel olduğunu (katılımcılar inancı kendi seçiyor) ve sınıflandırmanın LLM'lerle yapıldığını açıkça belirtiyorlar. Ayrıca uzman uzlaşmasınca doğru kabul edilen inançlarda da küçük bir düşüş (2,35–7,63 puan) gözleniyor.

## Key Points

- Tasarım: Üç çalışmanın havuzlanması, N = 3.341 ABD'li yetişkin; katılımcı kendi inancını bildiriyor, GPT-4 (gpt-4-0125-preview) kanıtla çürütmeye çalışan üç turluk diyalog yürütüyor; inanç güveni 0–100 ölçeğinde diyalog öncesi/sonrası ölçülüyor.
- Ana bulgu: Değişim içerik alanına değil kanıtsal statüye göre işliyor — çürütülebilir inançlarda büyük, yanlışlanamayan ya da kanıtla desteklenen inançlarda küçük; alanın etkisi kanıtsal statü hesaba katıldığında kayboluyor (p = .057).
- Alan düzeyinde düşüşler: komplo −12,15, paranormal/dogaüstü −9,43, sözde-bilimsel −7,86 puan; siyaset −6,07, diğer −4,61, din −3,39 — en çok ve en az yanıt veren alan arasında üç kattan fazla fark.
- Mekanizma: Model ilk yanıtında karşı-kanıtın var olduğu inançlara daha fazla çelişen kanıt yerleştiriyor; bu kalibrasyon kanıtsal statü → inanç değişimi ilişkisinin yaklaşık %18–21'ine aracılık ediyor (mediasyon).
- Doğruluk kontrolü: 10.020 model mesajının %97,7'si tam doğru bulunuyor (doğrulanabilir olgusal iddia içerenlerin %85'i); yine de model ikna ediciliği doğrulukla sınırlı değil — uzman uzlaşmasınca doğru olan inançlarda da küçük düşüş var.
- Yöntem doğrulaması: GPT-5.2 birincil kodlayıcı, Claude Sonnet 4.6 ve Gemini 3.1 Pro çapraz doğrulayıcı (evidential status ordinal α = .71, alan nominal α = .87); kodlama diyalogdan ve sonuçtan bağımsız, katılımcının kendi ifadesinden yapılıyor.
- Sınırlılıklar: Korelasyonel tasarım (inanç seçimi katılımcıya ait; etki inancın yapısından mı, inanç sahibinin özelliklerinden mi ayırt edilemiyor) ve sınıflandırmanın tamamen LLM'lere dayanması.

## Turkey Context

Türkiye açısından bu çalışma, dezenformasyonla mücadelede yaygın bir varsayımı tersine çeviriyor: Doğrulanmış bilgiyle çürütmenin etkisini belirleyen şey "hangi konu" (örneğin siyaset mi, sağlık mı) değil, inancın kanıt karşısındaki yapısı. Bu, Türkiye'de teyit platformlarının ve kamu kurumlarının önceliklendirme mantığı için doğrudan bir öneridir: sınırlı iletişim kaynağı, kanıtla çürütülebilir (yanlışlanabilir) ve zayıf dayanaklı iddialara ayrılmalı; siyaset alanında düşüşlerin görece küçük kalması, siyasi kimlikle örülü inançlarda kanıt temelli diyalogun sınırını gösteriyor.

İkincisi, yöntem Türkiye için taşınabilir bir altyapı sunuyor: Türkçe diyalog yürüten bir LLM ile 0–100 güven ölçeğinde ön/son ölçüm, ucuz ve ölçeklenebilir bir müdahale biçimi. Ancak üç uyarı var. (a) Çalışmanın tüm diyalogları İngilizce ve ABD örneklemiyle; Türkçe'de modelin kanıt kalibrasyonu (özellikle yerel olaylara ilişkin karşı-kanıt üretimi) ayrıca test edilmelidir. (b) Etki doğrulukla sınırlı değil — model "kanıt gibi görünen" içerikle de ikna ediyor ve yanlış yönde kullanıldığında aynı mekanizma yanlış inanç üretmek için de çalışıyor (yazarların kendi atıfları: Costello, Pelrine vd. 2026; Hackenburg vd. 2025). Türkiye'de seçim dönemlerinde bu, "AI ile ikna" tartışmasının düzenleme tarafını (BTK/RTÜK gündemi, platform şeffaflığı) güçlendiriyor. (c) Araştırma etiği ve veri koruma açısından kişisel inançlarla diyalog verisi toplamak, KVKK kapsamında özel nitelikli veri tartışması doğurur.

Akademik hat açısından not: Pennycook–Rand–Costello hattı (Science 2024 diyalog çalışması, PNAS Nexus 2025 insan/AI kaynak manipülasyonu) Türkiye'deki kutuplaşma ve komplo inançları literatürüyle köprü kurulabilecek en güçlü deneysel çerçeve; bu ön baskı, "neyin çürütülebilir olduğu" sorusunu ölçülebilir hale getirdiği için yerel replikasyonlar için hazır bir kodlama şeması (13 ince + 6 kaba alan, 5 kanıtsal statü) ve ölçüm protokolü sağlıyor.

## 🏷 Retorik Roller

- 🔍 **Araştırma Boşluğu**
- 🧩 **Yöntem**
- 📊 **Bulgular**

---

## 🔗 İlgili Bağlantılar
### 🧠 İlgili Kavramlar
- [[concepts/komplo-inanclari.md|Komplo İnançları]]
### 🏛 İlgili Kurum/Kişiler
- [[entities/osf-io.md|Osf Io]]
