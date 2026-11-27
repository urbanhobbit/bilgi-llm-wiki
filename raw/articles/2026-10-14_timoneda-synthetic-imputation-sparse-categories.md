---
type: raw_article
title: 'The Synthetic Imputation Approach: Using LLMs to Generate Synthetic Texts for Underrepresented Categories in Supervised Classification Tasks'
description: 'Joan C. Timoneda (Purdue), Political Analysis FirstView. Seyrek (low-N) kategoriler için üretken LLM ile döner örneklemeli sentetik metin üretimi; 75 gerçek gözlemle tam-veri benchmark'ına yaklaşan sınıflandırıcı performansı, en yakın komşu filtresi ve öngörülebilir aşırı-uyum.'
resource: 'https://doi.org/10.1017/pan.2026.10057'
tags:
- kurator
- yontem
- metin-madenciligi
- llm
- siniflandirma
- veri-artirimi
timestamp: '2026-11-26T16:45:00Z'
source_file: telegram_ad_hoc
category: AKADEMIK OZEL
priority: high
published: '2026-10-14'
---

# The Synthetic Imputation Approach (Timoneda 2026)

**Künye:** Joan C. Timoneda (Purdue University, Political Science). *Political Analysis* (2026), FirstView, ss. 1–15. DOI: 10.1017/pan.2026.10057. Açık erişim (CC BY 4.0). Gönderim 26 Ocak 2026, kabul 7 Temmuz 2026. Editör: Margaret E. Roberts. Replikasyon: doi.org/10.7910/DVN/XK6QHU.

## Problem: seyrek kategoriler (low-N)
Metin-kodlama görevlerinde bazı kategoriler bol, bazıları çok seyrek. Seyrek kategori iki mimari aileyi de farklı biçimde vuruyor:
- **Encoder-only (BERT, RoBERTa):** Kategori eğitim yığınlarında (batch) yeterince görünmüyor; gradyan güncellemelerinde etkisi kayboluyor. Tipik batch boyu 16–32 olduğu için 40 örneklik bir kategori bazı batch'lerde hiç görünmüyor.
- **Decoder-only (GPT ailesi):** Etiketlemede nadir kategoriye neredeyse hiç rastlanmadığı için **değerlendirme kararsızlaşıyor** ve model çoğunluk sınıfına kayıyor (measurement error).
- Ampirik eşik: kategori başına **~50 gözlem** pratik bir alt sınır (kesin sınır değil). Egami vd. (2023) DSL düzeltmesi devreye girmeden önce bu darboğazın aşılması gerekiyor.

## Yöntem: sentetik imputasyon (4 adım)
1. **Eşik kontrolü:** Her seyrek kategoride en az ~50 gerçek, insan-kodlu örnek.
2. **Üretim:** Üretken LLM (burada GPT-5), kategori tanımını taşıyan ama **üslup/yapı/aktör/ülke düzeyinde farklılaşan** yeni metinler üretiyor. Her yeni metin için insan-kodlu havuzdan **rastgele 5 örnek** taze olarak çekiliyor (rotating examples) — tek bir metne aşırı bağlanmayı ve kopya cümleleri engelliyor.
3. **En yakın-komşu filtresi:** Her sentetik metnin cümle gömme (sentence embedding) düzeyinde kosinüs benzerliği, örnek olarak kullanılan 5 metne karşı hesaplanıyor; önceden sabitlenmiş eşiği aşanlar atılıp yeniden üretiliyor. Ardından üretim sürecinin **elle denetimi** (örnekleme yoluyla).
4. **Kullanım:** Ya encoder sınıflandırıcı genişletilmiş veriyle ince ayarlanıyor ya da üretken LLM sınıflandırıcı tam veri üzerinde değerlendiriliyor.

Kritik tasarım disiplini: sentetik metinler **yalnızca eğitim katmanındaki insan-kodlu metinlerden** üretiliyor; doğrulama/test gözlemleri üretime sokulmuyor; RoBERTa uygulamalarında sentetikler **katlama (fold) içinde** üretilip yalnızca o katlamaya ekleniyor. Yani bilgi sızıntısı (leakage) kapatılmış.

**Önerilen hedef boyut:** Seyrek kategoriyi yaklaşık **150–200 metne** çıkarmak. Gerekçe encoder tarafında batch kompozisyonu (16'lık batch'te ortalama 2–3 örnek), decoder tarafında ise değerlendirme kararlılığı — iki farklı mekanizma aynı aralıkta buluşuyor.

## Bulgular
**Uygulama 1 — Politik nostalji** (Müller & Proksch 2024; 24 Avrupa ülkesi parti manifestolarından 1.200 cümle, 151 nostaljik / 1.049 değil, cümle ortalaması 20,8 kelime; *ton-tanımlı, dağınık sınırlı* kategori).

| Gerçek N | Sentetik eklenmiş RoBERTa F1 | Sentetik yok (baz) |
|---|---|---|
| 50 | 0,851 | 0,471 |
| 75 | 0,840 | — |
| 100 | ~0,822 (fark yok) | — |
| tam veri (151) | **0,822 (benchmark)** | 0,822 |

**Uygulama 2 — Uluslararası konuşmalar** (Global Populism Database, Hawkins vd. 2019; 843 konuşma / 190 lider / 58 ülke / 35 dilden çeviri; 218 "international" kategorisi; ortalama 414,7 kelime; *bağlam-tanımlı, sıkı ipuçlu* kategori).

