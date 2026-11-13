---
type: raw_article
title: Political Ingroup and Outgroup Cues Condition How Large Language Models Refute
  Conspiracy Theories
description: '**Tam metin okundu (28 sayfalık PsyArXiv ön baskısı, PDF 2.96 MB; ön
  kayıtlı/pre-registered).** Fitz ve Saunders (Colorado State University, Siyaset
  Bilimi), **yedi OpenAI modeliyle 135.845 konuşmalık...'
resource: https://osf.io/preprints/psyarxiv/4yexj_v1
tags:
- kurator
- high
timestamp: '2026-11-13T18:50:58Z'
source_file: 2026-11-13_llm-ingroup-outgroup-cues-conspiracy-refutation.json
category: KURATOR
priority: high
roles:
- result
- method
- limitation
- policy
published: '2026-11-08'
---

# Political Ingroup and Outgroup Cues Condition How Large Language Models Refute Conspiracy Theories

**Author(s):** Erin B. Fitz (corresponding) & Kyle L. Saunders — Department of Political Science, Colorado State University

**Published:** 2026-11-08

**Source:** [https://osf.io/preprints/psyarxiv/4yexj_v1](https://osf.io/preprints/psyarxiv/4yexj_v1)

## Summary

**Tam metin okundu (28 sayfalık PsyArXiv ön baskısı, PDF 2.96 MB; ön kayıtlı/pre-registered).** Fitz ve Saunders (Colorado State University, Siyaset Bilimi), **yedi OpenAI modeliyle 135.845 konuşmalık** tam faktöriyel bir deney yapıyor: LLM'ler komplo teorilerini (KT) kendiliğinden çürütüyor mu, ve **kullanıcının ve iddiada suçlanan aktörün siyasi kimliği** bu yanıtı değiştiriyor mu?

**Tasarım.** 2 sistem-promptu koşulu ("You are a helpful assistant." / + "The user is [kimlik]") × 6 kullanıcı kimliği (Demokrat, liberal, bağımsız, ılımlı, Cumhuriyetçi, muhafazakâr — hepsi eşit token uzunluğunda) × 3 KT aktörü (people / Democrats / Republicans) × **57 komplo teorisi** × 7 model × 10 tekrar = **143.640 deneme**, analiz edilen **n = 135.845** (~%5 başarısız; çoğu zarar içeren KT'lerde içerik filtresi). Modeller: GPT-4o, GPT-4.1, GPT-4.1 mini, GPT-5 mini, o4 mini, GPT-5.4 pro, GPT-5.5 (Mayıs 2024–Nisan 2026 sürümleri). Veri **Microsoft Azure üzerinden 3–28 Nisan 2026**'da toplandı; NAIRR Pilot (NAIRR240271) desteğiyle. KT seti: 9'u Demokrat/liberal (16%), 17'si Cumhuriyetçi/muhafazakâr (30%), 31'i partizansız/bilinmeyen (54%); ifadeler 10–12 token'a normalize edilmiş, "conspiracy" kelimesi çıkarılmış (priming önlemi).

**İki ölçü.** (1) **Refute (çürütme):** olumsuzlama + kanıt terimleri sözlüğü ("no credible evidence", "false claim" vb.). (2) **Motivated Responding (MR)** — makalenin kendi kavramı: kullanıcının bakış açısını **tanıyan ve kaygısını onaylayan** nezaket dili ("it's understandable to have concerns", "reasonable to wonder") — OpenAI Model Spec'in "samimiyetsizlikten kaçın ama nazikçe itiraz et" talimatının ölçülebilir karşılığı.

**Ana bulgular.** ① **Refute %82, MR %20.** Yanıt tipleri: yalnız Refute %66, Refute + MR %16, hiçbiri %14, yalnız MR %5. ② **Refute KT'ye göre çok değişiyor** (ICC = 0.58), MR daha az (ICC = 0.13). ③ **Kullanıcı kimliği refute olasılığını düşürüyor:** herhangi bir kimlik eklemek en az 2 puan düşürüyor, ama **Cumhuriyetçi (−0.06) ve muhafazakâr (−0.07)** kimlikleri anlamlı biçimde daha güçlü düşürüyor (p<.001). ④ **Aktör etkisi ters yönde ve daha büyük:** KT'yi "people" yerine bir partiye atfetmek refute olasılığını en az 7 puan **artırıyor**; **Demokratlar** aktörü daha güçlü (+0.13). ⑤ **MR, refute ile birlikte geliyor ve dış-grup iddialarında artıyor:** örneğin Cumhuriyetçi kullanıcı + Demokratları suçlayan KT → model hem çürütüyor hem kullanıcıyı onaylıyor. ⑥ **Asimetri:** Cumhuriyetçileri suçlayan KT'lere verilen yanıtlar kullanıcı kimliğine göre **daha çok** değişiyor; bu, iç/dış-grup farkını **yumuşatıyor**. Demokratları suçlayan KT'lerde ise Demokrat/liberal ile Cumhuriyetçi/muhafazakâr kullanıcılar arasındaki **fark büyüyor**. Somut: Cumhuriyetçi/muhafazakâr kullanıcı + "people" aktörü → en düşük yalnız-refute olasılığı (0.45), en yüksek "hiçbiri" (0.22), "yalnız MR" (0.10) ve "Refute + MR" (0.23).

**Yönetişim açısından en kritik bölüm.** Yazarlar OpenAI'ın **kendi yanlılık değerlendirmesini** eleştiriyor: OpenAI beş eksende ölçüm yapıyor ama **konuyu ve tonu aynı anda değiştirdiği** için hangi bileşenin varyansa yol açtığını **izole edemiyor**. Dahası OpenAI'ın "liberal charged" ve "conservative charged" örnek istemleri aynı anda konu, ton, hedef, çerçeveleme, token uzunluğu ve gereken düzeltme türü açısından farklılaşıyor. Dipnot 7: OpenAI, yanlılık analizinde **GPT-5 thinking modelini kendi yanıtlarının yargıcı** olarak kullanıyor (iyi uygulama ilkelerine aykırı). Sonuç cümlesi: "LLM'ler komplo teorilerini tutarlı biçimde çürütüyor ama bunu **siyasi olarak asimetrik** biçimde yapıyorsa, 'yetenekli ve güvenilir' olmak ne demek?"

**Sınırlılıklar (yazarların kendi beyanı):** yalnızca OpenAI modelleri (Anthropic/xAI yok); her gözlem **tek turlu** konuşma (ısrar/çok turlu baskı test edilmedi); ölçüler sözlük tabanlı ve ikili (nüans kaybı); 57 KT ağırlıklı ABD merkezli; insan katılımcı yok (kullanıcı simüle). Ön baskı, çalışma metni; ek materyal yazarlardan talep üzerine.

## Key Points

- Fitz & Saunders (Colorado State University), PsyArXiv ön baskısı, yayın 8.11.2026, DOI 10.31234/osf.io/4yexj_v1; ön kayıtlı (pre-registered), çalışma metni, 28 sayfa.
- Ölçek: 143.640 denenen API çağrısı, analiz edilen n = 135.845 konuşma; 57 komplo teorisi; 21 kullanıcı-aktör kimlik kombinasyonu; 7 OpenAI modeli; hücre başına 10 tekrar.
- Modeller: GPT-4o, GPT-4.1, GPT-4.1 mini, GPT-5 mini, o4 mini, GPT-5.4 pro, GPT-5.5 (Mayıs 2024–Nisan 2026). Veri toplama: Microsoft Azure, 3–28 Nisan 2026.
- İstem kurgusu: sistem promptu 'You are a helpful assistant.' (+ 'The user is [kimlik]'); kullanıcı promptu 'I saw that [aktör] [KT]. What do you think?' — model yanıtı yönlendirilmiyor.
- KT seti: 9 Demokrat/liberal eğilimli (%16), 17 Cumhuriyetçi/muhafazakâr (%30), 31 partizansız/bilinmeyen (%54); ifadeler 10–12 token'a çekilmiş, 'conspiracy' kelimesi çıkarılmış.
- Ölçüler: Refute (olumsuzlama + kanıt sözlüğü) ve MR = Motivated Responding (kullanıcıyı onaylayan nezaket dili: 'understandable', 'reasonable').
- Sonuç: Refute %82, MR %20. Yanıt tipleri: yalnız Refute %66, Refute+MR %16, hiçbiri %14, yalnız MR %5.
- Kullanıcı kimliği refute olasılığını düşürüyor (≥2 puan); Cumhuriyetçi (−0.06) ve muhafazakâr (−0.07) kimliklerde etki anlamlı biçimde daha büyük (p<.001).
- KT'yi partiye atfetmek refute olasılığını ≥7 puan artırıyor; Demokratlar aktörü daha güçlü etki (+0.13, p<.001).
- MR, refute ile birlikte görülüyor ve dış-grup iddialarında (ör. Cumhuriyetçi kullanıcı + Demokrat KT) artıyor; ikisi birlikte 'çürüt ama onayla' örüntüsü üretiyor.
- Asimetri: Cumhuriyetçileri suçlayan KT'lerde yanıtlar kullanıcı kimliğine göre daha çok değişiyor ve iç/dış-grup farkı yumuşuyor; Demokratları suçlayan KT'lerde Demokrat/liberal–Cumhuriyetçi/muhafazakâr farkı büyüyor.
- Varyans: KT düzeyi ICC Refute için 0.58 (KT'ye göre çok değişiyor), MR için 0.13.
- Yönetişim eleştirisi: OpenAI'ın yanlılık değerlendirmesi konu ve tonu aynı anda değiştirdiği için varyansın kaynağını izole edemiyor; OpenAI kendi yanlılık analizinde GPT-5 thinking'i yargıç olarak kullanıyor (dipnot 7).
- Sınırlılıklar: yalnız OpenAI modelleri; tek turlu konuşmalar; sözlük tabanlı ikili ölçüler; ABD merkezli KT seti; insan katılımcı yok (kullanıcı simülasyonu).
- Fon: NAIRR Pilot (NAIRR240271); NAIRR ortakları Azure ve OpenAI'nin çalışmayı gözden geçirmediği açıkça beyan edilmiş; çıkar çatışması yok.
- Kaynak künyesi doğrulandı: OSF API + PDF; X gönderisi (@pash22, 13.11.2026) makalenin 1. sayfasının görselini eklemiş (ek bilgi içermiyor).

## Turkey Context

Türkiye'ye aktarımı iki katmanda:

**1) Dezenformasyon ve siyasi kimlik.** Türkiye'de seçmenler giderek daha fazla bilgi için sohbet botlarına başvuruyor; makalenin gösterdiği örüntü — **kullanıcının kimliği çürütme olasılığını düşürüyor, iddianın kime atfedildiği ise yükseltiyor** — Türkiye bağlamında parti kimliği üzerinden test edilmedi. Kritik aktarım: modele "kullanıcı AKP'li/CHP'li" bilgisi verildiğinde komplo iddialarına verilen yanıt **ölçülebilir biçimde farklılaşıyor**; bu, Türkiye'de "bot tarafsız mı" tartışmasının ölçülebilir hale getirilebileceği anlamına gelir. Hipotez (doğrulanmamış): parti kimliğinin daha yüksek tuzlulukta olduğu Türkiye'de bu asimetri ABD'den **daha büyük** çıkar.

**2) Yapay zekâ yönetişimi.** Makalenin en taşınabilir kısmı yöntemsel eleştiri: bir modelin "tarafsızlığı", konu ve ton aynı anda değiştirilerek test edilemez; ayrıca modelin kendi çıktısını kendi yargıç modeliyle değerlendirmesi denetim açığı üretir. Bu, Türkiye'de yapay zekâ düzenlemesi tartışmasında henüz yer almayan bir ölçüt önerisi: **denetim tasarımının kendisi** (faktöriyel izolasyon + bağımsız yargıç) düzenleme metnine girmeli.

**Uyarı:** ön baskı, hakem değerlendirmesinden geçmemiş; bulgular tek turlu simüle konuşmalara dayanıyor. Türkiye analizinde "kanıt" olarak değil **mekanizma kanıtı / yöntem modeli** olarak kullanılmalı.

## 🏷 Retorik Roller

- 📊 **Bulgular**
- 🧩 **Yöntem**
- ⚠️ **Sınırlılıklar**
- 🏛 **Politika Önerisi**

---

## 🔗 İlgili Bağlantılar
### 🧠 İlgili Kavramlar
- [[concepts/dis-grup-dusmanligi.md|Dış-Grup Düşmanlığı]]
- [[concepts/komplo-inanclari.md|Komplo İnançları]]
- [[concepts/olcum-araclari.md|Ölçüm Araçları (Polarization Measurement)]]
### 🏛 İlgili Kurum/Kişiler
- [[entities/osf-io.md|Osf Io]]
