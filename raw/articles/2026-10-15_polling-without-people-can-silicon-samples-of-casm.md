---
type: raw_article
title: 'Polling Without People: Can Silicon Samples of CASM-Inspired LLM Personae
  Mimic Human Respondents in Pre-Election Polling?'
description: 'PS: Political Science & Politics''te (Cambridge University Press) 15
  Ekim 2026''da çevrimiçi yayımlanan ve 2026 ABD Temsilciler Meclisi seçimleri için
  ''silikon örneklem'' (synthetic sample) tahmini ürete...'
resource: https://www.cambridge.org/core/journals/ps-political-science-and-politics/article/polling-without-people-can-silicon-samples-of-casminspired-llm-personae-mimic-human-respondents-in-preelection-polling/6FCB4E198E9DB211D3847665FA700B5A
tags:
- kurator
- high
timestamp: '2026-10-22T17:51:10Z'
source_file: 2026-10-22_polling-without-people-casm-silicon-samples.json
category: KURATOR
priority: high
roles: []
published: '2026-10-15'
---

# Polling Without People: Can Silicon Samples of CASM-Inspired LLM Personae Mimic Human Respondents in Pre-Election Polling?

**Author(s):** Danielius Jonaitis, Brendan Corcoran, Binam Poudyal, Alexandra Roskam, Ava Ali, Shriya Agrawal, Raymond Duch, Roberto Cerina

**Published:** 2026-10-15

