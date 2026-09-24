---
title: "Segmentação comportamental para reduzir churn early-stage em SaaS jurídica"
tipo: case-study
stack: "Intercom · Google Sheets · Segmentação comportamental · Automação de e-mail e in-app"
date: 2026-09-20
---

# Segmentação comportamental para reduzir churn early-stage em SaaS jurídica

**Stack:** Intercom · Google Sheets · Segmentação comportamental · Automação de e-mail e in-app

## O problema

Uma SaaS jurídica B2B com foco em cálculos previdenciários e gestão de escritórios concentrava a maior parte do churn nos primeiros 30 dias de assinatura. O perfil predominante entre os que cancelavam: advogados solo ou escritórios com 1 a 3 pessoas que assinavam, usavam pouco o produto e não percebiam valor suficiente para renovar.

O ICP ideal da empresa eram escritórios médios e grandes (4+ advogados), com uso recorrente e potencial de expansão para um módulo de gestão (ERP jurídico). O problema: a aquisição ainda atraía volume alto do perfil fora do ICP, inflando o churn e distorcendo as métricas de cohort.

A régua de onboarding era genérica: a mesma sequência de e-mails para um advogado solo e para um escritório de 20 pessoas, o que reduzia a relevância das mensagens para qualquer perfil.

## A solução

Defini quatro segmentos com base em comportamento nos primeiros 14 dias, cruzando dados de uso do produto (logins, cálculos realizados, features acessadas, abandono de fluxo) com o perfil declarado no cadastro:

1. **Segmento A — Alto risco de churn:** menos de 3 logins e nenhum cálculo na primeira semana. Gatilho de intervenção imediata antes do dia 14.
2. **Segmento B — Potencial travado:** fez login, tentou um cálculo mas não concluiu. Foco em destravar o primeiro momento "aha" com suporte contextual e ativo.
3. **Segmento C — ICP ativo:** escritório com 4+ advogados, mais de 5 cálculos em 14 dias, acesso a mais de uma feature. Foco em expansão para o módulo de gestão.
4. **Segmento D — Ex-assinante:** cancelou nos primeiros 60 dias. Fluxo de reativação com ângulo de produto novo, não de reversão da decisão anterior.

Cada segmento recebeu uma jornada própria no Intercom, com e-mails automatizados, mensagens in-app contextuais, bifurcações por comportamento e alertas para o time de CS.

![Diagrama do fluxo de segmentação comportamental](/assets/images/crm-fluxo-segmentacao.png)

## Decisões de design

- Não usei tamanho do escritório como critério principal de segmentação: o comportamento nos primeiros 7 dias se mostrou um preditor mais forte de retenção do que o perfil declarado no cadastro

- O Segmento B recebeu mensagens que referenciavam o tipo de cálculo que o usuário tentou fazer (identificado pela sessão), e não mensagens genéricas de "tutorial". Isso aumentou a taxa de abertura porque a relevância percebida era alta

- A intervenção do Segmento A no dia 14 foi uma oferta de sessão de diagnóstico com CS, sem desconto de retenção. A hipótese era que usuários sem nenhum uso em 14 dias precisavam de orientação, não de preço

- O fluxo de reativação (Segmento D) foi construído como uma atualização de produto, não como um e-mail de "volte". O primeiro contato em 30 dias não tinha CTA de reativação explícito: apresentava uma novidade genuína e deixava a decisão de retorno aberta

- A análise de comportamento evidenciou que a etapa de configuração inicial (importação do CNIS) gerava abandono de 40% dos novos usuários, um gargalo que o time de produto não tinha visibilidade clara. O trabalho de CRM tornou o problema de produto mensurável

## Resultado

- Redução de 18 p.p. no churn de 30 dias nos Segmentos A e B combinados
- 64% de taxa de conclusão do primeiro cálculo entre usuários do Segmento B (potencial travado)
- 22% de conversão para o módulo de ERP entre usuários do Segmento C (ICP ativo)
- 11% de taxa de reativação no segundo trial entre ex-assinantes do Segmento D
- Identificação de gargalo crítico de produto que gerou demanda prioritária de melhoria na etapa de onboarding técnico

---

*Case hipotético criado para portfólio. Dados simulados com base em benchmarks de SaaS B2B no Brasil.*
