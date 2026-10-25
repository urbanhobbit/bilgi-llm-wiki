---
type: raw_article
title: Can AI interview? Comparing AI-led to Human-led Chat Interviews
description: 'SocArXiv ön baskı v2 (Crossref: 20 Ekim 2026; metin ''October 2026'');
  23 sayfa + ekler; DOI 10.31235/osf.io/7bdz2_v2; hakem değerlendirmesinden geçmemiş
  (ilk sürüm Temmuz 2025''te ön baskı olarak çıkmış...'
resource: https://osf.io/preprints/socarxiv/7bdz2_v2
tags:
- kurator
- high
timestamp: '2026-10-25T05:41:50Z'
source_file: 2026-10-25_guven-can-ai-interview.json
category: KURATOR
priority: high
roles:
- gap
- method
- result
- limitation
published: '2026-10-20'
---

# Can AI interview? Comparing AI-led to Human-led Chat Interviews

**Author(s):** Semra Guven, Tobias Gårdhus, Andreas Bjerre-Nielsen, Anna Rogers, Hjalmar Bang Carlsen (University of Copenhagen / SODAS / IT University of Copenhagen)

**Published:** 2026-10-20

**Source:** [https://osf.io/preprints/socarxiv/7bdz2_v2](https://osf.io/preprints/socarxiv/7bdz2_v2)

## Summary

SocArXiv ön baskı v2 (Crossref: 20 Ekim 2026; metin 'October 2026'); 23 sayfa + ekler; DOI 10.31235/osf.io/7bdz2_v2; hakem değerlendirmesinden geçmemiş (ilk sürüm Temmuz 2025'te ön baskı olarak çıkmış). Yazarlar: Semra Guven (Kopenhag Üniv.), Tobias Gårdhus, Andreas Bjerre-Nielsen, Hjalmar Bang Carlsen (SODAS — Center for Social Data Science, Kopenhag Üniv.) ve Anna Rogers (IT University of Copenhagen); Gårdhus ve Guven eşit katkı, Carlsen sorumlu yazar. Soru: LLM tabanlı bir 'yapay zeka görüşmeci', nitel görüşme verisinin kalitesi açısından eğitimli insan görüşmeciyle kıyaslandığında ne üretiyor — ve bu, nitel verinin ölçeklenebilirliği iddiasını taşıyabiliyor mu? Tasarım: N=41 üniversite öğrencisiyle randomize deney; katılımcılar eşzamanlı metin (chat) görüşmesinde ya eğitimli insan görüşmeciye ya da yerel olarak çalıştırılan açık ağırlıklı bir modele atanıyor; iki koşulda aynı arayüz, aynı konu (akademik yardım arama) ve aynı görüşme kılavuzu. 45 kişi randomize edildi, ilk gün arızalanan 4 yapay zeka görüşmesi atıldı, 41 görüşme analiz edildi (20 yapay zeka, 21 insan). Sistem: OpenHermes 2.5 (Mistral 7B'nin instruction-tuned hali, 7,24 milyar parametre, Q4 4-bit, Ollama ile yerel) üzerinde üç ajanlı mimari — sınıflandırma (soru daha önce yanıtlandı mı / tarama sorusu geçildi mi), yeniden formüle etme (önceki yanıtın bağlamını soruya taşıma) ve sonda üretme (bağlama duyarlı takip sorusu). Yapay zeka yalnızca önceden tanımlı açık uçlu ana sorulara sonda üretiyor; serbest soru üretmiyor — bu, önceki sistemlere (Chopra & Haaland 2023; Geiecke & Jaravel 2024) kıyasla bilinçli bir özerklik kısıtı. Kalite üç boyutta ölçülüyor (Small & Calarco 2022): maruz kalma (exposure), özgüllük (specificity, 1-5) ve alaka (relevance, 1-5); 909 soru-cevap çiftinden (618 yapay zeka, 291 insan) koşula göre dengeli 400'lük rastgele örnek kodlanmış (395 geçerli: 200 yapay zeka, 195 insan); iki kodlayıcı bağımsız puanlamış. Kodlayıcılar arası güvenilirlik: özgüllük Krippendorff α=0,648 (eşik 0,667'nin hemen altında), alaka α=0,365 (neredeyse tüm yanıtlar 5 puan olduğu için tavana yakın, ayırt edici değil). Analiz: Mann-Whitney U + Holm (9 karşılaştırma) ve eşdeğerlik iddiaları için Hodges-Lehmann kayma tahmini + dağılımdan bağımsız güven aralıkları. Bulgular — maruz kalma: medyan görüşme süresi benzer (28,9 vs 28,3 dk; p=0,769; ancak fark için GA -4,6 ile +12,8 dk arası, yani 13 dakikaya kadar yapay zeka lehine fark dışlanamıyor); yapay zeka görüşmeleri toplamda %65 daha fazla metin üretmiş (3.244 vs 1.968 karakter; p=0,011) çünkü iki kat fazla soru sormuş (31 vs 14; p<0,001); soru başına yanıt insan koşulunda daha uzun (150 vs 112 karakter, %34) ama çoklu test düzeltmesinden sonra anlamsız (p=0,412); soru formüle etme süresi insanda ~39 saniye, yapay zekada 3 saniye (p<0,001; dağılımlar hiç örtüşmüyor). Dakika başına: 1,18 vs 0,54 yanıt (p<0,001) ve 106 vs 72 karakter (p=0,008) — yani araştırmacının zamanı başına ~%48 daha fazla malzeme. Kalite: alaka iki koşulda da neredeyse tavan (M=4,9); tahmini kayma sıfır, GA -0,11 ile +0,05 → operasyonelleştirildiği biçimiyle eşdeğerlik iddiası güçlü. Özgüllük insan koşulunda biraz yüksek (3,8 vs 3,6) ama anlamsız (p=0,769); kayma -0,16, GA -0,71 ile +0,36 → insan lehine 0,75 puandan büyük fark dışlanabiliyor, ama 0,5 puanlık fark hâlâ mümkün; yani bu bir 'fark yok' bulgusu değil, 'fark saptanamadı' bulgusu. Tek belirgin dezavantaj: atlama (skip) düğmesi 22 kez, tamamı yapay zeka koşulunda, 5 katılımcı tarafından kullanılmış (5/20 vs 0/21; Fisher p=0,021, dokuz karşılaştırmalık aileye dahil değil); atlama sayıları yanıt sayılarından düşülünce sonuçlar değişmiyor (ortalama yanıt uzunluğu 112→108 karakter, p=0,296). Sağlamlık: gün içi karşılaştırmalar ve ilk günün dışlanması sonuçları değiştirmiyor (Ek C). Yazarların kendi sınırlamaları: karşılaştırma 'uzman' görüşmeciye değil, eğitimli uzman olmayan görüşmeciye karşı (American Voices Project tipi büyük ölçekli nitel veri toplama bağlamı); chat formatı sözlü ipuçlarını ve ilişki kurmayı ortadan kaldırdığı için insan görüşmeciyi dezavantajlıyor; kılavuzda rapport kurma girişi yok; model göreve özel ince ayar görmemiş, yani sonuçlar yapay zeka görüşmecinin üst sınırı değil; Mistral'in eğitim verisi belgelenmemiş (tam açık OLMo 7B denendi, yeterli performans alınamadı) — bu yüzden 'model-özgü görüşmeci etkisi' riski sürüyor; karakter sayısı derinlik yerine uzunluk ölçüyor (anlamsal geçerlilik), ve soru-cevap çifti birimi konuşma bağlamını yok sayıyor (birimleştirme). Sonuç: açık ağırlıklı 7B'lik yerel model, eğitimli uzman olmayan insan görüşmeciyle kıyaslanabilir ölçüde alakalı ve saptanabilir fark olmaksızın benzer özgüllükte veri üretiyor, birim zamanda belirgin biçimde daha fazla malzeme topluyor — ama bu, uzman görüşmecinin yerini alabileceği anlamına gelmiyor.

## Key Points

- SocArXiv v2 ön baskı (Crossref 20 Ekim 2026), DOI 10.31235/osf.io/7bdz2_v2 — hakem değerlendirmesi YOK; Guven, Gårdhus, Bjerre-Nielsen, Carlsen (SODAS/Kopenhag) ve Rogers (ITU).
- İlk doğrudan karşılaştırma: randomize chat görüşmesi, N=41 (20 yapay zeka / 21 insan); aynı arayüz, aynı konu, aynı kılavuz; 45 randomize, ilk gün arızalı 4 yapay zeka görüşmesi atıldı.
- Sistem: OpenHermes 2.5 (Mistral 7B, Q4, Ollama ile yerel) + üç ajan (sınıflandırma, yeniden formüle etme, sonda üretme); yapay zeka yalnızca önceden tanımlı ana sorulara sonda üretiyor.
- Maruz kalma: medyan süre benzer (28,9 vs 28,3 dk), toplam metin %65 fazla (3.244 vs 1.968 karakter), soru sayısı iki kat (31 vs 14); soru formüle etme 39 sn vs 3 sn.
- Verim: dakikada 1,18 vs 0,54 yanıt; dakikada 106 vs 72 karakter (~%48 fazla malzeme); soru başına yanıt insanda %34 daha uzun ama düzeltme sonrası anlamsız.
- Kalite: alaka iki koşulda da 4,9/5 ve eşdeğer (GA -0,11…+0,05); özgüllük 3,8 vs 3,6, anlamsız (p=0,769) — ancak 0,5 puanlık insan üstünlüğü dışlanamıyor (GA -0,71…+0,36).
- Tek net dezavantaj: atlamaların tamamı yapay zeka koşulunda (22 atlama, 5 katılımcı; 5/20 vs 0/21; Fisher p=0,021) — nedeni tasarımla ayırt edilemiyor.
- Sınırlar: uzman görüşmeciyle değil eğitimli uzman olmayanla karşılaştırma; chat formatı insanı dezavantajlıyor; rapport girişi yok; model ince ayarsız; Mistral eğitim verisi belgesiz; karakter sayısı derinlik yerine uzunluk ölçüyor.
- Açık bilim: github.com/ainterviewer/can-ai-interview — kılavuz, promptlar, kod ve toplulaştırılmış veriler açık; ham transkriptler gizlilik gereği kapalı.

## Turkey Context

Türkiye'de nitel araştırmanın en büyük darboğazı örneklem: derinlemesine görüşme 20-40 kişide kalıyor, nicel anket ise 1.000+ kişiye ulaşıyor. Makalenin gösterdiği şey — 7B'lik yerel bir modelin, eğitimli bir saha asistanıyla kıyaslanabilir özgüllükte veri üretip birim zamanda %48 daha fazla malzeme toplaması — Türkiye'deki araştırma altyapısı açısından doğrudan bir eşik. Birincisi hukuki: yazarların GDPR gerekçesi Türkiye'de KVKK'ya birebir çevrilebilir; hassas gruplarla (mülteciler, çocuklar, Alevi/Kürt kimlikleri, sendikalı işçiler) görüşmede veriyi yurt dışı bir API'ye göndermek hem KVKK hem kurumsal etik kurul açısından ciddi bir yük; yerel açık ağırlıklı model bu yükü kaldırıyor. İkincisi dil: makale İngilizce ve Mistral tabanlı bir modelle çalışıyor; Türkçe nitel görüşmede sonda kalitesi ayrıca test edilmeli — Türkçe için ince ayarlı açık modeller (ör. yerel Türkçe LLM'ler) bu tasarımın doğal uzantısı ve henüz kimse bu karşılaştırmayı yapmadı; bu, Türkiye'deki iletişim/sosyoloji bölümleri için düşük maliyetli, yayınlanabilir bir boşluk. Üçüncüsü yöntemsel: Türkiye'de 'yapay zeka anket yapabilir mi' tartışması ağırlıkla nicel (sentetik popülasyon, LLM ile anket simülasyonu) tarafında yürüyor; bu makale nitel tarafta, üstelik eşdeğerlik testi ve Hodges-Lehmann aralıklarıyla 'fark yok' iddiasını ciddiye alarak yöntemsel bir örnek sunuyor. Dördüncüsü emek ve etik: sonda üretimini 39 saniyeden 3 saniyeye indirmek, saha asistanlığı işini dönüştürür — Türkiye'de proje bazlı çalışan genç araştırmacılar için bu, 'veri toplama ucuzlar' değil 'kimin emeği görünmez olur' sorusu; atlama davranışının yalnızca yapay zeka koşulunda görülmesi (5/20 vs 0/21) de katılımcının makineye karşı sosyal maliyeti düşük gördüğünü ima ediyor, yani veri kalitesi kazancı katılımcı direnciyle birlikte okunmalı. Beşincisi: raporda açıkça yazıyor — bu, uzman görüşmecinin yerini alma iddiası değil; Türkiye'de nitel araştırmayı 'ucuzlatma' baskısı altında bu nüansın korunması kritik.

## 🏷 Retorik Roller

- 🔍 **Araştırma Boşluğu**
- 🧩 **Yöntem**
- 📊 **Bulgular**
- ⚠️ **Sınırlılıklar**

---

## 🔗 İlgili Bağlantılar
### 🏛 İlgili Kurum/Kişiler
- [[entities/osf-io.md|Osf Io]]
