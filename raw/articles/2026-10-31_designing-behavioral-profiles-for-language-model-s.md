---
type: raw_article
title: Designing Behavioral Profiles for Language Model Simulation of Out-of-Distribution
  Human Behavior (Na, Zhu, Cross & Bakker, arXiv 2611.00661)
description: '**Soru:** LLM''lere "insan gibi davran" demek simülasyonları iyileştiriyor,
  ama profile **hangi bilgiyi, ne kadar** koymak gerekir? Her insan sayısız özellikle
  tanımlanabilir; hepsini prompt''a sığdırma...'
resource: https://arxiv.org/abs/2611.00661
tags:
- kurator
- high
timestamp: '2026-11-05T00:24:27Z'
source_file: 2026-11-04_na-behavioral-profiles-llm-simulation.json
category: KURATOR
priority: high
roles:
- method
- result
published: '2026-10-31'
---

# Designing Behavioral Profiles for Language Model Simulation of Out-of-Distribution Human Behavior (Na, Zhu, Cross & Bakker, arXiv 2611.00661)

**Author(s):** Robin Na (MIT), Kehang Zhu (Stanford Digital Economy Lab), Logan Cross (Google DeepMind), Michiel A. Bakker (MIT)

**Published:** 2026-10-31

**Source:** [https://arxiv.org/abs/2611.00661](https://arxiv.org/abs/2611.00661)

## Summary

**Soru:** LLM'lere "insan gibi davran" demek simülasyonları iyileştiriyor, ama profile **hangi bilgiyi, ne kadar** koymak gerekir? Her insan sayısız özellikle tanımlanabilir; hepsini prompt'a sığdırmak ne mümkün ne de faydalı — ve hangi özelliklerin önemli olduğunu önceden bilmek zor.

**Yöntem (üç adım):**
1. **Aday özellikler:** her oyun ailesi için davranış literatürü taranarak özellik seti tanımlandı — public-goods **30**, çok taraflı pazarlık **20**, genelleştirilmiş 11-20 para-talep oyunları **7** aday özellik. Özellik kod kitabı 0/5/10 çapalarını, hangi durumda davranışın gözlenebilir olduğunu ve kanıt kurallarını tanımlıyor.
2. **Profil üretimi:** bir LLM, eski katılımcı kayıtlarını (eylemler, mesajlar, anketler) okuyup her özellik için **değer + güven + doğrudan kanıt** çıkarıyor.
3. **Simülasyon ve seçim:** ayrı bir LLM simülatörü bu profillerle oynuyor; eğitim verisinde **ileri özellik seçimi** (forward feature selection) ile hangi özelliklerin tahmini iyileştirdiği belirleniyor, sonra seçilen profiller **hiç değiştirilmeden** yeni katılımcı ve yeni deney tasarımlarında test ediliyor.

**Veri:** öğrenme aşamasında 3.691 public-goods katılımcı kaydı, 144 pazarlık katılımcısı, 1.670 para-talep seçimi; doğrulamada 250 public-goods oyunu, 48 pazarlık oyunu, 2.502 para-talep seçimi. Üç ailede de öğrenme ve doğrulama verisi **farklı katılımcılar ve çakışmayan tasarımlar** içeriyor.

**Ölçüm:** 1 boyutlu Wasserstein mesafesi; normalize edilmiş dağılımsal uyum skoru (0 = bilgisiz referans, 100 = iki insan veri seti arasındaki beklenen uyum).

**Bulgular:**
- **Tek özellikli profil, profilsiz simülasyondan ve genel amaçlı persona kütüphanelerinden daha iyi.** Public-goods'ta lider özellik *"withdrawal after adverse peer behavior"* (akran bedavacılığına katkıyı düşürme) → uyum skoru **65,5** [37,6-68,1]; profilsiz **−1,0**; Twin-2K-500 **18,6**, Nemotron **−1,5**, ANES **−8,7**. İyileşme **+66,5 puan** [42,3-79,5].
- **Daha fazla özellik yardımcı olmuyor.** Seçim ikinci özellikte duruyor (public-goods'ta *rule comprehension*; pazarlıkta *package breadth* + *integrative trade search*); üçüncü özellik her karşılaştırmada iyileşme sağlamadı, tüm adayları içeren "tam profil" belirgin avantaj vermedi.
- **Bazı özellikler zarar veriyor:** public-goods'ta *commitment making*, *reward propensity* ve *responsive/affiliative communication*; pazarlıkta *profitable-offer uptake* → profilsizden **daha kötü** simülasyon.
- **Özelliklerin göreli değeri öğrenme ve doğrulama arasında tutarlı** — yani faydalı özellik, yeni ortamda da faydalı kalıyor; bu, simülasyon tasarımını test edilebilir bir karar haline getiriyor.
- **Aileler arası transfer düzensiz:** bir oyun ailesinden öğrenilen profil başka aileye aktarıldığında kazanç tutarsız, hatta bazı yönlerde profilsizden **daha kötü**. Transfer yönü asimetrik.

**Sınır:** değerlendirme popülasyon ve tasarım düzeyinde; aynı kişinin oyunlar arası davranışını tahmin etme iddiası yok. Simülatör modelleri GPT-5 mini / GPT-5.1.

## Key Points

- Soru: LLM insan simülasyonunda profile hangi bilgi, ne kadar konmalı — cevap ampirik olarak test ediliyor, sezgiyle değil.
- Üç oyun ailesi için literatürden aday özellik seti: public-goods 30, pazarlık 20, genelleştirilmiş 11-20 para-talep 7 özellik.
- Profil üretimi: bir LLM eski katılımcı kayıtlarından özellik değeri + güven + doğrudan kanıt çıkarıyor; ayrı LLM simülatörü oynuyor.
- Seçim yöntemi: eğitim verisinde ileri özellik seçimi, ardından seçilen profil değiştirilmeden yeni katılımcı/yeni tasarımda doğrulama.
- Public-goods'ta lider özellik 'withdrawal after adverse peer behavior': uyum skoru 65,5 vs profilsiz −1,0; persona kütüphaneleri 18,6 / −1,5 / −8,7.
- Daha fazla özellik yardımcı olmuyor: seçim 2 özellikte duruyor, tam profil belirgin avantaj sağlamıyor.
- Bazı özellikler zararlı: commitment making, reward propensity, profitable-offer uptake → profilsizden kötü simülasyon.
- Özelliklerin göreli değeri öğrenme-doğrulama arasında tutarlı → faydalı bilgi yeni tasarımlarda da faydalı.
- Aileler arası transfer düzensiz ve yön asimetrik; yanlış profille simülasyon profilsizden kötü olabiliyor.
- Sınır: popülasyon/tasarım düzeyi transfer; aynı kişiyi oyunlar arası tahmin iddiası yok.

## Turkey Context

Türkiye'deki araştırma pratiği açısından iki doğrudan sonuç var.

**Birincisi, sentetik katılımcı üretimi ucuz ama bedava değil.** Türkiye'de anket maliyetleri ve saha kısıtları nedeniyle "LLM'e Türk seçmen profili verip anket simüle etme" cazip görünüyor. Bu makale, o işin en kritik adımının **hangi özelliklerin profile konacağı** olduğunu ve bunun test edilebilir bir karar olduğunu gösteriyor. Ama aktarım bedava değil: aday özellikler Batılı laboratuvar oyunlarından türetilmiş; Türkiye'de "akran bedavacılığına tepki" ya da "pazarlıkta paket genişliği" gibi özelliklerin aynı davranışsal ağırlıkta olduğu varsayılamaz. Kural: **kendi kayıtlarınızdan özellik seti kurun, hazır persona kütüphanesi kullanmayın** — makalenin bulgusu tam olarak bunu söylüyor.

**İkincisi, yöntem ihracı.** "İleri özellik seçimi + dağılımsal uyum skoru (Wasserstein)" ikilisi, Türkiye'de yapılan anket/saha deneylerinin simülasyonla karşılaştırılmasında da kullanılabilir: hangi demografik değişken seti seçmen davranışını gerçekten taşıyor? Türkiye'de bu soru genellikle sezgiyle yanıtlanıyor (eğitim + dindarlık + gelir), oysa aynı seçim verisiyle test edilebilir.

**Uyarı:** makalenin kendi sınırı Türkiye için daha sert geçerli — değerlendirme popülasyon düzeyinde; "şu seçmen şöyle oy verir" türü bireysel tahminler bu yöntemle üretilmiyor. Türkiye'de bu tür iddialar sık yapılıyor ve yöntem bunu desteklemiyor.

## 🏷 Retorik Roller

- 🧩 **Yöntem**
- 📊 **Bulgular**

---

## 🔗 İlgili Bağlantılar
### 🧠 İlgili Kavramlar
- [[concepts/olcum-araclari.md|Ölçüm Araçları (Polarization Measurement)]]
### 🏛 İlgili Kurum/Kişiler
- [[entities/arxiv-org.md|Arxiv Org]]
