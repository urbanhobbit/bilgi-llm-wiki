---
tags: [mcp, altyapı, sorgu]
sources: [mcp/wiki_server.py, scripts/build-weighted-graph.py]
created: 2026-11-21
updated: 2026-11-21
---

# MCP Sunucusu — Wiki'ye Soru Sormak

`mcp/wiki_server.py` — bilgi-llm-wiki'yi link biriktiren bir yerden **soru sorulabilen bir araca** dönüştürür.

## Kurulum

```bash
pip install 'mcp==1.9.4' 'pydantic==2.9.2' --break-system-packages
```

## Hermes'e bağlama

`~/.hermes/config.yaml` → `mcp_servers:` altına:

```yaml
  bilgiwiki:
    command: /usr/bin/python3
    args:
      - /home/E/bilgi-llm-wiki/mcp/wiki_server.py
    timeout: 60
```

Doğrulama: `hermes mcp test bilgiwiki` → 7 araç keşfedilmeli.

## Araçlar

- `search(query, limit)` — kavram/varlık/makale arama
- `get_concept(slug)` — kavram sayfası + ağırlıklı komşular
- `recent(days, tag)` — son N günde eklenenler
- `graph_neighbors(slug, k)` — normalize ağırlıklı komşuluk
- `data_health()` — veri sağlığı paneli
- `list_concepts(min_articles)` — kavram envanteri
- `bridges(min_score)` — köprü ve boşluk raporu

## Örnek sorgular

- "Son üç haftada yaş doğrulama üzerine ne geldi, özetle" → `recent(21)` + `search("yas dogrulama")`
- "Sosyal kutuplaşma en çok hangi kavramlarla bağlı?" → `graph_neighbors("sosyal-kutuplasma")`
- "Hangi konularda makale var ama bağ yok?" → `bridges()`

## Pitfall'lar

- `mcp` 2.x sürümüyle `Server.add_request_handler` API'si değişti ve `initialize_accepted`
  bayrağı legacy handshake'te oturmuyor → **mcp 1.9.4 + pydantic 2.9.2** kullan.
- pydantic 2.50 + mcp 1.x = `eval_type_backport` ImportError.
- `bundle.json` node ID'leri 65 karakterde kesiliyor → 20 raw dosya bundle'a girmiyor (fix bekliyor).

## Ağırlıklandırma

`scripts/build-weighted-graph.py` — ham ortak makale sayısı yerine:

```
score = PMI × log2(1 + raw)
```

`raw >= 5` eşiğiyle. 978 çiftten 241'i tutuldu. Bu sayede `siyaset-bilimi-metodolojisi`
gibi her şeye bağlanan kavramlar komşuluk listelerini doldurmuyor.
