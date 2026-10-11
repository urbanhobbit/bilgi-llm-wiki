---
type: raw_article
title: 'Agentic Knowledge Graphs Kursu: Viral X İddiasının Doğrulaması (DeepLearning.AI
  / Neo4j / Google ADK)'
description: '10 Ekim 2026 tarihli viral X paylaşımı (@Grow_withAI / Ryan Carter,
  103 bin takipçi, ~12,5 bin görüntüleme, 231 beğeni): ''Andrew Ng, sıfırdan Agentic
  Knowledge Graphs kurmayı öğreten 1 saatlik bir kur...'
resource: https://www.deeplearning.ai/courses/agentic-knowledge-graph-construction
tags:
- kurator
- medium
timestamp: '2026-10-11T05:39:32Z'
source_file: 2026-10-11_agentic-knowledge-graphs-claim-check.json
category: KURATOR
priority: medium
roles: []
published: '2026-10-10'
---

# Agentic Knowledge Graphs Kursu: Viral X İddiasının Doğrulaması (DeepLearning.AI / Neo4j / Google ADK)

**Author(s):** Ryan Carter (@Grow_withAI); kurs: Andreas Kollegger (Neo4j)

**Published:** 2026-10-10

**Source:** [https://www.deeplearning.ai/courses/agentic-knowledge-graph-construction](https://www.deeplearning.ai/courses/agentic-knowledge-graph-construction)

## Summary

10 Ekim 2026 tarihli viral X paylaşımı (@Grow_withAI / Ryan Carter, 103 bin takipçi, ~12,5 bin görüntüleme, 231 beğeni): 'Andrew Ng, sıfırdan Agentic Knowledge Graphs kurmayı öğreten 1 saatlik bir kurs yayımladı' iddiası. Paylaşım, bölüm zaman damgalarıyla (00:00 giriş, 03:07 agentik grafikler, 14:00 çok-ajanlı mimari, 23:00 Google ADK ile uygulama, 1:06:03 neden önemli) tweet'e eklenmiş 64:46'lık (3885 sn) bir videoyu tanıtıyor ve tezi şu şemada özetliyor: Prompts → Agents → Loops → Graphs; 'aynı modeller, aynı token'lar, daha iyi mimari'. DOĞRULAMA (kaynak: DeepLearning.AI kurs sayfası, 11 Ekim 2026'da doğrudan çekildi): bahsedilen kurs mevcut ama iddiadaki künye yanlış. (1) Kursun adı 'Agentic Knowledge Graph Construction', eğitmeni Andrew Ng değil Andreas Kollegger (Neo4j'de GenAI İnovasyon lideri); (2) süre 1 saat değil 3 saat 8 dakika (12 video ders, 8 kod örneği, 1 değerlendirme sınavı), güncelleme 17 Temmuz 2026, platform beta süresince ücretsiz; (3) kurs Google'ın ürünü değil, çok-ajanlı sistemi Google'ın Agent Development Kit (ADK) ile kuruyor ve grafiği Neo4j'e yazıyor; (4) kursun içeriği aslında 'ajan grafiği' (agent orchestration) değil 'bilgi grafiği' (knowledge graph: varlıklar + ilişkiler) inşası — yapılandırılmış veri (CSV: ürün/parça/tedarikçi) ile yapılandırılmamış veriden (ürün yorumları) şema öneren alt-ajanlar ve bunların birleştirilmesi. Tweet'in bölüm listesi de kurs müfredatıyla örtüşmüyor (kurs 12 derslik; tweet'te 1:06:03'te 'neden önemli' bölümü var, kursta karşılığı yok); süreler tweet'te 1 saat, aynı hafta dolaşan diğer kopyalarda 2 saat ve 2:22:31 olarak geçiyor. (5) Andrew Ng bağlantısı platform sahipliğinden geliyor: Ng DeepLearning.AI'nin kurucusu ve kendi verdiği ayrı bir kursu var — 'Knowledge Graphs for AI Agent API Discovery'. Dolayısıyla paylaşım, gerçek bir kursu 'ünlü künye' (Ng/Google) ve tutarsız sürelerle yeniden paketleyen viral şablonun 2026 Ekim dalgasına ait; hiçbir paylaşım orijinal kurs sayfasına link vermiyor. ALTTAKİ GERÇEK TEKNİK KAYMA: Google'ın ADK'si 1.0'da (I/O 2025) üç şablon iş akışı ajanı sunuyordu — sequential, loop, parallel; ADK 2.0 (2026) dokümantasyonu bu şablonların 'superseded' olduğunu söyleyip grafik-tabanlı (graph-based) ve dinamik iş akışlarına geçiyor: düğümler fonksiyon olarak çağrılıyor, yönlendirme mantığı sabit şablon yerine tam programlama diliyle yazılıyor; A2A protokolü (v0.2) farklı ekiplerin grafikleri arasındaki kenar/arayüz katmanı. Yani 2026'nın 'graph engineering' söylemi, Google'ın kendi çerçevesinde döngü (loop) primitifinin yetersiz kalması ve yerini grafik çalışma zamanına bırakmasıyla eşzamanlı. Dürüst çekinceler: 'graph engineering' Google'ın kullandığı bir ürün/ders/disiplin adı DEĞİL (terim Temmuz 2026 X tartışmasından çıktı) ve ADK tek uygulama değil — LangGraph ile AutoGen GraphFlow aynı şekle daha önce ulaşmıştı.

## Key Points

- Viral iddia (@Grow_withAI, 10 Ekim 2026): 'Andrew Ng sıfırdan Agentic Knowledge Graphs için 1 saatlik kurs yayımladı' + 64:46'lık video; tez: Prompts → Agents → Loops → Graphs
- Kurs GERÇEK ama künye YANLIŞ: 'Agentic Knowledge Graph Construction' — eğitmen Andreas Kollegger (Neo4j GenAI İnovasyon lideri), Andrew Ng değil
- Süre 1 saat değil 3 saat 8 dakika; 12 video ders, 8 kod örneği, 1 sınav; 17 Temmuz 2026 güncellemesi; platform beta süresince ücretsiz
- Kurs Google'ın ürünü değil: çok-ajanlı sistem Google ADK ile kuruluyor, grafik Neo4j'e yazılıyor (CSV + ürün yorumlarından düğüm/kenar şeması öneren alt-ajanlar)
- İçerik 'ajan grafiği' değil 'bilgi grafiği' (GraphRAG hattı): varlık + ilişki modellemesi; agent orchestration ile karıştırılmamalı
- Süre tutarsızlığı viral şablonun imzası: aynı hafta 1 saat / 2 saat / 2:22:31 versiyonları dolaştı ve hiçbiri orijinal kurs sayfasına link vermiyor
- Andrew Ng bağlantısı platform sahipliğinden: DeepLearning.AI kurucusu; kendi verdiği ayrı kurs 'Knowledge Graphs for AI Agent API Discovery'
- Gerçek teknik kayma: ADK 1.0'ın sequential/loop/parallel şablonları ADK 2.0'da 'superseded' — yerine grafik-tabanlı + dinamik iş akışları, düğümler fonksiyon, yönlendirme kod; A2A (v0.2) grafikler arası kenar katmanı
- 'Graph engineering' Google'ın kullandığı bir ad değil (terim Temmuz 2026 X söyleminden); LangGraph ve AutoGen GraphFlow aynı şekle daha önce ulaşmıştı

## Turkey Context

1) Dezenformasyon analizi için doğrudan ders: aynı hafta içinde aynı 'gerçek' kurs 1 saat, 2 saat ve 2:22:31 süreleriyle dolaştırıldı ve hiçbir paylaşım orijinal kurs sayfasına bağlantı vermedi — Türkiye'de yapay zeka içerik ekosisteminde (X, LinkedIn, YouTube kısa videoları) sık görülen 'ünlü künye + link'siz iddia' kalıbının ölçülebilir bir örneği. KURATOR hattı için iki çıkarım: (a) kaynak doğrulama ruti­ni (süre/künye/link üçlüsü) paylaşımın kendisini test etmek için yeterli; (b) 'Google/Ng yayımladı' gibi kurumsal künye, içeriğin yayılımını içerikten bağımsız artırıyor — bu, dezenformasyon literatüründeki 'provenance hijacking' mekanizmasının ticari AI eğitimi alanındaki karşılığı. 2) Türkiye'de yapay zeka eğitimi ve kurumsal yetkinlik: tam zamanlı 3 saatlik, kod örnekli ve sınavlı bir kurs ile 1 saatlik 'özet video' aynı ürünmüş gibi sunuluyor; kamu/üniversite/özel sektör AI eğitim programları (YTK, TEKNOFEST, üniversite sertifika programları) içerik seçerken bu ayrımı yapmalı — bilgi grafiği (veri/RAG hattı) ile ajan grafiği (orkestrasyon hattı) farklı mühendislik becerileri. 3) Yönetişim açısından: ADK 2.0'ın 'sabit şablon yerine kod olarak yönlendirme' (dynamic workflows) ve A2A protokolü, kurumsal ajan sistemlerinde denetlenebilirlik sorusunu büyütüyor — Türkiye'de kamu kurumlarında ajan tabanlı otomasyon yaygınlaşırsa, 'grafik yapısı kimin denetiminde' sorusu yapay zeka yönetişimi gündeminin parçası olacak.
