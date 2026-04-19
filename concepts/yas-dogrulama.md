---
title: Yaş Doğrulama Teknolojileri
created: 2026-04-11
updated: 2026-04-11
type: concept
tags: [yas-limitleri, kavram, kuresel]
sources: [raw/articles/2026-03-13_cocuk_dijital.md, raw/articles/2026-03-17_cocuk_dijital.md]
---

# Yaş Doğrulama Teknolojileri

## Tanım
Kullanıcıların belirli bir yaşın üzerinde olduğunu doğrulamak için platformlar tarafından kullanılan teknik yöntemler. "Yaş güvencesi" (age assurance) de denir; sadece sormaktan (self-declaration) biyometrik doğrulamaya kadar geniş bir yelpaze.

## Yöntemler (Kapsayıcılık Sırasıyla)

| Yöntem | Açıklama | Gizlilik Riski |
|--------|----------|---------------|
| Self-declaration | "Kaç yaşındasınız?" | Çok düşük | Çok kolay atlatılır |
| Kredi kartı | Ödeme araçlarıyla yaş çıkarımı | Orta | Paylaşılabilir |
| Kimlik belgesi | Resmi ID yükleme | Yüksek | Merkezi veri riski |
| Yüz yaşı tahmini | Kameradan yaş tahmini (facial age assurance) | Yüksek | Biyometrik veri |
| Veri çıkarımı | Mevcut davranış verilerinden yaş tahmini | Orta | Algoritmik önyargı |

## Avustralya Modeli (2025-2026)
Avustralya "makul adımlar" prensibi kapsamında **katmanlı** bir yaklaşım benimsedi:

**Temel kurallar:**
- Hükümet kimliği tek yöntem olamaz; kullanıcıya seçenek sunulmalı
- Salt self-declaration yeterli değil
- k-ID gibi özel yaş doğrulama servisleri yetkilendirildi
- Bireysel veriler saklanamaz; "sistem ve süreçlere odaklanan" kayıtlar tutulacak

**İlk günlerdeki sorunlar:**
- Bazı 14-15 yaşındaki kullanıcılar yüz tanıma testlerini geçebildi
- Bazı 16+ kullanıcılar yanlışlıkla engellendi (özellikle Snapchat)
- Ebeveynlerin çocuklarına VPN ve atlatma yöntemlerini öğrettiği vakalar

**Temel gerilim:**
- Etkili yaş doğrulama → daha fazla kişisel veri toplama
- Daha az veri → daha kolay atlatılabilir sistem

## Gizlilik Çerçevesi
- Platformların bireysel yaş kontrollerinden **kişisel veri saklamaması** bekleniyor
- AB GDPR ve UK GDPR'a göre biyometrik veri özel kategori; yaşa göre onay şartları farklı
- "Veri minimizasyonu" ilkesiyle uyumsuzluk potansiyeli

## Açık Sorular
- Mevcut teknolojilerle gizlilik ve doğruluk nasıl dengelenir?
- Çocukların yaş doğrulamayı aşmak için biyometrik verileri manipüle etmesi önlenebilir mi?
- Küresel tutarsız standartlar cross-border uyumu zorlaştırıyor

## İlgili Kavramlar
- [[concepts/sosyal-medya-yasagi-tartismasi.md]]
- [[concepts/dijital-haklar.md]]

## İlgili Varlıklar
- [[entities/esafety-commissioner.md]]
- [[entities/btk.md]]
