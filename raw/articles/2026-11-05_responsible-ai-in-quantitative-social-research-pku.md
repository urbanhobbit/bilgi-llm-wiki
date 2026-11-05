---
type: raw_article
title: 'Responsible AI in Quantitative Social Research: PKU Lecture Slides and Tutorials
  (Rongxin Ouyang, 2026)'
description: '**Ne:** Singapur Ulusal Üniversitesi (NUS) hesaplamalı iletişim doktora
  adayı **Rongxin Ouyang**, Pekin Üniversitesi''nde (PKU) *Social Research Methods*
  modülü kapsamında 5 Kasım 2026''da verdiği **"Re...'
resource: https://github.com/reycn/llm-social-research-pku
tags:
- kurator
- high
timestamp: '2026-11-05T04:26:04Z'
source_file: 2026-11-05_ouyang-responsible-ai-quant-social-research.json
category: KURATOR
priority: high
published: '2026-11-05'
---

# Responsible AI in Quantitative Social Research: PKU Lecture Slides and Tutorials (Rongxin Ouyang, 2026)

**Author(s):** Rongxin Ouyang (National University of Singapore, PhD Candidate in Computational Communication)

**Published:** 2026-11-05

**Source:** [https://github.com/reycn/llm-social-research-pku](https://github.com/reycn/llm-social-research-pku)

## Summary

**Ne:** Singapur Ulusal Üniversitesi (NUS) hesaplamalı iletişim doktora adayı **Rongxin Ouyang**, Pekin Üniversitesi'nde (PKU) *Social Research Methods* modülü kapsamında 5 Kasım 2026'da verdiği **"Responsibly Deploy AI in Quantitative Social Research"** dersinin slaytlarını ve 6 bölümlük uygulama eğitimini GitHub'a açtı. Ders, LLM'leri nicel sosyal araştırmada kullanmanın **geçerlilik, güvenilirlik ve yeniden üretilebilirlik** sorunlarını bir çerçeveye oturtuyor.

**Sunumun omurgası (56 slayt, LaTeX/Beamer, İngilizce; ayrıca `slides-zh/` altında Çince sürüm):**
1. **Giriş** — AI'ın araştırmadaki yeri; AI/ML/DL/LLM ayrımının karıştırılmaması; Transformer (Vaswani vd., 2017) sonrası "LLM çağı"nın 2020 (GPT-3) ile başlatılması.
2. **LLM öncesi AI** — Grimmer vd. (2021) tipolojisiyle keşif/ölçüm/nedensel çıkarım/tahmin; iki örnek: Zhao & Ye (2025) Douyin'de LDA, Mukerjee vd. (2023) Facebook'ta metriklerin haber üretimini biçimlendirmesi.
3. **LLM'lerin üç rolü** (Xu vd., 2026 + Liang 2026 + Zhou vd., 2026 sentezi): **Özne** (insan yerine), **Yöntem** (asistan / işbirlikçi / değerlendirici), **Nesne** (kendisi incelenen).
4. **Sorumlu konuşlandırma** — model seçimi (modeli f(veri, algoritma, hedef) olarak düşünmek; göreve göre model), geçerlilik-güvenilirlik, yeniden üretilebilirlik.
5. **Çıkarımlar + kaynak listesi** — Angrist & Pischke (2009) alıntısıyla: *"kuşkucu ol … paniğe kapılma"*.

**Özne rolünde lehte/aleyhte kanıt dengesi:** Argyle vd. (2023) anket yanıtlarının replike edilebildiğini, Park vd. (2023) inandırıcı sosyal davranış üretilebildiğini gösteriyor; karşı tarafta ise "ulaşılması zor nüfuslar"ı yansıtmama (Bollen vd., 2026; Pataranutaporn vd., 2025), partizan/eğilim yanlılığı (Santurkar vd., 2023) ve kültürel yanlılık (Tao vd., 2024 PNAS Nexus), ortalamaya yakın ama **varyansı düşük** yanıtlar (Bisbee vd., 2024; Boelaert vd., 2025), kimlik gruplarını **hem yanlış hem yassı** temsil (Wang vd., 2025, Nature Machine Intelligence) ve heterojenliği tipolojik kalıplara sıkıştırma (Xie & Xie, 2025) var. İyileştirme üç aşamaya ayrılıyor: **hizalama (kullanım öncesi)**, **optimizasyon (kullanım içi: ince ayar/prompt)**, **düzeltme (kullanım sonrası: ekonometrik ve ML literatüründeki post-processing)**.

**Yöntem rolleri:** asistan (görüşme, deney desteği, metin analizi, sosyal ağ madenciliği — Gilardi vd., 2023 kalabalık işçiden daha iyi etiketleme), işbirlikçi (literatür taraması, hipotez üretimi, protokol tasarımı), değerlendirici (protokol değerlendirme, çıktı eleştirisi; King & Worthington 2026 "AI hakemleri insan hakemleri domine ediyor" — hakem denetiminden geçmemiş). **Nesne** rolünde Zhou vd. (2026) tanımı ve Liu & Zhang (2026) örneği (LLM özetlerinin kamu duygu durumuna etkisi, müdahale = modelin kendisi). **Yeni sınır (3.10):** Imai & Nakamura (2026), çift/duyarsızlaştırılmış ML (Chernozhukov vd., 2017) hattını genişletip üretici modelin **iç temsillerini** kullanarak metin/görsel gibi yapısız müdahalelerin nedensel etkisini tahmin ediyor.

**Yeniden üretilebilirlik kontrol listesi (slayt 4.3):** sohbet arayüzü yerine **API** tercih et; model sürümünü, prompt'ları, "thinking" düzeyini ve parametreleri belgele; prosedürü ayrıntılı yaz; kod ve veriyi paylaş; rastgele tohum (seed) ve temperature'ı sabitle.

**Eğitim deposu (6 defter):** (2) LLM ile metin sınıflandırma not defteri; (3) **ajan tabanlı modelleme** — Card (1993) getiri modelinin OLS/2SLS replikasyonu, R betiği + veri + üretilen makale PDF'i (yıllık eğitim getirisi: OLS 0,052; 2SLS 0,132, ilk aşama F = 13,256, N = 3.010); (4) LLM'in ürettiği hakem yorumlarını eleştirel değerlendirme (Chen & Kim 2026, *Journal of Communication* + UChicago HAI OpenAIReview aracı); (5) YOLO ile nesne tespiti; (6) FLUX-3 ile uyaran (stimulus) üretimi. (1) RoBERTa ve (5)-(6) oturumda işlenmiyor, serbest keşif için bırakılmış.

**Kaynak listesi (slayt 6.1) — araç değeri taşıyan kısım:** model seçimi için artificialanalysis.ai ve arena.ai; makale taraması için **refine.ink** (AEA tarafından benimsenmiş) ve **OpenAIReview**; kaynakça doğrulama için **CiteVerify**; çoklu model yönetimi için magpie (macOS) / cc-switch; **AER-skills**; Sant'Anna'nın Claude Code iş akışı; kendi aracı **PDFMathTranslate** (bilimsel PDF'leri kendi dilinde okuma, EMNLP 2025 demo).

## Key Points

- Rongxin Ouyang (NUS, hesaplamalı iletişim doktora adayı) 5 Kasım 2026 PKU 'Social Research Methods' dersinin 56 slaytlık sunumu ve 6 bölümlük eğitim deposunu açtı; ikisi de GitHub'da, lisans belirtilmemiş (varsayılan telif).
- Sunum LLM'leri üç rolde çerçeveliyor: özne (insan yerine), yöntem (asistan/işbirlikçi/değerlendirici), nesne (incelenen teknoloji) — Xu vd. 2026, Liang 2026 ve Zhou vd. 2026 sentezi.
- Özne rolünde 'lehte' kanıt (Argyle vd. 2023 replikasyonu, Park vd. 2023) ile 'aleyhte' kanıt (kültürel/partizan yanlılık, düşük varyans, kimlik gruplarını yassılama) yan yana veriliyor; slaytlar simülasyonu koşulsuz önermiyor.
- İyileştirme üç aşamada: hizalama (kullanım öncesi, çoğunlukla laboratuvarların işi), optimizasyon (ince ayar/prompt), düzeltme (kullanım sonrası istatistiksel post-processing).
- Yeniden üretilebilirlik için beş kural: API > sohbet arayüzü; model sürümü + prompt + thinking düzeyi + parametrelerin belgelenmesi; ayrıntılı prosedür; kod/veri paylaşımı; seed ve temperature sabitleme.
- Uygulama eğitimleri soyut değil: Card (1993) eğitim getirisi modelinin ajan destekli tam replikasyonu (OLS 0,052 → 2SLS 0,132; ilk aşama F 13,256; N 3.010) ve LLM hakem yorumlarının eleştirel değerlendirmesi (Chen & Kim 2026, JOC).
- Araç listesi doğrudan kullanılabilir: refine.ink (AEA benimsemiş teknik ön-inceleme), OpenAIReview, CiteVerify, PDFMathTranslate, arena.ai / artificialanalysis.ai.
- Ölçüm/geçerlilik vurgusu Babbie (2021) ve Zhou vd. (2026) üzerinden kuruluyor: 'LLM'i yöntem olarak kullanmak, ölçüm hatası sorununu ortadan kaldırmıyor, taşıyor'.
- Sınır: slaytlar ders materyali, hakem denetimli bir makale değil; iddiaların çoğu başka çalışmalardan derleme — birincil kanıt için anılan kaynaklara gitmek gerekiyor.
- Teknik tutarsızlık: README 'shared at PHBS' diyor (PKU HSBC Business School olabilir), tweet ve slayt kapakları 'PKU' — aynı üniversitenin farklı birimleri; ders yeri doğrulanamadı.

## Turkey Context

Türkiye'deki araştırma pratiği için bu sunumun değeri, yöntem derslerinde eksik olan **kontrol listesi** boşluğunu doldurması.

**Birincisi, tez yöntem ekine doğrudan giren bir liste var.** Türkiye'de LLM'lerle metin sınıflandırma, duygu analizi ve açık uçlu soru kodlaması hızla yaygınlaştı; ama tezlerde çoğu zaman yalnızca "ChatGPT kullanıldı" yazıyor. Slayt 4.3'teki beş kural (API tercihi, sürüm/prompt/parametre belgelemesi, prosedür, kod-veri paylaşımı, seed-temperature sabitleme) Türkçe bir tez yöntem eki olarak birebir uyarlanabilir. Özellikle **sohbet arayüzü yerine API** kuralı, aynı analizin altı ay sonra tekrarlanabilmesi için kritik: sohbet arayüzünde model sürümü ve parametreler kullanıcıya görünmüyor.

**İkincisi, sentetik katılımcı tartışması Türkiye için erken ama geliyor.** Anket maliyetleri ve saha kısıtları nedeniyle "LLM'e Türk seçmen/öğrenci profili verip anket simüle etme" cazip. Sunum tam bu noktada dengeli: Argyle vd. (2023) gibi olumlu replikasyonların yanına **varyansın düşmesi** (Bisbee vd., 2024), **kültürel yanlılık** (Tao vd., 2024) ve **kimlik gruplarının yassılanması** (Wang vd., 2025) bulgularını koyuyor. Türkiye özelinde bu uyarı daha ağır: modellerin Türkçe ve Türkiye'ye özgü siyasal kimlik (Alevi-Sünni, Kürt-Türk, laik-muhafazakâr) temsilleri neredeyse hiç doğrulanmadı; sentetik veriyle üretilen "%X şöyle düşünüyor" iddiası, ölçüm hatasını gizleyen bir kolaylık olur.

**Üçüncüsü, araç listesi birebir taşınabilir.** refine.ink ve CiteVerify gibi araçlar Türkçe makale yazan araştırmacılar için de çalışır; PDFMathTranslate (yazarın kendi aracı) İngilizce literatürü Türkçe okumak için pratik. Buna karşılık **veri yerelleştirme** uyarısı gerekli: bu araçların bir kısmı bulut API'sine metin gönderiyor; KVKK kapsamında kişisel veri içeren saha metinlerini yüklemeden önce veri işleme koşulları kontrol edilmeli.

**Dördüncüsü, pedagojik boşluk.** Sunum PKU'da ayrı bir "Social Research Methods" modülünün parçası. Türkiye'de lisansüstü yöntem derslerinde LLM hâlâ çoğunlukla "intihal riski" başlığı altında ele alınıyor; geçerlilik/yeniden üretilebilirlik çerçevesiyle işlenmiyor. Bu slayt seti (CC lisansı olmasa da) Türkçeye uyarlanmış bir sürümle ders materyali olarak kullanılabilir — atıf ve izin gerekir.

---

## 🔗 İlgili Bağlantılar
### 🧠 İlgili Kavramlar
- [[concepts/olcum-araclari.md|Ölçüm Araçları (Polarization Measurement)]]
- [[concepts/siyaset-bilimi-metodolojisi.md|Siyaset Bilimi Metodolojisi]]
### 🏛 İlgili Kurum/Kişiler
- [[entities/github-com.md|Github Com]]
