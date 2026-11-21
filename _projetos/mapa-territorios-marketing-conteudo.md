---
title: "O que se busca sobre marketing de conteúdo: um mapa de territórios a partir do autocomplete"
tipo: case-study
stack: "Python · Autocomplete do Google · classificação por regras"
date: 2026-11-21
---

# O que se busca sobre marketing de conteúdo: um mapa de territórios a partir do autocomplete

**Stack:** Python (biblioteca padrão) · Autocomplete do Google · classificação por regras · CSV e JSON

> **Projeto autoral.** Feito por conta própria, com dados públicos coletados em 21/11/2026. Não usa dados, ferramentas internas ou materiais de nenhuma empresa em que trabalhei.

## A pergunta

Quando alguém começa a pesquisar sobre marketing de conteúdo, o que ela ou ele realmente digita? E o que isso diz sobre a distância entre o que quem produz conteúdo gosta de publicar e o que a audiência procura?

## O método

Em vez de partir de uma lista pronta de palavras-chave, usei uma **bola de neve** no autocomplete:

1. **Sementes.** Escolhi à mão 20 temas centrais do marketing de conteúdo, de "calendário editorial" a "storytelling".
2. **Nível 1.** Consultei cada semente, com e sem espaço no fim (o espaço faz o autocomplete sugerir a próxima palavra).
3. **Níveis 2 e 3.** As sugestões que mais se repetiram viraram novas sementes, o que revela caminhos que eu não tinha previsto.
4. **Limpeza.** Unifiquei grafias com e sem acento e descartei 114 termos em outras línguas ou longos demais para serem buscas, e 144 fora do assunto (por exemplo, "persona" como jogo, ou "storytelling" ligado a videogames).
5. **Classificação por regras visíveis.** Cada termo recebeu uma intenção de busca, por regras simples em palavras-chave, que qualquer pessoa pode ler e contestar no código.
6. **Pontuação.** Quanto mais consultas diferentes devolvem um termo, e quanto mais perto do topo ele aparece, maior a pontuação. As faixas são **núcleo** (10% de cima), **adjacente** (os 30% seguintes) e **cauda**.

Foram 320 consultas, com intervalo entre elas, e 1.265 sugestões únicas antes da limpeza. Sobraram **1.007 termos**.

## Decisões de método

- **Sem IA generativa na análise.** Usei regras explícitas para que cada classificação seja auditável. Se uma regra errar, dá para ver onde e corrigir.
- **A bola de neve em vez de uma lista fixa.** O que o autocomplete devolve ensina sobre o território, e a lista final não fica presa ao meu repertório inicial.
- **Distribuição por intenção, não só por volume.** Dois termos com a mesma frequência podem pedir conteúdos muito diferentes: um quer aprender, outro quer um modelo pronto.

## O que apareceu

### 1. A busca é mais por material pronto e curso do que por "como fazer"

<div class="perfil-barra-intencao">
<ul class="barras">
  <li>
    <div class="rotulo"><strong>Subtema ou variação</strong><small>261 termos · 26%</small></div>
    <div class="trilho"><span style="width:100%"></span></div>
  </li>
  <li>
    <div class="rotulo"><strong>Materiais prontos</strong><small>225 termos · 22%</small></div>
    <div class="trilho"><span style="width:86%"></span></div>
  </li>
  <li>
    <div class="rotulo"><strong>Canal e formato</strong><small>159 termos · 16%</small></div>
    <div class="trilho"><span style="width:61%"></span></div>
  </li>
  <li>
    <div class="rotulo"><strong>Formação e cursos</strong><small>124 termos · 12%</small></div>
    <div class="trilho"><span style="width:48%"></span></div>
  </li>
  <li>
    <div class="rotulo"><strong>Definição e conceito</strong><small>83 termos · 8%</small></div>
    <div class="trilho"><span style="width:32%"></span></div>
  </li>
  <li>
    <div class="rotulo"><strong>Ferramentas e IA</strong><small>42 termos · 4%</small></div>
    <div class="trilho"><span style="width:16%"></span></div>
  </li>
  <li>
    <div class="rotulo"><strong>Exemplos e referências</strong><small>40 termos · 4%</small></div>
    <div class="trilho"><span style="width:15%"></span></div>
  </li>
  <li>
    <div class="rotulo"><strong>Como fazer</strong><small>37 termos · 4%</small></div>
    <div class="trilho"><span style="width:14%"></span></div>
  </li>
  <li>
    <div class="rotulo"><strong>Tendências e dados</strong><small>25 termos · 2%</small></div>
    <div class="trilho"><span style="width:10%"></span></div>
  </li>
  <li>
    <div class="rotulo"><strong>Contratação e preço</strong><small>11 termos · 1%</small></div>
    <div class="trilho"><span style="width:4%"></span></div>
  </li>
</ul>
</div>

