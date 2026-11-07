---
type: concept
title: Sentetik Odak Grupları (AI-Simulated Focus Groups)
description: '## Tanım Partilerin ve kampanya ekiplerinin odak grubu araştırmasını yapay
  zeka destekli simülasyon teknolojileriyle (AEST) yürütmesi; dört teknoloji ailesi,
  belgelenmiş arıza kipleri ve risk/dayanak temelli bir karar matrisi.'
tags:
- kavram
- yapay-zeka
- siyasal-kampanya
- nitel-yontem
- yonetisim
timestamp: '2026-11-07T16:50:00Z'
created: '2026-11-07'
updated: '2026-11-07'
sources:
- raw/articles/2026-11-02_fake-plastic-voters-ai-simulated-focus-groups-in-party.md
confidence: medium
---

# Sentetik Odak Grupları (AI-Simulated Focus Groups)

## Tanım

Siyasal partiler odak gruplarını seçmeni anlamak için kullanır: katılımcıların bir konu hakkında **birlikte nasıl akıl yürüttüğünü**, hangi gerekçelerin işlediğini, hangi dilin "ortak akıl" hâline geldiğini gözlemlemek için. Yapay zeka destekli simülasyon teknolojileri (AI-enhanced simulation technologies, **AEST**) bu araştırmanın bir bölümünü — bazen tamamını — **çok daha hızlı ve ucuza** üretmeyi vaat ediyor. Sentetik odak grubu, bu vaadin kampanya araştırmasındaki karşılığıdır.

## Dört teknoloji ailesi

- **Dijital gölge / dijital ikiz:** gerçek kişilerin veri temelli vekilleri; ikiz, iki yönlü ve gerçek zamanlı veri bağı gerektirdiği için en pahalı ve en mahremiyet-yoğun seçenek.
- **Sentetik popülasyonlar:** nüfusun istatistiksel yapısını koruyan, her bireyi anonim bir ajan olarak üreten yapay nüfuslar; seçmen tabanı kompozisyonunu varyasyonlamak için kullanılır.
- **LLM tabanlı personaslar:** demografik/tutum profilini istemde tarif edip modeli o kişi gibi konuşturmak — **veriye dayanmayan** (ungrounded) katman.
- **Hibrit insan-AI grupları:** insan katılımcılar + AI katılımcı ve/veya AI moderatör; ya da tamamen insan grup + AI destekli transkripsiyon/özetleme.

## Karar matrisi (Novelli vd. 2026)

Literatürdeki en sistemli çerçeve, üç boyutu birleştiren bir **karar matrisi** öneriyor:

| Boyut | Düzeyler |
|---|---|
| **Stratejik amaç** | Mode 1 — anlamın etkileşimde oluşmasını gözlemek; Mode 2 — mesaj/çerçeve varyantlarını hızla test etmek |
| **Kullanım riski** | R0 sandbox · R1 operasyonel · R2 yüksek risk (ücretli medya, hedefleme, saha deneyi) |
| **Ampirik dayanak** | G0 yalnız LLM personası · G1 veriye dayalı · G2 insan kalibrasyonlu · G3 karma grup · G4 insan grup + AI desteği |

Kural özeti: **Mode 1'de simülasyon hiçbir risk düzeyinde insanın yerini alamaz** (G4 zorunlu); **Mode 2'de** dayanak eşiği riskle birlikte yükselir (R0 → G0-G1, R1 → G1-G2, R2 → G2 asgari) ve simülasyon **neyin test edileceğini** söyleyebilir, **neyin kullanılacağını** yetkilendiremez.

## Wiki'deki vaka kaydı

- [[raw/articles/2026-11-02_fake-plastic-voters-ai-simulated-focus-groups.md|Fake Plastic Voters: AI-Simulated Focus Groups (Novelli vd., Journal of Political Marketing, 2026)]] — matrisin tam açılımı, G/R düzeyleri, senaryo ve etik tartışması.

## Arıza kipleri

- **Sycophancy (yalpalamacılık):** modelin kullanıcıyı onaylama eğilimi; görüşmeyi "iyi haber" üretmeye iter.
- **Persona drift:** persona talimatına rağmen modelin varsayılan sesine kayması; karşıt kamplara atanan ajanlar bile modelin ana akım normlarına uyuyor.
- **Azınlık görüşlerinin bastırılması / "ortalama persona" çöküşü:** eğitim verisi ana akım dili ağırlıklandırdığı için sıra dışı, yerel, muhalif ifadeler seyreliyor.
- **Tekrar ve doyma:** oturumlar tekrarlandıkça ifadeler tekrara düşüyor, özgün içgörü havuzu hızla doyuyor.

Bunların hepsi Mode 1'in tam da ihtiyaç duyduğu şeyi — **beliren (emergent) etkileşim** — bozuyor. Mode 2'de ise sınırlı ve karşılaştırmalı görevlerde bu kusurlar daha tolere edilebilir.

## İkinci derece risk: deskilling

Simülasyon saatler içinde sonuç verirken insan odak grubu haftalar alır; seçim baskısı altında ekip hızlı olanı seçer. Bu rutinleşirse partiler **yorumlama zanaatını** kaybeder — kibar onay ile gerçek karşılığı, anlamlı sessizliği ayırt etme yetisi aşınır. Kadroda uzman bulunması işleyen yetkinlik anlamına gelmez: "durakta" duran uzmanlık karar süreçlerine girmez.

## Etik ve yönetişim

- **Rıza:** siyasi görüş araştırmasında AI katılımının açıklanmaması varsayılan olarak kabul edilemez; gecikmeli açıklama ancak istisnai, gerekçeli, bağımsız denetimli ve çözümleme (debriefing) ile olabilir.
- **Mahremiyet:** grounded sistemler (gölge/ikiz, sentetik popülasyon) kişisel ve siyasi görüşü açığa vuran veriyle çalışır; dayanak arttıkça mahremiyet yükü de artar — bu yüzden "daha grounded her zaman daha iyi" değil.
- **Şeffaflık:** simüle bulgular **asla** gerçek kamuoyu araştırması gibi sunulmamalı.
- **Hesap verebilirlik:** dokümantasyon, simülasyonu ısmarlayan ekiple yorumlayan ekibin ayrılması, iç itiraz (challenge) fonksiyonu, yüksek riskli kullanımda dış denetim.
- **Saldırgan kullanım:** rakip taban simülasyonuyla saldırı mesajı tasarlamak, katılımı bastıracak mesaj kalibrasyonu, simüle iterasyonla çerçevesi optimize edilmiş [[concepts/ai-generated-disinformation.md|AI-generated disinformation]] — yazarlar bu üçünü kategorik olarak kabul edilemez ilan ediyor.

## İlgili Varlıklar

- [[entities/www-tandfonline-com.md|Taylor & Francis]]
- [[entities/arxiv-org.md|arXiv]]

## İlgili Kavramlar

- [[concepts/sentetik-populasyonlar.md|Sentetik Popülasyonlar ve Birey-Tabanlı Simülasyon]]
- [[concepts/yapay-zeka-destekli-gorusmeler.md|Yapay Zeka Destekli Görüşmeler (AI Interviewing)]]
- [[concepts/yapay-zeka-yonetisimi.md|Yapay Zeka Yönetişimi]]
- [[concepts/arastirma-sonucu-tahminleme.md|Araştırma Sonucu Tahminleme]]
- [[concepts/siyasal-temsil.md|Siyasal Temsil]]
- [[concepts/ai-generated-disinformation.md|AI-Generated Disinformation]]
