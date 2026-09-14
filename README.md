# Estrutura do portfólio

```
.
├── _config.yml              # configuração do Jekyll (tema, coleção de projetos)
├── index.md                 # página inicial, agrupa os projetos por tipo automaticamente
├── _projetos/                # cada arquivo .md aqui vira uma página de projeto
│   ├── EXEMPLO-case-study.md      # apagar depois de seguir as instruções dentro dele
│   ├── EXEMPLO-ebook.md
│   ├── EXEMPLO-apresentacao.md
│   └── EXEMPLO-video.md
└── assets/
    ├── images/               # diagramas e prints dos workflows
    └── files/                # PDFs de e-books e apresentações
```

## Tipos de projeto

Cada arquivo em `_projetos/` precisa de um campo `tipo` no front matter,
que controla em qual seção da home ele aparece:

- `case-study` — fluxos de automação (os que já escrevemos: LinkedIn e SEO Audit Pro)
- `ebook` — e-books e materiais em PDF
- `apresentacao` — slides e apresentações
- `video` — vídeos (embed do YouTube ou link)

Veja os 4 arquivos `EXEMPLO-*.md` para o formato de cada tipo.

## Passo a passo para publicar

1. **Crie o repositório no GitHub** com o nome exato `danikomg.github.io`
   (esse nome específico ativa o GitHub Pages automaticamente para todo o site).

2. **Suba os arquivos desta pasta** para a raiz do repositório.

3. **Mova os dois case studies já escritos** (LinkedIn e SEO Audit Pro) para
   dentro de `_projetos/`, seguindo o `EXEMPLO-case-study.md`.

4. **Adicione os outros projetos** (e-books, apresentações, vídeos) criando
   um arquivo novo em `_projetos/` para cada um, a partir do exemplo correspondente.
   PDFs vão em `assets/files/`, imagens em `assets/images/`.

5. **Ative o GitHub Pages**: Settings → Pages → Source → branch `main`, pasta `/ (root)`.

6. Em alguns minutos o site fica disponível em `https://danikomg.github.io`.

## Próximos ajustes possíveis
- Trocar o tema `pages-themes/minimal` por outro do catálogo oficial
  (https://pages.github.com/themes/).
- Adicionar uma seção "Sobre" como página separada (`sobre.md`).
- Se a lista de projetos crescer muito, dá pra criar páginas de índice
  separadas por tipo (ex: `/case-studies/`, `/ebooks/`) em vez de tudo na home.
