---
layout: default
title: Início
---

# Daniel Rodrigues

Analista de marketing com experiência em automação, dados e produção de conteúdo. Abaixo estão projetos que documentam esse trabalho — fluxos de automação, e-books, estratégia, vídeos, mídias sociais e artigos publicados.

{% assign tipos = "case-study,ebook,estrategia,apresentacao,video,midia-social,artigo" | split: "," %}
{% assign nomes_tipos = "Case studies,E-books,Estratégia,Apresentações,Vídeos,Mídias Sociais,Artigos publicados" | split: "," %}

{% for tipo in tipos %}
  {% assign itens = site.projetos | where: "tipo", tipo %}
  {% if itens.size > 0 %}
## {{ nomes_tipos[forloop.index0] }}

<ul>
  {% for item in itens %}
    <li>
      {% if item.url_externo %}
        <a href="{{ item.url_externo }}" target="_blank" rel="noopener">{{ item.title }}</a>
      {% else %}
        <a href="{{ item.url | relative_url }}">{{ item.title }}</a>
      {% endif %}
      {% if item.stack %} — <em>{{ item.stack }}</em>{% endif %}
      {% if item.fonte %} — <em>{{ item.fonte }}</em>{% endif %}
    </li>
  {% endfor %}
</ul>
  {% endif %}
{% endfor %}
