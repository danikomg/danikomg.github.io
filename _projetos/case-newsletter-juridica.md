---
title: "Newsletter Jurídica: criação de newsletter recorrente para substituir e-mails avulsos"
tipo: case-study
stack: "Intercom · HTML (template próprio) · Google Apps Script · Google Sheets"
date: 2026-09-20
---

# Newsletter Jurídica: criação de newsletter recorrente para substituir e-mails avulsos

**Stack:** Intercom · HTML (template próprio) · Google Apps Script · Google Sheets

## O problema

A comunicação por e-mail de uma SaaS jurídica funcionava com disparos avulsos: cada novidade gerava um e-mail próprio, enviado para toda a base sem estrutura editorial definida. Atualizações de produto, artigos do blog, eventos e parcerias chegavam como mensagens isoladas, sem contexto entre si e sem identidade visual consistente.

Além da fragmentação, o modelo não diferenciava públicos por perfil de uso. O mesmo conteúdo chegava a usuários com comportamentos muito diferentes, e não havia mecanismo para coletar o que a base achava das comunicações.

A taxa média de abertura era de 26% e a de cliques, de 1,5%.

## A solução

Criei a Newsletter Jurídica: uma newsletter recorrente com identidade própria, remetente fixo, estrutura editorial definida e segmentação por perfil de uso.

A publicação foi desenvolvida do zero como arquivo HTML completo, com template construído à mão e testado nos principais clientes de e-mail. Cada edição segue a mesma estrutura de seções:

1. **CJ em Pauta** — novidades e atualizações de produto, com link para vídeo de demonstração quando disponível
2. **Conteúdo editorial** — artigo do blog, parceria ou pauta jurídica relevante para a audiência
3. **Feedback do leitor** — link para coleta de resposta via formulário, com dados salvos automaticamente em Google Sheets via Google Apps Script

As primeiras três edições rodaram com teste A/B de formato para validar a estrutura antes de fixá-la. A partir da nona edição, o disparo passou a ser segmentado em dois públicos: a lista padrão, que recebe a edição completa, e a lista de usuários de um módulo específico, que recebe a mesma edição com um banner exclusivo de produto.

![Diagrama comparativo: modelo anterior de e-mails avulsos e modelo da Newsletter Jurídica](/assets/images/newsletter-diagrama.png)

## Decisões de design

- Criei um remetente com nome próprio ("Sofia") em vez de usar o nome da empresa diretamente, para diferenciar a newsletter dos e-mails transacionais na caixa de entrada e aumentar a sensação de comunicação pessoal

- Construí o template em HTML puro, sem depender de builder de e-mail, para ter controle total sobre a renderização e evitar variações de layout entre clientes de e-mail

- A coleta de feedback foi integrada diretamente em cada edição, não como uma campanha separada: o leitor responde em um clique e os dados chegam automaticamente em uma planilha, sem etapas manuais

- A segmentação por perfil de uso foi implementada sem criar duas newsletters distintas: a mesma edição é disparada para dois públicos diferentes no Intercom, com um bloco condicional de conteúdo para cada um, o que simplifica a produção e mantém a consistência editorial

- As métricas de clique passaram a ser filtradas para excluir bots, que clicam automaticamente em todos os links e distorceriam os dados de engajamento real

## Resultado

- Taxa de abertura média: 26% antes, 31% depois (+5 p.p.)
- Taxa de cliques média: 1,5% antes, 2,6% depois (+1,1 p.p.)
- 15 edições publicadas e disparadas até agosto de 2026
- Feedback estruturado coletado a partir da primeira edição, sem processo manual
- Segmentação por perfil de produto implementada a partir da nona edição, sem duplicar o processo de produção
