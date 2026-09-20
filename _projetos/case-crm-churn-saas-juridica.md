---
layout: projeto
title: "Redução de churn em 30 dias: régua de ativação para SaaS jurídica"
tipo: case-study
data: 2026-09-20
resumo: "Segmentação comportamental, jornadas de onboarding diferenciadas e fluxo de reativação para reduzir churn early-stage em uma plataforma SaaS jurídica B2B."
ferramentas: [Intercom, CRM, Automação de e-mail]
destaque: true
link_externo: https://claude.ai/artifact/CDnJFZ4tWZg5FmmN43uLPF
---

## Contexto

Projeto hipotético baseado em dinâmicas reais de uma SaaS jurídica B2B voltada a escritórios de advocacia. A empresa concentrava a maior parte do churn nos primeiros 30 dias, com perfil predominante de advogados solo ou escritórios pequenos que assinavam, usavam pouco e cancelavam antes de perceber valor.

O ICP ideal eram escritórios médios e grandes (4+ advogados), com uso recorrente e potencial de expansão para um módulo de gestão (ERP jurídico). O desafio: não era viável cortar a aquisição do perfil fora do ICP a curto prazo — ele representava volume relevante de trial e MRR inicial.

## Problema central

Como separar, dentro da base de novos assinantes, os usuários com potencial de retenção dos que provavelmente churnariam de qualquer forma — e agir de forma diferente com cada grupo?

## Abordagem

Defini quatro segmentos com base em comportamento nos primeiros 14 dias (logins, cálculos realizados, features acessadas, abandono de fluxo):

- **Segmento A — Alto risco de churn:** menos de 3 logins e nenhum cálculo na primeira semana. Intervenção imediata antes do dia 14.
- **Segmento B — Potencial travado:** fez login, tentou um cálculo mas não concluiu. Destravar o primeiro momento "aha" com suporte ativo.
- **Segmento C — ICP ativo:** escritório com 4+ advogados, mais de 5 cálculos em 14 dias. Acelerar expansão para o módulo de gestão.
- **Segmento D — Ex-assinante:** cancelou nos primeiros 60 dias. Reativação com ângulo de produto novo, não de reversão da decisão anterior.

Cada segmento recebeu uma jornada própria no Intercom, com e-mails automatizados, mensagens in-app contextuais, bifurcações por comportamento e alertas para o time de CS.

## Detalhe do fluxo — Segmento A (alto risco)

| Dia | Canal | Ação |
|-----|-------|------|
| 1 | E-mail | Boas-vindas com CTA único: primeiro cálculo em 3 minutos |
| 3 | In-app | Nudge contextual na tela inicial com exemplo pré-preenchido |
| 7 | E-mail | Prova social de perfil similar (caso de uso narrativo) + alerta CS |
| 14 | E-mail | Oferta de sessão de diagnóstico com CS — sem push de desconto |
| 28 | E-mail | Encerramento de ciclo com pesquisa de saída de uma linha |

## Resultados simulados

| Métrica | Resultado |
|---------|-----------|
| Redução no churn de 30 dias (Seg. A + B) | -18 p.p. |
| Taxa de conclusão do 1º cálculo (Seg. B) | 64% |
| Conversão para ERP entre ICP ativo (Seg. C) | 22% |
| Taxa de reativação no 2º trial (Seg. D) | 11% |

Números baseados em benchmarks de SaaS B2B com churn concentrado no early stage.

## Aprendizado principal

A análise de comportamento evidenciou que a etapa de configuração inicial (importação do CNIS) gerava abandono de 40% dos novos usuários — um gargalo que o time de produto não tinha visibilidade clara. O trabalho de CRM tornou o problema de produto mensurável.

Usuários solo que concluíam ao menos 1 cálculo nos primeiros 7 dias tinham retenção quase equivalente ao ICP ideal, o que indicou que o comportamento inicial é um preditor mais forte de retenção do que o tamanho do escritório.

---

*Este é um case hipotético criado para portfólio. Os dados são simulados com base em benchmarks reais de SaaS B2B no Brasil.*
