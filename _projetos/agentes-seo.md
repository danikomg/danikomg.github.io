---
title: "Agentes de IA para produção e otimização de artigos de SEO"
tipo: case-study
stack: "Gemini Gems · Pesquisa em fontes oficiais · Markdown/Jekyll frontmatter"
date: 2026-09-16
---

# Agentes de IA para produção e otimização de artigos de SEO

**Stack:** Gemini Gems (agentes de prompt configurados) · Google Drive (base de conhecimento) · Markdown/Jekyll frontmatter

## O problema

Escrever artigos técnicos para um blog jurídico exige três coisas que raramente convivem bem no mesmo processo: precisão factual (citar a lei certa, a fonte oficial certa, o número do tema/súmula certo), uma voz editorial consistente que não soe como texto genérico de IA, e conformidade estrutural com o formato exato que o blog espera (frontmatter, FAQ, CTA, links internos). Fazer isso manualmente artigo por artigo é lento; fazer tudo em um único prompt de IA tende a misturar as três preocupações e piorar todas elas ao mesmo tempo.

## A solução

Desenhei três agentes especializados no Gemini (Gems), cada um responsável por uma única etapa da produção, encadeados em pipeline:

**Agente 1 — Estrategista de Briefing.** Recebe um destes dois pontos de entrada: uma palavra-chave nova (do projeto de descoberta de territórios) ou um artigo já publicado junto com sua auditoria de SEO (saída do SEO Audit Pro, outro projeto deste portfólio). A partir disso, classifica cada trecho do conteúdo original em Preservar, Atualizar, Incluir ou Remover, e produz um briefing prescritivo: estrutura exata de H2/H3, bloco de FAQ, e uma sugestão de CTA final coerente com o estágio de funil do tema (topo, meio ou fundo).

**Agente 2 — Redator com pesquisa profunda.** Segue o briefing à risca (não cria, não remove, não reordena seções) e escreve o artigo base pesquisando exclusivamente em fontes oficiais.

<pre style="white-space: pre-wrap; background: #f6f8fa; border: 1px solid #d0d7de; border-radius: 6px; padding: 12px; font-size: 13px;">
Regra número 2 — Pesquisa profunda só em fontes oficiais (DeepSearch)
Faça pesquisa profunda e consulte somente fontes oficiais primárias. Lista branca:
Legislação: planalto.gov.br (leis, decretos, Constituição), portais de normas oficiais.
Previdência / Trabalho: gov.br/inss, gov.br/esocial, gov.br/trabalho-e-emprego, gov.br/previdencia,
Instruções Normativas e Portarias publicadas no Diário Oficial da União (in.gov.br).
Tribunais: stf.jus.br, stj.jus.br, tst.jus.br, cjf.jus.br, TNU, TRFs e TJs oficiais.
[...]
Proibido como fonte: blogs jurídicos, escritórios concorrentes, Jusbrasil, agregadores,
fóruns, redes sociais, conteúdo gerado por IA de terceiros.

Regra número 3 — Zero alucinação
Só afirme o que conseguir verificar em fonte oficial. [...] Se um ponto do briefing não tiver
respaldo oficial localizável, escreva a seção com o que é verificável e sinalize entre colchetes
[VERIFICAR: ...] o que precisa de confirmação humana — não preencha com suposição.
</pre>

**Agente 3 — Editor e voz editorial.** Recebe o artigo base, tecnicamente correto mas "cru", e aplica a voz da marca sem tocar na precisão técnica nem na estrutura.

<pre style="white-space: pre-wrap; background: #f6f8fa; border: 1px solid #d0d7de; border-radius: 6px; padding: 12px; font-size: 13px;">
A voz de [Empresa] (essência)
[Empresa] existe para transformar o complexo em simples. Arquétipo: Sábio Acessível +
Homem Comum — fala com a mesma clareza para o advogado do interior e para o
escritório de São Paulo. [...]
• Primeira pessoa do singular. Quem escreve é um advogado experiente compartilhando
  o que sabe ("na minha experiência…", "o que eu sempre oriento…").
• Sem juridiquês. Traduza o tecniquês. [...] Simples não é raso: é o complexo explicado
  de um jeito que qualquer advogado aplica na segunda-feira de manhã.

Cadência e naturalidade (evite cara de texto de IA)
Nada de "vale ressaltar", "é importante destacar", "em suma", "no mundo de hoje", "de forma
eficaz/eficiente", gerúndio empilhado ou conclusões genéricas de autoajuda.
Evite começar parágrafos sempre do mesmo jeito e listas com bold + emoji.
Prefira verbo no presente, voz ativa, exemplos concretos do dia a dia do advogado.
</pre>

O Agente 3 entrega o artigo como um arquivo `.md` completo, já no frontmatter exato usado pelos posts do blog, pronto para commit no repositório. Campos que dependem de um ativo ou de uma decisão humana (autor, categoria, permalink, imagem) ficam marcados com `[PREENCHER]` em vez de receberem um valor inventado.

![Diagrama do pipeline dos 3 agentes de produção e otimização de artigos](/assets/images/fluxo-agentes-seo.svg)

## Decisões de design

- Separei em três agentes especializados em vez de um único prompt, porque pesquisa factual, redação e voz editorial pedem critérios de julgamento diferentes; um prompt genérico tende a fazer as três coisas de forma mediana
- O Agente 2 tem uma lista branca explícita de fontes oficiais e a instrução de sinalizar `[VERIFICAR: ...]` em vez de inventar quando não encontra respaldo, para que o texto nunca afirme algo sem base legal rastreável
- Mantive rigidez estrutural entre as etapas (o Agente 2 não pode alterar os H2/H3 do briefing do Agente 1; o Agente 3 não pode alterar a estrutura nem os fatos do Agente 2), para que cada etapa confie no que a anterior já decidiu, em vez de reabrir decisões a cada passagem
- O Agente 1 aceita dois pontos de entrada diferentes: uma palavra-chave nova, ou a saída de uma auditoria de SEO de um artigo existente, o que conecta este projeto de produção de conteúdo diretamente aos outros dois projetos de automação de SEO deste portfólio
- O output final já sai no frontmatter exato do blog, com os campos que exigem uma decisão humana claramente marcados, para que publicar seja colar o arquivo, não reformatar o texto

## Resultado

- Reduziu o tempo entre "pauta definida" e "artigo pronto para revisão humana", separando pesquisa, escrita e edição em etapas que rodam de forma independente
- Padronizou a voz editorial entre artigos escritos em momentos diferentes, sem depender de um único redator para manter a consistência
- Fechou o ciclo dos três projetos de SEO deste portfólio: descoberta de território → produção ou otimização do artigo → auditoria do que já está no ar
