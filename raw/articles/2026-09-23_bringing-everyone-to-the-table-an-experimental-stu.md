---
type: raw_article
title: 'Bringing Everyone to the Table: An Experimental Study of LLM-Facilitated Group
  Decision Making'
description: 'Ön kayıtlı, randomize bir deney: **1.475 katılımcı, 281 canlı grup**
  (5 kişilik; insan kolaylaştırıcı koşulunda 6), **hidden profile** görevinde (varsayımsal
  bir spor etkinliği için en iyi şehri seçme...'
resource: https://doi.org/10.1145/3816907
tags:
- kurator
- high
timestamp: '2026-11-19T02:21:46Z'
source_file: 2026-09-23_llm-facilitated-group-decision-making.json
category: KURATOR
priority: high
roles: []
published: '2026-09-23'
---

# Bringing Everyone to the Table: An Experimental Study of LLM-Facilitated Group Decision Making

**Author(s):** Mohammed Alsobay, David M. Rothschild, Jake M. Hofman, Daniel G. Goldstein (hepsi Microsoft Research)

**Published:** 2026-09-23

**Source:** [https://doi.org/10.1145/3816907](https://doi.org/10.1145/3816907)

## Summary

Ön kayıtlı, randomize bir deney: **1.475 katılımcı, 281 canlı grup** (5 kişilik; insan kolaylaştırıcı koşulunda 6), **hidden profile** görevinde (varsayımsal bir spor etkinliği için en iyi şehri seçmek) dört koşuldan birine atandı: kolaylaştırıcı yok · bir kerelik bilgi paylaşma mesajı · **insan kolaylaştırıcı** · **LLM (GPT-4o) kolaylaştırıcı**. Bulgular: (1) **LLM kolaylaştırma, paylaşılan bilgi miktarını anlamlı biçimde artırdı** (Δ = 2,9 bilgi; **Cohen's d = 0,61**), diğer üç koşula kıyasla da üstün; (2) artış **tartışmayı uzatarak** değil, **bilgi yoğunluğunu** artırarak geldi ve **en az katkı veren üyeyi yukarı çekerek** (extensive margin) gerçekleşti — LLM gruplarında **%61**'inde herkes en az bir yeni bilgi paylaştı (diğerlerinde %39-47); (3) **ama karar kalitesi değişmedi**: optimal şehri seçme oranı %31 (yok), %21 (mesaj), %30 (insan), %23 (LLM) — farklar anlamlı değil. Yazarların teşhisi: LLM kolaylaştırma **bilginin erişilebilirliğini** (availability) çözüyor, **kullanımını** (integration) çözmüyor.

## Key Points

- **Künye:** *Proc. ACM Hum.-Comput. Interact.* **10(6), CSCW059**, Ekim 2026, 36 sayfa, **80 kaynak**, hakemli, **CC BY 4.0**; DOI **10.1145/3816907**. Yazarlar: Alsobay, Rothschild, Hofman, Goldstein (**Microsoft Research**). Açık sürüm **arXiv 2508.08242v2**.
- **Erişim:** ACM DL bağlantısı yayıncı duvarına takılabilir; tam metin **arXiv PDF'inden** (12,3 MB, 17 sayfa) indirilip okundu. Tüm sayılar birincil metinden doğrulandı.
- **Tasarım:** ön kayıtlı (pre-registered) randomize deney, Prolific katılımcıları, **1.475 kişi / 281 grup**, koşul başına **70 geçerli grup**, 5 kişilik gruplar (insan kolaylaştırıcı koşulunda 6). Görev: **hidden profile** — dört şehir arasından (Eldoron = optimal, Myloria = yem) en iyisini seçmek; bilgi parçaları üyeler arasında asimetrik dağıtılmış.
- **Dört koşul:** (a) kolaylaştırma yok, (b) bir kerelik "bilgi paylaşın" mesajı, (c) **insan kolaylaştırıcı**, (d) **LLM (GPT-4o) kolaylaştırıcı**.
- **Bilgi paylaşımı (ana bulgu):** LLM vs yok → **Δ = 2,9 bilgi**, t(138)=3,58, **p < 0,001**, **Cohen's d = 0,61** (orta-büyük); LLM vs mesaj Δ = 1,58 (p = 0,021); LLM vs insan Δ = 2,47 (p < 0,001). **Ne tek seferlik mesaj ne de insan kolaylaştırıcı** "yok" koşuluna göre anlamlı fark üretmedi (p = 0,066 / 0,31).
- **Mekanizma — 'herkesi masaya getirmek':** LLM kolaylaştırma **minimum** katkıyı artırdı (Δ = 0,41 bilgi, p = 0,003) ama **maksimumu** değiştirmedi → etki, zaten aktif olanları değil **hiç katkı vermeyenleri** yukarı çekmekten geliyor. Herkesin en az bir bilgi paylaştığı grup oranı: **%61 (LLM)** vs %39 (yok), %44 (mesaj), %47 (insan); χ²(3, N=281) = 8,10, **p = 0,044**.
- **Kolaylaştırıcı davranışı (neden LLM üstün):** insan kolaylaştırıcı mesajlarının **%25**'inde belirli bir üyeye doğrudan seslenirken, LLM mesajlarının **%68**'inde sesleniyor; LLM **her grupta** en az bir kez üyeye seslendi, insan kolaylaştırıcıların yalnızca **%77**'si bunu yaptı.
- **Tartışma kalitesi:** mesaj sayısı koşullar arasında farklı değil (F(3,277)=0,46, p=0,71) ama **bilgi yoğunluğu** daha yüksek (Δ = 0,067, p = 0,002) ve bilgi **şehirler arasında daha dengeli** yayıldı (**Gini Δ = −0,05**, p = 0,017).
- **🔴 Karar sonucu — asıl haber:** optimal şehri (Eldoron) seçen grup oranı: **%31 (yok) · %21 (mesaj) · %30 (insan) · %23 (LLM)** — χ²(3, N=281) = 2,85, **p = 0,42 → anlamlı fark yok**. Katı rasyonel model (UWLM) uygulansa beklenen oranlar %60/%48/%47/%63 olurdu (p = 0,13). Yani **daha fazla bilgi karar kalitesini yükseltmedi**.
- **Yazarların teşhisi (kaydın en değerli kısmı):** LLM kolaylaştırma **bilginin erişilebilirliğini** (availability) artırıyor, **entegrasyonunu** (nasıl tartılacağı, yorumlanacağı, karara dönüşeceği) değiştirmiyor. "Etkili kolektif karar için gerekli **bir** koşulu" sağlıyor, "aşağı akıştaki entegrasyon sorunlarını" çözmüyor.
- **Tutumlar / maliyet:** NASA-TLX ile ölçülen iş yükü, grup uyumu (aynı grupla tekrar çalışmak isteyenlerin oranı **%77-80**), algılanan başarı ve adalet koşullar arasında **anlamlı fark göstermedi** — yani bilgi paylaşımı kazancı "bedelsiz" geldi.
- **Açık kaynak:** veri ve deney platformu **GRAIL (Group-AI Interaction Laboratory)** açık kaynak olarak yayımlandı — aynı deney Türkçe koşullarla **tekrarlanabilir**.

## Turkey Context

Türkiye'de grup kararı altyapısı yoğun: **kurul/komisyon toplantıları** (üniversite yönetim kurulları, il/ilçe komisyonları, MEB şuraları, kamu ihalelerinde muayene komisyonları) hem sık hem **bilgi asimetrisi** yüksek. Bu çalışma üç noktada doğrudan bağlanıyor. **Birincisi, ucuz müdahale:** LLM kolaylaştırıcı "sessiz üyeyi konuşturma"da insan kolaylaştırıcıdan **belirgin biçimde daha iyi** (%68 vs %25 doğrudan seslenme) ve maliyeti neredeyse sıfır — Türkiye'de **çevrimiçi yürütülen kurul toplantıları** için uygulanabilir tek gerçek AI faydası burada. **İkincisi, beklenti yönetimi:** aynı çalışma, daha fazla bilgi paylaşımının **karar kalitesini artırmadığını** gösteriyor; Türkiye'de "AI destekli karar alma" söylemi genellikle bunun tersini vaat ediyor. Kamu kurumlarında AI "karar destek" projeleri bu ayrımı yapmazsa, **daha çok bilgi + aynı karar** üretip hayal kırıklığı yaratacak. **Üçüncüsü, araştırma boşluğu:** GRAIL açık kaynak ve deney protokolü yayımlanmış — Türkiye'de (ör. üniversite kurulları veya STK yönetim kurulları örneklemiyle) **Türkçe replikasyon** düşük maliyetli ve doğrudan yayınlanabilir bir çalışma olur. Uyarı: bu bir **bulgu/kavram transferi**; deney ABD'li Prolific katılımcılarıyla, İngilizce ve yapay bir görev üzerinde yapıldı; Türkiye'ye dair ampirik iddia değil.

---

## 🔗 İlgili Bağlantılar
### 🧠 İlgili Kavramlar
- [[concepts/kolektif-zeka-ve-grup-karari.md|Kolektif Zeka ve Grup Kararı]] — makalenin doğrudan konusu
- [[concepts/muzakereci-demokrasi.md|Müzakereci Demokrasi]]
- [[concepts/sentetik-odak-gruplari.md|Sentetik Odak Grupları]]
