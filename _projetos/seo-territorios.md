---
title: "Descoberta automatizada de novos territórios de palavras-chave"
tipo: case-study
stack: "n8n · Sitemap XML · Gemini · Google Autocomplete · Google Sheets"
date: 2026-09-16
---

# Descoberta automatizada de novos territórios de palavras-chave

**Stack:** n8n · Sitemap XML · Gemini (IA generativa) · Autocomplete do Google · Google Sheets

## O problema

O SEO Audit Pro (outro projeto deste portfólio) resolve a auditoria do que já existe no blog, mas não responde a uma pergunta anterior: quais temas o blog *ainda não cobre* e deveriam ser cobertos? Encontrar esses gaps manualmente depende de intuição e de ferramentas pagas de pesquisa de palavra-chave, e tende a girar em torno dos mesmos núcleos temáticos já conhecidos.

## A solução

Construí um workflow no n8n que descobre territórios de conteúdo novos de forma automatizada e recorrente, sem depender de ferramentas pagas de SEO:

1. **Gatilho semanal** (toda segunda-feira, 7h) inicia o fluxo
2. **Leitura do sitemap** do blog, extraindo e normalizando todas as URLs já publicadas
3. **Geração de territórios adjacentes via IA**: a partir da lista de núcleos temáticos que o blog já cobre, a IA sugere 12 territórios de palavra-chave adjacentes e ainda não explorados, pensando no evento de vida que leva alguém a pesquisar sobre o tema
4. **Expansão de cada território em variações de busca**: perguntas ("como funciona X", "quem tem direito a X"), conectores ("X para", "X depois de") e ordem alfabética, gerando dezenas de consultas por território
5. **Consulta ao autocomplete do Google** para cada variação, com throttle para evitar bloqueio
6. **Filtro de gap e pontuação**: remove o que o blog já cobre, conta a frequência de cada sugestão como proxy de demanda de busca, e classifica em tiers (T1, T2, T3)
7. **Registro do snapshot** em uma planilha, com data, para acompanhar como a demanda por esses termos evolui ao longo do tempo

![Diagrama do fluxo de descoberta de territórios de palavras-chave](/assets/images/fluxo-seo-territorios.svg)

[Baixar o workflow (JSON exportado do n8n, com dados sensíveis removidos)](/assets/workflows/seo-territorios.json)

## Decisões de design

- Usei o autocomplete do Google como proxy de demanda de busca em vez de uma ferramenta paga de palavra-chave (Ahrefs, Semrush), porque o autocomplete já reflete buscas reais de usuários e tem custo zero
- Separei a etapa de geração de território (IA, criativa e menos previsível) da etapa de expansão em variações (regras fixas, determinística), para poder ajustar cada uma independentemente
- O fluxo não decide sozinho o que virar pauta: ele produz um snapshot pontuado e datado na planilha, deixando a priorização editorial como decisão humana
- Guardar o histórico por data (em vez de sobrescrever a mesma linha) permite ver quais termos ganham ou perdem demanda de busca ao longo do tempo, não só uma foto única

## Resultado

- Passou a alimentar a pauta editorial com territórios de conteúdo que não apareceriam só olhando para os núcleos temáticos já conhecidos
- Elimina a dependência de ferramentas pagas de pesquisa de palavra-chave para essa etapa específica de descoberta
- Roda automaticamente toda semana, virando insumo pronto para priorização em vez de uma pesquisa manual recorrente
