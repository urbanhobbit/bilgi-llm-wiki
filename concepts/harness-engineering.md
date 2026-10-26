---
type: concept
title: Harness Engineering (Agent Harness Mühendisliği)
description: 'Bir dil modelini ajan yapan çalışma zamanı katmanının (döngü, araçlar, bağlam yönetimi, durum, izinler, doğrulama) tasarımı; 2026 başında adlandırılan disiplin.'
tags:
- kavram
- yapay-zeka
- ajanlar
- yazilim-muhendisligi
timestamp: '2026-10-25T00:00:00Z'
created: 2026-10-25
updated: 2026-10-25
sources:
- raw/articles/2026-10-04_understanding-harness-engineering-48-page-handbook.md
confidence: medium
---

# Harness Engineering (Agent Harness Mühendisliği)

**Ajan = model + harness.** Harness engineering, bir dil modelini dünyaya bağlayan çalışma zamanının — döngü, araç arayüzleri, bağlam yönetimi, güvenlik kontrolleri, orkestrasyon ve genişleme yüzeyleri — tasarımı ve evrimidir. Disiplin 2026 başında adlandırıldı; literatürdeki en kapsamlı ampirik temel, on bir üretim kodlama harness'ının kaynak-kodu anatomisini çıkaran arXiv:2609.00006'dır (Barbaste, Darrigol, Vu, Wiltberger).

## Neden model seçiminden bağımsız bir katman

Aynı modelle çalışan iki ajan farklı davranır, çünkü fark modelde değil harness'tadır:

| Karar | Etkisi |
|---|---|
| **Bağlam politikası** | Modelin ne gördüğü; uzun görevlerde hangi bilginin yaşadığı (aktif bağlam vs kalıcı durum, compaction) |
| **Araç tasarımı** | Modelin eyleme geçmesinin ne kadar kolay olduğu (ACI — Agent–Computer Interface) |
| **Yürütme ortamı** | Sandbox ve izin sınırları: üretilen kodun neye erişebildiği |
| **Durum ve toparlanma** | İş tek bir süreç/bağlam penceresinden uzun sürdüğünde devamlılık |
| **Hata ve yeniden deneme** | Dış yan etki üreten araçlarda retry riski; idempotency |
| **Doğrulama** | Görevin gerçekten başarıldığının nasıl anlaşılacağı (evaluator loops, testler) |
| **Bütçe ve durma koşulu** | Kaç adım/ne kadar maliyet sonrası durulacağı |
| **Gözlemlenebilirlik** | Hatanın nerede oluştuğunun izlenebilmesi |

## Ampirik bulgular (arXiv:2609.00006)

- On bir üretim harness'ı inceleniyor: Claude Code, Codex CLI, Gemini CLI, Mistral Vibe, OpenHands, Aider, Mini-SWE-Agent, Hermes, Pi, OpenCode, OpenClaw (+ meta-harness Omnigent).
- Yedi kanonik alt sistem, her biri için minimal ve maksimal uygulama; 13 kesişen gözlem, 29 tekrar eden tasarım deseni, 18 tasarım önerisi ve 90 satırlık minimum uygulanabilir harness iskeleti.
- **İki yokluk** (~4 milyon satır Python/TypeScript/Rust): hiçbir ajan çalışma zamanı genel amaçlı bir ajan çerçevesi (agentic framework) içe aktarmıyor ve hiçbiri kodu vektör gömme ile getirmiyor — alan elle yazılmış async döngüler ve deterministik erişimle çalışıyor.
- **skills**, MCP'den daha hızlı yayılmış (9/11 vs 8/11); ACP altı sistemde ve yeni bir rolle: harness hosting.
- Çeyrek dönemlik yeniden sabitleme (re-pinning) ile boylamsal örneklem: yakınsama taklitçiliğe dönüşüyor, davranış politikası prompt metninden konfigürasyona kayıyor.

## Practitioner katmanı ve dikkat notu

2026'da "harness" çevresinde hızla çoğalan bir practitioner literatürü oluştu: @techNmak'in 48 sayfalık *Understanding Harness Engineering* el kitabı, Gilsiley Henrique Darú'nun 127 sayfalık açık "yaşayan kitabı" (v0.78.0, Zenodo 10.5281/zenodo.21632412) ve ticari rehberler. Bu içerik hızlı eskiyor, hakem değerlendirmesinden geçmiyor ve pazarlama diliyle iç içe; bu yüzden **standart değil, kontrol listesi taslağı** olarak okunmalı, doğrulama/değerlendirme bölümleri kişinin kendi testleriyle yeniden kurulmalıdır.

## İlgili Kavramlar

- [[concepts/yapay-zeka-yonetisimi.md|Yapay Zeka Yönetişimi]]
- [[concepts/yapay-zeka-destekli-gorusmeler.md|Yapay Zeka Destekli Görüşmeler (AI Interviewing)]]
- [[concepts/sentetik-populasyonlar.md|Sentetik Popülasyonlar]]

## İlgili Kaynaklar

- [[raw/articles/2026-10-04_understanding-harness-engineering-48-page-handbook.md|Understanding Harness Engineering (@techNmak, 48 sayfa, 2026)]] — practitioner el kitabı; PDF erişilemedi, kapsam yazarın thread'inden doğrulandı.
