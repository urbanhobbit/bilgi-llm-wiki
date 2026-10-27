---
type: concept
title: Metin Madenciliği ve Hesaplamalı Metin Analizi
description: 'Büyük metin korpuslarında örüntü çıkarmaya dayalı yöntemler: kelime/cümle gömmeleri (Sentence-BERT), kümeleme (HDBSCAN), konu modelleme, bibliyometrik eşleşme ve uzak okuma. Gözetimsiz yöntemler önceden kategori dayatmadan anlamsal ve topluluk yapıları üretir.'
tags:
- akademik
- metodoloji
- metin-madenciligi
- hesaplamali-sosyal-bilimler
timestamp: '2026-10-27T08:00:00Z'
created: 2026-10-27
updated: 2026-10-27
confidence: medium
---
# Metin Madenciliği ve Hesaplamalı Metin Analizi

Büyük metin korpuslarını okumadan önce yapılandırmaya yarayan yöntem ailesi. İki eksende ayrılır:

- **Gözetimli (supervised):** Önceden tanımlı kategorilerle sınıflandırma — ince ayarlı transformer sınıflandırıcıları, sözlük temelli kodlama.
- **Gözetimsiz (unsupervised):** Kategorileri veriden çıkarma — cümle gömmeleri + kümeleme, konu modelleme (LDA/BERTopic), bibliyografik eşleşme ağlarında topluluk algılama. Şimdicilik (presentism) riskini azaltır ama tek başına anlam üretmez: kümeler ancak yakın okuma ve ikincil literatürle etiketlenir.

**Tipik boru hattı:** korpus temizliği/OCR → cümle bölme → gömme (Sentence-BERT, BERTurk) → zaman dilimlerine ayırma → kümeleme (HDBSCAN) → yıllar arası birleştirme (kosinüs benzerliği) → göstergelerle yorumlama (TF-IDF, merkeze en yakın cümle/makale, en çok atıf alan referans).

**Bilinen tuzaklar:** OCR formül ve tabloları bozar (biçimsel modeller görünmez olur); atıf verisi 1960 öncesi için seyrek; sunum yanlılığı (present bias) nedeniyle dilimleme şart; eşik ve küme sayısı seçimleri analistin önselini taşır ve raporlanmalıdır.

**Bağlantılı kavramlar:** [[concepts/siyaset-bilimi-metodolojisi.md|Siyaset Bilimi Metodolojisi]], [[concepts/olcum-araclari.md|Ölçüm Araçları]]

## İlgili Makaleler
- [[raw/articles/2026-09-25_one-sentence-at-a-time-a-quantitative-history-of.md|One Sentence at a Time: A Quantitative History of Rationality in Economic Thought]] — 259.165 makale / 61 milyon cümle; yıllık temsilci vektör + HDBSCAN (17 anlamsal küme) ve 43 bibliyografik eşleşme ağı ile rasyonalite kavramının yüzyıllık dönüşümü.
