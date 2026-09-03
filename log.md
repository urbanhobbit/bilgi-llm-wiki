## [2026-08-31] ingest | Haftalık Bülten Entegrasyonu (Hafta 35/2026)
- Raw: [[raw/articles/2026-08-31_cocuk_dijital_kurator_bulteni.md]] — KURATOR Weekly Bulletin on Children and Digital World (Week 35/2026)
- KURATOR Topics: Telegram feed empty since 08-29 (4 consecutive empty ingestions); bulletin built from direct source sweep (arXiv API + accessible policy/news sources). Focus: global social-media-ban wave — UK under-16 ban announcement (GOV.UK 17 Jul 2026; Spring 2027 implementation; Australia model; messaging excluded; livestreaming/stranger-contact restrictions), Türkiye under-15 law details (Habertürk 1 May 2026; RG publication; ~6-month entry into force ≈ Nov 2026; age verification; separated service for 15+; parental controls; game-platform duties; BTK sanction ladder incl. 50% bandwidth reduction), EU Commission age-verification Recommendation 29 Apr 2026 (31 Dec 2026 MS deadline; DSA Art. 28), Meta $17.1B US-state settlement (NYT 26-28 Aug 2026), UK child deepfake reports record 420 H1 2026 (Guardian/IWF 8 Aug 2026), US school phone bans 38 states + DC (K-12 Legal Insights 6 Aug 2026)
- AKADEMİK ÖZEL Topics: 7 papers — Ramokapane et al. 'Children Are Not the Enemy: Child-Fit Security' (arXiv 2606.17957, Jun 2026), Nansen et al. 'From Phreaking to Sneaking' age-verification circumvention (arXiv 2605.00368, Australia), Zhang et al. XR games safety (arXiv 2604.24601), Bertaglia et al. ChildSafeAds YouTube commercial content (arXiv 2608.19165), Dai & Ouyang screen time/ADHD N=50,231 (arXiv 2508.10062), Blum et al. suicidal-ideation prediction (arXiv 2509.03530), Chu et al. BigTokDetect (arXiv 2508.06515); reading list Wang 2021, Cook 2022, Ta 2024, Zhao 2018
- Access: arXiv API OK (8 queries); gov.uk/guardian/haberturk/fpf/techpolicy.press fetched via urllib (200 OK); reuters/nytimes/k12legalinsights/ncsl blocked (401/403) — metadata-based classification
- Agent: KURATOR Weekly Bulletin Cronjob (source sweep, feed empty)

