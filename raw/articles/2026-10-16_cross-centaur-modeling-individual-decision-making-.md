---
type: raw_article
title: 'Cross-Centaur: Modeling Individual Decision-Making Across Psychological Tasks
  with Language Models'
description: Asano, Suganuma, Mori ve Baba'nın (Tokyo Üniversitesi; Sakana AI Labs)
  EMNLP 2026 Main (Oral) kabul edilen çalışması, dil modellerinin 'insan davranışının
  hesaplamalı modeli' olarak kullanılması hattı...
resource: https://arxiv.org/abs/2610.23157
tags:
- kurator
- medium
timestamp: '2026-10-19T13:27:39Z'
source_file: 2026-10-19_cross-centaur-individual-decision-making-llm.json
category: KURATOR
priority: medium
roles:
- gap
- method
- result
- limitation
published: '2026-10-16'
---

# Cross-Centaur: Modeling Individual Decision-Making Across Psychological Tasks with Language Models

**Author(s):** Hikaru Asano; Hidezo Suganuma; Ryutaro Mori; Yukino Baba (University of Tokyo; Sakana AI Labs)

**Published:** 2026-10-16

**Source:** [https://arxiv.org/abs/2610.23157](https://arxiv.org/abs/2610.23157)

## Summary

Asano, Suganuma, Mori ve Baba'nın (Tokyo Üniversitesi; Sakana AI Labs) EMNLP 2026 Main (Oral) kabul edilen çalışması, dil modellerinin 'insan davranışının hesaplamalı modeli' olarak kullanılması hattında bir sonraki adımı atıyor. Mevcut durum: Centaur (Binz ve ark. 2025), Psych-101 veri setiyle deney-deney karar dizileri üzerinde ince ayar yapılmış ve birçok görevde göreve özgü bilişsel modellerden daha iyi tahmin üretiyor; ancak Psych-101 aynı katılımcıları farklı görevlerde birbirine BAĞLAMIYOR. Dolayısıyla bu modeller popülasyon düzeyi düzenlilikleri öğreniyor, birey düzeyi düzenlilikleri (bir kişinin bir görevdeki davranışından başka bir görevdeki davranışını kestirme) öğrenemiyor. Yazarlar bunun için Cross-Psych-101 veri setini topluyor: Prolific üzerinden 601 katılımcı (yayımlanan sürüm 591; 10 kişi verisinin kamuya açılmasından çekilmiş), dört kategoriye (Bandit, Tradeoff, Structure, Social) yayılan 12 görev; her katılımcı rastgele iki kategori alıp her kategoride üç görev tamamlıyor. Kalite kontrolü (reCAPTCHA, anlama/dikkat testleri, yanıt süresi ve tarayıcı odağı filtreleri) sonrası 273.343 karardan %2,9'u eleniyor ve 261.551 geçerli karar kalıyor (ortalama yaş 42,2, SS 14,1; 300 kadın, 285 erkek, 6 diğer/belirtmemiş). Görev formülasyonu: hedef görev açıklaması + kaynak görev açıklaması + aynı katılımcının kaynak görevdeki davranış dizisi verildiğinde, o katılımcının hedef görevdeki eylemlerini tahmin etmek. Model: Qwen3-8B → Psych-101 ile Centaur → Cross-Psych-101 ile Cross-Centaur (sohbet biçimli denetimli ince ayar; Qwen3-1.7B, Llama-3.2-1B, Llama-3.1-8B ile sağlamlık kontrolleri). Sonuçlar: Cross-Centaur katılımcı-dışarıda bırakılmış (held-out participants) değerlendirmede hem aynı-görev hem görevler-arası koşullarda, hem aynı kategori hem farklı kategori transferinde en iyi negatif log-olabilirlik (NLL) değerlerini neredeyse tüm sütunlarda alıyor; hazır Qwen3-8B/14B'yi ve Centaur'u geçiyor. Kazançlar mütevazı ama tutarlı: örneğin Correlated Bandit'te NLL 1,493 → 1,462, Ultimatum'da 1,583 → 1,554, 2-Armed Bandit'te 0,300 → 0,294; buna karşılık bazı görevlerde fark yok veya hafif negatif (Social Value Orientation 1,613 → 1,629). İstem ablasyonları nedensel iddiayı destekliyor: kaynak davranışı BAŞKA bir katılımcıyla değiştirmek (shuffled) veya kaynak görevi tümüyle çıkarmak (target-only) performansı düşürüyor — yani kazanç, eşleşmiş bireye özgü kanıttan geliyor, yalnızca istem uzunluğundan veya görev önsavından değil. Probing analizleri (tek gizli katmanlı MLP, görev başına ayrı prob) Cross-Centaur'un gizli durumlarının pişmanlık (regret), risk tercihi gibi katılımcı düzeyi eğilimleri kodladığını ve bu temsillerin görevler arası taşındığını gösteriyor; risk tercihi için gizli durumun doğrusal projeksiyonu insan dağılımıyla uyumlu bir gradyan üretiyor. Yine de sınırlar belirgin: görev-dışarıda bırakılmış (task-held-out) koşulda kazançlar küçülüyor; öngörülen pişmanlık dağılımı insan dağılımından daha dar; tüm görevler kontrollü psikoloji paradigmaları; katılımcı havuzu yalnızca İngilizce akıcı kişilerden oluşuyor, dolayısıyla dilsel/kültürel genelleme yok. Yazarlar kendi etik uyarısını da ekliyor: insan davranış verisiyle eğitilmiş modeller 'toplum modeli' değildir; LLM tabanlı davranış simülasyonları hipotez keşif aracı olarak görülmeli, yüksek sonuçlu kararlarda insan yargısının yerini almamalı. Veri seti HuggingFace'te açık: HikaruAsano/cross-psych-101.

## Key Points

- Künye: arXiv:2610.23157 [cs.CL], 16 Ekim 2026 (v1); EMNLP 2026 Main Conference Oral kabulü arXiv yorum alanında doğrulandı; yazarlar Tokyo Üniversitesi + Sakana AI Labs.
- Çözülen boşluk: Centaur/Psych-101 hattı popülasyon düzeyi düzenlilikleri öğreniyor ama aynı katılımcıyı görevler arası bağlamadığı için birey düzeyi (kişiye özgü) tahmin yapamıyor.
- Yeni veri seti Cross-Psych-101: 591 katılımcı (601 toplandı, 10 kişi kamuya açılmadan çekildi), 261.551 geçerli karar, 12 görev / 4 kategori (Bandit, Tradeoff, Structure, Social); her katılımcı rastgele 2 kategori × 3 görev.
- Kalite: 273.343 kararın ~%2,9'u elendi (reCAPTCHA, anlama/dikkat testleri, yanıt süresi, tarayıcı odağı); örneklem ortalaması 42,2 yaş (SS 14,1), 300 kadın / 285 erkek / 6 diğer.
- Formülasyon: hedef görev tanımı + kaynak görev tanımı + aynı katılımcının kaynak davranışı → hedef görevdeki eylemlerin olasılığı; Qwen3-8B tabanlı, Centaur üzerine uyarlanmış Cross-Centaur.
- Ana sonuç: katılımcı-dışarıda bırakılmış değerlendirmede hem aynı-görev hem görevler-arası, hem aynı hem farklı kategori transferinde NLL en iyi (hazır Qwen3-8B/14B ve Centaur'dan iyi).
- Kazanç büyüklüğü dürüstçe mütevazı: Correlated Bandit 1,493→1,462; Ultimatum 1,583→1,554; 2-Armed Bandit 0,300→0,294; bazı görevlerde fark yok, Social Value Orientation'da hafif kötüleşme (1,613→1,629).
- Ablasyon: kaynak davranış başka katılımcıyla değiştirildiğinde veya kaynak görev çıkarıldığında performans düşüyor → kazanç eşleşmiş bireye özgü kanıttan geliyor, istem uzunluğundan veya genel dil önsavından değil.
- Probing: gizli durumlardan pişmanlık ve risk tercihi gibi katılımcı eğilimleri doğrusal olarak çözülebiliyor ve görevler arası taşınıyor; risk tercihi görselleştirmesinde insan dağılımıyla uyumlu gradyan.
- Sınırlar: görev-dışarıda bırakılmış koşulda kazançlar küçülüyor; öngörülen pişmanlık dağılımı insandan dar; yalnızca kontrollü psikoloji görevleri; yalnızca İngilizce akıcı katılımcılar (kültürel/dilsel genelleme yok); yazarların kendi ifadesiyle 'birleşik insan davranışı modeli' hedefinin ilk adımı.
- Etik çerçeve: LLM tabanlı davranış simülasyonu 'toplum modeli' değil; hipotez keşfi ve olası örüntüleri tarama aracı, yüksek sonuçlu kararlarda insan yargısının ikamesi değil.
- Veri: HuggingFace HikaruAsano/cross-psych-101 açık; temel Centaur ağırlığı marcelbinz/Psych-101 ekosisteminden.

## Turkey Context

Bu makale, Türkiye'de hızla yayılan 'sentetik denek / silicon sampling' pratiği için hem bir şablon hem bir uyarı. Şablon: aynı kişiden birden fazla görevde davranış toplayıp birey-düzeyi tahmin yapmak, tek seferlik anket simülasyonlarından metodolojik olarak daha güçlü — Türkiye'de siyasal davranış (risk tercihi, sosyal tercihler, kamusal mal katkısı, ültimatom oyunu) çalışmalarında katılımcıları boylamsal/çok-görevli tasarımla toplayan bir yerel veri seti, LLM'lerin Türk seçmene ne kadar genellenebildiğini test etmenin ön koşulu. Uyarı: çalışmanın katılımcı havuzu yalnızca İngilizce akıcı kişilerden oluşuyor ve yazarlar bunu açık bir sınır olarak yazıyor; dolayısıyla 'LLM Türk katılımcıyı da temsil eder' iddiası bu bulgularla desteklenmiyor. Ayrıca kazançların mütevazı olması (NLL'de ~0,01-0,04 iyileşme, bazı görevlerde sıfır) Türkiye'deki uygulamalı araştırmacılar için önemli bir beklenti ayarı: LLM'e 'sentetik örneklem' olarak dayanıp anket deneyi maliyetinden kaçınmak, birey düzeyi tahminde mevcut haliyle savunulabilir değil; popülasyon düzeyi ortalama eğilimler için daha makul, birey düzeyi iddialar için değil. Kutuplaşma/dezenformasyon çalışmaları açısından dolaylı değer: 'Social' kategorisindeki kamusal mal, sosyal değer yönelimi ve ültimatom görevleri, işbirliği ve dış-grup davranışının bireysel farklarla nasıl modellendiğine dair bir hat açıyor; Türkiye'de parti kimliğiyle işbirliği davranışını birleştiren deneyler için doğal bir uzantı.

## 🏷 Retorik Roller

- 🔍 **Araştırma Boşluğu**
- 🧩 **Yöntem**
- 📊 **Bulgular**
- ⚠️ **Sınırlılıklar**

---

## 🔗 İlgili Bağlantılar
### 🧠 İlgili Kavramlar
- [[concepts/sentetik-populasyonlar.md|Sentetik Popülasyonlar ve Birey-Tabanlı Simülasyon]]
### 🏛 İlgili Kurum/Kişiler
- [[entities/arxiv-org.md|Arxiv Org]]
### 📄 İlgili Makaleler
- [[raw/articles/2026-10-15_synthetic-populations-for-epidemic-demographic-and.md|Synthetic populations for epidemic, demographic and mobility modeling (Torre ve ark., 2026)]] — popülasyon düzeyi sentetik birey ile birey düzeyi öğrenilmiş davranış modeli aynı simülasyon hattının iki ucu.
