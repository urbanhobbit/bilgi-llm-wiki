---
type: raw_article
title: 'Multi-Agent Ethnography: Post-Conventional Anthropological Practice Through
  Human−AI Collaboration'
description: 'Antropolojide **çok-ajanlı etnografi (MAE)** önerisi: LLM tabanlı ajanlar,
  araştırma yaşam döngüsünün **tamamında** (tasarım, saha, analiz, yayın) dağıtık
  bir insan-AI ağında **yapılandırılabilir işbi...'
resource: https://doi.org/10.1080/00664677.2026.2614501
tags:
- kurator
- high
timestamp: '2026-11-18T17:53:35Z'
source_file: 2026-02-08_multi-agent-ethnography.json
category: KURATOR
priority: high
roles: []
published: '2026-02-08'
---

# Multi-Agent Ethnography: Post-Conventional Anthropological Practice Through Human−AI Collaboration

**Author(s):** Matt Artz (Azimuth Labs; geliştirme Aalborg Üniversitesi Techno-Anthropology Lab'daki doktora çalışması kapsamında)

**Published:** 2026-02-08

**Source:** [https://doi.org/10.1080/00664677.2026.2614501](https://doi.org/10.1080/00664677.2026.2614501)

## Summary

Antropolojide **çok-ajanlı etnografi (MAE)** önerisi: LLM tabanlı ajanlar, araştırma yaşam döngüsünün **tamamında** (tasarım, saha, analiz, yayın) dağıtık bir insan-AI ağında **yapılandırılabilir işbirlikçiler** olarak konumlanıyor. Yazar, MAE'yi antropolojinin yöntemsel yenilik geleneğine (multi-sited → multi-species etnografi) yerleştiriyor ve AI'nın "**siber takım arkadaşı**" (cybernetic teammate, Dell'Acqua vd. 2025) kapasitesine dayanıyor. Argümanın teknik kanıtı: **AI Anthropology Toolkit** — üç ajanı (kod kitabı üretimi, transkript bölütleme, kodlama + tematik analiz) sohbet üzerinden koordine eden bir **MCP sunucusu**. Bu, tek bir araştırmacının normalde bir ekip gerektiren **analitik genişliğe** (birden çok epistemolojik mercekle eşzamanlı karşılaştırma) erişmesini sağlıyor. Yazar sınırları da sayıyor: **veri mahremiyeti, çevresel maliyet, algoritmik yanlılık** — ama arazinin "antropolojik olarak bilgilendirilmiş AI araçlarının kurulabilir, erişilebilir ve etnografik pratiği güçlendirici olduğunu" gösterdiğini söylüyor.

## Key Points

- **Künye:** "Multi-Agent Ethnography: Post-Conventional Anthropological Practice Through Human−AI Collaboration", **Matt Artz** (Azimuth Labs), *Anthropological Forum* **36(2): 222–240**, yayın **8 Şubat 2026**, **72 kaynak**, hakemli. Tam metin **kapalı erişim** (T&F Cloudflare; Unpaywall closed).
- **Erişim:** paylaşılan DOI doğrudan açılmadı; künye **Crossref**, özet **Semantic Scholar** API'sinden alındı. **Tam metin okunmadı** → yöntem bölümü, vaka verisi ve etki iddiaları doğrulanmadı; aşağıdaki teknik ayrıntılar yazarın **kamusal araç dokümantasyonundan** (GitHub/PyPI/mattartz.me) çapraz doğrulandı.
- **Kavramsal çerçeve:** MAE, LLM ajanlarını **araştırma ortağı** olarak konumlar. Dayanak: AI'nın "siber takım arkadaşı" işlevi (Dell'Acqua vd. 2025). İddia: **antropolojik olarak tasarlanmış** ajanlar, insanın ya da AI'nın tek başına ulaştığından daha geniş araştırma kapasitesi üretir.
- **Teknik artefakt — AI Anthropology Toolkit (doğrulandı):** GitHub `MattArtzAnthro/AI-Anthropology-Toolkit` (**27 yıldız, 7 çatal**, oluşturma 2 Ağu 2025, son push **17 Kas 2026**, lisans NOASSERTION); PyPI paketi `ai-anthropology-toolkit` **v3.11.1** (Python ≥3.10); MCP sunucusu `ai-anthro-mcp`; Claude Code / Codex CLI / Gemini CLI'ye `uvx` ile eklenebiliyor.
- **Üç ajan (makale ile araç dokümantasyonu uyumlu):** (1) **Qualitative Codebook Builder** — kaynak literatürden kod kitabı; (2) **Interview Transcript Semantic Chunker** — anlamsal bölütleme + tutarlılık skoru; (3) **Coding and Thematic Analysis** — tümdengelimli/tümevarımlı/hibrit kodlama, çok-mercekli paralel analiz ve mercekler arası karşılaştırma.
- **Yöntemsel yenilik olarak öne çıkan şey:** **epistemolojik mercek (lens) birinci sınıf tasarım parametresi** — duruş (tasarım antropolojisi, yorumlayıcı, hesaplamalı, işletme, STS) kod kitabını ve analizi şekillendiriyor; `--distinct-codes` / `--overlapping-codes` bayrağı, kodların birbirini dışlayıp dışlamadığına dair **yöntemsel taahhüdü** araştırmacıya bırakıyor (varsayılan yok). Bu, "AI ajanı yöntem kararını sessizce verir" eleştirisine karşı tasarımsal bir cevap.
- **Versiyon geçmişi (yazarın sitesi):** V1 bağımsız Jupyter notebook'lar → **V2 MCP ile orkestre edilen ajanlar** → V3 web uygulaması. Zenodo'da arşivli; Aalborg Üniversitesi Techno-Anthropology Lab doktora çalışmasının çıktısı.
- **Yazarın kabul ettiği sınırlar:** veri mahremiyeti, **çevresel maliyet** (LLM çağrıları), **algoritmik yanlılık**. Bunlar makalede "önemli değerlendirmeler" olarak geçiyor ama nasıl ele alındığı (tam metin kapalı olduğu için) doğrulanamadı.
- ⚠️ **Eleştirel notlar:** (1) Makale, kendi aracının **tanıtımı** ile ampirik değerlendirmesi arasındaki çizgiyi netleştirmiyor gibi görünüyor — özet, aracın **yapılabilirliğini** gösteriyor, **araştırma kalitesini** ölçen bir karşılaştırma sunmuyor; (2) "tek araştırmacı ekip genişliğine erişir" iddiası **doğrulanmış bir kazanç** değil, mimari bir imkân; (3) MCP ekosistemi hızla değişiyor — makale Ocak 2026'daki sürümü tanımlıyor, paket şu an 3.11.1 (17 Kas 2026).

## Turkey Context

Türkiye'de nitel araştırma (etnografi, derinlemesine görüşme) ağırlıkla **tek araştırmacı + öğrenci asistan** modeliyle yürüyor ve transkript-kodlama yükü akademik takvimin en büyük darboğazı; MAE tam bu darboğaza oturuyor. Üç bağ: **Birincisi, uygulanabilirlik:** araç **Türkçe transkriptlerde** kodlama için doğrudan kullanılabilir (MCP + LLM); ama kod kitabı ve mercek tanımı Türkçe yapılmadığında kodlar İngilizce literatürün kavramlarına kayar — yerel kavram seti (ör. "mahalle baskısı", "hatır", "gönül") için **mercek tasarımı** şart. **İkincisi, KVKK:** görüşme transkriptleri **özel nitelikli kişisel veri** içerebilir; bulut LLM'e göndermek açık rıza ve veri işleme sözleşmesi gerektirir. Araç yerel model seçeneği sunuyor mu, sunmuyorsa Türkiye'deki kurumsal etik kurullar için **kullanılamaz** — bu, makalenin "veri mahremiyeti" notunun Türkiye'deki en somut karşılığı. **Üçüncüsü, ekip genişliği:** Türkiye'de nitel araştırma fonları küçük; "tek araştırmacı ekip genişliğine erişir" iddiası, TÜBİTAK 1001/3501 projelerinde **asistan bütçesi yerine araç bütçesi** tartışmasını açabilir. Uyarı: makalenin tam metni okunamadı; bu not bir **araç/kavram transferi**, Türkiye'ye dair ampirik iddia değil.

---

## 🔗 İlgili Bağlantılar
### 🧠 İlgili Kavramlar
- [[concepts/cok-ajanli-etnografya.md|Çok-Ajanlı Etnografya]] — makalenin önerdiği yaklaşım
- [[concepts/kuram-operasyonellestirme-llm.md|Kuram Operasyonelleştirme (LLM)]]
- [[concepts/yapay-zeka-destekli-gorusmeler.md|Yapay Zeka Destekli Görüşmeler]]
- [[concepts/metin-madenciligi.md|Metin Madenciliği]]
### 🏛 İlgili Kurum/Kişiler
- [[entities/matt-artz.md|Matt Artz]]
- [[entities/ai-anthropology-toolkit.md|AI Anthropology Toolkit]] — makalenin teknik kanıtı (MCP sunucusu)
