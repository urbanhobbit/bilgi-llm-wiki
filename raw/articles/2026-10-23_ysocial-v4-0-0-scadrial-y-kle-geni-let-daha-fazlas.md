---
type: raw_article
title: 'YSocial v4.0.0 (Scadrial): yükle, genişlet, daha fazlasını simüle et'
description: 'LLM tabanlı ajanlarla sosyal medya simülasyonu yapan açık kaynak YSocial
  platformunun 4.0.0 sürümü (kod adı *Scadrial*). Sürümün ana iddiası, sorulan soruya
  doğrudan cevap vermesi: **"Aynı deney, fark...'
resource: https://y-not.social/blog/2026/ysocial-4/
tags:
- akademik
- medium
timestamp: '2026-10-28T17:52:59Z'
source_file: 2026-10-28_batch-user-links-1-ysocial.json
category: AKADEMİK ÖZEL
priority: medium
roles:
- method
published: '2026-10-23'
---

# YSocial v4.0.0 (Scadrial): yükle, genişlet, daha fazlasını simüle et

**Author(s):** YSocial ekibi — Giulio Rossetti vd. (CNR-ISTI, Pisa)

**Published:** 2026-10-23

**Source:** [https://y-not.social/blog/2026/ysocial-4/](https://y-not.social/blog/2026/ysocial-4/)

## Summary

LLM tabanlı ajanlarla sosyal medya simülasyonu yapan açık kaynak YSocial platformunun 4.0.0 sürümü (kod adı *Scadrial*). Sürümün ana iddiası, sorulan soruya doğrudan cevap vermesi: **"Aynı deney, farklı platform tasarımı — insanların söylediklerini ne kadar değiştiriyor?"** v4 ile birlikte YSocial üç ayrı platform dilini simüle ediyor: hızlı ve gürültülü **mikroblog**, konu başlıkları etrafında örgütlenen **forum** ve yeni eklenen **fotoğraf paylaşımı** (Instagram benzeri; ajanlar akışı kaydırıyor, hikâye izliyor, beğeni/yorum yapıyor, DM atıyor, hatta paylaştıkları görselleri üretiyor). Aynı ajanlar, aynı deney iş akışı, üç farklı ortam: hangisinde görüşler daha hızlı kutuplaşıyor, topluluklar nerede oluşuyor, dikkati ne çekiyor — yan yana karşılaştırma mümkün.

Kurulum tarafında ürünleşme adımı: tek tıkla masaüstü kurulum (macOS Apple silicon/Intel, Windows, Linux x64/arm64), ayrıca pip wheel, Docker imajı ve kaynak kod; her sürümde SHA256SUMS. Kurulum kendi özel Python ortamını hazırlıyor, veri tek klasörde toplandığı için yedekleme/taşıma tek kopya.

Mimari tercih "küçük çekirdek + eklenti ekosistemi": yönetim panelinden resmî ve topluluk eklentileri GitHub sürümünden ya da branch'ten kuruluyor, çekirdekten bağımsız güncelleniyor. Ajanlara **hafıza** eklendi — kime ne söylediğini, hangi başlıkları izlediğini, hangi topluluğa ait olduğunu turlar boyunca hatırlıyor, ilişkiler birikiyor; **moderatör** gibi özel rol ajanları ve koşular arasında insan katılımcılara yanıt veren **reaktif ajanlar** hibrit simülasyonları canlı tutuyor. Arayüz ve LLM istemleri İngilizce + İtalyanca; istem paketleri deney bazında seçildiği için diller arası karşılaştırma yapılabiliyor.

Araştırma tarafı: deneyler oluşturulup klonlanabiliyor, dışa aktarılıp yeniden başlatılabiliyor; günlükler, ilerleme ve görüş evrimi tek tıkla izleniyor; ajanlarla sosyal arayüz üzerinden görüşme/sohbet yapılabiliyor; analiz için gömülü Jupyter Lab ve ySights kütüphanesi, şema gezgini ile SQL/pandas erişimi var. Telemetri anonim ve kapatılabilir. Fotoğraf paylaşımı büyük simülasyonlar için Ray çalışma zamanı üzerinde koşuyor.

## Key Points

- Üç platform tek laboratuvarda: mikroblog, forum, fotoğraf paylaşımı — tasarım etkisini karşılaştırmalı test etme
- Tek tıkla kurulum + pip/Docker/kaynak; eklenti kayıt defteri (çekirdekten bağımsız güncelleme)
- Ajan hafızası, moderatör ve reaktif (insanla hibrit) ajanlar
- Arayüz + istemler İngilizce/İtalyanca, deney bazında istem paketi
- Araştırma altyapısı: klonla/dışa aktar/yeniden başlat, Jupyter Lab, ySights, SQL/pandas şema erişimi

## Turkey Context

YSocial, Türkiye'de kutuplaşma ve dezenformasyon araştırmalarının en zayıf halkasını — **nedensel iddia kurma** — dolaylı olarak güçlendiren bir araç. Anket verisi korelasyon veriyor, X/Twitter verisi davranışsal iz bırakıyor ama müdahale edilemiyor; simülasyon ise platform tasarımını (algoritmik sıralama, forum mu mikroblog mu, görsel mi metin mi) kontrollü biçimde değiştirip görüş dinamiklerini izlemeye imkân tanıyor. Türkiye özelinde üç soru bu platformda test edilebilir: (1) kapalı/forum tipi alanlar (Ekşi benzeri) ile açık mikroblog alanları arasında kutuplaşma hızı farklı mı; (2) görsel içerik ağırlıklı platformlarda duygusal kutuplaşma daha mı hızlı birikiyor; (3) moderasyon müdahalesi (moderatör ajanı) hangi tasarımda daha etkili.

Pratik katkı fırsatı: v4 istem paketlerini dil bazında seçiyor ama yalnızca İngilizce ve İtalyanca var. **Türkçe istem paketi** yazmak (kültürel olarak yüklü konular, Türkçe kısaltma/argo, yerel siyasal kimlikler) hem topluluğa somut bir katkı hem de Türkiye'de karşılaştırmalı bir deney hattı kurmanın en ucuz yolu. Lisansüstü yöntem derslerinde de kullanılabilir: öğrenci, bir kutuplaşma hipotezini önce simülasyonda kurup sonra anket verisiyle karşılaştırdığında "model nedir, veri neyi sınar" ayrımını somut olarak öğreniyor.

Uyarı: LLM ajanları insan değil; simülasyon sonuçları **mekanizma keşfi** için değerli, ama doğrudan insan davranışı tahmini olarak okunmamalı. Türkiye'de bulgu raporlarken "simülasyonda gözlendi" ile "sahada gözlendi" ayrımını korumak şart; KURATOR hattında bu tür çıktıları "sentetik kanıt" olarak etiketlemek, bültenlerdeki kanıt hiyerarşisini korur.

## 🏷 Retorik Roller

- 🧩 **Yöntem**
