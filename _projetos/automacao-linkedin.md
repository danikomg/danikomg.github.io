---
title: "Automação de publicação no LinkedIn com n8n"
tipo: case-study
stack: "n8n · Google Sheets · Gemini · Google Drive · Slack"
date: 2026-08-31
---

# Automação de publicação no LinkedIn com n8n

**Stack:** n8n · Google Sheets · Gemini (IA generativa) · Google Drive · Slack

## O problema

A publicação de conteúdo no LinkedIn de uma empresa B2B (SaaS jurídico) dependia de um processo manual: alguém precisava acompanhar o calendário editorial, escrever a legenda a partir do artigo do blog, gerar uma arte de capa e publicar no horário certo — toda semana, sem falha. Esse processo consumia tempo do time de marketing em uma tarefa repetitiva e sujeita a atrasos quando havia sobrecarga de outras entregas.

## A solução

Desenhei e implementei um workflow no n8n que automatiza o processo do início ao fim, mantendo um ponto de aprovação humana antes da publicação:

1. **Gatilho agendado** (toda quinta, 10h15) inicia o fluxo
2. **Leitura do calendário editorial** em uma planilha do Google Sheets, filtrando apenas os itens marcados como "a publicar"
3. **Extração automática do conteúdo** do artigo do blog correspondente
4. **Geração da legenda** via IA generativa, a partir do artigo e de diretrizes de tom de voz
5. **Revisão automática de estilo**, uma segunda passada de IA para eliminar maneirismos e padronizar o texto
6. **Geração da arte de capa**, também via IA
7. **Upload dos ativos** para uma pasta compartilhada no Google Drive
8. **Atualização de status** na planilha (de "a publicar" para "em revisão")
9. **Aprovação final via Slack**, com botões para aprovar ou pedir ajuste antes da publicação

![Diagrama do fluxo de automação de publicação no LinkedIn](/assets/images/fluxo-linkedin.svg)

[Baixar o workflow (JSON exportado do n8n, com dados sensíveis removidos)](/assets/workflows/automacao-linkedin.json)

## Decisões de design

- Mantive uma etapa de aprovação humana no fim do fluxo em vez de publicação 100% automática, para preservar controle editorial e evitar erros de IA indo ao ar sem revisão
- Separei a geração de conteúdo da revisão de estilo em duas chamadas de IA distintas, porque um único prompt genérico não segurava a consistência de tom ao longo do tempo
- Usei a planilha existente do calendário editorial como fonte da verdade, em vez de criar um sistema paralelo, para não mudar a rotina do time de conteúdo

## Resultado

- Eliminou o trabalho manual semanal de montar o post (legenda + arte)
- Reduziu o tempo de execução da tarefa de ~30-45 minutos por semana (escrever legenda, gerar e ajustar arte, publicar no horário certo) para ~5-10 minutos (revisar e aprovar no Slack)
- Deu ao time apenas a tarefa de aprovar/ajustar, em vez de produzir do zero
- Antes, a publicação também dependia de encaixar a tarefa na fila de prioridades da semana; com o fluxo automatizado, o post fica pronto para aprovação toda quinta às 10h15, sem depender de disponibilidade de alguém para começar
