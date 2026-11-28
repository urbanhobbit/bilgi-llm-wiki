---
type: dataset
title: "Military Doctrines: A Corpus of National Security Strategy Documents"
authors:
- J. Andrés Gannon
year: 2026
date: 2026-11-10
venue: "Harvard Dataverse (V1, CC0 1.0)"
doi: 10.7910/DVN/OHOMP8
open_access: true
license: CC0-1.0
language: en
tags:
- national-security-strategy
- text-as-data
- corpus
- military-doctrines
- defense-white-papers
- comparative-politics
- text-reuse
source: "https://x.com/mlemoglie/status/2126255179028672979"
url: https://doi.org/10.7910/DVN/OHOMP8
project_url: https://militarydoctrines.com
accessed: 2026-11-27
confidence: high
---

# Military Doctrines — Ulusal Güvenlik Stratejisi Metinleri Külliyatı

> **Künye:** Gannon, J. Andrés (2026). *Military Doctrines: A Corpus of National Security Strategy Documents*. Harvard Dataverse, V1. DOI: [10.7910/DVN/OHOMP8](https://doi.org/10.7910/DVN/OHOMP8) | Lisans: **CC0 1.0** (kamu malı) | Proje sitesi: [militarydoctrines.com](https://militarydoctrines.com)
> **Kurum:** Vanderbilt University | **Sürüm:** 2026.11 (yayın 10 Kasım 2026)
> **İlgili çalışma:** Gannon, "A Text-as-Data Approach to Measuring Interstate Relations Using National Security Strategies" (working paper)

## Ne Var?

- **823 belge**, **112 ülke/bölge/örgüt**, **1962–2025** dönemi.
- Belge türleri: ulusal güvenlik stratejileri, savunma beyaz kitapları (defense white papers), askeri doktrinler, ilgili strateji belgeleri.
- Her belge için üç katman: (1) orijinal PDF, (2) çıkarılmış tam metin (pymupdf4llm; taranmışlar için Marker OCR), (3) ~128 token'lık parçalara (chunk) bölünmüş metin.
- **586 belge "core corpus"**: hükümetin bütününü kapsayan (whole-of-government) ulusal güvenlik ve savunma stratejileri (`keep = 1`). Kalan 237 belge katalogda var ama kapsam dışı (`keep = 0`): sektörel stratejiler (siber, terörle mücadele), yatırım planları, dış politika beyaz kitapları, mükerrer baskılar.
- **Dil dağılımı:** 627 İngilizce, 196 İngilizce olmayan (orijinal dilinde verilmiş).
- **Tür etiketi:** 37 belge `cyber`, 1 belge `terrorism`, 785 genel strateji.
- 5 adet PDF zip'i (0,4–2,3 GB arası) + tek tabloda tam metin (`nss_fulltext.csv.gz`, 54 MB) + parça tabloları + metadata (`nss_metadata.csv`, 823 satır).

## Değişkenler (metadata)

`file_names` · `country_name` (lowercase, boşluksuz: `us`, `southkorea`, `eu`) · `year` · `title` (İngilizce olmayanlar için İngilizce çeviri) · `language` (`eng`/`noneng`) · `keep` (1 = çekirdek külliyat) · `type` (`cyber`/`terrorism`/boş)

## Dönemsel Dağılım (metadata'dan hesaplandı)

- 1960'lar: 1 · 1970'ler: 5 · 1980'ler: 10 · **1990'lar: 54** · **2000'ler: 248** · **2010'lar: 383** · 2020–2025: 122
- Belirgin kırılma 1990 sonrası: Soğuk Savaş sonrası savunma belgesi üretimi patlaması. Zirve 2010'lar.

## En Çok Belge Üreten Aktörler (ilk 15)

avustralya 38 · abd 35 · japonya 32 · tayvan 28 · çekya 25 · birleşik krallık 22 · güney kore 21 · bulgaristan 20 · letonya 20 · litvanya 20 · hindistan 19 · norveç 19 · slovenya 19 · danimarka 16 · rusya 16

**Okuma:** Listenin başında ABD değil Avustralya var; Tayvan (28) ve Baltık üçlüsü (Letonya/Litvanya 20'şer) gibi küçük-orta güçler, tehdit algısı yoğunlaştıkça strateji belgesi üretimini hızlandırıyor. Yani belge sayısı bir *kapasite* değil bir *tehdit algısı / kurumsal olgunluk* göstergesi.

## Türkiye

Veri setinde Türkiye'den **5 belge** (bu, Türkiye'nin strateji belgesi üretiminin görece seyrek olduğunu gösteriyor):

- **2000** — Defense White Paper (`keep=1`)
- **2007** — Defense White Paper (`keep=1`)
- **2013** — National Cyber Security Strategy and Action Plan (`keep=0`, siber)
- **2019** — Stratejik Plan (`keep=1`, noneng — Türkçe)
- **2021** — National Artificial Intelligence Strategy (`keep=0`)

**Not:** 2007 sonrası genel ulusal güvenlik stratejisi belgesi yok; 2019'daki "Stratejik Plan" muhtemelen bir kurum planı (ör. Savunma Sanayii / MSB) olup tam metinden doğrulanmalı. 2023 sonrası yeni bir güvenlik stratejisi belgesinin külliyatta bulunmaması, veri setinin Türkiye kapsamının güncellenmesi gerektiğine işaret ediyor.

## Neden Önemli

- **Tekrar kullanım potansiyeli yüksek:** CC0 lisans + tam metin + hazır chunk'lar → LLM tabanlı kodlama, tehdit çerçevelemesi (threat framing), dış politika tonu, "düşman" inşası, stratejik kültür karşılaştırmaları için hazır veri.
- **Devlet söyleminin birincil kaynağı:** anket veya haber verisi yerine doğrudan devletin kendi tehdit tanımı. "Ülkeler kendi güvenlik tehditlerini nasıl adlandırıyor?" sorusunu ölçülebilir kılıyor.
- **Zaman serisi:** 1962–2025 aralığı, Soğuk Savaş sonu, 11 Eylül sonrası ve 2014/2022 sonrası kırılmalarını metin düzeyinde karşılaştırmaya izin veriyor.
- **Devletlerarası ilişki ölçümü:** İlgili working paper, bu külliyatı ikili ilişki (dyadic relations) ölçümü için kullanıyor — Türkiye-Yunanistan, Türkiye-Rusya gibi çiftlerde karşılıklı tehdit atfı incelenebilir.

## Sınırlılıklar

- **Dil dengesizliği:** %76 İngilizce; İngilizce olmayan 196 belge çevrilmemiş, yani İngilizce metin madenciliği yapan çalışmalar sistematik olarak İngilizce yayın yapan ülkelere/çeviri pratiği olan devletlere yanlı olur.
- **Erişim ≠ kapsam:** Bazı ülkeler belgelerini yayımlamıyor (gizlilik), bazıları hiç üretmiyor. Külliyat "var olan belgeler"in değil "erişilebilen belgeler"in külliyatı.
- **OCR kalitesi:** Taranmış belgelerde Marker OCR hataları, tablo/başlık artıkları metne karışmış (`![ ](...)` placeholder'ları).
- **`keep=1` sınırı keyfi:** Hangi belgenin "whole-of-government" sayıldığı kodlayıcı kararı; sektörel stratejilerin dışlanması siber/terörle mücadele söylemini analiz dışı bırakıyor (oysa `type` alanı bunları ayrıca işaretliyor).

## Kullanım Notları

- Tam metin: `nss_fulltext.csv.gz` (54 MB) — tek tabloda metadata + `text`.
- Parça tabloları: `nss_chunks_all.zip` — belge başına `_chunks.csv`.
- Dosya adlandırma: `{country}_{year}_{TitleWithoutSpaces}[_noneng]` — PDF, `.txt` ve `_chunks.csv` aynı kök adı paylaşır.
- Dataverse API: `https://dataverse.harvard.edu/api/datasets/:persistentId/?persistentId=doi:10.7910/DVN/OHOMP8`
- Proje sitesinde her belge için aranabilir tablo + changelog var.

## Kaynak Notu

Veri seti, X'te Marco Le Moglie (@mlemoglie) paylaşımıyla görüldü (27 Kasım 2026). Künye Crossref/DataCite ve Dataverse API'siyle doğrulandı; metadata tablosu (`nss_metadata.tab`) indirilip dağılımlar yerel olarak hesaplandı.

---

## 🔗 İlgili Bağlantılar
### 🧠 İlgili Kavramlar
- [[concepts/metin-madenciligi.md|Metin Madenciliği ve Hesaplamalı Metin Analizi]]
- [[concepts/olcum-araclari.md|Ölçüm Araçları (Polarization Measurement)]]
