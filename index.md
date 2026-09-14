---
layout: default
title: Início
---

# Daniel Rodrigues

Analista de marketing com experiência em automação, dados e produção de conteúdo. Abaixo estão projetos que documentam esse trabalho — fluxos de automação, e-books, apresentações e vídeos.

{% assign tipos = "case-study,ebook,apresentacao,video" | split: "," %}
{% assign nomes_tipos = "Case studies,E-books,Apresentações,Vídeos" | split: "," %}

{% for tipo in tipos %}
  {% assign itens = site.projetos | where: "tipo", tipo %}
  {% if itens.size > 0 %}
## {{ nomes_tipos[forloop.index0] }}

<ul>
  {% for item in itens %}
    <li>
      <a href="{{ item.url | relative_url }}">{{ item.title }}</a>
      {% if item.stack %} — <em>{{ item.stack }}</em>{% endif %}
    </li>
  {% endfor %}
</ul>
  {% endif %}
{% endfor %}