Somando **materiais prontos** (225 termos, 22%) e **formação e cursos** (124 termos, 12%), mais de um terço do mapa é busca por atalho: PDF, planilha, modelo, curso gratuito. Já "como fazer" aparece em só 37 termos (4%). Exemplos de materiais: “redação publicitaria pdf”; “marketing de conteudo b2b livro”; “redação publicitária a prática na prática pdf”; “calendario editorial notion”.

### 2. O calendário editorial é um território de material pronto

Dos 65 termos ligados a calendário editorial, 35 (54%) pedem material pronto, como "calendário editorial notion", "calendário editorial excel" e "calendário editorial redes sociais download". Outros 12 (18%) trazem ano ou mês, como "calendário editorial 2026". Só 1 termo pede o conceito e 1 pede "como fazer". Quem busca esse tema quer a planilha do ano, não a teoria.

### 3. Marcas viram atalho de formação

HubSpot aparece em 41 termos, 26 deles classificados como formação, quase sempre com "academy" ou "certificação", e a Rock Content aparece em 16. Dentro do próprio tema "marketing de conteúdo", 21 dos 44 termos (48%) são sobre cursos. A marca funciona como substituto da palavra "curso", e isso importa para quem planeja conteúdo de formação.

### 4. A IA já entrou na conversa, inclusive como "skill"

Termos de ferramentas e IA somam 42. Chamou a atenção que "claude" aparece em 18 termos, 17 deles ligados a "copywriting" ("copywriting skill claude" e variações), ou seja, gente procurando instruções prontas para a IA escrever. É um território novo, ainda pequeno, ao lado dos tradicionais.

## Os temas com mais variações

| Tema-semente | Termos distintos |
|---|---|
| storytelling | 148 |
| copywriting | 126 |
| newsletter | 91 |
| inbound marketing | 83 |
| e-mail marketing | 71 |
| calendário editorial | 65 |
| jornada do cliente | 60 |
| seo para blog | 50 |
| roteiro de vídeo | 47 |
| redação publicitária | 47 |

## O núcleo: termos com maior pontuação

| Termo | Intenção | Pontuação |
|---|---|---|
| redação publicitaria pdf | Materiais prontos | 28.34 |
| métricas de conteúdo | Subtema ou variação | 25.17 |
| redação publicitaria curso | Formação e cursos | 22.82 |
| marketing de conteudo b2b livro | Materiais prontos | 21.2 |
| métricas de marketing de conteudo | Subtema ou variação | 20.82 |
| inteligência artificial para criar conteudo | Ferramentas e IA | 20.6 |
| marketing de conteúdo rock content curso | Formação e cursos | 20.14 |
| estratégia de conteúdo para redes sociais | Canal e formato | 19.2 |
| inteligencia artificial para criar conteudo instagram | Ferramentas e IA | 19.2 |
| redação publicitaria senac | Formação e cursos | 19.0 |
| inteligencia artificial para conteudo | Ferramentas e IA | 18.56 |
| inbound marketing curso gratuito | Formação e cursos | 18.45 |

## Limites do estudo

- **Autocomplete não é volume de busca.** Ele mostra o que o Google sugere, não quantas pessoas pesquisam. Uso a repetição como indício de relevância, nunca como número de buscas.
- **A coleta é de um dia só.** As sugestões mudam com o tempo, a região e o histórico de quem pesquisa. Um retrato, não uma série.
- **As sementes são escolhas minhas.** Temas que eu não listei ficam sub-representados, e comparar canais (e-mail, LinkedIn, Instagram) não é confiável, porque "newsletter", "e-mail marketing" e "conteúdo para linkedin" estavam entre as sementes e puxam essas contagens para cima. "Pauta de conteúdo" e "métricas de conteúdo", por exemplo, devolveram poucas sugestões.
- **As regras de classificação são simples.** Há termos que caem em "subtema ou variação" por falta de uma regra melhor, e essa é a maior categoria (261 termos).
- **Mesmo com limpeza, sobra ruído.** Revisei por amostra, mas o filtro por palavras-chave não pega tudo.

## Arquivos para reproduzir

- [termos.csv](/assets/territorios/termos.csv): os 1.007 termos, já classificados
- [resumo.json](/assets/territorios/resumo.json): os agregados usados nesta página
- [coletar.py](/assets/territorios/coletar.py): a coleta em bola de neve
- [analisar.py](/assets/territorios/analisar.py): limpeza, classificação e pontuação

Para rodar, basta ter Python 3 e executar `python3 coletar.py bruto.json` e depois `python3 analisar.py bruto.json pasta_de_saida`. Trocar as sementes no começo de `coletar.py` gera o mapa de qualquer outro tema.

<style>
  .barras { list-style: none; padding: 0; margin: 1rem 0; }
  .barras li { margin-bottom: .9rem; }
  .barras .rotulo { display: flex; justify-content: space-between; align-items: baseline; }
  .barras small { color: #6b5b95; font-size: .78rem; }
  .barras .trilho { height: 8px; background: #eee9f5; border-radius: 4px; margin-top: .3rem; }
  .barras .trilho span { display: block; height: 100%; background: #5b2a86; border-radius: 4px; }
</style>
