---
type: entity
title: AI Anthropology Toolkit
description: Nitel araştırma için açık kaynak hesaplamalı araç seti; MCP sunucusu üzerinden kod kitabı, transkript bölütleme ve tematik kodlama ajanlarını koordine ediyor.
tags:
- software
- qualitative-research
- mcp
- open-source
timestamp: '2026-11-18T00:00:00Z'
created: '2026-11-18'
updated: '2026-11-18'
sources:
- raw/articles/2026-02-08_multi-agent-ethnography-post-conventional-anthropo.md
---

# AI Anthropology Toolkit

Matt Artz tarafından geliştirilen, **çok-ajanlı etnografya** yaklaşımını uygulayan açık kaynak araç seti.

**Doğrulanmış teknik künye (18 Kas 2026):**
- GitHub: `MattArtzAnthro/AI-Anthropology-Toolkit` — 27 yıldız, 7 çatal, oluşturma 2 Ağu 2025, son push 17 Kas 2026
- PyPI: `ai-anthropology-toolkit` **v3.11.1** (Python ≥3.10)
- MCP sunucusu: `ai-anthro-mcp`; `uvx --from "ai-anthropology-toolkit[data,api]==3.11.1" ai-anthro-mcp` ile Claude Code / Codex CLI / Gemini CLI'ye eklenebiliyor
- Versiyonlar: V1 notebook'lar → **V2 MCP ajanları** → V3 web uygulaması; Zenodo'da arşivli

**Üç ajan:** Qualitative Codebook Builder · Interview Transcript Semantic Chunker · Coding and Thematic Analysis. Ayrıca veri toplama (OpenAlex, CrossRef, PubMed, YouTube, podcast RSS), atıf biçimlendirme ve kod ağı analizi (GEXF dışa aktarım) araçları.

## İlgili Makaleler
- [[raw/articles/2026-02-08_multi-agent-ethnography-post-conventional-anthropo.md|Artz (2026) — Multi-Agent Ethnography]]
