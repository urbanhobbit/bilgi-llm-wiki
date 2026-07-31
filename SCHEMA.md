# Wiki Schema

**Last updated:** 2026-07-23

---

## Domain

**KURATOR Araştırma Veritabanı** — Kutuplaşma, popülizm, dezenformasyon, dijital çocuk hakları, AI yönetişimi ve demokrasi üzerine disiplinlerarası akademik kaynaklar. KURATOR pipeline'ı (processed_links → OKF → bundle → viz) ile beslenir.

Alt alanlar:
- **Kutuplaşma:** Duygusal/affektif, ideolojik, sosyal, partizan kutuplaşma
- **Popülizm & Demokrasi:** Popülist iktidarlar, demokratik erozyon, müzakereci demokrasi
- **Dezenformasyon:** Komplo inançları, yanlış bilgi, medya okuryazarlığı, prebunking
- **Çocuk & Dijital:** Sosyal medya yasakları, yaş doğrulama, çocuk hakları, ekran süresi
- **AI & Toplum:** Generative AI, yapay zeka etiği, AI yönetişimi, demokrasi-AI kesişimi

---

## Conventions

- **Dosya adları:** lowercase, tireler, boşluk yok (örn. `affective-polarization.md`)
- **Her sayfa YAML frontmatter ile başlar** (şablon aşağıda)
- **`wikilink`** kullan — her sayfada minimum 2 outbound wikilink
- **Her işlem `log.md`'ye kaydedilir**
- **Her yeni sayfa `index.md`'ye eklenir** (doğru seksiyon altında, alfabetik)
- **Provenance marker:** 3+ kaynaktan sentezlenen sayfalarda, paragraf sonuna `^[raw/articles/kaynak.md]` eklenir
- **Güncelleme:** Bir sayfa güncellendiğinde `updated` tarihi frontmatter'da güncellenir

---

## Frontmatter Templates

### raw/articles/ (Ham Makale)

```yaml
---
type: raw_article
title: 'Makale Başlığı'
description: 'Kısa özet (1-2 cümle)'
resource: 'Orijinal URL'
tags:
- kurator
- high
timestamp: 'YYYY-MM-DDTHH:MM:SSZ'
source_file: processed_links/xxx.json
category: KURATOR | GENEL | AKADEMIK ÖZEL
priority: high | medium | low
published: 'YYYY-MM-DD'
---
```

### concepts/ (Kavram Sayfası)

```yaml
---
type: concept
title: 'Kavram Adı'
description: 'Tanım ve önem açıklaması'
tags: [tag-taxonomy'den]
timestamp: 'YYYY-MM-DDTHH:MM:SSZ'
created: YYYY-MM-DD
updated: YYYY-MM-DD
sources: [raw/articles/kaynak-1.md, raw/articles/kaynak-2.md]
related: [ilgili-kavram]
confidence: high | medium | low          # optional — ne kadar sağlam kanıtlı
contested: true                           # optional — çelişkili kaynaklar varsa
contradictions: [diger-sayfa]             # optional — hangi sayfayla çelişiyor
---
```

### entities/ (Kurum/Kişi/Yayıncı Sayfası)

```yaml
---
type: entity
title: 'Kurum Adı'
description: 'Kısa tanıtım'
resource: 'Kurum ana URL\'si'
tags: [tag-taxonomy'den]
timestamp: 'YYYY-MM-DDTHH:MM:SSZ'
created: YYYY-MM-DD
updated: YYYY-MM-DD
---
```

---

## Tag Taxonomy

### Kategori Etiketleri (amaç)
| Etiket | Kullanım | Açıklama |
|--------|----------|----------|
| `kurator` | Tüm makaleler | KURATOR pipeline'dan gelen kaynak |
| `kavram` | concepts/ sayfaları | Kavramsal/kategorik sayfa |
| `yuksek-oncelik` | Yüksek öncelikli kaynaklar | Kritik bulgu |