## [2026-08-29] ingest | Haftalık Bülten Entegrasyonu (Hafta 35/2026)
- Raw: [[raw/articles/2026-08-29_cocuk_dijital_kurator_bulteni.md]] — KURATOR Weekly Bulletin on Children and Digital World (Week 35/2026)
- Raw: [[raw/articles/2026-08-29_akademik_ozel.md]] — AKADEMİK ÖZEL TARAMA Weekly Screening (2026-08-29)
- KURATOR Topics: No direct children/digital (KURATOR) links this week (23-28 Aug 2026 stream was academic-heavy, 9/9 academic). Adjacent youth/digital intersections highlighted: Llobet & Rosen 'Futuring practices in and against the unequal distribution of futures' (Children's Geographies, DOI 10.1080/14733285.2026.2704529 — direct children's research; two-site ethnography Buenos Aires informal settlement + UK unaccompanied migrant children), Schulz et al. 'Online Discourse is Falsely Polarized by Self-Selection' (PsyArXiv 7z69m_v1; 1.7M posts, 40 countries, N=49,222; extreme views over-represented 6-22%), Elfes, Bastos & Aiello 'Measuring Narrative Polarization' (PNAS Nexus 5(8) pgag270; 212 YouTube videos + 90,029 comments), Bauer et al. 'Group Identity and Belief Formation' (Economic Journal ueag105; label-removal cuts out-group info avoidance 50%), Akser & Baybars 'Repressed media and illiberal politics in Turkey' (SEBSS, DOI 10.1080/14683857.2022.2088647)
- AKADEMİK Topics: 9 papers — Elfes et al. narrative polarization (PNAS Nexus), Larreguy & Tiburcio counter-attitudinal info consumption (EJ ueag104; Mexico ~2,500 panel), Soroka & Wlezien parallel partisan responsiveness (PSQ qqag064; 4-decade thermostatic model), Bauer et al. group identity (EJ ueag105), Abramowitz & Saunders 'Is Polarization a Myth?' (JOP 2008; 1952-2004 ANES), Llobet & Rosen futuring children (Children's Geographies), Acemoglu et al. economic misperceptions & democracy support (NBER WP 35644; Argentina pre-registered N=11,377; academic sources/gazettes beat social media), Schulz et al. false polarization (PsyArXiv), Akser & Baybars Turkey media repression (SEBSS)
- Scrapling wiki ingestion test: 33% block rate (3/9: LinkedIn safety redirects to T&F doi.org/10.1080/14733285.2026.2704529 + tandfonline 10.1080/14683857.2022.2088647, OUP PNAS Nexus pgag270 — 404 with ~320KB LinkedIn wrapper; X posts 200/99-205KB with 1.0-3.4K chars content) — below 50% threshold, metadata-based classification for blocked academic publishers
- Agent: Weekly Bulletin Integration Cronjob

## [2026-08-28] ingest | FIMI kavram sayfası eklendi
- Concept: [[concepts/fimi.md|FIMI (Foreign Information Manipulation and Interference)]] — AB/EEAS çerçevesi; tanım, aktörler (Rusya/Çin), Türkiye bağlamı (CoE Kas 2025 raporu), ilgili kavram bağlantıları
- Index: Concepts bölümüne FIMI + 4 eksik ilgili kavram eklendi (dezenformasyon, geopolitical, election-interference, ai-generated)
- Scripts: CONCEPT_KEYWORDS'a "fimi" eklendi (okf_ingestion.py + add_wikilinks.py)
- Bundle + viz.html yeniden üretildi (add_wikilinks → okf_viz_generator)
- Agent: Manuel (kullanıcı isteği)

## [2026-08-22] ingest | Haftalık Bülten Entegrasyonu (Hafta 34/2026)
- Raw: [[raw/articles/2026-08-22_cocuk_dijital_kurator_bulteni.md]] — KURATOR Weekly Bulletin on Children and Digital World (Week 34/2026)
- Raw: [[raw/articles/2026-08-22_akademik_ozel.md]] — AKADEMİK ÖZEL TARAMA Weekly Screening (2026-08-22)
- KURATOR Topics: No direct children/digital (KURATOR) links this week (16-21 Aug 2026 stream was academic-heavy). Adjacent youth/digital intersections highlighted: Kutun, Binbuğa & Yılmaz 'New politics of the social and authoritarianism in the Near East' (TWQ special issue — youth/gender movements incl. Boğaziçi protests), Hoes & Altay 'Debriefings in misinformation research' (PSRM; N=896 pre-registered; only specific fact-check debriefings reduce misperceptions), Gelman, Bullock & Sood 'Fragility of the manipulable-voter model', Canalejo-Molero et al. 'Priming European values does not reduce affective polarization' (16 countries, ~27,000 participants), Farrell & Newman 'Janus Face of the LIIO' (IO 75(2))
- AKADEMİK Topics: Wysocki, Lawson & Rhemtulla 'Statistical Control Requires Causal Justification' (AMPPS 5(2), 2022), Adcock & Collier 'Measurement Validity' (APSR 95(3), 2001), Roller 'Analytical Critical Thinking in Qualitative Research' (RDR, 19 Aug 2026), Gelman blog 'Improvement in political analysis in the past 25 years' (18 Aug 2026), Handby 'Defending Methodological Anarchism' (JOP), Kipnis reviews 'Against Affect' (Critical Inquiry, 20 Aug 2026), Grossmann 'How Social Science Got Better' (OUP 2021), Schickler & Rodriguez 'College Campus and the Culture War' (SAPD, 2026), Bonin 'Rise and closure of liberal democracy' (IPSR, 2026), Kutun et al. TWQ special issue, Kuehnhanss & Scharfbillig 'Identity threat, values, attitudes' (Political Psychology 47(4)), Fowler et al. 'How Americans Explain Party ID' (POQ, 2026), Canalejo-Molero et al. (EPSR, 2026), Farrell & Newman (IO 2021)
- Scrapling wiki ingestion test: 20% block rate (2/10: LinkedIn safety redirects to SAGE journals.sagepub.com + Taylor & Francis tandfonline.com 404/blocked; X posts 200/73-158KB, LinkedIn post 200/104KB) — below 50% threshold, metadata-based classification for blocked academic publishers
- Agent: Weekly Bulletin Integration Cronjob

## [2026-08-15] ingest | Haftalık Bülten Entegrasyonu (Hafta 33/2026)
- Raw: [[raw/articles/2026-08-15_cocuk_dijital_kurator_bulteni.md]] — KURATOR Weekly Bulletin on Children and Digital World (Week 33/2026)
- Raw: [[raw/articles/2026-08-15_akademik_ozel.md]] — AKADEMİK ÖZEL TARAMA Weekly Screening (2026-08-15)
- KURATOR Topics: UNICEF x GSMA 'Life Online' survey (211,300+ U-Reporters; 35% online vs 27% face-to-face identity comfort; 28% trust AI info without verification — under-18 most susceptible; ~3/5 say children's needs rarely considered in digital policy), MIT Media Lab 'Dialogues with AI' study (arXiv:2510.01537; +21% immediate improvement but −15.3% unsupported performance at week 4 — AI dependency paradox), Kasirzadeh & Gabriel 'Agentic profiles for effective AI governance' (Nature 656:320-328; autonomy/efficacy/goal complexity/generality), Yang 'Misreading social identity theory' (Political Studies Review; discrimination ≠ dislike, conflict-centred framework)
- AKADEMİK Topics: Kopstein 'Polarization and Political Violence' (Journal of Democracy 37(3):38-49; polarization necessary-but-not-sufficient for violence), Siegel & Weiss 'Shooting the Messenger' (APSR R&R update 2026-08-11; press attacks → backlash, +10% SD sign correction), de Benedictis-Kessner et al. 'Partisan Polarization in Local Politics' (APSR R&R; 491 mayors + 25,521 residents; elites 26pt vs public 13pt polarization; climate 52pt gap), Ferrara 'Practitioner's Guide to LLMs in Economic History' (NBER WP 35374), Rani et al. 'Dialogues with AI' (MIT), Causal Falsification of Digital Twins (JMLR; Cornish et al. arXiv:2301.07210), Hetherington et al. worldview & COVID-19 (Political Psychology), Van Bavel interview (Eurasia Review), Lula helplessness discourse (Reactionary Politics WP No.4), Elites as Democratic Gatekeepers (SocArXiv), SOUTHMOD at 10 (UNU-WIDER)
- Scrapling wiki ingestion test: 30% block rate (3/10: Wiley, Eurasia Review, reacpol.net 403 Cloudflare; X, chagaiweiss PDF, arXiv 200 OK) — below 50% threshold, metadata-based classification for blocked academic publishers
- Agent: Weekly Bulletin Integration Cronjob

## [2026-08-08] ingest | Haftalık Bülten Entegrasyonu (Hafta 32/2026)
- Raw: [[raw/articles/2026-08-08_cocuk_dijital_kurator_bulteni.md]] — KURATOR Weekly Bulletin on Children and Digital World (Week 32/2026)
- Raw: [[raw/articles/2026-08-08_akademik_ozel.md]] — AKADEMİK ÖZEL TARAMA Weekly Screening (2026-08-08)
- KURATOR Topics: Nature Human Behaviour longitudinal study (5,227 Italian students, early social media use harms learning outcomes, smartphone pervasiveness mediator), European Parliament media literacy & digital learning resolution (447 votes, 2026-07-07), Finland 2026 National Media Education Policy (OKM 2026:36, 3 goals + 18 measures, Kuvi coordination), UN Global Principles for Information Integrity (5 principles, humane information ecosystem), DASY Digital Addiction Scale for Turkish Youth (SAGE Open Q1, 23 items, 3 factors, α=.946)
- AKADEMİK Topics: Druckman et al. affective polarization measurement review (AP 1978 20.38°→2024 51.64°, survey mode effects), Generative Grounded Theory (Schmitt et al. JCP, 7-step GenAI-grounded theory), AI-assisted pre-bunking election misinformation (Linegar et al. RSOS, pre-registered N=4,293), China Backlash narrative discourse (Geyiktepe & Rodrik NBER WP 35539, bottom-up narrative diffusion), real-news party cues (Skytte AJPS, n=12,177, modest 3.3% effects), democratic backsliding public support (Choi, Democratization), Lyotard post-truth narratives (Baier TCS), electoral campaigns & news polarization (Menéndez JMP, Spanish Media Monitor), literature review component classification (Bolanos-Burgos et al. PeerJ CS, Sci-Sentence benchmark, 37 LLMs, 96%+ F1)
- Scrapling wiki ingestion test: 50% block rate (5/10: T&F, SAGE, EDMO publications, Royal Society, PeerJ 403 Cloudflare; UN, NBER, Nature, Economic Misfit, Finland 200 OK) — metadata/Crossref-based classification for blocked academic publishers
- Agent: Weekly Bulletin Integration Cronjob



## [2026-08-03] ingest | Haftalık Bülten Entegrasyonu (Hafta 32/2026)

- Raw: [[raw/articles/2026-08-03_cocuk_dijital_kurator_bulteni.md]] — KURATOR Weekly Bulletin on Children and Digital World (Week 32/2026)
- Topics: Australia under-16 ban 3-month eSafety report (80%+ teens still on social media, age assurance not enforced, penalties doubled), Turkey 15-under social media ban law in force (Resmi Gazete 2026-05-01, Sosyal Hizmetler Kanunu, age verification + parental controls + game platforms), Austria under-14 ban agreement (SPÖ/ÖVP/NEOS, EU-level age limit goal), AI-CSAM legal battle (SpaceXAI/Stability AI class action expanded, UNICEF 'deepfake abuse is abuse', UN escalating AI threats), Child-fit security paradigm (arXiv 2606.17957), UK OSA privacy risk study (arXiv 2606.05273), CAREBench child-safety benchmark (500 prompts/12 categories), EU CSAR voluntary detection position, OECD adolescent social-emotional wellbeing, UNESCO Growing Up in a Connected World family guide, California school phone limits, YDPR youth digital policy repository
- Agent: KURATOR Weekly Bulletin Cronjob

## [2026-08-01] ingest | Haftalık Bülten Entegrasyonu (Hafta 31/2026)
- Raw: [[raw/articles/2026-08-01_cocuk_dijital_kurator_bulteni.md]] — KURATOR Weekly Bulletin on Children and Digital World (Week 31/2026)
- Raw: [[raw/articles/2026-08-01_akademik_ozel.md]] — AKADEMİK ÖZEL TARAMA Weekly Screening (2026-08-01)
- Topics: UK under-16 social media ban (Starmer), KOSA Senate 91-3, Massachusetts under-14 ban Oct 2026, China content classification, AADC EdTech audit (5 GenAI tools non-compliant), Pew/BBC parent-teen AI perception gap, Turkey 15-under regulation framework (Bakan Göktaş), misinformation-as-strategy (Ecker et al. TiCS), synthetic contact AI reduces cross-partisan animosity (arXiv 2607.02181), GPT vs BERT/LIWC stance detection, echo chambers agent-based model, polarization of trust in science, cultural capital & productivity of ideas
- Scrapling block rate: 40% (6/10 links accessible) — automatic extraction viable
- Agent: Weekly Bulletin Integration Cronjob

## [2026-07-25] ingest | Haftalık Bülten Entegrasyonu (Hafta 30/2026)
- Raw: [[raw/articles/2026-07-25_cocuk_dijital_kurator_bulteni.md]] — KURATOR Weekly Bulletin on Children and Digital World (Week 30/2026)
- Raw: [[raw/articles/2026-07-25_akademik_ozel.md]] — AKADEMİK ÖZEL TARAMA Weekly Screening (2026-07-25)
- Topics: Global social media bans (Massachusetts, Brazil, China), AI use by teens (Pew Research, BBC Future), Turkey social media regulation framework (Bakan Göktaş), 5Rights GC25 5th year anniversary, Australia ban research briefing (Molly Rose Foundation), age verification systems, UK Parliament research briefing, EU DSA, prebunking field study, disinformation management
- Agent: Weekly Bulletin Integration Cronjob

## [2026-07-25] ingest | EDMO Weekly Pulse — 24 July 2026
- Raw: [[raw/articles/2026-07-24-edmo-weekly-pulse.md]] — EDMO Weekly Pulse: EDMO defending election integrity via the RRS: True transparency and censorship nonsense
- Source: https://edmo.eu/pulse/
- Agent: Hermes cronjob (EDMO Weekly Pulse Ingestion)
## [2026-07-18] ingest | EDMO Weekly Pulse - 16 July 2026
- Raw: [[raw/articles/2026-07-16-edmo-weekly-pulse.md]] — So much the worse for the facts?
- Topics: Disinformation creating "alternative facts", FIFA World Cup racist/Islamophobic disinformation, FIFA racism monitoring stats, Algeria-Austria match-fixing false allegations, Infantino AI deepfake, AI funeral images Iran Khamenei, US President shared AI-manipulated Iran strike photo, Anti-NATO disinformation Ankara summit, wildfire conspiracy theories targeting renewable energy
- Sections: ON THE RISE (So much the worse for the facts?), ZOOM-IN (3 fact-checks: World Cup racism, match-fixing, Infantino deepfake), GLOBAL PULSE (4 items: AI Iran funeral, US Iran photo, Anti-NATO Ankara, wildfire renewables), ON A DIFFERENT NOTE (BENEDMO white paper on AI in disinformation)

## [2026-07-11] ingest | EDMO Weekly Pulse - 09 July 2026
- Raw: [[raw/articles/2026-07-09-edmo-weekly-pulse.md]] — Europe Caught in the Crossfire of NATO-related Disinformation
- Topics: NATO Ankara summit disinformation, US/Russian anti-NATO narratives, Ukraine drone false-flag claims, fake BBC French mercenary story, Germany-Ukraine aid housing myth, AI-generated German election law video, Romanian coordinated Facebook amplification, Pechory Lavra blame deflection, Palestinian flag KGB myth, RT sanctions evasion on X, platform monetization of repeat disinformers
- Sections: ON THE RISE (NATO crossfire), ZOOM-IN (3 fact-checks: drone, mercenaries, housing), ELECTION BEAT (Germany AI video, Romania Facebook coordination), GLOBAL PULSE (Pechory Lavra, Palestinian flag, RT on X), ON A DIFFERENT NOTE (Meta monetization enforcement failure)

## [2026-07-09] ingest | Bulutgil & Mylonas — Theory before method
- Raw: [[raw/articles/bulutgil-mylonas-methodological-pluralism-2026.md]] — H. Zeynep Bulutgil & Harris Mylonas (2026), "Theory before method: The case for methodological pluralism in political science", International Political Science Review, SAGE. DOI: 10.1177/01925121261445570. 82 references. Popperian framework for comparative theory testing.
- New entity: [[entities/journals-sagepub-com.md]] — SAGE Publications (akademik yayınevi)
- Updated index.md (+2 pages, 138 total)

## [2026-07-08] ingest | IPIE Report: Mis/Disinformation Resilience Index Review
- Raw: [[raw/articles/2026-07-08-ipie-misinformation-resilience-index-review.md]] — IPIE TP2026.1: 10 indexes compared (GDI, MRMI, DRI, GVI, GPI, FIMI, ROD, EV, MLI, MVI)
- New entity: [[entities/ipie.md]] — International Panel on the Information Environment
- New concept: [[concepts/misinformation-resilience-indexes.md]] — Comparative review with typology and methodology analysis
- Updated index.md (+2 pages, 136 total)

## [2026-07-20] ingest | KURATOR Haftalık Bülten: Çocuklar ve Dijital Dünya (Hafta 29/2026)
- Raw: [[raw/articles/2026-07-20_cocuk_dijital_kurator_bulteni.md]] — KURATOR Weekly Bulletin on Children and Digital World
- Topics: Australia social media ban 6-month assessment (80% still accessing, 5M+ accounts removed, $99M penalty proposed), UK Online Safety Act implementation gaps (50% girls still at risk, Internet Matters report), Turkey 15-year-old regulation framework, Aura Digital Wellbeing Index 2026 (usage pattern > screen time), Child-Fit Security paradigm (arXiv 2606.17957), AI Chatbot Age Gating (arXiv 2602.10251), TikTok Kids Mode audit, school phone bans in California/Michigan/Massachusetts/Pennsylvania/UK, IEEE 2089.1 age verification certification, FTC TruHeight penalty, 5Rights GC25 5-year assessment, ParentZone reports, NYT AI attention hacking concern, Candice Odgers Guardian interview questioning ban efficacy
- Sections: Yönetici Özeti, Araştırma Konuları (4 themes), Akademik Kaynaklar (6 papers), Haberler ve Raporlar (7 items), Karşılaştırmalı Analiz (table), Öneriler (8 items), İstatistikler (8 data points), Kaynakça (17 items)
- Updated index.md (+1 page, 139 total)
## [2026-07-21] ingest | OKF Auto-Ingestion
- Raw: [[raw/articles/2026-07-21_is-misinformation-all-around-us-citizens-perceptio.md]] — Is Misinformation All Around Us? Citizens’ Perceptions of Misinformation Nearness Regarding Its Span, Availability, and Accessibility
- Source files: 2026-07-21_tandf-misinformation-nearness.json
- Agent: OKF Ingestion Pipeline

## [2026-07-22] ingest | OKF Auto-Ingestion
- Raw: [[raw/articles/2026-07-22_public-responses-to-atrocities-depend-on-partisans.md]] — Public responses to atrocities depend on partisanship and context, not legal labels
- Source files: 2026-07-22_pnas-atrocities-labels.json
- Agent: OKF Ingestion Pipeline

## [2026-07-22] ingest | OKF Auto-Ingestion
- Raw: [[raw/articles/2025-05-23_addressing-the-digital-determinants-of-youth-menta.md]] — Addressing the digital determinants of youth mental health and well-being: policy brief
- Source files: 2026-07-22_who-youth-digital-mental-health.json
- Agent: OKF Ingestion Pipeline

## [2026-07-22] ingest | OKF Auto-Ingestion
- Raw: [[raw/articles/2026-07-21_france-set-to-pass-eu-first-ban-on-social-media-fo.md]] — France set to pass EU-first ban on social media for under-15s
- Source files: 2026-07-22_france-social-media-ban-under15.json
- Agent: OKF Ingestion Pipeline

## [2026-07-22] ingest | OKF Auto-Ingestion
- Raw: [[raw/articles/2026-07-22_hub-na-n-g-the-library-children-and-young-people-s.md]] — Hub na nÓg — The Library: Children and Young People's Participation Resources
- Source files: 2026-07-22_hubnanog-library-child-participation.json
- Agent: OKF Ingestion Pipeline

## [2026-07-22] ingest | OKF Auto-Ingestion
- Raw: [[raw/articles/2026-07-21_can-ai-help-us-find-the-books-that-bridge-politica.md]] — Can AI Help Us Find the Books That Bridge Political Divides?
- Source files: 2026-07-22_ai-bridge-political-divides-books.json
- Agent: OKF Ingestion Pipeline

## [2026-07-23] ingest | OKF Auto-Ingestion
- Raw: [[raw/articles/2026-07-23_polarized-by-fear-exploring-the-links-between-fear.md]] — Polarized by Fear: Exploring the Links Between Fear of Terrorism, Ideological Extremity, and Populist Voting
- Source files: 2026-07-23_user_classified.json
- Agent: OKF Ingestion Pipeline

## [2026-07-23] ingest | OKF Auto-Ingestion
- Raw: [[raw/articles/2026-07-21_polarized-by-fear-exploring-the-links-between-fear.md]] — Polarized by Fear: Exploring the Links Between Fear of Terrorism, Ideological Extremity, and Populist Voting
- Raw: [[raw/articles/2026-07-23_conspiracy-beliefs-as-a-metacognitive-dimension-of.md]] — Conspiracy Beliefs as a Metacognitive Dimension of Intergroup Attitudes: A Novel Framework for Interventions
- Source files: 2026-07-23_20260723_121925_tandf-fear-terrorism.json, 2026-07-23_user_classified_2.json
- Agent: OKF Ingestion Pipeline

## [2026-07-23] ingest | OKF Auto-Ingestion
- Raw: [[raw/articles/2026-07-23_partisan-hearts-polarized-minds-revisiting-the-rel.md]] — Partisan Hearts, Polarized Minds? Revisiting the Relationship Between Partisanship and Polarization
- Source files: 2026-07-23_user_classified_3.json
- Agent: OKF Ingestion Pipeline

## [2026-07-24] ingest | OKF Auto-Ingestion
- Raw: [[raw/articles/2026-07-24_ideas-or-strategy-the-impact-of-populist-incumbent.md]] — Ideas or Strategy? The Impact of Populist Incumbents on Liberal Democracy
- Raw: [[raw/articles/2026-07-24_five-years-of-general-comment-no-25-from-promises-.md]] — Five years of General comment No. 25: From promises to progress
- Raw: [[raw/articles/2026-07-24_these-are-the-countries-moving-to-ban-social-media.md]] — These are the countries moving to ban social media for children | TechCrunch
- Raw: [[raw/articles/2026-07-24_every-country-regulating-kids-social-media-in-2026.md]] — Every Country Regulating Kids' Social Media in 2026 (And What Parents Should Do) | WhitelistVideo Blog | WhitelistVideo
- Raw: [[raw/articles/2026-07-24_what-parents-say-about-their-teen-s-ai-use-pew-res.md]] — What parents say about their teen’s AI use | Pew Research Center
- Raw: [[raw/articles/2026-07-24_parents-think-they-know-how-kids-use-ai-they-don-t.md]] — Parents think they know how kids use AI. They don't
- Raw: [[raw/articles/2026-07-24_ma-social-media-ban-for-under-14s-what-parents-nee.md]] — MA Social Media Ban for Under 14s: What Parents Need to Know | WhitelistVideo Blog | WhitelistVideo
- Raw: [[raw/articles/2026-07-24_site-not-available.md]] — Site Not Available
- Raw: [[raw/articles/2026-07-24_article5a0029f0-0ed8-4730-8222-017ca1f1c10e-html.md]] — Article5A0029F0 0Ed8 4730 8222 017Ca1F1C10E.Html
- Raw: [[raw/articles/2026-07-24_kids-protecting-childrens-data.md]] — Kids Protecting Childrens Data
- Raw: [[raw/articles/2026-07-24_complying-coppa.md]] — Complying Coppa
- Raw: [[raw/articles/2026-07-24_childrens-online-privacy-protection-rule.md]] — Childrens Online Privacy Protection Rule
- Raw: [[raw/articles/2026-07-24_china-issues-new-rules-classifying-online-content-.md]] — China issues new rules classifying online content harmful to minors
- Raw: [[raw/articles/2026-07-24_brazil-is-first-latin-american-country-to-enshrine.md]] — Brazil is first Latin American country to enshrine age-appropriate design standards into law
- Raw: [[raw/articles/2026-07-24_age-checking-systems-can-now-be-certified-against-.md]] — Age checking systems can now be certified against 5Rights-led technical standard
- Raw: [[raw/articles/2026-07-24_united-states-of-america-5rights.md]] — United States of America - 5rights
- Raw: [[raw/articles/2026-07-24_mrf-australia-social-media-ban-research-briefing-a.md]] — Mrf_Australia Social Media Ban Research_Briefing April 26.Pdf
- Raw: [[raw/articles/2026-07-24_the-uk-s-proposed-in-real-life-study-of-social-med.md]] — The UK's Proposed "In Real Life" Study of Social Media Reduction is Scientifically Unsound.
- Raw: [[raw/articles/2026-07-24_our-top-health-agency-s-surveys-found-what-really-.md]] — Our top health agency’s surveys found what really makes teenagers depressed. Authorities' deafening silence said: no one cares
- Raw: [[raw/articles/2026-07-24_sosyal-medya-d-zenlemesi-bakan-g-kta-temel-er-evey.md]] — Sosyal medya d�zenlemesi! Bakan G�kta�: Temel �er�eveyi olu�turduk
- Raw: [[raw/articles/2026-07-24_ocuklara-y-nelik-sosyal-medya-d-zenlemesinin-er-ev.md]] — "Çocuklara yönelik sosyal medya düzenlemesinin çerçevesini oluşturduk" - Son Dakika Haberleri
- Raw: [[raw/articles/2026-07-24_socialmediaageverificationlawsbycountry.md]] — Socialmediaageverificationlawsbycountry
- Raw: [[raw/articles/2026-07-24_socialmediaageverificationlawsintheunitedstates.md]] — Socialmediaageverificationlawsintheunitedstates
- Raw: [[raw/articles/2026-07-24_just-a-moment.md]] — Just a moment...
- Raw: [[raw/articles/2026-07-24_page-not-found-unicef.md]] — Page not found | UNICEF
- Raw: [[raw/articles/2026-07-24_the-digital-services-act-shaping-europe-s-digital-.md]] — The Digital Services Act | Shaping Europe’s digital future
- Raw: [[raw/articles/2026-07-24_managing-disinformation-on-social-media-platforms-.md]] — Managing disinformation on social media platforms | Electronic Markets | Springer Nature Link
- Raw: [[raw/articles/2026-07-24_prebunking-misinformation-techniques-in-social-med.md]] — Prebunking misinformation techniques in social media feeds: Results from an Instagram field study | HKS Misinformation Review
- Raw: [[raw/articles/2026-07-24_404-sayfa-bulunamad-t24.md]] — 404 - Sayfa Bulunamadı | T24
- Raw: [[raw/articles/2026-07-24_s-69784532.md]] — S 69784532
- Raw: [[raw/articles/2026-07-24_yapay-zeka-teknolojileri-dezenformasyon-tartismala.md]] — Yapay Zeka Teknolojileri Dezenformasyon Tartismalari
- Source files: 2026-07-23_user_classified_4.json, 2026-07-24_categorized.json
- Agent: OKF Ingestion Pipeline

## [2026-07-24] ingest | OKF Auto-Ingestion
- Raw: [[raw/articles/2026-07-24_the-case-for-using-generative-ai-to-run-deliberati.md]] — The Case for Using Generative AI to Run Deliberation Simulations
- Source files: 2026-07-23_user_classified_5.json
- Agent: OKF Ingestion Pipeline

## [2026-07-24] ingest | OKF Auto-Ingestion
- Raw: [[raw/articles/2026-07-24_ideological-and-affective-polarization-in-argentin.md]] — Ideological and Affective Polarization in Argentina
- Source files: 2026-07-24_user_classified_1.json
- Agent: OKF Ingestion Pipeline

## [2026-07-24] ingest | OKF Auto-Ingestion
- Raw: [[raw/articles/2026-07-24_why-do-young-us-americans-avoid-cross-partisan-dat.md]] — Why do young US Americans avoid cross-partisan dating? A closer look at mediators and variation by gender and party
- Raw: [[raw/articles/2026-07-24_the-polarizing-effect-of-the-march-for-science-on-.md]] — The Polarizing Effect of the March for Science on Attitudes toward Scientists
- Source files: 2026-07-24_user_links.json
- Agent: OKF Ingestion Pipeline

## [2026-07-25] ingest | OKF Auto-Ingestion
- Raw: [[raw/articles/2026-07-25_towards-a-methodologically-congruent-framework-for.md]] — Towards a methodologically congruent framework for GenAI use in nonpositivist qualitative research
- Source files: 2026-07-24_genai-qualitative-framework.json
- Agent: OKF Ingestion Pipeline

## [2026-07-28] ingest | OKF Auto-Ingestion
- Raw: [[raw/articles/2026-07-28_un-fairness-by-design-what-an-age-appropriate-desi.md]] — (Un)fairness by design: what an Age Appropriate Design Code audit reveals about GenAI in EdTech
- Source files: 2026-07-24_edtech-aadc-audit.json
- Agent: OKF Ingestion Pipeline

## [2026-07-28] ingest | OKF Auto-Ingestion
- Raw: [[raw/articles/2026-07-28_political-polarization-of-trust-in-science.md]] — Political polarization of trust in science
- Source files: 2026-07-28_polarization-trust-science.json
- Agent: OKF Ingestion Pipeline

## [2026-07-28] ingest | OKF Auto-Ingestion
- Raw: [[raw/articles/2026-07-28_engaging-young-people-as-partners-in-policy-and-pr.md]] — Engaging Young People As Partners in Policy and Practice: Summary of Lessons from 25 Years of Global Youth Development
- Source files: 2026-07-28_georgetown-youth-engagement.json
- Agent: OKF Ingestion Pipeline

## [2026-07-29] ingest | OKF Auto-Ingestion
- Raw: [[raw/articles/2026-07-29_five-years-of-general-comment-no-25-from-promises-.md]] — Five years of General comment No. 25: From promises to progress
- Raw: [[raw/articles/2026-07-29_these-are-the-countries-moving-to-ban-social-media.md]] — These are the countries moving to ban social media for children | TechCrunch
- Raw: [[raw/articles/2026-07-29_every-country-regulating-kids-social-media-in-2026.md]] — Every Country Regulating Kids' Social Media in 2026 (And What Parents Should Do) | WhitelistVideo Blog
- Raw: [[raw/articles/2026-07-29_what-parents-say-about-their-teen-s-ai-use-pew-res.md]] — What parents say about their teen's AI use | Pew Research Center
- Raw: [[raw/articles/2026-07-29_parents-think-they-know-how-kids-use-ai-they-don-t.md]] — Parents think they know how kids use AI. They don't
- Raw: [[raw/articles/2026-07-29_ma-social-media-ban-for-under-14s-what-parents-nee.md]] — MA Social Media Ban for Under 14s: What Parents Need to Know | WhitelistVideo Blog
- Raw: [[raw/articles/2026-07-29_unavailable-blocked-status-451.md]] — Unavailable (Blocked - Status 451)
- Raw: [[raw/articles/2026-07-29_unavailable-blocked-status-429.md]] — Unavailable (Blocked - Status 429)
- Raw: [[raw/articles/2026-07-29_unavailable-blocked-status-404.md]] — Unavailable (Blocked - Status 404)
- Raw: [[raw/articles/2026-07-29_wikipedia-lkelere-g-re-sosyal-medya-ya-do-rulama-y.md]] — Wikipedia: Ülkelere Göre Sosyal Medya Yaş Doğrulama Yasaları
- Raw: [[raw/articles/2026-07-29_wikipedia-amerika-birle-ik-devletleri-nde-sosyal-m.md]] — Wikipedia: Amerika Birleşik Devletleri'nde Sosyal Medya Yaş Doğrulama Yasaları
- Raw: [[raw/articles/2026-07-29_uk-parlamentosu-commons-library-ocuk-evrimi-i-g-ve.md]] — UK Parlamentosu Commons Library: Çocuk Çevrimiçi Güvenliği Araştırma Raporu
- Raw: [[raw/articles/2026-07-29_unicef-dijital-haklar-rehberi-2026-g-ncellemesi.md]] — UNICEF: Dijital Haklar Rehberi 2026 Güncellemesi
- Raw: [[raw/articles/2026-07-29_ab-dijital-strateji-dijital-hizmetler-yasas-dsa-pa.md]] — AB Dijital Strateji: Dijital Hizmetler Yasası (DSA) Paketi
- Raw: [[raw/articles/2026-07-29_springer-electronic-markets-dergisi-dijital-platfo.md]] — Springer: Electronic Markets Dergisi - Dijital Platform Düzenlemeleri ve Çocuk Koruma
- Raw: [[raw/articles/2026-07-29_harvard-misinformation-review-instagram-da-n-bilgi.md]] — Harvard Misinformation Review: Instagram'da Ön Bilgilendirme ve Dezenformasyonla Mücadele
- Raw: [[raw/articles/2026-07-29_t24-yapay-zeka-se-im-dezenformasyonu-ve-demokratik.md]] — T24: Yapay Zeka, Seçim Dezenformasyonu ve Demokratik Süreçler
- Raw: [[raw/articles/2026-07-29_dw-t-rk-e-almanya-se-imleri-ve-dezenformasyon-sava.md]] — DW Türkçe: Almanya Seçimleri ve Dezenformasyon Savaşları
- Raw: [[raw/articles/2026-07-29_digital-t-rk-e-yapay-zeka-teknolojileri-ve-dezenfo.md]] — Digital Türkçe: Yapay Zeka Teknolojileri ve Dezenformasyon Tartışmaları
- Source files: 2026-07-29_categorized.json
- Agent: OKF Ingestion Pipeline

## [2026-07-29] ingest | OKF Auto-Ingestion
- Raw: [[raw/articles/2026-07-29_young-children-s-assent-and-dissent-in-research-ag.md]] — Young children's assent and dissent in research: agency, privacy and relationships within ethical research spaces
- Source files: 2026-07-28_children-assent-dissent.json
- Agent: OKF Ingestion Pipeline

## [2026-07-29] ingest | OKF Auto-Ingestion
- Raw: [[raw/articles/2026-07-29_synthetic-contact-with-ai-reduces-cross-partisan-a.md]] — Synthetic Contact with AI Reduces Cross-Partisan Animosity
- Source files: 2026-07-28_synthetic-contact-ai.json
- Agent: OKF Ingestion Pipeline

## [2026-07-29] ingest | OKF Auto-Ingestion
- Raw: [[raw/articles/2026-07-29_gpt-outperforms-bert-and-liwc-for-stance-and-anger.md]] — GPT outperforms BERT and LIWC for stance and anger detection in German news articles and user comments
- Source files: 2026-07-29_gpt-stance-detection.json
- Agent: OKF Ingestion Pipeline

## [2026-07-30] ingest | OKF Auto-Ingestion
- Source files: 2026-07-29_misinformation-as-strategy.json
- Agent: OKF Ingestion Pipeline

## [2026-07-30] ingest | OKF Auto-Ingestion
- Raw: [[raw/articles/2026-07-30_cultural-capital-and-the-productivity-of-ideas-evi.md]] — Cultural Capital and the Productivity of Ideas: Evidence from Historical Texts
- Source files: 2026-07-30_cultural-capital-llm.json
- Agent: OKF Ingestion Pipeline

## [2026-07-30] ingest | OKF Auto-Ingestion
- Raw: [[raw/articles/2026-07-29_misinformation-as-strategy-epistemic-consequences-.md]] — Misinformation as strategy: Epistemic consequences and the undermining of shared truth
- Source files: 2026-07-30_121405.json
- Agent: OKF Ingestion Pipeline

## [2026-07-30] ingest | OKF Auto-Ingestion
- Raw: [[raw/articles/2026-07-30_the-echoes-from-social-media-modeling-how-filter-b.md]] — The echoes from social media: modeling how filter bubbles and network structure shape echo chamber emergence
- Source files: 2026-07-30_echo-chambers-filter-bubbles.json
- Agent: OKF Ingestion Pipeline

## [2026-07-31] ingest | OKF Auto-Ingestion
- Raw: [[raw/articles/2026-07-31_the-youth-digital-policy-repository-a-tool-for-tra.md]] — The youth digital policy repository: A tool for tracking digital media legislation aimed at minors
- Source files: 2026-07-30_youth-digital-policy-repo.json
- Agent: OKF Ingestion Pipeline

## [2026-07-31] ingest | OKF Auto-Ingestion
- Raw: [[raw/articles/2026-07-31_changing-partisanship-contributes-significantly-to.md]] — Changing Partisanship Contributes Significantly to Rising Affective Polarization: Evidence from a Decomposition of Panel Data
- Source files: 2026-07-31_churn-affective-polarization.json
- Agent: OKF Ingestion Pipeline

## [2026-07-31] ingest | OKF Auto-Ingestion
- Raw: [[raw/articles/2026-07-31_computational-public-opinion-measurement-a-systema.md]] — Computational Public Opinion Measurement: A Systematic Review of Methods and Methodological Limitations
- Source files: 2026-07-31_cpom-systematic-review.json
- Agent: OKF Ingestion Pipeline

## [2026-07-31] ingest | OKF Auto-Ingestion
- Raw: [[raw/articles/2026-07-31_misinformation-as-strategy-epistemic-consequences-.md]] — Misinformation as strategy: Epistemic consequences and the undermining of shared truth — Trends in Cognitive Sciences (@TrendsCognSci) tanıtım gönderisi
- Raw: [[raw/articles/2026-07-31_cultural-capital-and-the-productivity-of-ideas-evi.md]] — Cultural Capital and the Productivity of Ideas: Evidence from Historical Texts — Inclusive Productivity Network (@incprodmon) paylaşımı
- Raw: [[raw/articles/2026-07-31_gpt-outperforms-bert-and-liwc-for-stance-and-anger.md]] — GPT outperforms BERT and LIWC for stance and anger detection in German news articles and user comments — Frontiers in Political Science (@FrontPolSci)
- Raw: [[raw/articles/2026-07-31_outgroup-chatbot-conversations-correct-partisan-mi.md]] — Outgroup chatbot conversations correct partisan misperceptions and reduce hostility — Jay Van Bavel (@jayvanbavel)
- Source files: 2026-07-31_categorized_batch2.json
- Agent: OKF Ingestion Pipeline

## [2026-08-01] ingest | OKF Auto-Ingestion
- Raw: [[raw/articles/2026-08-01_relating-cognitive-skills-and-personality-traits-t.md]] — Relating Cognitive Skills and Personality Traits to Economic Preferences: Decision-Making under Cognitive Shocks and Guessing
- Source files: 2026-07-31_heckman-deliberation-noise.json
- Agent: OKF Ingestion Pipeline

## [2026-08-01] ingest | OKF Auto-Ingestion
- Raw: [[raw/articles/2026-08-01_untrustworthy-sources-on-facebook-and-instagram-in.md]] — Untrustworthy sources on Facebook and Instagram in 2020: Concentrated exposure but no attitudinal effects
- Source files: 2026-07-31_nyhan-untrustworthy-sources-2020.json
- Agent: OKF Ingestion Pipeline

## [2026-08-01] ingest | OKF Auto-Ingestion
- Raw: [[raw/articles/2026-08-01_how-children-learn-complex-environmental-concepts-.md]] — How children learn complex environmental concepts through digital storytelling: divergent pathways to knowledge and stewardship intention
- Source files: 2026-08-01_children-digital-storytelling-environment.json
- Agent: OKF Ingestion Pipeline

## [2026-08-01] ingest | OKF Auto-Ingestion
- Raw: [[raw/articles/2026-08-01_political-parties-as-drivers-of-u-s-polarization-1.md]] — Political Parties as Drivers of U.S. Polarization: 1927-2018
- Source files: 2026-08-01_parties-drivers-polarization.json
- Agent: OKF Ingestion Pipeline

## [2026-08-01] ingest | OKF Auto-Ingestion
- Raw: [[raw/articles/2026-08-01_building-child-friendly-neighbourhoods-empowering-.md]] — Building child-friendly neighbourhoods: Empowering communities with data-driven action
- Source files: 2026-08-01_oecd-child-friendly-neighbourhoods.json
- Agent: OKF Ingestion Pipeline

## [2026-08-02] ingest | OKF Auto-Ingestion
- Raw: [[raw/articles/2026-08-02_growing-up-in-a-connected-world-a-family-guide-for.md]] — Growing Up in a Connected World: A Family Guide for the Digital Age
- Source files: 2026-08-02_unesco-growing-up-connected-world.json
- Agent: OKF Ingestion Pipeline

## [2026-08-02] ingest | OKF Auto-Ingestion
- Raw: [[raw/articles/2026-06-22_growing-up-in-a-connected-world-a-family-guide-for.md]] — Growing Up in a Connected World: A Family Guide for the Digital Age
- Raw: [[raw/articles/2026-08-02_untrustworthy-sources-on-facebook-and-instagram-in.md]] — Untrustworthy sources on Facebook and Instagram in 2020: Concentrated exposure but no attitudinal effects
- Raw: [[raw/articles/2026-08-02_relating-cognitive-skills-and-personality-traits-t.md]] — Relating Cognitive Skills and Personality Traits to Economic Preferences: Decision-Making under Cognitive Shocks and Guessing
- Raw: [[raw/articles/2026-08-02_computational-public-opinion-measurement-a-systema.md]] — Computational Public Opinion Measurement: A Systematic Review of Methods and Methodological Limitations
- Raw: [[raw/articles/2026-08-02_changing-partisanship-contributes-significantly-to.md]] — Changing Partisanship Contributes Significantly to Rising Affective Polarization: Evidence from a Decomposition of Panel Data
- Raw: [[raw/articles/2026-08-02_the-youth-digital-policy-repository-a-tool-for-tra.md]] — The youth digital policy repository: A tool for tracking digital media legislation aimed at minors
- Raw: [[raw/articles/2026-08-02_how-children-learn-complex-environmental-concepts-.md]] — How children learn complex environmental concepts through digital storytelling: divergent pathways to knowledge and stewardship intention
- Raw: [[raw/articles/2026-08-02_political-parties-as-drivers-of-u-s-polarization-1.md]] — Political Parties as Drivers of U.S. Polarization: 1927-2018
- Raw: [[raw/articles/2026-08-02_building-child-friendly-neighbourhoods-empowering-.md]] — Building child-friendly neighbourhoods: Empowering communities with data-driven action
- Source files: 2026-08-02_121102_ingestion.json, 2026-08-02_categorized.json
- Agent: OKF Ingestion Pipeline

## [2026-08-03] ingest | OKF Auto-Ingestion
- Raw: [[raw/articles/2026-07_enhancing-adolescent-social-and-emotional-well-bei.md]] — Enhancing adolescent social and emotional well-being
- Source files: 2026-08-03_oecd-adolescent-social-emotional-wellbeing.json
- Agent: OKF Ingestion Pipeline

## [2026-08-03] ingest | OKF Auto-Ingestion
- Raw: [[raw/articles/2026-06-05_family-school-partnership-initiatives-to-improve-s.md]] — Family–school partnership initiatives to improve student attendance: A systematic review
- Source files: 2026-08-03_family-school-partnership-attendance.json
- Agent: OKF Ingestion Pipeline

## [2026-08-03] ingest | OKF Auto-Ingestion
- Raw: [[raw/articles/2026-08-03_international-youth-day-webinar-meaningful-child-a.md]] — International Youth Day webinar: meaningful child and youth participation (Child and Youth Friendly Governance Project)
- Source files: 2026-08-03_child-youth-friendly-governance-webinar.json
- Agent: OKF Ingestion Pipeline

## [2026-08-03] ingest | OKF Auto-Ingestion
- Raw: [[raw/articles/2026-07-24_public-support-for-democracy-and-different-pattern.md]] — Public support for democracy and different patterns of democratic backsliding
- Source files: 2026-08-03_public-support-democracy-backsliding.json
- Agent: OKF Ingestion Pipeline

## [2026-08-03] ingest | OKF Auto-Ingestion
- Raw: [[raw/articles/2026-08-03_un-global-principles-for-information-integrity-a-h.md]] — UN Global Principles for Information Integrity: a humane information ecosystem (United Nations)
- Source files: 2026-08-03_un-information-integrity-principles.json
- Agent: OKF Ingestion Pipeline

## [2026-08-03] ingest | OKF Auto-Ingestion
- Raw: [[raw/articles/2026-07_the-china-backlash-quantifying-the-narrative-disco.md]] — The China Backlash: Quantifying the Narrative Discourse on China
- Source files: 2026-08-03_china-backlash-narrative-discourse.json
- Agent: OKF Ingestion Pipeline

## [2026-08-03] ingest | OKF Auto-Ingestion
- Raw: [[raw/articles/2026-08-03_longitudinal-effect-of-early-social-media-use-on-s.md]] — Longitudinal effect of early social media use on standardized learning outcomes during school career
- Source files: 2026-08-03_gui-early-social-media-school-outcomes.json
- Agent: OKF Ingestion Pipeline

## [2026-08-03] ingest | OKF Auto-Ingestion
- Raw: [[raw/articles/2024-01_narratives-of-post-truth-lyotard-and-the-epistemic.md]] — Narratives of Post-Truth: Lyotard and the Epistemic Fragmentation of Society
- Source files: 2026-08-03_baier-narratives-post-truth.json
- Agent: OKF Ingestion Pipeline

## [2026-08-04] ingest | OKF Auto-Ingestion
- Raw: [[raw/articles/2026-01-20_electoral-campaigns-and-news-polarization-luis-men.md]] — Electoral Campaigns and News Polarization (Luis Menéndez, Job Market Paper)
- Source files: 2026-08-03_menendez-electoral-campaigns-news-polarization.json
- Agent: OKF Ingestion Pipeline

## [2026-08-04] ingest | OKF Auto-Ingestion
- Raw: [[raw/articles/2026-07-07_european-parliament-adopts-resolution-on-a-new-str.md]] — European Parliament adopts resolution on a new strategy for media literacy and digital learning (EDMO)
- Source files: 2026-08-03_ep-media-literacy-resolution.json
- Agent: OKF Ingestion Pipeline

## [2026-08-05] ingest | OKF Auto-Ingestion
- Raw: [[raw/articles/2026-07-01_modelling-and-classifying-the-components-of-litera.md]] — Modelling and classifying the components of literature reviews: a novel annotation schema and evaluation of transformer models
- Source files: 2026-08-03_bolanos-litreview-components.json
- Agent: OKF Ingestion Pipeline

## [2026-08-05] ingest | OKF Auto-Ingestion
- Raw: [[raw/articles/2026-08-05_towards-scalable-ai-assisted-pre-bunking-of-electi.md]] — Towards scalable AI-assisted pre-bunking of election misinformation: evidence from a pre-registered US panel experiment
- Source files: 2026-08-03_linegar-ai-prebunking.json
- Agent: OKF Ingestion Pipeline

## [2026-08-06] ingest | OKF Auto-Ingestion
- Raw: [[raw/articles/2026-05-27_media-literacy-education-policy-in-finland-2026-na.md]] — Media Literacy Education Policy in Finland (2026) — National Media Education Policy
- Source files: 2026-08-06_finland-media-literacy-policy.json
- Agent: OKF Ingestion Pipeline

## [2026-08-07] ingest | OKF Auto-Ingestion
- Raw: [[raw/articles/2026-07_validity-and-reliability-study-of-digital-addictio.md]] — Validity and Reliability Study of Digital Addiction Scale for the Turkish Youth (DASY)
- Source files: 2026-08-06_dasy-digital-addiction-scale-youth.json
- Agent: OKF Ingestion Pipeline

## [2026-08-08] ingest | OKF Auto-Ingestion
- Raw: [[raw/articles/2026-06-26_generative-grounded-theory-ggt-inductive-theory-bu.md]] — Generative grounded theory (GGT): Inductive theory building in the age of generative AI
- Source files: 2026-08-08_ggt-generative-grounded-theory.json
- Agent: OKF Ingestion Pipeline

## [2026-08-08] ingest | OKF Auto-Ingestion
- Raw: [[raw/articles/2026-07_measuring-affective-polarization-matching-concepts.md]] — Measuring affective polarization: Matching concepts to measures
- Source files: 2026-08-08_druckman-affective-polarization-measures.json
- Agent: OKF Ingestion Pipeline

## [2026-08-08] ingest | OKF Auto-Ingestion
- Raw: [[raw/articles/2025-09-16_the-effect-of-real-news-party-cues.md]] — The effect of real-news party cues
- Source files: 2026-08-08_skytte-real-news-party-cues.json
- Agent: OKF Ingestion Pipeline

## [2026-08-08] ingest | OKF Auto-Ingestion
- Raw: [[raw/articles/2026-07_the-effect-of-real-news-party-cues.md]] — The effect of real-news party cues
- Raw: [[raw/articles/2025-12-08_shooting-the-messenger-the-polarizing-effects-of-p.md]] — Shooting the Messenger: The Polarizing Effects of Political Attacks on the Press
- Source files: 2026-08-08_121505_ingestion.json, 2026-08-08_siegel-weiss-shooting-messenger.json
- Agent: OKF Ingestion Pipeline

## [2026-08-09] ingest | OKF Auto-Ingestion
- Raw: [[raw/articles/2021-06-07_the-nature-of-affective-polarization-disentangling.md]] — The Nature of Affective Polarization: Disentangling Policy Disagreement from Partisan Identity
- Source files: 2026-08-08_dias-lelkes-affective-polarization-nature.json
- Agent: OKF Ingestion Pipeline

## [2026-08-10] ingest | OKF Auto-Ingestion
- Raw: [[raw/articles/2026-08-04_matraix-simulating-the-world-with-8-3-billion-pers.md]] — MatrAIx: Simulating the World with 8.3 Billion Persona Agents
- Source files: 2026-08-08_matraix-simulated-users.json
- Agent: OKF Ingestion Pipeline

## [2026-08-10] ingest | OKF Auto-Ingestion
- Raw: [[raw/articles/2026-08-10_decision-making-under-deep-uncertainty-from-theory.md]] — Decision Making under Deep Uncertainty: From Theory to Practice
- Source files: 2026-08-08_dmdu-decision-deep-uncertainty.json
- Agent: OKF Ingestion Pipeline

## [2026-08-10] ingest | OKF Auto-Ingestion
- Raw: [[raw/articles/2026-07-17_in-defense-of-qualitative-description-reclaiming-l.md]] — In defense of qualitative description: reclaiming "little t" theory as a site of knowledge advancement
- Source files: 2026-08-08_reynolds-qualitative-description-little-t.json
- Agent: OKF Ingestion Pipeline

## [2026-08-10] ingest | OKF Auto-Ingestion
- Raw: [[raw/articles/2026-01-12_survey-quality-and-acquiescence-bias-a-cautionary-.md]] — Survey Quality and Acquiescence Bias: A Cautionary Tale
- Source files: 2026-08-10_cruz-survey-quality-acquiescence-bias.json
- Agent: OKF Ingestion Pipeline

## [2026-08-10] ingest | OKF Auto-Ingestion
- Raw: [[raw/articles/2026-07-01_polarization-and-political-violence-when-polarizat.md]] — Polarization and Political Violence: When Polarization Turns Violent
- Source files: 2026-08-10_kopstein-polarization-political-violence.json, 2026-08-08_categorized_batch4.json
- Agent: OKF Ingestion Pipeline (batch4 duplikatları temizlendi: survey-quality/in-defense/matraix 2026-08-10 kopyaları silindi)

## [2026-08-10] ingest | OKF Auto-Ingestion
- Raw: [[raw/articles/2026-08-07_misreading-social-identity-theory-why-affective-po.md]] — Misreading social identity theory: Why affective-polarisation research got it wrong
- Source files: 2026-08-10_yang-misreading-social-identity-theory.json
- Agent: OKF Ingestion Pipeline

## [2026-08-10] ingest | OKF Auto-Ingestion
- Raw: [[raw/articles/2026-06-29_a-practitioner-s-guide-to-using-large-language-mod.md]] — A Practitioner's Guide to Using Large Language Models and Generative AI in Economic History
- Source files: 2026-08-10_ferrara-llm-genai-economic-history-guide.json
- Agent: OKF Ingestion Pipeline

## [2026-08-10] ingest | OKF Auto-Ingestion
- Raw: [[raw/articles/2025-10-01_dialogues-with-ai-reduce-beliefs-in-misinformation.md]] — Dialogues with AI Reduce Beliefs in Misinformation but Build No Lasting Discernment Skills
- Source files: 2026-08-10_rani-ai-misinformation-discernment-skills.json
- Agent: OKF Ingestion Pipeline

## [2026-08-11] ingest | OKF Auto-Ingestion
- NOT: 2026-08-10_categorized.json işlendi ancak 4 makale (polarization/misreading/a-practitioner/dialogues) zaten asıl dosyalarıyla mevcuttu; 2026-08-11_* duplikatları oluşturuldu ve 2026-08-12'de temizlendi
- Source files: 2026-08-10_categorized.json
- Agent: OKF Ingestion Pipeline (duplikatlar silindi — asıl dosyalar korundu)


## [2026-08-12] update | OKF Manuel Guncelleme
- Updated: [[raw/articles/2025-12-08_shooting-the-messenger-the-polarizing-effects-of-p.md]] — Siegel & Weiss (2026-08-11 versiyonu): 2 genisletme deneyi + rafine bulgular + yeni pre-registration (#302,893)
- Source: 2026-08-12_siegel-weiss-shooting-messenger-update.json (t.co → ayni PDF URL; duplikat degil, guncelleme)
- Agent: OKF Ingestion Pipeline (manuel)
## [2026-08-12] ingest | OKF Auto-Ingestion
- Raw: [[raw/articles/2023-10-02_bridging-gaps-how-investment-in-public-childcare-a.md]] — Bridging gaps: how investment in public childcare affects women's employment in Italy and Spain
- Source files: 2026-08-12_maestripieri-public-childcare-women-employment.json
- Agent: OKF Ingestion Pipeline

## [2026-08-12] ingest | OKF Auto-Ingestion
- Raw: [[raw/articles/2025-07-01_social-media-fake-news-and-political-polarization-.md]] — Social Media, Fake News, and Political Polarization: Challenges for Indian Democracy
- Source files: 2026-08-12_singh-social-media-fake-news-india.json
- Agent: OKF Ingestion Pipeline

## [2026-08-12] ingest | OKF Auto-Ingestion
- Raw: [[raw/articles/2026-08-08_causal-falsification-of-digital-twins.md]] — Causal Falsification of Digital Twins
- Source files: 2026-08-12_cornish-causal-falsification-digital-twins.json
- Agent: OKF Ingestion Pipeline

## [2026-08-12] ingest | OKF Auto-Ingestion
- Raw: [[raw/articles/2025-04-01_feminist-digital-humanities-intersections-in-pract.md]] — Feminist Digital Humanities: Intersections in Practice (DARIAH-EU webinar + kitap, 2025)
- Source files: 2026-08-12_feminist-digital-humanities-webinar.json
- Agent: OKF Ingestion Pipeline

## [2026-08-12] ingest | OKF Auto-Ingestion
- Raw: [[raw/articles/2026-08-10_i-will-take-care-of-this-country-the-paradox-of-he.md]] — "I will take care of this country": The paradox of helplessness in Lula's discourse amid the rise of the far right in Brazil
- Source files: 2026-08-12_lula-helplessness-far-right-brazil.json
- Agent: OKF Ingestion Pipeline

## [2026-08-12] ingest | OKF Auto-Ingestion
- Raw: [[raw/articles/2026-08-11_eurasia-review-interviews-dr-jay-van-bavel-on-iden.md]] — Eurasia Review Interviews: Dr. Jay Van Bavel On Identity, Misinformation, And The Partisan Brain
- Source files: 2026-08-12_van-bavel-partisan-brain-interview.json
- Agent: OKF Ingestion Pipeline

## [2026-08-12] ingest | OKF Auto-Ingestion
- Raw: [[raw/articles/2026-07-26_more-than-a-partisan-pandemic-worldview-and-covid-.md]] — More than a partisan pandemic: Worldview and COVID-19 response in the United States
- Source files: 2026-08-12_hetterington-worldview-covid19.json
- Agent: OKF Ingestion Pipeline

## [2026-08-13] ingest | OKF Auto-Ingestion
- Raw: [[raw/articles/2026-07-29_life-online-rights-offline-unicef-u-report-blog-li.md]] — Life online, rights offline — UNICEF U-Report blog (Life Online anketi yorumu)
- Source files: 2026-08-12_unicef-life-online-rights-offline.json
- Agent: OKF Ingestion Pipeline

## [2026-08-13] ingest | OKF Auto-Ingestion
- Raw: [[raw/articles/2026-03-01_from-worm-to-human-scaling-brain-emulation-isaak-f.md]] — From Worm to Human: Scaling Brain Emulation — Isaak Freeman MIT tezi
- Source files: 2026-08-12_freeman-scaling-brain-emulation.json
- Agent: OKF Ingestion Pipeline

## [2026-08-13] ingest | OKF Auto-Ingestion
- Raw: [[raw/articles/2026-08-12_agentic-profiles-for-effective-ai-governance.md]] — Agentic profiles for effective AI governance
- Source files: 2026-08-12_kasirzadeh-agentic-profiles-ai-governance.json
- Agent: OKF Ingestion Pipeline

## [2026-08-13] ingest | OKF Auto-Ingestion
- Raw: [[raw/articles/2026-07-03_elites-as-democratic-gatekeepers-theory-and-eviden.md]] — Elites as Democratic Gatekeepers: Theory and Evidence from Norway
- Source files: 2026-08-13_goldstein-elites-democratic-gatekeepers.json
- Agent: OKF Ingestion Pipeline

## [2026-08-13] ingest | OKF Auto-Ingestion
- Raw: [[raw/articles/2026-08-01_southmod-at-10-a-decade-of-better-evidence-for-tax.md]] — SOUTHMOD at 10: A decade of better evidence for tax and social policy — UNU-WIDER
- Source files: 2026-08-13_unu-wider-southmod-10.json
- Agent: OKF Ingestion Pipeline

## [2026-08-13] ingest | OKF Auto-Ingestion
- Raw: [[raw/articles/2025-12-15_partisan-polarization-in-local-politics-de-benedic.md]] — Partisan Polarization in Local Politics — de Benedictis-Kessner, Einstein, Glick, Palmer & Warshaw (APSR R&R, Aralık 2025)
- Source files: 2026-08-13_categorized_batch2.json
- Agent: OKF Ingestion Pipeline

## [2026-08-16] ingest | OKF Auto-Ingestion
- Raw: [[raw/articles/2026-02_effects-of-political-polarization-on-non-electoral.md]] — Effects of political polarization on non-electoral participation — Kołczyńska (Comparative European Politics 24(1), 2026)
- Source files: 2026-08-15_categorized.json
- Agent: OKF Ingestion Pipeline

## [2026-08-16] ingest | OKF Auto-Ingestion
- Raw: [[raw/articles/2026-04-23_the-college-campus-and-the-culture-war-the-develop.md]] — The College Campus and the Culture War: The Development of Party Polarization on Higher Education, 1980–2025 — Schickler & Rodriguez (SAPD, 2026)
- Source files: 2026-08-16_categorized.json
- Agent: OKF Ingestion Pipeline

## [2026-08-17] ingest | OKF Auto-Ingestion
- Raw: [[raw/articles/2022-04_statistical-control-requires-causal-justification-.md]] — Statistical Control Requires Causal Justification — Wysocki, Lawson & Rhemtulla (AMPPS 5(2), 2022)
- Source files: 2026-08-16_categorized_batch2.json
- Agent: OKF Ingestion Pipeline

## [2026-08-18] ingest | OKF Auto-Ingestion
- Raw: [[raw/articles/2026-08-09_the-rise-and-closure-of-liberal-democracy-a-system.md]] — The rise and closure of 'liberal democracy': A systematic review in contemporary political science, 1990–2025 — Bonin (IPSR, 2026)
- Source files: 2026-08-16_categorized_batch3.json
- Agent: OKF Ingestion Pipeline

## [2026-08-19] ingest | OKF Auto-Ingestion
- Raw: [[raw/articles/2026-08-04_big-if-true-fragility-of-the-manipulable-voter-mod.md]] — Big if true: Fragility of the manipulable-voter model and the implications for politics and social science — Gelman, Bullock & Sood (2026)
- Source files: 2026-08-17_categorized.json
- Agent: OKF Ingestion Pipeline

## [2026-08-19] ingest | OKF Auto-Ingestion
- Raw: [[raw/articles/2026-08-18_the-improvement-in-political-analysis-in-the-past-.md]] — The improvement in political analysis in the past 25 years — Gelman blog (18 Ağu 2026): Morris, Silver & McKown-Dawson'ın istatistiksel iş akışı gösterimleri
- Source files: 2026-08-19_categorized.json
- Agent: OKF Ingestion Pipeline

## [2026-08-19] ingest | OKF Auto-Ingestion
- Raw: [[raw/articles/2025-09-29_defending-methodological-anarchism-in-empirically-.md]] — Defending Methodological Anarchism in Empirically Informed Political Theory — Handby (JOP, Online First)
- Source files: 2026-08-19_categorized_batch2.json
- Agent: OKF Ingestion Pipeline

## [2026-08-19] ingest | OKF Auto-Ingestion
- Raw: [[raw/articles/2026-08-14_the-new-politics-of-the-social-and-authoritarianis.md]] — The new politics of the social and authoritarianism in the Near East: gender and youth politics and movements — Kutun, Binbuğa & Yılmaz (Third World Quarterly özel sayı girişi, 2026)
- Source files: 2026-08-19_categorized_batch3.json
- Agent: OKF Ingestion Pipeline

## [2026-08-19] ingest | OKF Auto-Ingestion
- Raw: [[raw/articles/2001-09_measurement-validity-a-shared-standard-for-qualita.md]] — Measurement Validity: A Shared Standard for Qualitative and Quantitative Research — Adcock & Collier (APSR 95(3), 2001)
- Source files: 2026-08-19_categorized_batch4.json
- Agent: OKF Ingestion Pipeline

## [2026-08-19] ingest | OKF Auto-Ingestion
- Raw: [[raw/articles/2026-08-19_analytical-critical-thinking-in-qualitative-resear.md]] — Analytical Critical Thinking in Qualitative Research — Margaret R. Roller (Research Design Review, 19 Ağu 2026)
- Source files: 2026-08-19_rdr_analytical_critical_thinking.json
- Agent: OKF Ingestion Pipeline

## [2026-08-20] ingest | OKF Auto-Ingestion
- Raw: [[raw/articles/2026-08-19_why-political-polarization-is-rising-and-how-to-re.md]] — Why Political Polarization Is Rising, and How to Reverse It — Journal of Democracy kutuplaşma derlemesi (5 makale, 2026)
- Source files: 2026-08-19_jod_polarization_email_blast.json
- Agent: OKF Ingestion Pipeline

## [2026-08-21] ingest | OKF Auto-Ingestion
- Raw: [[raw/articles/2026-07-22_identity-threat-personal-values-and-political-atti.md]] — Identity threat, personal values, and political attitudes: Evidence from a large-scale survey across the European Union — Kuehnhanss & Scharfbillig (Political Psychology 47(4), 2026)
- Source files: 2026-08-19_kuehnhanss_identity_threat.json
- Agent: OKF Ingestion Pipeline

## [2026-08-21] ingest | OKF Auto-Ingestion
- Raw: [[raw/articles/2026-07-01_how-do-americans-explain-their-party-identificatio.md]] — How Do Americans Explain Their Party Identification and Out-Partisan Animosity? — Fowler, Huber, Jin & Orr (Public Opinion Quarterly, 2026)
- Source files: 2026-08-20_fowler_party_identification.json
- Agent: OKF Ingestion Pipeline

## [2026-08-21] ingest | OKF Auto-Ingestion
- Raw: [[raw/articles/2026-08-10_debriefings-in-misinformation-research-should-incl.md]] — Debriefings in misinformation research should include fact-checks to correct misperceptions and increase perceived learning — Hoes & Altay (Political Science Research and Methods, 2026)
- Source files: 2026-08-20_hoes_debriefings.json
- Agent: OKF Ingestion Pipeline

## [2026-08-21] ingest | OKF Auto-Ingestion
- Raw: [[raw/articles/2026-08-20_laura-kipnis-reviews-against-affect-lisa-downing-u.md]] — Laura Kipnis reviews Against Affect — Lisa Downing (University of Nebraska Press, 2026) · Critical Inquiry, 20 Ağu 2026
- Source files: 2026-08-20_kipnis_against_affect.json
- Agent: OKF Ingestion Pipeline

## [2026-08-21] ingest | OKF Auto-Ingestion
- Raw: [[raw/articles/2021-08-19_how-social-science-got-better-overcoming-bias-with.md]] — How Social Science Got Better: Overcoming Bias with More Evidence, Diversity, and Self-Reflection — Matt Grossmann (Oxford University Press, 2021)
- Source files: 2026-08-21_grossmann_social_science.json
- Agent: OKF Ingestion Pipeline

## [2026-08-21] ingest | OKF Auto-Ingestion
- Raw: [[raw/articles/2026-06-04_priming-common-european-and-democratic-values-does.md]] — Priming common European and democratic values does not reduce affective polarization — Canalejo-Molero, Cicchi, Ferreira da Silva, Garzia, Reiljan & Trechsel (European Political Science Review, 2026)
- Source files: 2026-08-21_canalejo_depolarization.json
- Agent: OKF Ingestion Pipeline

## [2026-08-21] ingest | OKF Auto-Ingestion
- Raw: [[raw/articles/2026-08-21_the-janus-face-of-the-liberal-international-inform.md]] — The Janus Face of the Liberal International Information Order: When Global Institutions Are Self-Undermining — Farrell & Newman (International Organization 75(2), 2021)
- Source files: 2026-08-21_farrell_janus_face.json
- Agent: OKF Ingestion Pipeline

## [2026-08-23] ingest | OKF Auto-Ingestion
- Raw: [[raw/articles/2026-08-21_childcare-in-transition-evidence-that-patterns-of-.md]] — Childcare in Transition: Evidence That Patterns of Childcare Differ by Degree of Market Integration in Northwestern Tanzania — Hassan, Lawson, Schaffnit, Urassa & Sear (Demography, 2026)
- Source files: 2026-08-21_hassan_childcare.json
- Agent: OKF Ingestion Pipeline

## [2026-08-23] ingest | OKF Auto-Ingestion
- Raw: [[raw/articles/2026-08-17_group-identity-and-belief-formation-a-microfoundat.md]] — Group Identity and Belief Formation: A Microfoundation of Political Polarization — Bauer, Chen, Hett & Kosfeld (The Economic Journal, 2026)
- Source files: 2026-08-23_bauer_group_identity.json
- Agent: OKF Ingestion Pipeline

## [2026-08-23] ingest | OKF Auto-Ingestion
- Raw: [[raw/articles/2026-08-14_political-polarization-and-counter-attitudinal-inf.md]] — Political Polarization and Counter-attitudinal Information Consumption and Internalization — Larreguy & Tiburcio (The Economic Journal, 2026)
- Source files: 2026-08-23_larreguy_counterattitudinal.json
- Agent: OKF Ingestion Pipeline

## [2026-08-24] ingest | OKF Auto-Ingestion
- Raw: [[raw/articles/2026-08-19_parallel-partisan-public-responsiveness-to-policy-.md]] — Parallel Partisan Public Responsiveness to Policy and the News
- Source files: 2026-08-24_120959_ingestion.json
- Agent: OKF Ingestion Pipeline

## [2026-08-25] ingest | OKF Auto-Ingestion
- Raw: [[raw/articles/2008-04_is-polarization-a-myth.md]] — Is Polarization a Myth?
- Raw: [[raw/articles/2026-08-21_online-discourse-is-falsely-polarized-by-self-sele.md]] — Online Discourse is Falsely Polarized by Self-Selection
- Raw: [[raw/articles/2008-04_is-polarization-a-myth-abramowitz-saunders-the-jou.md]] — Is Polarization a Myth? — Abramowitz & Saunders (The Journal of Politics, 2008)
- Source files: 2026-08-25_002505_ingestion.json, 2026-08-25_categorized.json
- Agent: OKF Ingestion Pipeline

## [2026-08-26] ingest | OKF Auto-Ingestion
- Raw: [[raw/articles/2026-07-26_futuring-practices-in-and-against-the-unequal-dist.md]] — Futuring practices in and against the unequal distribution of futures — Llobet & Rosen (Children's Geographies, 2026)
- Source files: 2026-08-25_llobet-rosen-futuring-children.json
- Agent: OKF Ingestion Pipeline

## [2026-08-27] ingest | OKF Auto-Ingestion
- Raw: [[raw/articles/2026-08-24_where-the-grass-seems-greener-economic-mispercepti.md]] — Where the Grass Seems Greener: Economic Misperceptions and Support for Democracy — Acemoglu et al. (NBER WP 35644, 2026)
- Source files: 2026-08-27_acemoglu-economic-misperceptions-support-democracy.json
- Agent: OKF Ingestion Pipeline

## [2026-08-28] ingest | OKF Auto-Ingestion
- Raw: [[raw/articles/2026-08-10_measuring-narrative-polarization-in-online-discour.md]] — Measuring Narrative Polarization in Online Discourse — Elfes, Bastos & Aiello (PNAS Nexus 5(8), 2026)
- Source files: 2026-08-28_narrative-polarization.json
- Agent: OKF Ingestion Pipeline

## [2026-08-28] ingest | OKF Auto-Ingestion
- Raw: [[raw/articles/2022-06-14_repressed-media-and-illiberal-politics-in-turkey-t.md]] — Repressed media and illiberal politics in Turkey: the persistence of fear — Akser & Baybars (Southeast European and Black Sea Studies 23(1), 2023)
- Source files: 2026-08-28_repressed-media-turkey.json
- Agent: OKF Ingestion Pipeline

## [2026-08-31] ingest | OKF Auto-Ingestion
- Raw: [[raw/articles/2026-08-31_qualitative-research-in-an-era-of-artificial-intel.md]] — Qualitative Research in an Era of Artificial Intelligence: A Pragmatic Approach to Data Analysis, Workflow, and Computation
- Source files: 2026-08-31_categorized.json
- Agent: OKF Ingestion Pipeline

## [2026-09-01] ingest | OKF Auto-Ingestion
- Raw: [[raw/articles/2026-08-31_from-avoider-to-challenger-how-individuals-respond.md]] — From avoider to challenger: How individuals respond when faced with misinformation
- Raw: [[raw/articles/2026-08-27_monitoring-misinformation-building-discernment-a-c.md]] — Monitoring misinformation, building discernment: A crowdsourcing study during the 2025 Australian federal election
- Source files: 2026-09-01_hks-misinfo-review-cift.json
- Agent: OKF Ingestion Pipeline

## [2026-09-03] ingest | OKF Auto-Ingestion
- Raw: [[raw/articles/2026-09-02_toward-an-integrated-and-globally-equitable-unders.md]] — Toward an integrated and globally equitable understanding of political polarization
- Source files: 2026-09-03_nature-comms-global-polarization.json
- Agent: OKF Ingestion Pipeline

