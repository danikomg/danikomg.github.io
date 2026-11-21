#!/usr/bin/env python3
"""
Limpa, classifica e agrega a coleta do autocomplete.

Entrada: bruto.json (saída de coletar.py)
Saída:   termos.csv  (um termo por linha, já limpo e classificado)
         resumo.json (agregados usados na página do projeto)
"""
import csv
import json
import re
import sys
import unicodedata
from collections import Counter, defaultdict


def sem_acento(s):
    return "".join(c for c in unicodedata.normalize("NFD", s) if unicodedata.category(c) != "Mn")


def norm(s):
    return re.sub(r"\s+", " ", sem_acento(s.lower())).strip()


# ---------------------------------------------------------------- limpeza
INGLES = {
    "the", "in", "with", "for", "to", "how", "jobs", "remote", "part", "time", "last", "days",
    "of", "and", "best", "free", "what", "is", "your", "you", "tool", "tools", "writer", "writing",
    "website", "analyzer", "examples", "template", "templates", "marketing", "content", "strategy",
    "course", "online", "near", "me", "ai", "blog", "post", "seo", "plan", "generator", "checker",
}
# palavras do inglês que também são comuns no jargão em português: só contam se vierem juntas
PALAVRAS_PT_JARGAO = {"marketing", "content", "ai", "blog", "post", "seo", "template", "templates", "tool", "tools", "plan", "examples", "online"}
OUTRAS_LINGUAS = {"và", "là", "gì", "y", "qué", "cómo", "los", "las", "el", "una", "difference", "between"}
INGLES_FORTE = (INGLES - PALAVRAS_PT_JARGAO) | OUTRAS_LINGUAS

FORA_DE_ESCOPO = [
    "persona non grata", "persona 5", "persona 4", "persona 3", "persona tv", "persona jogo",
    "desconto", "cupom", "hostinger", "tradu", "emprego", "vaga", "vagas", "salario",
    "deltarune", "undertale", "toby", "fox", "conjug", "adulto", "xxx", "sexo", "porn", "jogo", "game",
    "filme", "serie", "novela", "letra de", "musica", "banda", "anime", "personagem", "terraria",
]


def eh_ingles(t):
    toks = t.split()
    if len(toks) > 9:
        return True  # frases longas demais: provavelmente títulos de página, não buscas
    if any(x in OUTRAS_LINGUAS for x in toks):
        return True
    fortes = sum(1 for x in toks if x in INGLES_FORTE)
    return fortes >= 2 or (fortes >= 1 and len(toks) >= 3 and sum(1 for x in toks if x in INGLES) >= 3)


def fora_de_escopo(t):
    return any(f in t for f in FORA_DE_ESCOPO)


# ---------------------------------------------------------------- intenção
REGRAS_INTENCAO = [
    ("Formação e cursos", ["curso", "cursos", "senac", "sebrae", "escola", "academy", "faculdade", "graduacao", "certificacao", "formacao", "treinamento", "aula", "aulas", "workshop", "bootcamp", "mba", "pos graduacao", "university", "skillshare", "udemy", "alura", "coursera"]),
    ("Materiais prontos", ["pdf", "download", "baixar", "planilha", "excel", "modelo", "modelos", "template", "templates", "notion", "trello", "canva", "checklist", "gratis", "gratuito", "gratuita", "livro", "ebook", "e-book", "slides", "ppt"]),
    ("Ferramentas e IA", ["ferramenta", "ferramentas", "software", "plataforma", "app", "aplicativo", "gerador", "ia", "inteligencia artificial", "chatgpt", "claude", "gpt", "gemini", "copilot", "automacao", "automatizar"]),
    ("Contratação e preço", ["agencia", "empresa", "empresas", "contratar", "preco", "precos", "quanto custa", "quanto cobrar", "orcamento", "servico", "servicos", "freelancer", "freela", "consultoria"]),
    ("Tendências e dados", ["tendencias", "tendencia", "estatisticas", "estatistica", "dados", "pesquisa", "relatorio", "benchmark", "2025", "2026", "futuro", "mercado"]),
    ("Exemplos e referências", ["exemplo", "exemplos", "inspiracao", "cases", "case", "casos de sucesso", "ideias", "ideia"]),
    ("Definição e conceito", ["o que e", "oque e", "o que significa", "significado", "conceito", "definicao", "para que serve", "o que faz", "tipos de", "diferenca", " vs ", "ou "]),
    ("Como fazer", ["como", "passo a passo", "dicas", "melhores praticas", "guia", "estrategia para", "como criar", "como fazer", "como escrever"]),
]


