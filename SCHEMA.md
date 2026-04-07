# Wiki Schema

## Domain
**Çocuklar ve Dijital Dünya Araştırma** - Çocukların dijital ortamlardaki deneyimleri, dijital kısıtlamalar, yaş limitleri, çocuk katılımı ve dijital vatandaşlık üzerine akademik ve popüler kaynaklardan derlenmiş bilgi tabanı.

## Conventions
- **Dosya adları:** lowercase, tireler, boşluk yok (örn: dijital-cocuk-haklari.md)
- **Her wiki sayfası YAML frontmatter bloğu ile başlar:**
  ```yaml
  ---
  title: Sayfa Başlığı
  created: YYYY-MM-DD
  updated: YYYY-MM-DD
  type: entity | concept | comparison | query | summary
  tags: [tag1, tag2]
  sources: [raw/articles/kaynak-adı.md]
  ---
  ```
- **[[wikilink]]** kullan - sayfalar arası bağlantılar için
- **Sayfayı güncellediğinde updated tarihini güncelle**
- **Her yeni sayfa index.md'ya eklenmeli**
- **Her işlem log.md'ya kaydedilmeli**

## Entity Pages
Her önemli varlık için bir sayfa (kişi, kurum, platform, politika). İçermeli:
- Genel açıklama / nedir
- Önemli tarihler ve veriler
- Diğer varlıklarla ilişkiler
- Kaynak referansları

## Concept Pages
Her kavram veya konu için bir sayfa. İçermeli:
- Tanım / açıklama
- Mevcut bilgi durumu
- Açık sorular veya tartışmalar
- İlgili kavramlar (wikilink'ler)

## Comparison Pages
Karşılaştırmalı analizler. İçermeli:
- Ne ve neden karşılaştırılıyor
- Karşılaştırma boyutları (tablo formatı tercih edilir)
- Sonuç veya sentez
- Kaynaklar

## Source Summaries
Raw bir kaynak alındığında, kaynak klasöründe bir özet yaz:
raw/articles/kaynak-adı.md (orijinal) için bir wiki companion özet oluştur.

## Research Bulletin Format
**Aylık KURATOR bültenleri için:**
- 10-20+ kaynak (4 akademik + 6+ popüler)
- Her kaynak için 250-300 kelime özet + 250+ kelime Türkiye yorumu
- Konular: (1) Dijital kısıtlamalar, (2) Çocuk katılımı, (3) Dijital deneyimler
- İstatistik tabloları, politik öneriler (kronolojik), glossary

## Tags
- #dijital-haklar - çocukların dijital hakları
- #yas-limitleri - yaş sınırı politikaları
- #katilim - çocuk katılımı ve dijital vatandaşlık
- #turkiye - Türkiye özelinde analizler
- #kuresel - küresel karşılaştırmalar
- #akademik - akademik kaynaklar
- #populer - popüler kaynaklar
