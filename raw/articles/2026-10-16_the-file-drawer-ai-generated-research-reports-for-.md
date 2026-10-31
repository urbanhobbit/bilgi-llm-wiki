---
type: raw_article
title: 'The File Drawer: AI-generated research reports for unpublished studies (filedrawer.org)'
description: Columbia Üniversitesi'nde siyaset bilimci Yamil Velez'in geliştirdiği
  Filedrawer, yayımlanmamış anket deneylerini ('dosya çekmecesi'nde kalan çalışmaları)
  ajan-tabanlı bir iş akışıyla kısa araştırma r...
resource: https://filedrawer.org/
tags:
- kurator
- high
timestamp: '2026-10-31T18:45:53Z'
source_file: 2026-10-16_filedrawer-ai-research-reports.json
category: KURATOR
priority: high
roles:
- method
- policy
published: '2026-10-16'
---

# The File Drawer: AI-generated research reports for unpublished studies (filedrawer.org)

**Author(s):** Yamil Ricardo Velez (Columbia University, siyaset bilimi); fikir: Robb Willer (Stanford)

**Published:** 2026-10-16

**Source:** [https://filedrawer.org/](https://filedrawer.org/)

## Summary

Columbia Üniversitesi'nde siyaset bilimci Yamil Velez'in geliştirdiği Filedrawer, yayımlanmamış anket deneylerini ('dosya çekmecesi'nde kalan çalışmaları) ajan-tabanlı bir iş akışıyla kısa araştırma raporlarına çeviren açık kaynak bir platform. Girdi: Qualtrics dışa aktarımı + QSF anket şeması + ön-analiz planı (PAP). Çıktı: git'e işlenebilir bir 'çalışma paketi' — findings-first yazılmış report.md, düzenlenmiş veri (raw_tidy.csv + clean.csv), 01_tidy.py'den 04_exploratory.py'ye yeniden üretilebilir betikler, sonuç tabloları, pap.json ve her analizin **registered / deviation / exploratory** olarak etiketlenmesi. Raporun asıl ayırt edici iddiası bu: sistem, kayıtlı ön-analiz planı ile uygulanan spesifikasyonu alan alan karşılaştırıp her analizin statüsünü otomatik işaretliyor; keşifsel analizler '(EXPLORATORY — not pre-registered)' etiketiyle ayrılıyor. Ayrıca OpenAlex üzerinden yalnızca gerçekten erişilen literatürü atıflayan kısa bir literatür notu, tasarım diyagramı, hakem mektubu ve araştırma potansiyeli memorandumu üretiyor. provenance/ klasöründe model adları, token kullanımı, maliyet, girdi hash'leri ve tam LLM istek günlüğü tutuluyor; her raporun sayfasında 'tamamen ajan üretimi + otomatik hakem geçişi' mi yoksa 'insan inceledi' mi olduğunu gösteren bir rozet var. Gizlilik mimarisi kayda değer: ham yanıtlayıcı verisi makineden çıkmıyor, modeller yalnızca şema, sütun adları, sınırlı özet profiller ve yerelde üretilmiş toplulaştırılmış tabloları görüyor; data/ dizinine araç erişimi 'yapısal olarak' reddediliyor (prompt talimatıyla değil). İlk katman KİŞİSEL VERİ (PII) taraması yalnızca başlık satırı ve ilk beş veri satırını yerelde okuyup Qualtrics tanımlayıcı listesi, regex'ler ve işe alım platformu kimlikleriyle (Prolific, MTurk, Connect, UUID, IPv4/6) eşleşen sütunları düşürüyor. Site Ekim 2026 itibarıyla altı çalışma paketi barındırıyor (N=446 ile 8.572 arası); beşi tamamen ajan üretimi, biri insan incelemesinden geçmiş; model maliyeti çalışma başına $0,37–$1,41. Proje MIT lisanslı ve Python 3.11+ paketi olarak yayınlanmış; statik pano GitHub Pages'te ya da 256 MB'lık, sıfıra ölçeklenen bir Fly makinesinde çalışıyor. Motivasyon açıkça politik: düşük öncelikli ya da 'slop' çalışmaları zaten tıkanmış dergilerden uzak tutmak, dosya çekmecesini insanlara ve ajanlara açmak (meta-analiz, güç hesabı) ve veri/hat yeniden kullanımını atıfla ödüllendirmek. Raporlar CV'lik değil, replikasyon paketi gibi kamu malı sayılıyor.

## Key Points

- Kim/ne: Yamil R. Velez (Columbia, siyaset bilimi; 'tailored surveys and experiments using Generative AI' çalışma hattı), Robb Willer'ın (Stanford) 'eski veriyi kısa araştırma raporuna çeviren kamuya açık kaynak' fikrinden yola çıkmış. Site filedrawer.org, kod github.com/yrvelez/filedrawer (MIT, filedrawer 0.1.0, Python >=3.11, pandas/statsmodels/scipy bağımlılıkları).
- Girdi/çıktı hattı: Qualtrics dışa aktarımı + QSF şeması + ön-analiz planı → report.md (badge'ler: provenance, hakem kararı, ön-kayıt, sürüm, tasarım, veri, maliyet), tasarım diyagramı, hakem mektubu, araştırma potansiyeli memorandumu, data/raw_tidy.csv + data/clean.csv, scripts/01_tidy.py…04_exploratory.py, results/ tabloları, pap.json, provenance/ (model, token, maliyet, girdi hash'i, tam istek günlüğü).
- Yöntemsel çekirdek: her analiz, kayıtlı PAP ile uygulanan spesifikasyon alan alan karşılaştırılarak registered / deviation / exploratory olarak etiketleniyor; exploratory sonuçlar '(EXPLORATORY — not pre-registered)' ibaresiyle ayrılıyor. llms.txt ajanlara 'keşifsel bir tahmini kayıtlı sonuç gibi sunma' kuralını açıkça yazıyor — bu, otomatik üretilen raporlarda bilinen en büyük riski (etiket kayması) tasarım düzeyinde engelleme girişimi.
- Gizlilik: ham yanıtlayıcı verisi hiçbir modele gitmiyor; modeller yalnızca şema, sütun adları, sınırlı özet profiller (değer sayımları, ortalamalar), PAP metni ve yerelde betiklerle üretilmiş toplulaştırılmış tabloları görüyor. data/ dizinine araç erişimi yapısal olarak reddediliyor. PII taraması Qualtrics tanımlayıcı listesi (IPAddress, RecordedDate, ResponseId, alıcı alanları, konum, panel kimlikleri), regex'ler (e-posta, IP, telefon, coğrafi, doğum tarihi) ve değer düzeyinde işe alım kimlikleriyle (Prolific, MTurk, CloudResearch Connect, UUID, Qualtrics response id, IPv4/IPv6) çalışıyor; --allow-pii ile atlanabiliyor ama provenance'a uyarı yazılıyor ve release --force olmadan reddediyor.
- Sitedeki mevcut paketler (31 Ekim 2026 itibarıyla 6): duygusal kutuplaşmayı azaltmaya yönelik 33 öğrenci tasarımı müdahale (N=4.485, OSF ön-kayıt), bilime güven mesajları (N=8.572, OSF), yapay zeka ürünü medyayı ayırt etme (N=2.030, Aspredicted #151.281, Zenodo DOI 10.5281/zenodo.23166168), chatbot'u ikna ölçüm aracı olarak kullanma (N=446), dezenformasyon paylaşımı üzerine ego-ağ konjointi (N=1.500, Aspredicted #132.508), ANES 2024 duygu termometreleri üzerine 'silicon sampling' testi (N=100, insan inceledi).
- Doğrulama notu (tweet iddiası → gerçek): 'her tahmini sonuçlarla, her analizi PAP ile karşılaştırır' → doğru, pap.json + registered/deviation/exploratory etiketlemesi README ve llms.txt'de belgeli. 'Raporlar DOI alabiliyor' → doğru ama şu an tek bir pakette (Zenodo). 'Veriler GitHub'da, filedrawer.org yalnızca metadata barındırıyor' → doğru. 'Hiçbir birey düzeyi veri filedrawer.org'a ya da modellere ulaşmıyor' → ifade doğru, ancak altı paketin beşi **de-identifiye yanıtlayıcı düzeyi veriyi kamuya açık GitHub deposunda yayımlıyor** (data/clean.csv); gizlilik iddiası model/site sınırıyla ilgili, verinin yayımlanmamasıyla değil.
- Açık kaynak durumu: MIT lisansı (telif 2026 Yamil Velez), kamuya açık README ve llms.txt; ajanlar için makine-okunur rehber ve index.json. Statik pano GitHub Pages veya 256 MB Fly makinesinde (sıfıra ölçekleniyor) çalışıyor — yani barındırma maliyeti marjinal, bu da Velez'in 'birkaç projeyi barındırmayı taahhüt ettim' ifadesini maddi olarak mümkün kılıyor.
- Sınır: hat şu an yalnızca anket deneyleri, konjointler ve yöntem karşılaştırmaları için çalışıyor (Velez'in kendi alanı); gözlemsel, nitel ve saha çalışmaları için katkı çağrısı açık. Beş paket 'tamamen ajan üretimi + otomatik hakem geçişi'; insan incelemesi tek pakette var, yani kalite güvencesi büyük ölçüde otomatik.
- Model maliyeti: çalışma başına $0,37–$1,41 (provenance'ta raporlanıyor). Bu, 'otomatik araştırma raporu' üretiminin marjinal maliyetinin tek haneli doların altına indiğini gösteren somut bir veri noktası — dosya çekmecesi sorununun ölçeklenebilirliği açısından asıl haber bu.

## Turkey Context

Türkiye'de dosya çekmecesi sorunu akademik teşvik sistemiyle daha da derin: yayın sayısı, dergi indeksi ve atıf üzerinden işleyen teşvik/yükseltme rejimi, sonucu 'anlamlı' çıkmayan çalışmayı yayımlamayı değil rafa kaldırmayı ödüllendiriyor; ön-kayıt (OSF, AsPredicted) kültürü ise psikoloji ve siyaset biliminde hâlâ istisna. Filedrawer'ın önerisi bu boşluğa doğrudan oturuyor: eğer yayımlanmamış anket deneyleri DOI alabilen, atıf alabilen, verisi ve betiği açık 'çalışma paketleri'ne dönüşebilirse, Türkiye'deki araştırma fonlarının (TÜBİTAK 1001/3501, üniversite BAP'ları) ürettiği ama hiçbir yere gitmeyen veri görünür hale gelebilir. İkinci ve daha acil konu KVKK: Türkiye'de anket verisi neredeyse her zaman kişisel veri içeriyor (telefon, e-posta, IP, açık uçlu yanıt), ve araştırmacıların çoğu de-identifikasyonu elle yapıyor. Filedrawer'ın 'PII taraması yalnızca başlık + ilk beş satırı yerelde okur, modeller veriyi hiç görmez' mimarisi, KVKK uyumlu bir 'veri paylaşmadan rapor üretme' hattı için pratik bir şablon; özellikle bulut tabanlı LLM kullanmak isteyen ama kurum etik kurulundan izin alamayan ekipler için. Üçüncüsü, yerel model seçeneği: platform OpenRouter üzerinden ticari modeller ya da yerel açık ağırlıklı modellerle çalışabildiği için, verinin yurt dışına çıkmaması gereken kurumlarda (kamu üniversiteleri, TÜBİTAK projeleri) yerel modellerle (ör. Trendyol-LLM, Cosmos, Kumru ailesi) kurulabilir — maliyet $1 mertebesinde kaldığı için bu artık altyapı değil yapılandırma meselesi. Dördüncüsü, metodolojik risk: otomatik üretilen raporlar Türkiye'de 'yayın' sayılır mı, intihal taramasından geçer mi, hakemlik değeri taşır mı? Filedrawer'ın cevabı raporu CV'lik değil 'replikasyon paketi gibi kamu malı' saymak; Türkiye'de ise teşvik rejimi tam tersini ödüllendirdiği için bu modelin kurumsal karşılığı henüz yok. Son not: proje şu an yalnızca anket deneyi/konjoint hattını destekliyor; Türkiye'de yaygın olan saha deneyi ve nitel çalışma formatları için henüz kapsam dışı — Velez'in katkı çağrısı tam olarak bu boşluğa işaret ediyor.

## 🏷 Retorik Roller

- 🧩 **Yöntem**
- 🏛 **Politika Önerisi**
