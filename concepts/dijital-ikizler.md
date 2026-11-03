---
type: concept
title: Dijital İkizler (Program Değerlendirmede)
description: 'Gözlemsel/idari veriyle bir programın counterfactual sonucunu modelleyip gerçek deney sonuçlarıyla doğrulama: Chetty ve ark. (2026) RCT tabanlı doğrulama, Cornish ve ark. (2023-2026) nedensel falsifikasyon yaklaşımı.'
tags:
- akademik
- metodoloji
- nedensel-cikarim
- program-degerlendirme
- makine-ogrenmesi
timestamp: '2026-11-03T00:00:00Z'
created: 2026-11-03
updated: 2026-11-03
confidence: medium
---
# Dijital İkizler (Program Değerlendirmede)

Bir programın/deneyin, **müdahale olmasaydı ne olurdu** sorusunu zengin gözlemsel veriyle modelleyen ve bu modeli gerçek deneysel sonuçlarla sınayan yaklaşım. Mühendislikteki "dijital ikiz" benzetmesinden gelir: gerçek sistemin, üzerinde deney yapılabilen bir simülasyonu.

**Mantık:** Programa katılanlarla katılmayanları karşılaştırmak (seçim yanlılığı) klasik olarak güvenilmez sayıldı — LaLonde (1986) sonrası literatürün ana sonucu buydu. Dijital ikiz yaklaşımı bu sonucu büyük veriyle yeniden açıyor: eğer kovaryatlar yeterince zenginse (önceki kazanç geçmişi, demografi, mekân, sektör), makine öğrenmesiyle kurulan counterfactual, rastgele atamanın sağladığı karşılaştırma grubuna yaklaşabilir.

**İki doğrulama geleneği:**
- **RCT tabanlı doğrulama (ampirik):** Chetty, Fogel, Katz, Noray, Porter, Reisinger (2026, Opportunity Insights) — 37 RCT kullanarak gözlemsel tahmincinin *yanlılık dağılımını* kestiriyor; RMSE RCT'ninkine eşdeğer çıkınca tahminci "deneysel olarak doğrulanmış dijital ikiz" sayılıyor. Parametrik tahmincilere göre RMSE'de %60 azalma.
- **Nedensel falsifikasyon (kuramsal):** Cornish, Taufiq, Doucet, Holmes (arXiv:2301.07210, JMLR) — gözlemsel veri, unconfoundedness gibi sakat varsayımlar olmadan bir ikizi *sertifiye edemez*; bu yüzden ikizin doğru **olmadığı** durumları aramak gerekir (falsification prosedürü).

**Asgari koşullar:**
1. Tüm nüfusu ya da geniş bir karşılaştırma havuzunu kapsayan **idari veri** (vergi, sosyal güvenlik, sağlık kaydı).
2. Yüksek boyutlu, gürültüsüz **kovaryat seti** — model esnekliğinin kaynağı burada.
3. Doğrulama için **mevcut RCT'ler** (tek bir RCT yetmez; yanlılık dağılımı için çok sayıda deneme gerekir).
4. Çapraz uyum (cross-fitting) ve DML gibi çift-yönlü düzeltmeli tahminciler.

**Tuzaklar:**
- **Dış geçerlilik:** Chetty ve ark. deneysel örneklem dışına çıktıklarında etkilerin aynı program içinde bile mekâna ve yıla göre değiştiğini buldu — tek program-şehir-yıl hücresinden genelleme yapılamaz.
- **Doğrulama verisinin seçiciliği:** doğrulama seti hangi program türlerini içeriyorsa, ikiz yalnızca o alanda güvenilirdir (Chetty: iş gücü eğitimi).
- **Veri rejimi:** Türkiye gibi ülkelerde idari veriye araştırmacı erişimi KVKK ve kurumsal kısıtlarla kapalı → yöntem bugün uygulanamaz.
- **Mekanizma körlüğü:** ikiz etkiyi tahmin eder, *neden* olduğunu açıklamaz; mekanizma için nitel araştırma gerekir (J-PAL pratikleri).
- **Ticarileşme/çıkar:** yöntemi geliştiren araştırmacının aynı yöntemle yatırım yapan bir kuruluşu yönetmesi (Chetty → Opportunity Capital) çıkar beyanı gerektirir.

**Bağlantılı kavramlar:** [[concepts/arastirma-sonucu-tahminleme.md|Araştırma Sonucu Tahminleme]], [[concepts/siyaset-bilimi-metodolojisi.md|Siyaset Bilimi Metodolojisi]], [[concepts/surec-takibi-ve-nedensel-mekanizma.md|Süreç Takibi ve Nedensel Mekanizma]]

## İlgili Makaleler
- [[raw/articles/2026-11_digital-twins-validated-with-37-rcts.md|Digital Twins Validated With 37 RCTs]] — Chetty ve ark. (Kasım 2026): 327 milyon kişinin vergi kaydı, 105.216 katılımcı, 37 RCT ile doğrulama, RMSE'de %60 azalma.
- [[raw/articles/2026-08-08_causal-falsification-of-digital-twins.md|Causal Falsification of Digital Twins]] — Cornish ve ark. (arXiv:2301.07210): ikiz doğrulamasının nedensel çıkarım olarak formüle edilmesi ve falsifikasyon prosedürü.