def intencao(t):
    global CANAIS
    pad = f" {t} "
    for nome, chaves in REGRAS_INTENCAO:
        for c in chaves:
            if (" " in c and c in t) or (" " not in c and f" {c} " in pad):
                return nome
    if any(c in t for cs in CANAIS.values() for c in cs):
        return "Canal e formato"
    return "Subtema ou variação"


# ---------------------------------------------------------------- entidades e canais
FERRAMENTAS_MARCAS = {
    "Notion": ["notion"], "Excel": ["excel"], "Trello": ["trello"], "Canva": ["canva"], "ChatGPT": ["chatgpt", "chat gpt"], "Claude": ["claude"],
    "Rock Content": ["rock content", "rock university"], "RD Station": ["rd station"], "Hotmart": ["hotmart"],
    "HubSpot": ["hubspot"], "Google (docs/sheets/trends)": ["google docs", "google sheets", "google trends", "google analytics"],
}
CANAIS = {
    "Instagram": ["instagram"], "LinkedIn": ["linkedin"], "YouTube": ["youtube"], "TikTok": ["tiktok"],
    "Blog": ["blog"], "E-mail": ["email", "e-mail", "newsletter"], "Redes sociais (geral)": ["redes sociais", "social media"],
    "WhatsApp": ["whatsapp"], "Podcast": ["podcast"],
}


def acha(mapa, t):
    return [k for k, vs in mapa.items() if any(v in t for v in vs)]


