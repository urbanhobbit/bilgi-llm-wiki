---
type: raw_article
title: 'feat(skills): add Karpathy''s llm-wiki skill for persistent markdown knowledge
  bases'
description: Andrej Karpathy'nin LLM Wiki pattern'ini temel alan yeni bir Hermes Agent
  yetenek modülü ekleyen pull request. PR, ajanın kalıcı, birbirine bağlı markdown
  bilgi tabanları oluşturmasını ve sürdürmesini...
resource: https://github.com/NousResearch/hermes-agent/pull/5100/files
tags:
- genel
- low
timestamp: '2026-06-26T15:22:33Z'
source_file: 2026-06-11_categorized.json
category: GENEL
priority: low
---

# feat(skills): add Karpathy's llm-wiki skill for persistent markdown knowledge bases

**Source:** [https://github.com/NousResearch/hermes-agent/pull/5100/files](https://github.com/NousResearch/hermes-agent/pull/5100/files)

## Summary

Andrej Karpathy'nin LLM Wiki pattern'ini temel alan yeni bir Hermes Agent yetenek modülü ekleyen pull request. PR, ajanın kalıcı, birbirine bağlı markdown bilgi tabanları oluşturmasını ve sürdürmesini sağlayan üç katmanlı bir mimari sunuyor: ham kaynaklar (makaleler, belgeler, transkriptler), ajan tarafından yönetilen wiki sayfaları (varlıklar, kavramlar, karşılaştırmalar) ve şema yapılandırması. Geleneksel RAG sistemlerinin her sorguda bilgiyi sıfırdan yeniden keşfetmesine karşılık, LLM Wiki pattern bilgiyi yapılandırılmış bir wiki'de derleyerek zaman içinde biriktiriyor. Çapraz referanslar, çelişkiler ve sentezler her oturumda yeniden türetilmek yerine büyüyerek devam ediyor. teknium1 tarafından 4 Nisan 2026'da açılan PR, 7 Nisan'da kapatılmış ve birleştirilmiş.

## Key Points

- Karpathy'nin LLM Wiki pattern'ini Hermes Agent'a entegre eden PR
- Üç katmanlı mimari: ham kaynaklar, wiki sayfaları, şema yapılandırması
- Geleneksel RAG'a alternatif olarak kalıcı bilgi tabanı yaklaşımı
- Açık kaynak yapay zeka geliştirme ekosistemine katkı
- Türkiye'de açık kaynak yapay zeka araçlarının yaygınlaştırılması için örnek teşkil ediyor

## Turkey Context

Teknik içerikli bu pull request, Türkiye'de yapay zeka ve açık kaynak yazılım geliştirme ekosistemi açısından çeşitli bağlamlarda değerlendirilebilir. Cumhurbaşkanlığı Dijital Dönüşüm Ofisi tarafından yürütülen Ulusal Yapay Zeka Stratejisi (2021-2025), yapay zeka alanında yetkinlik geliştirme, Ar-Ge teşvikleri ve açık kaynak ekosisteminin güçlendirilmesi hedeflerini içermektedir. Bu strateji belgesinde, yapay zeka araçlarının yerelleştirilmesi ve Türkçe doğal dil işleme modellerinin geliştirilmesi öncelikli alanlar arasında sayılmıştır. LLM Wiki gibi kalıcı bilgi tabanı yaklaşımları, özellikle TÜBİTAK BİLGEM Yapay Zeka Enstitüsü ve ASELSAN gibi savunma sanayii kurumlarının Ar-Ge süreçlerinde bilgi birikimini sistematik şekilde yönetmelerine katkı sağlayabilir.

Türkiye'de açık kaynak yapay zeka araçlarının kullanımı her geçen yıl artmaktadır. BTK'nın 2025 yılı sektör raporuna göre, Türkiye'deki yazılım geliştirici sayısı 250 bine yaklaşmıştır ve bu geliştiricilerin önemli bir bölümü GitHub gibi platformlarda açık kaynak projelere katkıda bulunmaktadır. Özellikle Hermes Agent gibi ajan çerçevelerine yapılan katkılar, Türk mühendislerin global yapay zeka ekosisteminde daha görünür hale gelmesini sağlamaktadır. ODTÜ Yapay Zeka Laboratuvarı, Boğaziçi Üniversitesi Yapay Zeka Araştırma Merkezi (BAİTAM) ve İTÜ Yapay Zeka Kulübü gibi akademik yapılar, bu tür araçları araştırma verimliliğini artırmak ve lisansüstü çalışmalarda kullanmaktadır.

KVKK (6698 sayılı Kanun) kapsamında, yapay zeka modellerinin eğitim verilerinin yönetimi ve kişisel verilerin korunması konuları, LLM Wiki gibi bilgi tabanı sistemlerinde dikkate alınması gereken önemli düzenleyici çerçevelerdir. Kişisel Verileri Koruma Kurulu'nun 2024 yılında yayınladığı yapay zeka ve veri işleme konulu rehber, özellikle büyük dil modellerinin eğitiminde kullanılan verilerin anonimleştirilmesi ve veri minimizasyonu ilkelerine vurgu yapmaktadır. Ayrıca, Dijital Hizmetler Kanunu kapsamında getirilen yükümlülükler, yapay zeka tabanlı sistemlerin şeffaflık ve hesap verebilirlik gereksinimlerini etkilemektedir.

Sonuç olarak, Hermes Agent'a eklenen bu LLM Wiki yeteneği, Türkiye'nin yapay zeka ekosisteminde bilgi yönetimi ve araştırma verimliliği açısından önemli bir araç olarak değerlendirilebilir. Açık kaynak topluluklarının bu tür katkıları teşvik etmesi ve yerelleştirme çalışmaları, Türkiye'nin küresel yapay zeka yarışında rekabetçi konumunu güçlendirecektir.

---

## 🔗 İlgili Bağlantılar
### 🧠 İlgili Kavramlar
- [[concepts/platform-seffaflik.md|platform-seffaflik]]
- [[concepts/yapay-zeka-cocuklar.md|Yapay Zeka ve Çocuklar]]
### 📄 Aynı Kaynaktan
- [[raw/articles/2026-05-02_scrapling_integration.md|Scrapling Integration Report]]
- [[raw/articles/2026-06-26_bilgi-llm-wiki-github-archive-download.md|Bilgi LLM Wiki - GitHub Archive Download]]
- [[raw/articles/2026-06-26_bilgi-llm-wiki-raw-articles-main.md|Bilgi LLM Wiki - Raw Articles (main)]]
- [[raw/articles/2026-06-26_bilgi-llm-wiki-raw-articles-master.md|Bilgi LLM Wiki - Raw Articles (master)]]
- [[raw/articles/2026-06-26_github-pull-request-5100-nousresearch-hermes-agent.md|GitHub Pull Request #5100 - NousResearch/hermes-ag]]
