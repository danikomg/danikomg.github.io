# Portfólio de Daniel Rodrigues

Site em Jekyll publicado com GitHub Pages em https://danikomg.github.io.

## Estrutura

```
.
├── _config.yml        configuração do Jekyll (tema, coleção de projetos)
├── index.md           página inicial, agrupa os projetos por tipo automaticamente
├── _includes/         trechos reutilizáveis (ex: seção "Como eu trabalho")
├── _layouts/          layout das páginas
├── _projetos/         cada arquivo .md vira uma página de projeto
└── assets/            imagens, PDFs e vídeos usados nos projetos
```

## Como adicionar um projeto

Crie um arquivo em `_projetos/` com um campo `tipo` no início (front matter). Ele define em qual seção da home o projeto aparece: `case-study`, `ebook`, `estrategia`, `apresentacao`, `video`, `midia-social` ou `artigo`.

Para esconder um projeto sem apagar o arquivo, use `published: false`. Atenção: o arquivo continua visível no repositório público, então não use isso para conteúdo confidencial.
