#!/usr/bin/env python3
"""
Registra uma coleta na série histórica e compara com a coleta anterior.

Uso:  python3 serie.py PASTA_DA_ANALISE RAIZ_DO_REPOSITORIO [AAAA-MM-DD]

PASTA_DA_ANALISE  pasta onde analisar.py gravou termos.csv e resumo.json
RAIZ_DO_REPOSITORIO  raiz do site (onde ficam _data/ e assets/)
AAAA-MM-DD        data da coleta (padrão: hoje, em UTC)

O que grava:
  assets/territorios/series/termos-AAAA-MM-DD.csv   foto completa desta coleta
  assets/territorios/termos.csv e resumo.json        sempre a coleta mais recente
  _data/territorios_serie.csv                        uma linha por coleta (alimenta a tabela da página)
  _data/territorios_mudancas.json                    termos novos e termos que saíram desde a coleta anterior
"""
import csv
import json
import re
import shutil
import sys
import unicodedata
from datetime import datetime, timezone
from pathlib import Path

MINIMO_DE_TERMOS = 600  # abaixo disso a coleta é considerada ruim e nada é gravado

COLUNAS = ["data", "termos", "materiais_prontos_pct", "formacao_pct", "como_fazer_pct",
           "ferramentas_ia_pct", "termos_novos", "termos_que_sairam"]


def chave(t):
    t = "".join(c for c in unicodedata.normalize("NFD", t.lower()) if unicodedata.category(c) != "Mn")
    return re.sub(r"\s+", " ", t).strip()


def ler(caminho):
    with open(caminho, encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f))


def pct(linhas, intencao):
    n = sum(1 for r in linhas if r["intencao"] == intencao)
    return round(100 * n / len(linhas), 1)


def main(pasta_analise, raiz, data=None):
    raiz = Path(raiz)
    analise = Path(pasta_analise)
    data = data or datetime.now(timezone.utc).strftime("%Y-%m-%d")

    linhas = ler(analise / "termos.csv")
    if len(linhas) < MINIMO_DE_TERMOS:
        print(f"Coleta rejeitada: só {len(linhas)} termos (mínimo {MINIMO_DE_TERMOS}).", file=sys.stderr)
        sys.exit(1)

    series = raiz / "assets" / "territorios" / "series"
    series.mkdir(parents=True, exist_ok=True)

    # coleta anterior = a mais recente com data menor que esta
    anteriores = sorted(p for p in series.glob("termos-*.csv") if p.stem.split("termos-")[1] < data)
    novos = sairam = None
    anterior_data = ""
    if anteriores:
        anterior = anteriores[-1]
        anterior_data = anterior.stem.split("termos-")[1]
        antes = {chave(r["termo"]): r for r in ler(anterior)}
        agora = {chave(r["termo"]): r for r in linhas}
        novos_chaves = [k for k in agora if k not in antes]
        sairam_chaves = [k for k in antes if k not in agora]
        novos = sorted((agora[k] for k in novos_chaves), key=lambda r: -float(r["pontuacao"]))
        sairam = sorted((antes[k] for k in sairam_chaves), key=lambda r: -float(r["pontuacao"]))

    # grava a foto desta coleta e atualiza "a mais recente"
    shutil.copyfile(analise / "termos.csv", series / f"termos-{data}.csv")
    destino = raiz / "assets" / "territorios"
    shutil.copyfile(analise / "termos.csv", destino / "termos.csv")
    shutil.copyfile(analise / "resumo.json", destino / "resumo.json")

    # série: uma linha por data (reexecutar no mesmo dia substitui a linha)
    arq_serie = raiz / "_data" / "territorios_serie.csv"
    arq_serie.parent.mkdir(parents=True, exist_ok=True)
    existentes = {}
    if arq_serie.exists():
        for r in ler(arq_serie):
            existentes[r["data"]] = r
    existentes[data] = {
        "data": data,
        "termos": len(linhas),
        "materiais_prontos_pct": pct(linhas, "Materiais prontos"),
        "formacao_pct": pct(linhas, "Formação e cursos"),
        "como_fazer_pct": pct(linhas, "Como fazer"),
        "ferramentas_ia_pct": pct(linhas, "Ferramentas e IA"),
        "termos_novos": "" if novos is None else len(novos),
        "termos_que_sairam": "" if sairam is None else len(sairam),
    }
    with open(arq_serie, "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=COLUNAS)
        w.writeheader()
        for d in sorted(existentes):
            w.writerow(existentes[d])

    # mudanças da coleta mais recente em relação à anterior
    mud = {
        "data": data,
        "anterior": anterior_data,
        "novos": [r["termo"] for r in (novos or [])[:12]],
        "sairam": [r["termo"] for r in (sairam or [])[:12]],
    }
    with open(raiz / "_data" / "territorios_mudancas.json", "w", encoding="utf-8") as f:
        json.dump(mud, f, ensure_ascii=False, indent=1)

    print(f"Coleta de {data} registrada: {len(linhas)} termos"
          + ("" if novos is None else f", {len(novos)} novos e {len(sairam)} que saíram desde {anterior_data}")
          + ".")


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print(__doc__)
        sys.exit(2)
    main(sys.argv[1], sys.argv[2], sys.argv[3] if len(sys.argv) > 3 else None)
