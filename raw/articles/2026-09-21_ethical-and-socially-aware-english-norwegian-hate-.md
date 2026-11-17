---
type: raw_article
title: 'Ethical and Socially Aware English-Norwegian Hate Speech Detection: A Systematic
  Design Framework'
description: 'Ehtesham Hashmi ve Sule Yildirim Yayilgan (NTNU Gjøvik), **İngilizce–Norveççe
  nefret söylemi tespiti için altı aşamalı bir tasarım çerçevesi** öneriyor: etik
  sistem tasarımı, iki dilli veri toplama, y...'
resource: https://www.mdpi.com/2504-4990/8/9/292
tags:
- kurator
- high
timestamp: '2026-11-17T16:02:36Z'
source_file: 2026-11-17_hate-speech-detection-framework.json
category: KURATOR
priority: high
roles:
- method
- policy
published: '2026-09-21'
---

# Ethical and Socially Aware English-Norwegian Hate Speech Detection: A Systematic Design Framework

**Author(s):** Ehtesham Hashmi, Sule Yildirim Yayilgan (NTNU, Bilgi Güvenliği ve İletişim Teknolojisi Bölümü, Gjøvik)

**Published:** 2026-09-21

**Source:** [https://www.mdpi.com/2504-4990/8/9/292](https://www.mdpi.com/2504-4990/8/9/292)

## Summary

Ehtesham Hashmi ve Sule Yildirim Yayilgan (NTNU Gjøvik), **İngilizce–Norveççe nefret söylemi tespiti için altı aşamalı bir tasarım çerçevesi** öneriyor: etik sistem tasarımı, iki dilli veri toplama, yanlılık analizi ve azaltımı, açıklanabilir yapay zeka (LIME, Captum) ve paydaş doğrulaması. **14.008 örnek**lik iki dilli veri kümesi (11.528 İngilizce + 2.480 Norveççe, X ve Facebook'taki kamuya açık gönderilerden iki aylık toplama) çok-etiketli toksisite sınıflandırması (potansiyel nefret / saldırgan / ofansif / nötr) ve çok-görevli kimlik özniteliği çıkarımı (din, ırk, cinsiyet, cinsel yönelim) için kullanılıyor. Sınıf dengesizliği ve kimlik kaynaklı yanlılık; eşanlamlı artırma, kimlik-koşullu etiket-karşıtlığı artırması ve dengeli kayıp yeniden ağırlıklandırma ile azaltılıyor. Sonuç: **NorBERT-small makro F1 0,92, alt-küme doğruluğu 0,94** (artırma öncesi F1 0,64), dil bazında İngilizce 0,92 / Norveççe 0,89 / kod-değiştiren metin 0,87. Çerçevenin asıl katkısı model değil, **etik ve paydaş-temelli tasarım süreci**: üç paydaş grubu (STK'lar/medya/araştırmacılar; kolluk/govde; platformlar/geliştiriciler) ile gereksinim atölyeleri, GDPR uyumlu veri yönetişimi ve "cezalandırma aracı değil, önleyici müdahale hedefleme aracı" çerçevesi. Bu haliyle makale bir **yapay zeka yönetişimi** (AI governance) önerisi de sunuyor: paydaş gereksinimleri, GDPR uyumu, insan-döngüde doğrulama ve açıklanabilirlik katmanlarının modele içkin tasarımı. Sınırlılıklar açıkça yazılmış: veri kümesi GDPR nedeniyle **yayımlanamıyor** (yeniden üretilebilirlik yok), adillik yalnızca "flip rate" ile ölçülmüş, ayrı bir test bölümü yok, korpus İngilizce ağırlıklı, ve model **konuşma/şebeke düzeyi bilgiyi modellemiyor**.

## Key Points

- **Künye (Crossref + tam metin):** "Ethical and Socially Aware English–Norwegian Hate Speech Detection: A Systematic Design Framework", *Machine Learning and Knowledge Extraction* (MDPI) 8(9): 292, yayın 21 Eylül 2026, DOI 10.3390/make8090292, CC BY 4.0, 39 sayfa, 30 kaynak. Yazarlar: Ehtesham Hashmi, Sule Yildirim Yayilgan (NTNU, IIK, Gjøvik). Fon: Norveç Araştırma Konseyi, SOCYTI projesi, hibe no. 331736.
- **Tam metin okundu** (mdpi.com 403 verdi; PDF `mdpi-res.com/d_attachment/make/make-08-00292/article_deploy/make-08-00292.pdf` üzerinden 200, 11 sayfa gösterim / 39 sayfa metin, pdftotext ile çıkarıldı). Aşağıdaki tüm sayılar makale metninden.
- **Veri kümesi:** 14.008 örnek — İngilizce 11.528, Norveççe 2.480 (Tablo 6). İki aylık dönemde X ve Facebook'taki **kamuya açık** gönderilerden toplandı; sosyal öznitelik zenginleştirmesi için Kaggle cyberbullying veri kümesi (sayankr007) eklendi. Etiketleme insan-döngüde + model destekli (Llama 3 Uncensored ön-etiketleme, ardından uzman doğrulaması).
- **Etiketler ve uyum:** çok-etiketli PH (potansiyel nefret), PO (potansiyel ofansif), PA (potansiyel saldırgan), N (nötr); Cohen's κ PH 0,82, PO 0,79, PA 0,76, N 0,85 (Tablo 7).
- **Modeller:** ML/DL referans taban çizgileri + transformer ailesi. NorBERT-small (artırma + yeniden ağırlıklandırma sonrası) P 0,91 / R 0,92 / F1 0,92 / alt-küme doğruluğu 0,94 — taban çizgisi P 0,71 / R 0,61 / F1 0,64 / A 0,64'ten (Tablo 14-15). nb-BERT-base ve NorBERT-base F1 ~0,65 → 0,91; NorBERT-xs 0,87; NoTram 0,86; ELECTRA-base 0,87; mBART-base 0,86.
- **Dil bazlı kırılım (Tablo 16):** İngilizce P 0,92 / R 0,93 / F1 0,92; Norveççe 0,89; İngilizce–Norveççe kod-değiştiren metin 0,87 — Norveççe ve kod-değişiminde belirgin düşüş, yazarların kendi sınırlılık beyanında da vurgulanıyor.
- **Yanlılık azaltımı:** (1) eşanlamlı tabanlı artırma, (2) kimlik-koşullu etiket-karşıtlığı artırması (12 kural, Tablo 12: kimlik terimini değiştir, toksisite etiketi aynı kalmalı), (3) dengeli kayıp yeniden ağırlıklandırma. Tablo 17'de 50 ikili ikame için taban çizgisi vs artırılmış model duyarlılığı karşılaştırılıyor: duyarlılık birçok ikamede düşüyor, **ancak bazı kimlik çiftlerinde artık farklar sürüyor**.
- **Çok-görevli sosyal öznitelik çıkarımı:** görev düzeyinde toplam F1 yüksek, ama sınıf dengesizliği ağır — Budizm, Hispanic, Indigenous, Heteroseksüel, Aseksüel gibi sınıflarda sınıf-bazlı performans güvenilir biçimde değerlendirilemiyor (Tablo 20).
- **Araç (Tablo 5) ne yapıyor, ne yapmıyor:** metin girişi (çevrimdışı/toplu), ön işleme, toksisite sınıflandırma, kimlik özniteliği çıkarımı, LIME token açıklaması ve **demografik ısı haritası**. Gerçek zamanlı veri çekme ve operasyonel konuşlandırma **gelecek iş** olarak yazılı: "full deployment remains future work, requiring a real-time interface".
- **Sınırlılıklar (Bölüm 7, aynen):** veri kümesi gizlilik/GDPR nedeniyle yayımlanamıyor → doğrudan yeniden üretilebilirlik yok; adillik değerlendirmesi yalnızca FR (flip rate) ve tahmin olasılığı değişimiyle sınırlı — demografik parite, eşitlenmiş odds, alt-grup hata farkları ve kesişimsel adillik kapsanmıyor; sosyal öznitelik görevlerinde ağır sınıf dengesizliği; **ayrı bir doğrulama bölümü kullanılmadı** (held-out bölümü artırmadan önce ayrıldı ama epoch düzeyinde değerlendirmede incelendi → "tamamen dokunulmamış test seti" sayılmaz); korpus İngilizce ağırlıklı; **konuşma/şebeke düzeyi bilgi modellenmiyor**; güven/şeffaflık/açıklama etkinliği için nicel kullanıcı çalışması yok.
- **⚠️ Haber kaynağı ile makale arasında üç uyuşmazlık (claim-check):** (a) HSNW, aracın "nefret söylemi örneklerini birbirine bağlayan, ifadelerin **görsel bir şebekesini** üreten" bir işlevi olduğunu ve "nefret söyleminin nereden doğduğunu, nasıl devralındığını" gösterdiğini yazıyor — makalede böyle bir işlev yok; tek görselleştirme demografik ısı haritası ve makale açıkça "does not model conversational or network-level information" diyor. (b) HSNW verinin "Facebook, **Reddit** ve Twitter"dan toplandığını söylüyor; makalede **Reddit hiç geçmiyor** (39 sayfada 0 eşleşme), kaynak X + Facebook + Kaggle cyberbullying veri kümesi. (c) HSNW "14.000 cümle" diyor; makalede 14.008 **gönderi/örnek** (cümle değil). HSNW'nin doğru aktardığı nokta: "big massacres always begin with small actions and language" sözü makalede Adama Dieng'e (BM Soykırımın Önlenmesi Özel Danışmanı, kaynak [6]) atfen geçiyor.
- **HSNW'nin çerçevesi makalede yok:** Norveç'te 2012'den beri bildirilen nefret suçlarının "beş kat" artması, bunların ~%40'ının nefret söylemi olması, PST'nin siyasetçi/yorumculara yönelik tehdit artışı ve Gaute Skjervø / Marian Hussein örnekleri **haber metnine ait**; makalenin kendi ampirik bulgusu değil. Kayıt bu sayıları makaleye atfetmiyor.

## Turkey Context

Türkiye açısından üç ayrı katman var. **Birincisi, hukuki çerçeve:** makale Norveç Ceza Kanunu § 185'i (nefret söylemi suçu) ve BM Medeni ve Siyasi Haklar Sözleşmesi'ni referans alıyor; Türkiye'de karşılığı TCK 216 ve 5237 sayılı kanunun nefret/ayrımcılık hükümleri. Yazarların "cezalandırma değil önleyici müdahale hedefleme" çerçevesi, Türkiye'de nefret söylemiyle mücadelede baskın olan **ceza-adli yaklaşımına** bir alternatif sunuyor: hangi ortamların (yerel Facebook grupları, X hashtag'leri, TikTok yorumları) önleyici programlara ihtiyaç duyduğunu tespit etmek. **İkincisi, dil ve veri:** Türkçe, Norveççe gibi eklemeli ve kod-değişimine açık bir dil; makalenin kendi bulgusu Norveççe ve kod-değiştiren metinde F1'in 0,92'den 0,87-0,89'a düştüğünü gösteriyor — yani çerçeve Türkçeye taşınacaksa **Türkçe morfoloji + Arapça/Kürtçe kod-değişimi** için ayrı bir değerlendirme şart. Türkiye'de kamuya açık, etik kurul onaylı bir Türkçe nefret söylemi veri kümesi neredeyse yok; Hrant Dink Vakfı'nın nefret söylemi izleme raporları nitel/toplam düzeyinde kalıyor, makine öğrenmesi için etiketli korpus üretmiyor. Makalenin veri kümesini **GDPR gerekçesiyle yayımlamaması**, Türkiye'de KVKK gerekçesiyle aynı duvara çarpacak araştırmacılar için önemli bir uyarı: çerçevenin aktarılabilir kısmı model değil, **veri yönetişimi ve paydaş süreci**. **Üçüncüsü, yapay zeka yönetişimi:** makale AB Yapay Zeka Yasası'nın "yüksek risk" mantığına paralel bir etik tasarım katmanı (paydaş gereksinimleri, GDPR, açıklanabilirlik, insan-döngüde) kuruyor; Türkiye'nin yaklaşan yapay zeka kanunu tartışmasında bu tür **kolluk kullanımı için ayrı etik denetim** şartı henüz yok. Uyarı: makale hiçbir Türkiye verisi içermiyor; bu not bir **transfer edilebilirlik değerlendirmesi**, ampirik aktarım değil.

## 🏷 Retorik Roller

- 🧩 **Yöntem**
- 🏛 **Politika Önerisi**

---

## 🔗 İlgili Bağlantılar
### 🧠 İlgili Kavramlar
- [[concepts/nefret-soylemi.md|Nefret Söylemi]] — makalenin tespit etmeyi amaçladığı olgu; Türkçe bağlam notu
- [[concepts/yapay-zeka-yonetisimi.md|Yapay Zeka Yönetişimi]] — etik tasarım, paydaş doğrulaması ve kolluk kullanımı katmanı
- [[concepts/cocuk-veri-gizliligi.md|Çocuk Veri Gizliliği]]
