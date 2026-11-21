#!/usr/bin/env python3
"""
Mapa de territórios de busca em marketing de conteúdo (PT-BR).

Método: "bola de neve" no autocomplete do Google.
  Nível 0: sementes escolhidas à mão (temas centrais do marketing de conteúdo).
  Nível 1: sugestões de cada semente (com e sem espaço final, que pede a próxima palavra).
  Nível 2: as sugestões mais recorrentes do nível 1 viram novas sementes.
  Nível 3: as mais recorrentes do nível 2, em número limitado.

Cada sugestão guarda quantas consultas a devolveram, de quais temas-semente ela veio,
a profundidade mínima e a posição média na lista. Tudo isso alimenta a análise.

Uso:  python3 coletar.py saida.json
Requer apenas a biblioteca padrão do Python. Respeita um intervalo entre consultas.
"""
import json
import sys
import time
import urllib.parse
import urllib.request
from collections import defaultdict

URL = "https://suggestqueries.google.com/complete/search?client=chrome&hl=pt-BR&gl=BR&q={q}"
INTERVALO = 0.35          # segundos entre consultas
LIMITE_NIVEL2 = 160       # quantas sugestões do nível 1 viram sementes
LIMITE_NIVEL3 = 120       # quantas do nível 2 viram sementes

SEMENTES = [
    "marketing de conteúdo",
    "estratégia de conteúdo",
    "calendário editorial",
    "pauta de conteúdo",
    "seo para blog",
    "copywriting",
    "storytelling",
    "newsletter",
    "e-mail marketing",
    "inbound marketing",
    "funil de conteúdo",
    "jornada do cliente",
    "persona",
    "conteúdo para linkedin",
    "conteúdo b2b",
    "roteiro de vídeo",
    "reaproveitar conteúdo",
    "métricas de conteúdo",
    "inteligência artificial para conteúdo",
    "redação publicitária",
]

cache = {}
consultas = 0
falhas = 0


def sugerir(q):
    global consultas, falhas
    if q in cache:
        return cache[q]
    url = URL.format(q=urllib.parse.quote(q))
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (pesquisa-autoral)"})
    lista = []
    ok = False
    for tentativa in range(3):
        try:
            with urllib.request.urlopen(req, timeout=15) as r:
                dados = json.loads(r.read().decode("utf-8"))
            lista = [s.strip() for s in dados[1]]
            ok = True
            break
        except Exception:
            time.sleep(2 * (tentativa + 1))
    if not ok:
        falhas += 1
    cache[q] = lista
    consultas += 1
    time.sleep(INTERVALO)
    if consultas % 50 == 0:
        print(f"  {consultas} consultas feitas", file=sys.stderr)
    return lista


def main(saida):
    # registro por sugestão
    reg = defaultdict(lambda: {"consultas": set(), "temas": set(), "prof": 99, "posicoes": []})

    def registrar(termo_consulta, tema, prof):
        for pos, s in enumerate(sugerir(termo_consulta), start=1):
            chave = s.lower()
            r = reg[chave]
            r["consultas"].add(termo_consulta)
            r["temas"].add(tema)
            r["prof"] = min(r["prof"], prof)
            r["posicoes"].append(pos)
        return None

    # nível 1
    for tema in SEMENTES:
        registrar(tema, tema, 1)
        registrar(tema + " ", tema, 1)

    sementes_set = {s.lower() for s in SEMENTES}

    def top(prof, limite):
        itens = [
            (k, v) for k, v in reg.items()
            if v["prof"] == prof and k not in sementes_set
        ]
        itens.sort(key=lambda kv: (-len(kv[1]["consultas"]), -len(kv[1]["temas"]), sum(kv[1]["posicoes"]) / len(kv[1]["posicoes"])))
        return itens[:limite]

    # nível 2
    for termo, v in top(1, LIMITE_NIVEL2):
        for tema in list(v["temas"]):
            registrar(termo, tema, 2)

    # nível 3
    for termo, v in top(2, LIMITE_NIVEL3):
        for tema in list(v["temas"]):
            registrar(termo, tema, 3)

    if consultas == 0 or falhas > 0.2 * consultas:
        print(f"Coleta abortada: {falhas} falhas em {consultas} consultas.", file=sys.stderr)
        sys.exit(1)

    saida_dados = []
    for termo, v in reg.items():
        saida_dados.append({
            "termo": termo,
            "consultas": len(v["consultas"]),
            "temas": sorted(v["temas"]),
            "profundidade": v["prof"],
            "posicao_media": round(sum(v["posicoes"]) / len(v["posicoes"]), 2),
        })
    with open(saida, "w", encoding="utf-8") as f:
        json.dump({
            "coletado_em": time.strftime("%Y-%m-%d"),
            "total_consultas": consultas,
            "consultas_com_falha": falhas,
            "sementes": SEMENTES,
            "sugestoes": saida_dados,
        }, f, ensure_ascii=False, indent=1)
    print(f"Pronto: {len(saida_dados)} sugestões únicas, {consultas} consultas.", file=sys.stderr)


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "saida.json")
