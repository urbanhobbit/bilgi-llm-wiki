---
type: raw_article
title: Polarization and echo chambers in Reddit's political discourse (Cirulli et
  al., EPJ Data Science)
description: EPJ Data Science'ta yayımlanan çalışma (Cirulli, Desiderio, Cimini &
  Saracco; 12 Ekim 2026, DOI 10.1140/epjds/s13688-026-00707-5), Reddit'in "Twitter/Facebook'a
  göre kutuplaşmaya daha dirençli" olduğu...
resource: https://doi.org/10.1140/epjds/s13688-026-00707-5
tags:
- kurator
- high
timestamp: '2026-11-05T00:50:08Z'
source_file: 2026-10-28_reddit-polarization-echo-chambers-epjds.json
category: KURATOR
priority: high
roles:
- method
- result
published: '2026-10-12'
---

# Polarization and echo chambers in Reddit's political discourse (Cirulli et al., EPJ Data Science)

**Author(s):** Daniele Cirulli, Antonio Desiderio, Giulio Cimini, Fabio Saracco (Roma Tor Vergata / Enrico Fermi RC / ISI Foundation / DTU / CNR-IAC / IMT Lucca)

**Published:** 2026-10-12

**Source:** [https://doi.org/10.1140/epjds/s13688-026-00707-5](https://doi.org/10.1140/epjds/s13688-026-00707-5)

## Summary

EPJ Data Science'ta yayımlanan çalışma (Cirulli, Desiderio, Cimini & Saracco; 12 Ekim 2026, DOI 10.1140/epjds/s13688-026-00707-5), Reddit'in "Twitter/Facebook'a göre kutuplaşmaya daha dirençli" olduğu varsayımını **2016 ABD başkanlık seçimi** örneğiyle test ediyor ve varsayımı çürütüyor.

**Veri:** Reddit Politosphere arşivinden **498 siyasi subreddit**, Ocak 2013 – Aralık 2017: **120,4 milyon yorum**, **1,9 milyon kullanıcı**, 16,8 milyon gönderi, 208,3 bin haber alan adı.

**Yöntem — iki katmanlı ağ + istatistiksel doğrulama:**
1. **Kullanıcı-etkileşim ağı:** subreddit'ler, ortak kullanıcı tabanlarına göre birbirine bağlanıyor.
2. **Bilgi-diyeti ağı:** subreddit'ler, paylaşılan haber alan adlarına göre bağlanıyor.
Ham eş-oluşumlar kullanıcı aktivitesi ve popülerlik yanlılığı taşıdığı için **maksimum entropi sıfır modelleriyle** istatistiksel olarak filtreleniyor, ardından Louvain ile topluluk tespiti yapılıyor. Doğrulamanın etkisi ölçülmüş: kullanıcı-subreddit projeksiyonunda **modülerlik yaklaşık bir kat artıyor, yoğunluk bir kat azalıyor — sadece düğümlerin %16'sı atılarak.** Doğrulama olmadan topluluklar parametre seçimine aşırı duyarlı ve istikrarsız; doğrulanmış ağlarda topluluklar yöntem değişikliğine dayanıklı.

**Bulgular:**
- **Hem etkileşim hem konu temelli topluluklarda net kutuplaşma.** Doğrulanmış kümeler **Demokratik, Muhafazakâr ve Yasaklı (Banned)** subreddit blokları olarak ayrışıyor — siyasi hizalama hem kimin kiminle konuştuğunu hem hangi içeriğin dolaştığını belirliyor.
- **Genel eğilim 2013-2017 arasında kutuplaşma azalıyor**, ama Demokratik ve Muhafazakâr gruplar sürekli yüksek kutuplaşmada kalıyor. **Yasaklı topluluklarda kutuplaşma neredeyse altı kat artıyor.**
- **Yasak, tartışmayı bitirmiyor:** başlangıçta aşırı sağla hizalı yasaklı toplulukların kullanıcıları 2016 seçimleri sırasında muhafazakâr subreddit'lere kayıyor ve **orijinal topluluklar yasaklandıktan sonra da muhafazakâr söylemi etkilemeye devam ediyor.**
- **Dil yakınsaması:** ideolojik gruplar içinde kullanıcılar zamanla birbirine daha benzer dil kalıpları kullanıyor; **aynı bilgi kaynaklarını paylaşan topluluklar aynı kullanıcı tabanını da paylaşıyor** — yankı odasının iki ayağı (homofili + bilgi tekeli) birlikte oluşuyor.
- **En çarpıcı bulgu — maruz kalma düşmanlığı azaltmıyor:** büyük siyasi olaylar sırasında gruplar arası etkileşim artıyor, ama karşıt gruplar arasında **yorum puanları düşüyor**. Yani daha fazla temas, kutuplaşmanın azalmasıyla değil **artmış antagonizmayla** aynı zamana denk geliyor.

**Yazarların çerçevesi:** Reddit, yankı odası örgütlenmesiyle tutarlı yapısal örüntüler taşıyan **kutuplaşmış bir ortam**. Ağ doğrulaması, çevrimiçi sosyal medyada anlamlı etkileşim ve bilgi paylaşımı örüntülerini saptamak için anahtar yöntem olarak öneriliyor.

## Key Points

- 498 siyasi subreddit, 120,4 milyon yorum, 1,9 milyon kullanıcı, 208,3 bin haber alan adı (2013-2017).
- İki katmanlı ağ: kullanıcı-etkileşim ağı + bilgi-diyeti (haber alan adı) ağı.
- Maksimum entropi sıfır modelleriyle doğrulama: modülerlik ~1 kat artıyor, yoğunluk ~1 kat azalıyor, düğümlerin yalnızca %16'sı atılarak.
- Doğrulanmış topluluklar üç bloğa ayrışıyor: Demokratik, Muhafazakâr, Yasaklı (Banned).
- Genel kutuplaşma 2013-2017'de azalırken Demokratik ve Muhafazakâr gruplar yüksek kutuplaşmada kalıyor; Yasaklı gruplarda kutuplaşma ~6 kat artıyor.
- Yasak, etkiyi bitirmiyor: yasaklı topluluk kullanıcıları muhafazakâr subreddit'lere kayıp söylemi etkilemeye devam ediyor.
- Dil yakınsaması + ortak bilgi kaynağı: aynı haber sitelerini paylaşan topluluklar aynı kullanıcı tabanını da paylaşıyor (yankı odasının iki ayağı).
- Karşıt gruplar arası etkileşim seçim döneminde artıyor ama yorum puanları düşüyor → maruz kalma antagonizmayı artırıyor, kutuplaşmayı azaltmıyor.
- Yöntem katkısı: doğrulama olmadan topluluk tespiti parametreye aşırı duyarlı; doğrulanmış ağda topluluklar yöntem değişikliğine dayanıklı.
- Reddit'e dair 'daha az kutuplaşmış platform' varsayımı bu veriyle desteklenmiyor.

## Turkey Context

Türkiye'deki platform tartışması açısından üç aktarım var.

**Birincisi, "Reddit gibi platformlar daha temiz" varsayımı tehlikeli.** Türkiye'de de niş platformlar (Reddit, Ekşi Sözlük, Discord, Telegram grupları) genellikle "ana akım sosyal medyadan daha az kutuplaşmış" sayılıyor. Bu çalışma, konu-temelli yapının yankı odasını engellemediğini gösteriyor: subreddit yapısı ideolojik kümelenmeyi **kolaylaştırıyor**, çünkü kullanıcı kendi ilgi alanına göre değil, kendi siyasi kimliğine göre topluluk seçiyor.

**İkincisi, yasak siyaseti üzerine doğrudan kanıt.** Yasaklı aşırı sağ toplulukların kullanıcıları yasaktan sonra kaybolmuyor; muhafazakâr ana akım topluluklara kayıp **söylemi oradan sürdürüyor**. Türkiye'de de kapatma/yasaklama tartışmaları (ör. Ekşi Sözlük, Twitter/X erişim engelleri, Telegram kanalları) genellikle "kapatınca biter" varsayımıyla yürüyor. Veri bunun tersini söylüyor: yasak, topluluğu dağıtmıyor, **daha meşru görünen bir kaba taşıyor**.

**Üçüncüsü, "maruz kalma iyileştirir" tezinin çürütülmesi.** Seçim döneminde gruplar arası etkileşim artıyor ama karşıt gruplar arasında yorum puanları düşüyor. Bu, Türkiye'de yaygın "karşıt görüşler bir arada konuşsun, gerilim azalır" varsayımına doğrudan aykırı. Temas hipotezi (Allport) çevrimiçi ortamda, **kurumsal çerçeve ve ortak hedef olmadan** çalışmıyor; çıplak temas düşmanlığı besleyebiliyor.

**Yöntem dersi:** Türkiye'de dezenformasyon ve kutuplaşma araştırmaları çoğunlukla içerik analizi veya anketle yapılıyor. Bu çalışmanın yaptığı şey — kullanıcı-etkileşim ağı ile haber kaynağı ağını birleştirip istatistiksel olarak doğrulamak — Türkiye verisiyle (ör. Ekşi Sözlük başlık-yazar ağı + paylaşılan haber linkleri) uygulanabilir ve "hangi topluluk hangi kaynağı okuyor" sorusunu ölçülebilir kılar.

## 🏷 Retorik Roller

- 🧩 **Yöntem**
- 📊 **Bulgular**

---

## 🔗 İlgili Bağlantılar
### 🧠 İlgili Kavramlar
- [[concepts/filtre-baloncuklari.md|Filtre Balonları (Filter Bubbles)]] — echo chamber ve yankı odası örüntüleri
- [[concepts/sosyal-kutuplasma.md|Sosyal Kutuplaşma ve Dijital Platformlar]] — political polarization ölçümü
- [[concepts/ideolojik-kutuplasma.md|İdeolojik Kutuplaşma]] — ideological polarization: Demokratik/Muhafazakâr/Yasaklı bloklar
- [[concepts/partizan-kimlik.md|Partizan Kimlik]] — grup içi dil yakınsaması ve karşıt gruba yönelik antagonizma
- [[concepts/metin-madenciligi.md|Metin Madenciliği]] — dil analizi ve natural language processing ile söylem ölçümü
- [[concepts/siyaset-bilimi-metodolojisi.md|Siyaset Bilimi Metodolojisi]] — maksimum entropi sıfır modelleri ve doğrulama, araştırma yöntemleri açısından
- [[concepts/sosyal-medya-yasagi-tartismasi.md|Sosyal Medya Yasağı Tartışması]] — yasak sonrası kullanıcı göçü ve söylemin taşınması
### 🏛 İlgili Kurum/Kişiler
- [[entities/arxiv-org.md|arXiv]]