| Gerçek N | Sentetik eklenmiş RoBERTa F1 | Sentetik yok (baz) |
|---|---|---|
| 50 | 0,923 | 0,561 |
| 75 | 0,903 | — |
| 100 | ~0,895 (fark yok) | — |
| 150 | 0,893 | — |
| tam veri (218) | **0,895 (benchmark)** | 0,895 |

- **SSMBA karşılaştırması:** 50 gerçek metinle 0,982 F1 — benchmark'ın çok üzerinde. Bu "iyi haber" değil: maskeleme+yeniden kurma cümle yapısını koruduğu için metinler orijinaline fazla yakın, model tekrar eden örüntüyü öğreniyor ve **yapay olarak yüksek** puan alıyor. Timoneda'nın yöntemi bu tuzağı özellikle hedefliyor.
- **Aşırı-uyum örüntüsü öngörülebilir:** n=25'te F1 0,903, n=10'da 0,944 (benchmark 0,822). Yani 50'nin altında performans **şişer** — ama şişmenin yönü ve büyüklüğü tahmin edilebilir olduğu için araştırmacı "cezalı skor" raporlayabilir; projeyi bırakmak ya da nadir kategoriyi daha geniş bir kategoriye katlamak zorunda kalmaz.
- **Decoder tarafı (GPT-4o few-shot):** Nostaljide 50 gerçek + 101 sentetik ile benchmark'a yakın, güven aralıkları aşırı-uyum işareti vermiyor. Konuşmalarda 50 gerçek metinle F1 0,861 ≈ tam-veri 0,859 — yani neredeyse hiç gerçek veri olmadan benchmark'a ulaşılıyor.

## Sınırlılıklar (yazarın kendi notları)
1. **Belirsizlik yayılımı yok.** "Çoklu imputasyon" benzetmesi *sezgi* düzeyinde; Rubin kuralları gibi biçimsel bir belirsizlik aktarımı uygulanmamış. Öneri: farklı tohum/örnek setleriyle birden çok sentetik set üretip aşağı-akış tahminlerini ortalama almak; açık ağırlıklı (open-weight) modellerle modelin gizli durumunu da hesaba katmak.
2. **Kapalı model bağımlılığı.** Üretim GPT-5 (kapalı API) ile yapıldı; yeniden üretilebilirlik ve duyarlılık analizi kısıtlı. Barrie vd. (2024) LLM çıktılarının aşağı-akış katsayıları istikrarsızlaştırabildiğini gösteriyor.
3. **Kategori kayması (concept drift) riski.** Üretken model üslup kayabilir ya da kategori sınırını insan-kodlu verinin desteklediğinden fazla genişletebilir; elle denetim bu yüzden zorunlu tutuluyor.
4. **Kavramsal doğruluk ölçülmüyor.** Metrikler sınıflandırıcı F1'i. Sentetik metinlerin kategori tanımına *kavramsal* sadakati, kodlayıcılar arası uyum (inter-coder reliability) ile sistematik olarak test edilmiştir değil.
5. **DSL ile ilişki:** Yöntem Egami vd. (2023) design-based supervised learning'in *yerine* değil, *önkoşulu* olarak konumlanıyor — önce sınıflandırıcıyı eğitilebilir kılmak, sonra ölçüm hatasını düzeltmek.

## KURATOR açısından neden önemli
- **Seyrek olgu problemi:** Dezenformasyon, nefret söylemi, siyasal şiddet, darbe çağrısı gibi kategoriler doğal olarak nadir. Bu yöntem, "örnek az, kategori genişletilemez" gerekçesiyle iptal edilen kodlama projelerini yeniden mümkün kılıyor — ama **şişirilmiş F1** riskini de beraberinde getiriyor.
- **Yanlış-pozitif enflasyonu:** Sentetik eğitim verisi, sınıflandırıcının nadir kategoriyi "daha kolay" yakalamasını sağlıyor. Dezenformasyon tespiti gibi alanlarda bu, gerçek dünyada olmayan bir kesinlik algısı üretebilir; ölçüm hatası düzeltmesi olmadan aşağı-akış çıkarım bozulur (bkz. [[concepts/kuram-operasyonellestirme-llm.md]]).
- **Türkiye uygulamaları:** Türkçe kod kitabı ile üretilen sentetik metinlerde deyim, ironi, imla varyasyonu ve resmi/dolaylı ifade kalıpları nedeniyle kategori kayması riski İngilizceye göre daha yüksek. Elle denetim ve en yakın-komşu filtresi burada kritik.
- Wiki bağlantıları: [[concepts/metin-madenciligi.md]], [[concepts/olcum-araclari.md]]

---

## 🔗 İlgili Bağlantılar
### 🧠 İlgili Kavramlar
- [[concepts/dezenformasyon.md|Dezenformasyon]]
- [[concepts/olcum-araclari.md|Ölçüm Araçları (Polarization Measurement)]]
- [[concepts/platform-economy-misinformation.md|Platform Economy and Misinformation (Platform Ekonomisi ve Dezenformasyon)]]
- [[concepts/populizm.md|Popülizm]]
- [[concepts/siyasal-siddet.md|Siyasal Şiddet]]
### 🏛 İlgili Kurum/Kişiler
- [[entities/joan-c-timoneda.md|Joan C. Timoneda]]