def main(entrada, pasta):
    d = json.load(open(entrada, encoding="utf-8"))
    bruto = d["sugestoes"]

    # 1) agrupa variantes com e sem acento
    grupos = {}
    for s in bruto:
        k = norm(s["termo"])
        g = grupos.setdefault(k, {"termo": s["termo"], "consultas": 0, "temas": set(), "prof": 99, "pos": [], "variantes": 0})
        g["consultas"] += s["consultas"]
        g["temas"].update(s["temas"])
        g["prof"] = min(g["prof"], s["profundidade"])
        g["pos"].append(s["posicao_media"])
        g["variantes"] += 1
        if "ç" in s["termo"] or "ã" in s["termo"] or "é" in s["termo"] or "ê" in s["termo"]:
            g["termo"] = s["termo"]  # prefere a grafia acentuada

    total_bruto = len(grupos)
    descartados = Counter()
    limpos = []
    for k, g in grupos.items():
        if eh_ingles(k):
            descartados["inglês"] += 1
            continue
        if fora_de_escopo(k):
            descartados["fora do tema ou ruído"] += 1
            continue
        g["chave"] = k
        limpos.append(g)

    # 2) classificação
    for g in limpos:
        k = g["chave"]
        g["intencao"] = intencao(k)
        g["ferramentas"] = acha(FERRAMENTAS_MARCAS, k)
        g["canais"] = acha(CANAIS, k)
        g["pos_media"] = round(sum(g["pos"]) / len(g["pos"]), 2)
        g["tema"] = sorted(g["temas"])[0] if len(g["temas"]) == 1 else "transversal"

    # 3) pontuação e faixas (nomes próprios: núcleo, adjacente, cauda)
    for g in limpos:
        g["score"] = round(g["consultas"] * 2 + len(g["temas"]) * 3 + (4 - min(g["prof"], 3)) + (6 - min(g["pos_media"], 6)) * 0.3, 2)
    ordenados = sorted(limpos, key=lambda g: -g["score"])
    n = len(ordenados)
    for i, g in enumerate(ordenados):
        g["faixa"] = "núcleo" if i < n * 0.10 else "adjacente" if i < n * 0.40 else "cauda"

    # 4) saída por termo
    with open(f"{pasta}/termos.csv", "w", encoding="utf-8", newline="") as f:
        w = csv.writer(f)
        w.writerow(["termo", "tema_semente", "intencao", "faixa", "pontuacao", "consultas_que_devolveram", "profundidade", "posicao_media", "canais", "ferramentas_ou_marcas"])
        for g in ordenados:
            w.writerow([g["termo"], g["tema"], g["intencao"], g["faixa"], g["score"], g["consultas"], g["prof"], g["pos_media"], "|".join(g["canais"]), "|".join(g["ferramentas"])])

    # 5) agregados
    por_intencao = Counter(g["intencao"] for g in limpos)
    por_tema = Counter(g["tema"] for g in limpos)
    por_faixa = Counter(g["faixa"] for g in limpos)
    canais = Counter(c for g in limpos for c in g["canais"])
    ferr = Counter(c for g in limpos for c in g["ferramentas"])

    # modificadores mais frequentes (palavras que acompanham os termos)
    stop = set("de do da dos das para o a os as e em no na nos nas um uma com por que como ao ou se sem sobre pra".split())
    mods = Counter()
    for g in limpos:
        for tk in set(g["chave"].split()):
            if tk not in stop and len(tk) > 2:
                mods[tk] += 1
    base_tokens = set()
    for s in d["sementes"]:
        base_tokens.update(norm(s).split())
    mods_sem_base = [(m, c) for m, c in mods.most_common(200) if m not in base_tokens][:30]

    # tema x intenção
    matriz = defaultdict(Counter)
    for g in limpos:
        matriz[g["tema"]][g["intencao"]] += 1

    # exemplos por intenção e por tema (os de maior pontuação)
    ex_intencao = defaultdict(list)
    for g in ordenados:
        if len(ex_intencao[g["intencao"]]) < 6:
            ex_intencao[g["intencao"]].append(g["termo"])
    ex_tema = defaultdict(list)
    for g in ordenados:
        if len(ex_tema[g["tema"]]) < 5:
            ex_tema[g["tema"]].append(g["termo"])

    # termos que aparecem por mais de um tema (pontes entre territórios)
    pontes = [g["termo"] for g in ordenados if len(g["temas"]) >= 2][:15]

    resumo = {
        "coletado_em": d["coletado_em"],
        "total_consultas": d["total_consultas"],
        "sementes": d["sementes"],
        "sugestoes_brutas": len(bruto),
        "sugestoes_apos_unir_variantes": total_bruto,
        "descartados": dict(descartados),
        "termos_finais": len(limpos),
        "por_intencao": por_intencao.most_common(),
        "por_tema": por_tema.most_common(),
        "por_faixa": por_faixa.most_common(),
        "canais": canais.most_common(),
        "ferramentas_marcas": ferr.most_common(),
        "modificadores": mods_sem_base,
        "matriz_tema_intencao": {t: dict(c) for t, c in matriz.items()},
        "exemplos_por_intencao": ex_intencao,
        "exemplos_por_tema": ex_tema,
        "nucleo_top25": [g["termo"] for g in ordenados[:25]],
        "pontes": pontes,
    }
    json.dump(resumo, open(f"{pasta}/resumo.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(json.dumps({k: resumo[k] for k in ["sugestoes_brutas", "sugestoes_apos_unir_variantes", "descartados", "termos_finais", "por_intencao", "por_faixa", "canais", "ferramentas_marcas"]}, ensure_ascii=False, indent=1))


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