### Araştırma Alanı Etiketleri
| Etiket | Kullanım |
|--------|----------|
| `kutuplasma` | Kutuplaşma (affektif, ideolojik, sosyal) |
| `populizm` | Popülizm, demokratik erozyon |
| `dezenformasyon` | Yanlış bilgi, komplo inançları, medya okuryazarlığı |
| `cocuk-dijital` | Çocuklar, sosyal medya, ekran süresi |
| `ai-toplum` | Yapay zeka etiği, AI yönetişimi, demokrasi |
| `sosyal-medya` | Platformlar, algoritmalar, regülasyon |
| `dijital-haklar` | Veri gizliliği, çocuk hakları, dijital vatandaşlık |
| `siyasal-siddet` | Terörizm, radikalleşme, şiddet |
| `turkiye` | Türkiye bağlamı |
| `kuresel` | Küresel/kıtalararası perspektif |
| `akademik` | Akademik dergi makalesi |
| `metodoloji` | Yöntem, ölçüm araçları, veri |

### Kaynak/Entity Etiketleri
| Etiket | Kullanım |
|--------|----------|
| `yayinci` | Akademik yayıncı / dergi |
| `kamu-kurumu` | Devlet kurumu / düzenleyici |
| `sivil-toplum` | STK / think tank |
| `universite` | Üniversite / araştırma merkezi |
| `kisi` | Araştırmacı / yazar |
| `haber-kaynagi` | Medya kuruluşu |
| `edmo-hub` | EDMO merkezi |

**Kural:** Her etiket bu taxonomide tanımlı olmalı. Yeni etiket önce buraya eklenmeli.

---

## Page Thresholds

| Durum | Ne yapılır? |
|-------|-------------|
| Bir kavram/konu **2+ kaynakta** geçiyor | concepts/ sayfası oluştur |
| Bir kaynak makalesi **merkezi bir kavram** hakkında | concepts/ sayfası oluştur |
| Bir kurum/kişi **2+ kaynakta** geçiyor | entities/ sayfası oluştur |
| Bir konu hakkında **derin sentez** yapıldı | queries/ sayfası oluştur |
| **2+ kavram karşılaştırması** | comparisons/ sayfası oluştur |
| Sadece geçerken bahsedilen bir şey | **sayfa oluşturma** — mevcut sayfaya ekle |
| Sayfa **~200 satırı** geçti | Alt konulara böl, çapraz bağlantı ver |
| Bir sayfanın içeriği **tamamen eskidi** | `_archive/` içine taşı, index'ten çıkar |

---

## Update Policy (Çelişki Yönetimi)

Yeni bilgi mevcut içerikle çeliştiğinde:

1. **Tarihleri kontrol et** — yeni kaynak genelde eskiyi günceller
2. **Gerçekten çelişiyorsa**, her iki pozisyonu da **tarih + kaynakla** not et
3. Frontmatter'a işaretle: `contested: true`, `contradictions: [sayfa-adi]`
4. Çelişkiyi lint raporunda kullanıcıya bildir (otomatik düzeltme yapma)

---

## Confidence & Quality Signals

- **`confidence: high`** — 3+ bağımsız kaynak, güçlü ampirik destek
- **`confidence: medium`** — 1-2 kaynak, makul destek
- **`confidence: low`** — tek kaynak, zayıf kanıt, spekülatif
- **`contested: true`** — sayfada çelişkili iddialar var
- **Zorunlu değil** ama hızlı gelişen/kanaate dayalı konularda önerilir

---

## Directory Structure

```
bilgi-llm-wiki/
├── SCHEMA.md              # Bu dosya (kurallar, yapı)
├── index.md               # Tüm sayfaların listesi (katalog)
├── log.md                 # Kronolojik işlem kaydı
├── raw/articles/          # Katman 1: Değişmez kaynak makaleler
├── concepts/              # Katman 2: Kavram sayfaları
├── entities/              # Katman 2: Kurum/kişi/yayıncı sayfaları
├── queries/               # (Gelecek) Kaydedilmiş sorgu sonuçları
├── comparisons/           # (Gelecek) Yan yana karşılaştırmalar
├── okf-bundle/            # OKF formatında bundle (otomatik)
└── _archive/              # (Gelecek) Arşivlenmiş sayfalar
```
