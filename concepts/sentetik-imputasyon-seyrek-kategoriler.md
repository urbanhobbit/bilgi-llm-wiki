---
type: concept
title: 'Sentetik İmputasyon: Seyrek Kategorilerde LLM ile Veri Artırımı'
description: 'İnsan-kodlu az sayıda örnekten üretken LLM ile sentetik metin üretip seyrek (low-N) kategorileri genişletme yöntemi; döner örnekleme, en yakın-komşu filtresi, öngörülebilir aşırı-uyum ve ölçüm hatası riskleri.'
tags:
- kavram
- metodoloji
- metin-madenciligi
- llm
- siniflandirma
- veri-artirimi
timestamp: '2026-11-26T16:50:00Z'
created: '2026-11-26'
updated: '2026-11-26'
sources:
- raw/articles/2026-10-14_timoneda-synthetic-imputation-sparse-categories.md
related:
- concepts/metin-madenciligi.md
- concepts/olcum-araclari.md
- concepts/kuram-operasyonellestirme-llm.md
confidence: medium
---

# Sentetik İmputasyon: Seyrek Kategorilerde LLM ile Veri Artırımı

## Tanım

**Sentetik imputasyon**, gözetimli metin sınıflandırmasında **seyrek (low-N) kategorileri** genişletmek için üretken bir LLM'i, insan-kodlu az sayıda örnekten yeni metinler üretmeye yönlendirme yöntemidir (Timoneda 2026, *Political Analysis*). Eksik değerleri doldurma mantığındaki çoklu imputasyondan aldığı sezgi şudur: yeterince bilgilendirici az sayıda gözlem varsa, bilinmeyen gözlemlerin dağılımına yaklaşan örnekler üretilebilir.

Klasik artırma yöntemlerinden ayrıldığı yer: **değiştirme (paraphrase) ya da yeniden kurma değil, yalnızca verinin ince olduğu yere bilgi ekleme**. Orijinal veri korunur; sentetikler yalnızca seyrek kategoriye eklenir.

## Neden gerekli: iki mimari, iki farklı arıza

- **Encoder-only (BERT, RoBERTa):** Kategori, ince ayar sırasında yeterince sık geçmediği için **gradyan güncellemelerinde kaybolur**. 16–32'lik batch'lerde 40 örneklik bir kategori bazı batch'lerde hiç görünmez.
- **Decoder-only (GPT ailesi):** Etiketleme görevinde nadir kategori test setinde neredeyse hiç bulunmadığı için **değerlendirme kararsızlaşır** ve model çoğunluk sınıfına kayar.
- Pratik eşik: kategori başına **~50 insan-kodlu gözlem**; hedef genişletme **150–200 metin**.

## Yöntemin dört adımı

1. **Eşik kontrolü** — her seyrek kategoride ≥50 gerçek örnek.
2. **Döner örneklemeli üretim** — her yeni metin için havuzdan **rastgele 5 insan-kodlu örnek** taze çekilir; modelden içerik dışında (üslup, yapı, aktör, ülke) farklılaşması istenir. Tek örneğe bağlanma ve kopya üretme bu şekilde engellenir.
3. **En yakın-komşu filtresi** — kosinüs benzerliği önceden sabitlenmiş eşiği aşan sentetik metin atılır ve yeniden üretilir; ardından elle denetim (örnekleme).
4. **Kullanım** — encoder için genişletilmiş eğitim seti, decoder için genişletilmiş değerlendirme seti.

**Kaçak önleme (leakage control):** sentetikler yalnızca eğitim katmanındaki insan-kodlu metinlerden üretilir; test/doğrulama gözlemleri üretime sokulmaz; encoder uygulamalarında üretim **fold içinde** yapılır ve yalnızca o fold'a eklenir.

## Kanıt (Timoneda 2026)

Politik nostalji (1.200 cümle; 151 pozitif; ton-tanımlı, dağınık sınır) ve uluslararası konuşmalar (843 konuşma; 218 "international"; bağlam-tanımlı, sıkı ipuçlu) veri setleri, RoBERTa-large (10×10 CV) ve GPT-4o few-shot ile test edildi:

- **75 gerçek gözlem** ile her iki mimaride de tam-veri benchmark'ına eşdeğer performans (nostalji 0,840 ≈ 0,822; konuşmalar 0,893 = 0,895).
- Sentetik **yokken** 50 gözlemde çöküş: 0,471 (nostalji) ve 0,561 (konuşmalar).
- 50'nin altında **aşırı-uyum** başlıyor ama öngörülebilir: n=25'te 0,903, n=10'da 0,944 (benchmark 0,822). Bu, "cezalı skor raporlama" ile yönetilebilir.

## Karşı-örnek: neden SSMBA tehlikeli

Maskeleme + yeniden kurma (SSMBA) cümle yapısını korur → sentetik metin orijinaline fazla benzer → model tekrar eden örüntüyü öğrenir → 50 gerçek metinle **0,982 F1** (benchmark 0,822). Bu bir başarı değil, **ölçüm hatasının maskelenmesi**. Genel kural: benchmark'ı belirgin biçimde aşan artırma yöntemi, gerçek performans değil sızıntı/benzerlik üretiyor demektir.

## Sınırlılıklar

1. **Belirsizlik aktarımı yok:** çoklu imputasyon benzetmesi sezgisel; Rubin kuralları uygulanmamış. Öneri: çoklu sentetik set + açık ağırlıklı modellerle duyarlılık analizi.
2. **Kapalı model bağımlılığı:** GPT-5 ile üretim yeniden üretilebilirliği sınırlar; LLM çıktıları aşağı-akış katsayılarını istikrarsızlaştırabilir (Barrie vd. 2024).
3. **Kategori kayması:** model üslup kayabilir ya da kategori sınırını genişletebilir; elle denetim zorunlu.
4. **Kavramsal doğruluk ölçülmüyor:** metrik sınıflandırıcı F1'i; kodlayıcılar arası uyumla kavramsal sadakat testi yok.
5. **Yerine değil önkoşulu:** Egami vd. (2023) design-based supervised learning ölçüm hatasını *sonradan* düzeltir; sentetik imputasyon sınıflandırıcıyı *önce* eğitilebilir kılar. İkisi tamamlayıcı.

## KURATOR bağlamında kullanım notları

- Dezenformasyon, nefret söylemi, siyasal şiddet gibi **doğal olarak seyrek** kategorilerde örnek azlığı gerekçesiyle iptal edilen kodlama projelerini mümkün kılar.
- Ancak nadir kategoriyi "daha kolay yakalanır" hâle getirdiği için **yanlış-pozitif enflasyonu** riski taşır; aşağı-akış çıkarımda ölçüm hatası düzeltmesi yapılmazsa bulgular şişer.
- **Türkçe** kod kitabıyla uygulamada deyim, ironi, imla varyasyonu ve dolaylı/resmi ifade kalıpları kategori kaymasını artırır; en yakın-komşu filtresi ve elle denetim daha da kritik.

## İlgili

- Ham kayıt: [[raw/articles/2026-10-14_timoneda-synthetic-imputation-sparse-categories.md]]
- [[concepts/metin-madenciligi.md]] — gözetimli/gözetimsiz ayrımı ve sınıflandırma hattı
- [[concepts/olcum-araclari.md]] — ölçüm hatası ve araca bağımlılık
- [[concepts/kuram-operasyonellestirme-llm.md]] — kod kitabının LLM'e devredilmesi ve kuramsal kayma riski
