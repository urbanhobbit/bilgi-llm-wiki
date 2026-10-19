---
type: concept
title: Sentetik Popülasyonlar ve Birey-Tabanlı Simülasyon
description: Sayım ve idari kayıtlardan üretilen, her bireyin yaş/cinsiyet/hane/iş-okul/mekân atamasıyla temsil edildiği yapay nüfuslar; ajan-tabanlı modellerin (ABM) altyapısı ve LLM tabanlı 'sentetik birey' yaklaşımları.
tags:
- kavram
- sentetik-populasyonlar
- synthetic-population
- agent-based-modeling
- simulation
- metodoloji
timestamp: '2026-10-19T00:00:00Z'
created: '2026-10-19'
updated: '2026-10-19'
sources: []
related: []
confidence: medium
---

# Sentetik Popülasyonlar ve Birey-Tabanlı Simülasyon

## Tanım
Sentetik popülasyon, gerçek nüfusun istatistiksel yapısını (yaş-cinsiyet piramidi, hane kompozisyonu, yoğunluk, meslek dağılımı, işe gidiş akışları) koruyan, ancak her bireyi anonim bir "ajan" olarak üreten yapay bir nüfus veri setidir. Birey-tabanlı (individual-based) ya da ajan-tabanlı modellerin (agent-based models, ABM) girdisidir: salgın yayılımı, afet/çevresel maruziyet, kentsel hareketlilik ve demografik projeksiyon gibi temalar bu taban üzerinde simüle edilir. Temel mantık, toplulaştırılmış (compartmental) modellerin homojen karışım varsayımını kırmak: temaslar hane, okul, işyeri ve boş zaman mekânlarında gerçekleşir; kimin kiminle karşılaştığı mekânsal ve sosyo-demografik konumdan türer.

## Üretim hattının tipik aşamaları
1. **Hane üretimi:** sayım bölgesi düzeyinde hane tipi dağılımından örnekleme, ardından yaş piramidinden bireylere yaş/cinsiyet atama.
2. **Coğrafi yerleştirme:** haneleri beklenen nüfus yoğunluğuna göre sayım bölgesi/bina düzeyinde konumlandırma.
3. **Faaliyet ataması:** çalışan/öğrenci/çalışmayan statüsü, ekonomik sektör, eğitim kademesi.
4. **Ana faaliyet mekânı:** gerçek işyeri ve okul kayıtları (kapasite + coğrafi referans) ve belediye düzeyi işe gidiş-geliş (OD) matrisleriyle iş/okul ataması.
5. **Zaman programı:** ulusal zaman kullanımı anketleri, toplu iş sözleşmeleri ve açılış saatlerinden günlük aktivite zamanlaması.

## Doğrulama ölçütleri
- **Demografik marjinaller:** yaş-cinsiyet piramidi ve hane büyüklüğü dağılımında toplam ve MAPE hatası.
- **Mekânsal isabet:** sayım bölgesi (census tract) ve il (NUTS-3) düzeyinde nüfus sayısı hatası.
- **Hareketlilik:** sentetik ve gerçek OD seyahat olasılıkları arasında korelasyon.
- **Temas yapısı:** hane içi eş-bulunma (co-presence) matrisinin Polymod/Prem/Mistry gibi temas anketleriyle karşılaştırılması.

## Yöntemsel tartışmalar
- **Mekânsal açıklık ile sadakat arasındaki denge:** coğrafi ayrıntı eklemek, yaş yapılı hane karışımı gibi sosyo-demografik doğruluğu bozmamalı; en yeni çalışmalar bu ikisinin birlikte sağlanabildiğini gösteriyor.
- **Veri vintajı ve erişim:** sayım mikro verisi, OD matrisleri ve zaman kullanımı anketleri farklı yıllara ait olabilir; küçük yerleşimlerde OD akışları seyrek ve yüksek varyanslıdır. Açık lisans/erişim, yeniden üretilebilirliğin ön koşulu.
- **LLM tabanlı "sentetik birey":** popülasyon düzeyi değil birey düzeyi davranışı taklit etme hattı (Centaur/Cross-Centaur çizgisi), aynı kişinin farklı görevlerdeki davranışını birbirine bağlayan veri setleriyle ilerliyor. Bu hat, ABM'lerin sabit davranış kuralları yerine öğrenilmiş davranış modelleri kullanmasının önünü açıyor; ancak etkiler şu an mütevazı ve örneklemler dilsel/kültürel olarak dar. **Karşı-kanıt (2026, Nature Human Behaviour):** 74 ülkede 67.201 kişiyle eşleştirilmiş sanal ankette LLM yanıtları birey düzeyinde zayıf ama sistematik hizalama gösteriyor (korelasyonların %87,5'i sıfırın üzerinde), demografik gradyanların %77,8'ini tutturuyor, fakat **kültürel boyutlarda %48,1'de kalıyor** — yani şans düzeyinde. Hata ekonomik gelişmişlik ve dijital bağlantıyla artıyor; yeni modeller eskilerden daha iyi değil. Sonuç: LLM tabanlı sentetik birey, hipotez/tasarım aracı olarak değerli, temsili anket vekili olarak değil.

## Neden önemli
Politika müdahalelerinin (okul kapatma, mesafelenme, aşılama, afet tahliyesi) geri tepmeleri ve dağılımsal etkileri ancak heterojen bireyler üzerinde test edilebilir. Sentetik popülasyon, gerçek mikro veriye erişmeden bu testi mümkün kılar — gizlilik korunur, senaryo tekrarlanabilir olur. Aynı zamanda hesaplamalı sosyal bilim (computational social science) içinde yeniden kullanılabilir ortak altyapı işlevi görür: tek bir veri seti, epidemiyolojiden kentsel planlamaya ve seçmen davranışının mekânsal modellenmesine kadar farklı literatürlere taban sağlar.

## İlgili kavramlar
- [[concepts/siyaset-bilimi-metodolojisi.md|Siyaset Bilimi Metodolojisi]] — hesaplamalı sosyal bilim, machine learning modeling ve araştırma tasarımı tartışmaları.
- [[concepts/olcum-araclari.md|Ölçüm Araçları]] — simülasyon çıktılarının ölçüm ve doğrulama sorunları.

## İlgili Makaleler
- [[raw/articles/2026-10-15_synthetic-populations-for-epidemic-demographic-and.md|Synthetic populations for epidemic, demographic and mobility modeling (Torre ve ark., 2026)]]
- [[raw/articles/2026-10-16_cross-centaur-modeling-individual-decision-making-.md|Cross-Centaur: Modeling Individual Decision-Making Across Psychological Tasks with Language Models (Asano ve ark., 2026)]]
- [[raw/articles/2026-10-12_simulated-responses-from-large-language-models-are.md|Simulated responses from LLMs are weak proxies for human economic preferences across 74 countries (Chen ve ark., Nature Human Behaviour, 2026)]] — LLM tabanlı sentetik bireyin sınırları: kültürel boyutlarda hizalama şans düzeyinde.