**Source:** [https://www.cambridge.org/core/journals/ps-political-science-and-politics/article/polling-without-people-can-silicon-samples-of-casminspired-llm-personae-mimic-human-respondents-in-preelection-polling/6FCB4E198E9DB211D3847665FA700B5A](https://www.cambridge.org/core/journals/ps-political-science-and-politics/article/polling-without-people-can-silicon-samples-of-casminspired-llm-personae-mimic-human-respondents-in-preelection-polling/6FCB4E198E9DB211D3847665FA700B5A)

## Summary

PS: Political Science & Politics'te (Cambridge University Press) 15 Ekim 2026'da çevrimiçi yayımlanan ve 2026 ABD Temsilciler Meclisi seçimleri için 'silikon örneklem' (synthetic sample) tahmini üreten yöntem makalesi. Sekiz yazarlı ekip (Amsterdam Üniversitesi ağırlıklı; Raymond Duch, Oxford Nuffield) anket yanıtlamanın bilişsel süreçlerini (CASM — Cognitive Aspects of Survey Methodology, Tourangeau 1984; Schwarz 2007) LLM persona mimarisine aktarıyor: yorumlama → yargı üretimi → haritalama ve raporlama olmak üzere üç aşamalı, aşamalı istem (prompt) zinciri. Her persona; atanmış sosyo-demografik profil, rastgele üretilmiş bireysel biyografi ve 'önemli olay anıları' içeriyor. Yargı üretimi iki moda ayrılıyor: 'retrieval' (personanın belleğinden çekme) ve 'construction' (o hafta okuduğu haberlerden inşa etme); mod Bernoulli çekilişiyle atanıyor ve haber maruziyeti GDELT'ten persona-medya diyeti + okuma bütçesine göre örnekleniyor. Model: gpt-oss-120B; bilgi kesme tarihi Haziran 2024 sonrası Wikipedia olay kayıtlarıyla RAG üzerinden güncelleniyor. Uygulama: 31 Ağustos – 6 Eylül 2026 haftası için 4.000 sentetik birey, ardından 1,5 milyondan fazla hücreye derin çok düzeyli regresyon ve post-stratifikasyon (deep MrP) ile ulusal ve bölge düzeyi tahmin. Sonuçlar: Demokratlar %58,4 – Cumhuriyetçiler %39,8 – Diğer %1,7; D–R marjı D+18,7 (95% GA 15,0–21,8); katılım tahmini %62,8. Aynı haftanın gerçek anket ortalaması D+8,7 iken model ~10 puan daha Demokrat; koltuk projeksiyonu 292'e 143 (Demokratlar için 266–307 aralığı). Yön doğru (CASM zenginleştirmesi salt demografik persona tabanına göre tahminleri Demokratlara kaydırıyor, haberle 'inşa' eden personae 'retrieval' personae'den daha büyük Demokrat marj üretiyor; katılım tahmini 2024 gerçekleşmesinin yalnızca 1,48 puan altında), ama seviye yanlış: kalıcı sol-eğilim (leftward bias), aşırı dar güven aralıkları (sentetik örneklemlerde belgelenen under-dispersion), ve 'undecided' seçeneğinin ankette olmaması nedeniyle 'Diğer' kategorisinin tamamen erimesi. Yazarlar bu farkın büyük ölçüde kararsızların Demokratlara kırılması varsayımından geldiğini, ancak kesin yüzdelerin tutmasının olası olmadığını açıkça yazıyor; yöntemin tahmin doğruluğunu kesin olarak kanıtlamadığını ve 2026 seçiminin 'canlı test' olacağını vurguluyor. Makale ayrıca metodolojik bir uyarı içeriyor: yüksek frekanslı, çok ucuz (yanıt başına bir sentin kesri) ve istenen demografik dağılıma göre örneklenebilir sentetik anketler, insan verisi toplamanın maliyet ve provenans sorunlarını ortadan kaldırmıyor; zenginleştirme insan verisine dayanıyorsa 'insansız anket' iddiası zayıflıyor.

## Key Points

- CASM temelli 3 aşamalı persona hattı (yorumlama → yargı → raporlama), gpt-oss-120B, 4.000 persona, deep MrP ile 1,5 milyon hücreye projeksiyon.
- Tahmin: D+18,7 (58,4 / 39,8), katılım %62,8, 292 Demokrat koltuğu — aynı hafta anket ortalaması D+8,7.
- Yön doğru, seviye yanlış: ~10 puan sistematik Demokrat yanlılığı; aşırı dar güven aralıkları (under-dispersion).
- 'Kararsız' seçeneğinin modele kapalı olması 'Diğer %7,3'ün tamamen erimesine ve marjın şişmesine yol açıyor.
- Ucuz ve yüksek frekanslı ama provenans sorunu sürüyor: zenginleştirme insan verisine dayanıyorsa 'insansız anket' iddiası sınırlı.

## Turkey Context

Türkiye açısından üç ayrı katman var. Birincisi, yöntemsel: Türkiye'de seçim anketleri pahalı, panel altyapısı zayıf ve seçim dönemlerinde haftalık takip talebi yüksek; sentetik persona + MrP hattı, özellikle il-ilçe düzeyinde yüksek frekanslı tahmin için cazip görünüyor. Ancak makalenin kendi bulgusu bu cazibeyi sınırlıyor: model ABD'de bile ~10 puan sistematik sol-eğilim üretiyor. Türkiye'de LLM'lerin siyasal eğilim dağılımı (Kürt meselesi, laiklik, mültecilik, dindarlık eksenleri) çok daha az temsil edildiği için bu yanlılığın yönünü önceden kestirmek imkânsız; 'silikon örneklem' Türkiye'de doğrulama yapılmadan kullanılırsa anket piyasasının mevcut güven sorununu derinleştirebilir. İkincisi, düzenleyici: 298 sayılı Seçimlerin Temel Hükümleri Kanunu ve YSK kararları seçim döneminde anket yayımlamayı kaynağa, tarihe ve örnekleme ilişkin bildirim yükümlülüklerine bağlıyor; 'sentetik katılımcı' ile üretilen bir 'anket'in bu rejimde nasıl beyan edileceği mevzuatta tanımsız — yani yöntem, bir 'anket midir' sorusu hukuken açık. Üçüncüsü, AI yönetişimi: sentetik seçmen simülasyonları, seçim anketlerinin yeniden 'bilimsel' görünüm kazanması için kullanılabilir; aynı teknik, kampanyaların mikro-hedefleme ve mesaj testi için de kullanılabilir. Türkiye'de yapay zeka düzenlemesi tartışmasında (kişisel verilerin korunması + seçim dönemi dezenformasyon) 'sentetik anket' özel bir başlık olarak henüz yok; bu makale o boşluğun erken bir uyarısı sayılabilir. Doğrulama için asgari koşul: aynı hafta gerçek bir insan anketiyle eşzamanlı karşılaştırma ve 'kararsız' seçeneğinin modellendiği bir tasarım.

---

## 🔗 İlgili Bağlantılar
### 🧠 İlgili Kavramlar
- [[concepts/sentetik-populasyonlar.md|Sentetik Popülasyonlar ve Birey-Tabanlı Simülasyon]]
- [[concepts/siyaset-bilimi-metodolojisi.md|Siyaset Bilimi Metodolojisi]]
- [[concepts/olcum-araclari.md|Ölçüm Araçları]]
- [[concepts/yapay-zeka-demokrasi.md|Yapay Zeka ve Demokrasi]]
### 🏛 İlgili Kurum/Kişiler
- [[entities/cambridge-university-press.md|Cambridge University Press]]
### 📄 İlgili Makaleler
- [[raw/articles/2026-10-12_simulated-responses-from-large-language-models-are.md|Simulated responses from LLMs are weak proxies for human economic preferences across 74 countries (Chen ve ark., Nature Human Behaviour, 2026)]]
- [[raw/articles/2026-10-16_cross-centaur-modeling-individual-decision-making-.md|Cross-Centaur: Modeling Individual Decision-Making Across Psychological Tasks with Language Models (Asano ve ark., 2026)]]
