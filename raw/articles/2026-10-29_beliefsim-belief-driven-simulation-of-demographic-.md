---
type: raw_article
title: 'BeliefSim: belief-driven simulation of demographic misinformation susceptibility'
description: Angana Borah, Zohaib Khan, Rada Mihalcea (Michigan) ve Verónica Pérez-Rosas'ın
  (Texas State) PANDORA 2026 atölyesinde sunulan çalışması, **LLM'lerin demografik
  dezenformasyon duyarlılığını simüle edip...
resource: https://aclanthology.org/2026.pandora-1.20/
tags:
- kurator
- high
timestamp: '2026-11-06T14:36:50Z'
source_file: 2026-11-06_beliefsim-demographic-misinformation-susceptibility.json
category: KURATOR
priority: high
roles:
- result
- method
published: '2026-10-29'
---

# BeliefSim: belief-driven simulation of demographic misinformation susceptibility

**Author(s):** Angana Borah, Zohaib Khan, Rada Mihalcea (University of Michigan); Verónica Pérez-Rosas (Texas State University)

**Published:** 2026-10-29

**Source:** [https://aclanthology.org/2026.pandora-1.20/](https://aclanthology.org/2026.pandora-1.20/)

## Summary

Angana Borah, Zohaib Khan, Rada Mihalcea (Michigan) ve Verónica Pérez-Rosas'ın (Texas State) PANDORA 2026 atölyesinde sunulan çalışması, **LLM'lerin demografik dezenformasyon duyarlılığını simüle edip edemeyeceğini** test ediyor — ve demografik etiket yerine **inanç (belief) öncelini** modelin koşullamasına sokmayı öneriyor.

**Neden önemli:** Dezenformasyona duyarlılık gruplar arasında farklı; ama bu farkın kaynağı "kimlik etiketi" mi yoksa "mevcut inançlar" mı? Yazarlar ikincisini test ediyor. Model, demografik grubun **WVS (Dünya Değerler Araştırması) inanç dağılımlarından** türetilen bir önsel ile koşullanıyor.

**Veri ve tasarım:**

| Bileşen | Ayrıntı |
|---|---|
| Değerlendirme verisi | PANDORA (318 katılımcı × 3 iddia; RumourEval kaynaklı) + MIST-1 (409 katılımcı × 100 iddia) → **13,8 bin iddia-instance**, 27,6 bin gözlenen inanç yargısı |
| İnanç önseli | WVS Wave 7'den **126 inanç sorusu**, 7 boyutlu psikoloji temelli taksonomi (dünya görüşü/kimlik, epistemik güven, bilişsel stil, komplo zihniyeti, ahlak/değerler, duygu-temelli sezgiler, sezgisel kısayollar) |
| Demografik eksenler | Cinsiyet, yaş (≤35 / ≥60), yerleşim (kır/kent), eğitim — ikili gruplar, tek eksen |
| Modeller | 6 açık kaynak (Llama-3-8B/3.2-3B, Qwen2.5-14B, Mistral-7B, OLMo-2-7B, DeepSeek-7B) + 1 kapalı (Grok-4-Fast) |

**Ana bulgular (yüzde = duyarlılık hizalaması):**

| Koşul | PANDORA | MIST-1 |
|---|---|---|
| Zero-shot | 56,8 | 88,9 |
| Yalnız demografi | **düşürüyor** (56,2) | **düşürüyor** (87,3) |
| İnanç önseli (en iyi boyut) | **65,4** | **90,6** |
| İnanç + demografi | **65,6** | **90,9** |
| Yalnız gözlenen inançlar | 58,7 | 89,7 |

- **İnanç önseli kazanımın asıl kaynağı; demografi tek başına zararlı** (her iki veri setinde zero-shot'ın altına düşürüyor).
- **En güçlü inanç boyutları:** duygu-temelli ve ahlak/değerler; hangisinin işe yaradığı demografik eksene göre değişiyor.
- Model tablosu: Qwen 62,3 / 96,0 (en iyi) · Llama-3-8B 57,5 / 90,5 · Grok-4-Fast 57,1 / 87,2 · Mistral 56,0 / 70,1 · OLMo 50,6 / 77,0 · DeepSeek 52,4 / 59,0 (en kötü).
- **Karşı-olgusal test (flip-rate):** demografik etiketi değiştirince tahmin ne kadar dönüyor? Mistral en düşük (utility %0,3 / shortcut %1,6), Qwen düşük (%2,4 / %3,4); **Llama-3-8B (%14,1 / %11,2) ve DeepSeek (%12,6 / %11,2) belirgin biçimde kısayol-bağımlı**. Kır/kent ve eğitim eksenleri en kırılgan.
- **İki aşamalı ince ayar (BeliefSim-FT):** inanç adaptörü (WVS dağılımlarını KL ile öğrenir: Qwen 0,051 · Mistral 0,087 · Llama 0,287) + duyarlılık başlığı. MIST-2 çapraz katılımcı transferinde **%92,4 doğruluk / 0,906 F1** (Qwen); 2 aşamalı LoRA %89,3, tek aşamalı baseline %72,0. Flip-rate neredeyse sıfıra iniyor.

**Yazarların kendi uyarıları (kayda geçirilmeli):** flips ≠ stereotip kanıtı; düşük flip oranı adaleti garanti etmez; örneklem **yalnız ABD + İngilizce**, tek eksenli ikili demografi (8 grup), kesişimsellik yok; 6 açık + 1 kapalı model; çerçeve **birey tahmini veya hedefleme için değil**, yalnız araştırma/denetim için. Etik uyarı açık: demografik önsel = grup düzeyi prior, kişi hakkında hüküm değil.

## Key Points

- Soru: LLM'ler demografik dezenformasyon duyarlılığını simüle edebilir mi, ve bunu demografi mi yoksa inançlar mı açıklıyor?
- Veri: PANDORA (318 katılımcı × 3 iddia) + MIST-1 (409 × 100) = 13,8 bin değerlendirme instance'ı, 27,6 bin gözlenen inanç yargısı.
- İnanç önseli WVS Wave 7'den 126 soruyla kuruluyor; 7 boyutlu taksonomi (dünya görüşü, epistemik güven, bilişsel stil, komplo zihniyeti, ahlak, duygu sezgileri, kısayollar).
- Demografi tek başına zero-shot'ı DÜŞÜRÜYOR (PANDORA 56,8→56,2; MIST 88,9→87,3); inanç önseli yükseltiyor (65,4 / 90,6).
- İnanç + demografi en iyi: PANDORA 65,6 / MIST 90,9 — demografi ancak inanç önselinin üstüne küçük katkı (+0,2-1,2 puan) veriyor.
- En etkili inanç boyutları duygu-temelli ve ahlak/değerler; hangisinin işe yaradığı eksene göre değişiyor.
- Model farkı büyük: Qwen 62,3/96,0 en iyi; DeepSeek 52,4/59,0 en kötü.
- Karşı-olgusal flip-rate: Llama-3-8B (%14,1 utility) ve DeepSeek (%12,6) demografik kısayola bağımlı; Mistral (%0,3) ve Qwen (%2,4) değil — kayma en çok kır/kent ve eğitim ekseninde.
- BeliefSim-FT: iki aşamalı adaptasyon MIST-2'de %92,4 doğruluk, 0,906 F1 (Qwen); 2 aşamalı LoRA %89,3, tek aşamalı baseline %72,0.
- Sınırlılık: yalnız ABD + İngilizce, ikili tek eksenli demografi (8 grup), kesişimsellik yok, 6 açık + 1 kapalı model.
- Etik: çerçeve birey tahmini/hedefleme için değil; flip-rate stereotip kanıtı sayılmaz; düşük flip adaleti garanti etmez.
- LinkedIn özetiyle fark: '92,4% doğruluk' MIST-2/Qwen sonucu; PANDORA+MIST-1'de BeliefSim-FT (0,792) 2 aşamalı LoRA'nın (0,800) hafif altında — kazanç veri setine bağlı.

## Turkey Context

Türkiye için üç somut hat. (1) **Yöntem transferi mümkün, veri değil:** çerçeve WVS Wave 7'ye dayanıyor ve Türkiye WVS'de var — yani "Türkiye'de eğitim/kır-kent gruplarının inanç önseli" kurulabilir. Ama değerlendirme verisi (PANDORA/MIST) ABD + İngilizce; Türkçe iddia seti ve Türkiye'den insan yargısı olmadan simülasyon doğrulanamaz. Türkiye'de seçim dönemi dezenformasyonu (2023, 2024) için böyle bir Türkçe benchmark gerçek bir boşluk.

(2) **Siyasi açıdan kritik uyarı:** Türkiye gibi yüksek kutuplaşma ve düşük kurumsal güven ortamında "grup düzeyi inanç önseli" ile simülasyon yapmak, seküler/muhafazakâr, Kürt/Türk, kır/kent eksenlerinde **stereotip üretme riski** taşıyor. Yazarların kendi uyarısı burada daha da ağır: model "bu grubun inancı şudur" diye kurulduğunda, bu bir ölçüm değil, WVS dağılımının projeksiyonu.

(3) **Pratik kullanım:** Türkiye'de dezenformasyonla mücadele politikası (doğrulama platformları, medya okuryazarlığı) için bu çerçeve "hangi gruba hangi ön-yanlış inanç gidiyor" sorusunu **ucuz simülasyonla** ön-test etme imkânı verir — ama yalnız hipotez üretmek için; saha verisi yerine geçmez.

Ders: bu makale, "demografi = açıklama" varsayımını ampirik olarak çürütüyor (demografi tek başına performansı düşürüyor). Türkiye'de de "gençler/köylüler/muhafazakârlar şöyle düşünür" cümleleri, inanç ölçüsü olmadan aynı hatayı yapar.

## 🏷 Retorik Roller

- 📊 **Bulgular**
- 🧩 **Yöntem**

---

## 🔗 İlgili Bağlantılar
### 🧠 İlgili Kavramlar
- [[concepts/dezenformasyon.md|Dezenformasyon]]
- [[concepts/komplo-inanclari.md|Komplo İnançları]]
- [[concepts/onvargi-ve-stereotipler.md|Önyargı ve Stereotipler]]
