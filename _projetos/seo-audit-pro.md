---
title: "SEO Audit Pro: auditoria automatizada de SEO em escala"
tipo: case-study
stack: "n8n · Google Search Console · Google Analytics 4 · Gemini · Google Sheets"
date: 2026-08-31
---

# SEO Audit Pro: auditoria automatizada de SEO em escala

**Stack:** n8n · Google Search Console · Google Analytics 4 · IA generativa (Gemini) · Google Sheets

## O problema

O blog de uma empresa B2B (SaaS jurídico) tinha mais de 300 artigos publicados ao longo de vários anos, sem um processo estruturado para identificar quais precisavam de atualização, correção técnica ou revisão de estrutura. Auditar isso manualmente, artigo por artigo, cruzando dados de tráfego, ranqueamento e qualidade on-page, era inviável em escala — e era o tipo de trabalho que antes dependia de uma agência externa.

## A solução

Construí um workflow no n8n ("SEO Audit Pro") que roda a auditoria de forma automatizada em todo o acervo do blog:

1. **Extração de dados de performance** de cada URL via Google Search Console (cliques, impressões, posição média) e Google Analytics 4 (tráfego, engajamento)
2. **Análise on-page automatizada** de cada artigo (estrutura de headings, presença de FAQ/schema, outros elementos de template)
3. **Avaliação de potencial via IA**, cruzando os dados coletados para apontar oportunidades (ex: página com boa posição mas baixo CTR, ou heading hierarchy quebrada)
4. **Consolidação em planilha estruturada**, com uma linha por URL e as métricas e diagnósticos organizados para leitura e priorização

A primeira rodada completa processou 317 URLs únicas (656 linhas de dados, cruzando GA4, GSC, avaliação on-page e potencial de otimização por IA/GEO).

![Diagrama do fluxo do SEO Audit Pro](/assets/images/fluxo-seo-audit-pro.svg)

## Decisões de design

- Separei a coleta de dados brutos (GSC/GA4) da etapa de diagnóstico via IA, para poder auditar novamente sem reprocessar tudo do zero quando só os dados de tráfego mudam
- Estruturei a saída como planilha (e não relatório em texto) porque o consumo real é priorização: alguém precisa filtrar e ordenar, não só ler
- A auditoria não dispara ações automaticamente — ela alimenta uma rotina manual de escolha e atualização de artigos, mantendo controle editorial sobre o que muda no blog

## Resultado

- Identificou problemas de nível de template (hierarquia de headings, ausência de schema de FAQ) que afetavam múltiplos artigos ao mesmo tempo, e não seriam óbvios olhando artigo por artigo
- Virou a base de uma rotina mensal de atualização de conteúdo antigo (seleção de artigos combinando potencial de SEO, atualizações legais recentes e variedade de temas)
- Substituiu um processo que antes dependia de agência externa, trazendo a auditoria para dentro do time

*(Espaço para incluir, se possível, algum número de antes/depois de tráfego ou CTR em artigos priorizados pela auditoria.)*
