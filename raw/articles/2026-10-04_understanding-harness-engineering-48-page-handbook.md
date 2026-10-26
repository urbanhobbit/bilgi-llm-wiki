---
type: raw_article
title: Understanding Harness Engineering (48-page handbook by @techNmak)
description: '@techNmak (Tech with Mak, ~47,9 bin takipçi) tarafından yazılan ve 4
  Ekim 2026''da X''te yayımlanan 48 sayfalık teknik el kitabı; kapak: ''Understanding
  Harness Engineering — From Agent Loops and Tool In...'
resource: https://drive.google.com/file/d/1PT-P2PVoiZpfYoe5eWks1_DGt2aSvbDh/view
tags:
- kurator
- medium
timestamp: '2026-10-26T03:20:15Z'
source_file: 2026-10-04_technmak-understanding-harness-engineering.json
category: KURATOR
priority: medium
published: '2026-10-04'
---

# Understanding Harness Engineering (48-page handbook by @techNmak)

**Author(s):** @techNmak (Tech with Mak); paylaşan: Kirk Borne

**Published:** 2026-10-04

**Source:** [https://drive.google.com/file/d/1PT-P2PVoiZpfYoe5eWks1_DGt2aSvbDh/view](https://drive.google.com/file/d/1PT-P2PVoiZpfYoe5eWks1_DGt2aSvbDh/view)

## Summary

@techNmak (Tech with Mak, ~47,9 bin takipçi) tarafından yazılan ve 4 Ekim 2026'da X'te yayımlanan 48 sayfalık teknik el kitabı; kapak: 'Understanding Harness Engineering — From Agent Loops and Tool Interfaces to Context, Sandboxes, Verification, and Long-Running Work / A short technical handbook for AI engineers, developers, and serious learners', 'Special Topic — Understanding AI Series', sayfa 1/48. Kirk Borne aynı Google Drive bağlantısını 4 Ekim'de ve 25 Ekim 2026'da yeniden paylaştı. ⚠️ PDF'in kendisi bu kayıt sırasında OKUNAMADI: Drive bağlantısı hem doğrudan indirmede hem r.jina.ai/microlink render'larında oturum açma ekranına düşüyor (401 / 'Google Drive: Sign-in'), yani dosya halka açık indirilebilir değil ya da bu ağa kapalı. Bu yüzden aşağıdaki içerik özeti yazarın kendi tanıtım thread'inden ve doğrulanabilen kapak görselinden; kitabın içi okunmadı. Yazarın tanımladığı kapsam: (1) ajan döngüsü, (2) Agent–Computer Interfaces (ACI), (3) araçlar, (4) MCP, (5) skills, (6) aktif bağlam ile kalıcı durum ayrımı (active context vs durable state), (7) bağlam sıkıştırma (compaction), (8) sandbox'lar, (9) izinler, (10) kimlik bilgileri (credentials), (11) prompt injection, (12) yürütme bütçeleri (execution budgets), (13) doğrulama (verification), (14) değerlendirici döngüleri (evaluator loops), (15) uzun süreli işlerde toparlanma (long-running recovery), (16) yeniden deneme (retries), (17) idempotency, (18) alt-ajanlar (subagents), (19) gözlemlenebilirlik (observability), (20) ajan değerlendirmesi ve (21) yaygın yanlış anlamalar. Yazarın çerçevesi: 'yetenekli bir model tek başına ajan değildir; modelin hangi bağlamı gördüğüne, hangi araçları kullanabildiğine, araçların nasıl yürütüldüğüne, adımlar arasında hangi durumun yaşadığına, hangi eylemlerin onay gerektirdiğine, hataların nasıl döndüğüne, ne zaman yeniden deneneceğine, ne zaman durulacağına ve görevin gerçekten başarıldığının nasıl doğrulanacağına karar veren katman agent harness'tir'. Aynı modelle çalışan iki ajanın farklı davranmasının nedeni de bu katman: arayüzler, durum, ortam, geri bildirim döngüleri, kısıtlar ve doğrulama. Ayrıca retry'ların dış yan etki üreten araçlarda tehlikeli olduğunu, alt-ajanların paralellik kadar koordinasyon ve tutarlılık sorunu getirdiğini, daha fazla araç/skill/iskeletin ajanı belirsizliği artırarak kötüleştirebileceğini vurguluyor. Doğrulanabilir bağlam (bu el kitabından bağımsız, ayrı kaynaklar): 'harness engineering' 2026 başında adlandırılmış bir disiplin olarak literatüre girdi — arXiv:2609.00006 (Barbaste, Darrigol, Vu, Wiltberger) on bir üretim kodlama harness'ının (Claude Code, Codex CLI, Gemini CLI, Mistral Vibe, OpenHands, Aider, Mini-SWE-Agent, Hermes, Pi, OpenCode, OpenClaw) kaynak-kodu anatomisini çıkarıyor; yedi kanonik alt sistemi, 13 kesişen gözlemi, 29 tasarım desenini ve 18 tasarım önerisini raporluyor; yaklaşık 4 milyon satır kodda hiçbir ajan çalışma zamanının genel amaçlı ajan çerçevesi içe aktarmadığını ve hiçbirinin vektör gömme ile kod getirmediğini buluyor (elle yazılmış async döngüler + deterministik erişim), skills'in MCP'den daha hızlı yayıldığını (9/11 vs 8/11) ve ACP'nin altı sistemde 'harness hosting' rolüyle çıktığını gösteriyor. Kamuya açık alternatif artefaktlar da var: Gilsiley Henrique Darú'nun 127 sayfalık 'Harness Engineering' yaşayan kitabı (v0.78.0, Ağustos 2026, Zenodo DOI 10.5281/zenodo.21632412, AI eş-yazarlığı beyanıyla) ve ticari/practitioner rehberleri. El kitabının kendisi hakem değerlendirmesinden geçmedi, kaynakça ve iddiaları bağımsız doğrulanmadı; 2026'da hızla çoğalan 'harness' içeriğinin bir örneği.

## Key Points

- 'Understanding Harness Engineering', @techNmak (Tech with Mak), 4 Ekim 2026, 48 sayfa; 'Understanding AI Series — Special Topic'; kapak görseli doğrulandı (sayfa 1/48).
- ⚠️ PDF erişilemedi: Google Drive bağlantısı oturum açma ekranına düşüyor (doğrudan indirme, r.jina.ai, microlink dahil) — içerik okunmadı, özet yazarın thread'i ve kapaktan.
- Kapsam (yazarın listesi): ajan döngüsü, ACI, araçlar, MCP, skills, aktif bağlam vs kalıcı durum, compaction, sandbox, izinler, credentials, prompt injection, yürütme bütçeleri, doğrulama, evaluator loops, uzun işlerde toparlanma, retries, idempotency, alt-ajanlar, gözlemlenebilirlik, ajan değerlendirmesi.
- Çerçeve: ajan = model + harness; aynı modelle iki ajanın farklı davranması harness farkından (arayüz, durum, ortam, geri bildirim, kısıt, doğrulama).
- Uyarılar: dış yan etki üreten araçlarda retry tehlikeli; alt-ajanlar koordinasyon/tutarlılık maliyeti getirir; fazla araç/skill/iskelet ajanı kötüleştirebilir.
- Bağımsız literatür teyidi: arXiv:2609.00006 (2026) on bir kodlama harness'ını kaynak kodundan analiz ediyor — yedi kanonik alt sistem, 13 gözlem, 29 desen, 18 öneri.
- Aynı çalışma: ~4 milyon satır kodda hiçbir ajan runtime'ı genel amaçlı ajan çerçevesi kullanmıyor ve vektör gömme ile kod getirmiyor; skills (9/11) MCP'den (8/11) daha yaygın.
- Kamuya açık alternatifler: Darú'nun 127 sayfalık 'Harness Engineering' kitabı (v0.78.0, Zenodo 10.5281/zenodo.21632412); ticari rehberler ve İspanyolca uyarlama.
- Değerlendirme: hakemsiz, hızla eskiyen practitioner içeriği; kayıt 'kavramsal çerçeve' değeri taşıyor, kanıt değeri değil.

## Turkey Context

Türkiye'de 'yapay zeka ajanı' projeleri 2025-2026'da kamu ihale ve özel sektör yol haritalarına girdi; ama satın alma ve tasarım tartışmaları neredeyse tamamen model seçimi (hangi LLM, kaç parametre, yerli model mi) üzerinden yürüyor. Bu el kitabının çerçevesi tam o boşluğa düşüyor: aynı modelle iki ajanın farklı davranması harness farkından; yani 'hangi model' sorusu tek başına ne maliyeti ne güvenilirliği açıklıyor. Türkiye'de kurumsal ajan projelerinde en sık atlanan katmanlar bu listede sıralanıyor: izin sınırları, kimlik bilgisi yönetimi, yürütme bütçesi, doğrulama ve uzun süreli işlerde toparlanma. İkincisi kamu açısından: e-Devlet benzeri ajan arayüzlerinde 'görev gerçekten başarıldı mı' doğrulaması ve idempotency, çift işlem/çift ödeme riskini doğrudan ilgilendiriyor — retry'ın dış yan etki üreten araçlarda tehlikeli olduğu uyarısı, kamu sistemleri için teknik değil idari bir risk başlığı. Üçüncüsü KVKK/veri yerelleştirme: el kitabı credentials ve sandbox katmanını merkeze alıyor; Türkiye'de yerel/açık ağırlıklı model tercihi bu katmanlarla birlikte tasarlanmadığında güvenlik kazancı kâğıt üzerinde kalıyor. Dördüncüsü eleştirel not: bu içerik hızla eskiyor ve pazarlama diliyle iç içe; Türkiye'deki kurumlar için doğru kullanım, el kitabını 'standart' değil 'kontrol listesi taslağı' olarak almak ve doğrulama/değerlendirme bölümlerini kendi testleriyle yeniden kurmak. Beşincisi araştırma tarafı: bu tür practitioner artefaktları akademik literatürle (arXiv:2609.00006 gibi kaynak-kodu çalışmaları) çapraz okunmadığında, 'harness' kavramı Türkiye'de yeni bir sihirli sözcüğe dönüşme riski taşıyor — oysa literatür, alanın henüz standartlaşmadığını ve çoğu iddianın vaka çalışması düzeyinde olduğunu gösteriyor.
