"""Saidas do trabalho: tabelas e graficos, a partir do CSV de resultados.

Dividido em duas secoes:

    TABELAS   gera analise.md - tabelas por metrica, crescimento observado
              x previsto, sensibilidade ao tipo de entrada e a leitura dos
              numeros que responde as perguntas do enunciado
    GRAFICOS  gera a pasta graficos/ - tempo, comparacoes e movimentacoes
              x n, a sensibilidade de cada algoritmo e o comparativo final

Uso direto:
    python relatorio.py
Ou pela linha de comando principal:
    python main.py tables
    python main.py charts
"""

import math
import os

import matplotlib
matplotlib.use("Agg")

import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

import experimento

ARQUIVO_ENTRADA = "resultados.csv"
ARQUIVO_ANALISE = "analise.md"
PASTA_GRAFICOS = "graficos"

METRICAS = [
    ("tempo_medio", "Tempo medio (s)", "{:.6f}"),
    ("comparacoes", "Comparacoes", "{:,.0f}"),
    ("movimentacoes", "Movimentacoes", "{:,.0f}"),
    ("trocas", "Trocas", "{:,.0f}"),
]


def indexar(resultados):
    """(algoritmo, tipo, n) -> Resultado"""
    return {(r.algoritmo, r.tipo_entrada, r.n): r for r in resultados}


def _ordenados(resultados, chave):
    """Valores distintos de um campo, na ordem em que aparecem."""

    vistos = []

    for r in resultados:

        valor = getattr(r, chave)

        if valor not in vistos:
            vistos.append(valor)

    return vistos


# ------------------------------------------------------------------ TABELAS

def tabela_markdown(cabecalho, linhas):

    partes = ["| " + " | ".join(cabecalho) + " |",
              "|" + "|".join(["---"] * len(cabecalho)) + "|"]

    for linha in linhas:
        partes.append("| " + " | ".join(linha) + " |")

    return "\n".join(partes)


def tabelas_por_metrica(resultados):
    """Uma tabela algoritmo x n para cada metrica e tipo de entrada."""

    indice = indexar(resultados)

    algoritmos = _ordenados(resultados, "algoritmo")
    tipos = _ordenados(resultados, "tipo_entrada")
    tamanhos = sorted(_ordenados(resultados, "n"))

    blocos = []

    for campo, titulo, formato in METRICAS:

        blocos.append(f"\n## {titulo}\n")

        for tipo in tipos:

            linhas = []

            for algoritmo in algoritmos:

                celulas = [algoritmo]

                for n in tamanhos:

                    resultado = indice.get((algoritmo, tipo, n))

                    celulas.append(
                        formato.format(getattr(resultado, campo))
                        if resultado else "-"
                    )

                linhas.append(celulas)

            blocos.append(f"\n### Entrada: {tipo}\n")
            blocos.append(
                tabela_markdown(
                    ["Algoritmo"] + [f"n = {n:,}" for n in tamanhos], linhas
                )
            )

    return "\n".join(blocos)


def _razao_teorica(classe, n_anterior, n_atual):
    """Quanto o custo deveria crescer, segundo a complexidade teorica."""

    if "n^2" in classe:
        return (n_atual / n_anterior) ** 2

    if "log" in classe:
        return (n_atual * math.log2(n_atual)) / (n_anterior * math.log2(n_anterior))

    return n_atual / n_anterior


def tabela_crescimento(resultados, tipo="aleatoria"):
    """Razao observada entre tamanhos consecutivos x razao teorica."""

    indice = indexar(resultados)

    algoritmos = _ordenados(resultados, "algoritmo")
    tamanhos = sorted(_ordenados(resultados, "n"))

    linhas = []

    for algoritmo in algoritmos:

        # No caso medio vale a complexidade media do algoritmo
        classe = experimento.info(algoritmo)["medio"]

        disponiveis = [n for n in tamanhos if (algoritmo, tipo, n) in indice]

        for anterior, atual in zip(disponiveis, disponiveis[1:]):

            tempo_anterior = indice[(algoritmo, tipo, anterior)].tempo_medio
            tempo_atual = indice[(algoritmo, tipo, atual)].tempo_medio

            if tempo_anterior <= 0:
                continue

            observada = tempo_atual / tempo_anterior
            teorica = _razao_teorica(classe, anterior, atual)

            linhas.append([
                algoritmo,
                f"{anterior:,} -> {atual:,}",
                classe,
                f"{observada:.2f}x",
                f"{teorica:.2f}x",
                f"{observada / teorica:.2f}",
            ])

    return tabela_markdown(
        ["Algoritmo", "Transicao de n", "Classe teorica",
         "Crescimento observado", "Crescimento previsto", "Obs./Prev."],
        linhas,
    )


def _maior_n_com_todos_os_tipos(indice, algoritmo, tipos):
    """Maior n em que o algoritmo foi medido em todos os cenarios."""

    tamanhos = sorted(
        n for (a, _, n) in indice
        if a == algoritmo
        and all((algoritmo, tipo, n) in indice for tipo in tipos)
    )

    return tamanhos[-1] if tamanhos else None


def tabela_sensibilidade(resultados):
    """Tempo por tipo de entrada, no maior n comum a todos os cenarios."""

    indice = indexar(resultados)

    algoritmos = _ordenados(resultados, "algoritmo")
    tipos = _ordenados(resultados, "tipo_entrada")

    linhas = []

    for algoritmo in algoritmos:

        n = _maior_n_com_todos_os_tipos(indice, algoritmo, tipos)

        if n is None:
            continue

        tempos = {
            tipo: indice[(algoritmo, tipo, n)].tempo_medio for tipo in tipos
        }

        melhor = min(tempos.values())
        pior = max(tempos.values())

        linhas.append(
            [algoritmo, f"{n:,}"]
            + [f"{tempos[tipo]:.6f}" for tipo in tipos]
            + [f"{pior / melhor:.1f}x" if melhor > 0 else "-"]
        )

    return tabela_markdown(
        ["Algoritmo", "n"] + [f"Tempo: {t}" for t in tipos]
        + ["Pior / melhor cenario"],
        linhas,
    )


def leitura_dos_numeros(resultados):
    """Respostas diretas as perguntas do enunciado, a partir dos numeros."""

    indice = indexar(resultados)

    algoritmos = _ordenados(resultados, "algoritmo")
    tipos = _ordenados(resultados, "tipo_entrada")

    linhas = ["\n## Leitura dos resultados\n"]

    # --- Melhor e pior desempenho em entrada aleatoria ---
    tamanhos_comuns = sorted(
        n for n in _ordenados(resultados, "n")
        if all((a, "aleatoria", n) in indice for a in algoritmos)
    )

    if tamanhos_comuns:

        n = tamanhos_comuns[-1]

        tempos = sorted(
            (indice[(a, "aleatoria", n)].tempo_medio, a) for a in algoritmos
        )

        melhor_tempo, melhor = tempos[0]
        pior_tempo, pior = tempos[-1]

        linhas.append(
            f"- **Entrada aleatoria (n = {n:,}, maior tamanho rodado por todos):** "
            f"melhor desempenho do **{melhor}** ({melhor_tempo:.6f} s); "
            f"pior desempenho do **{pior}** ({pior_tempo:.6f} s) - "
            f"{pior_tempo / melhor_tempo:.1f}x mais lento."
        )

    # --- Maior n de cada algoritmo, em entrada aleatoria ---
    for algoritmo in algoritmos:

        disponiveis = sorted(
            n for (a, t, n) in indice if a == algoritmo and t == "aleatoria"
        )

        if not disponiveis:
            continue

        n = disponiveis[-1]
        r = indice[(algoritmo, "aleatoria", n)]

        linhas.append(
            f"- **{algoritmo}** no maior n medido (n = {n:,}, aleatoria): "
            f"{r.tempo_medio:.6f} s, {r.comparacoes:,.0f} comparacoes, "
            f"{r.movimentacoes:,.0f} movimentacoes "
            f"(teorico: {experimento.info(algoritmo)['medio']} no caso medio)."
        )

    # --- Sensibilidade ao tipo de entrada ---
    linhas.append("")

    sensibilidades = []

    for algoritmo in algoritmos:

        n = _maior_n_com_todos_os_tipos(indice, algoritmo, tipos)

        if n is None:
            continue

        tempos = {
            tipo: indice[(algoritmo, tipo, n)].tempo_medio for tipo in tipos
        }

        melhor_tipo = min(tempos, key=tempos.get)
        pior_tipo = max(tempos, key=tempos.get)

        if tempos[melhor_tipo] > 0:
            sensibilidades.append(
                (tempos[pior_tipo] / tempos[melhor_tipo],
                 algoritmo, n, melhor_tipo, pior_tipo)
            )

    for razao, algoritmo, n, melhor_tipo, pior_tipo in sorted(
        sensibilidades, reverse=True
    ):
        linhas.append(
            f"- **{algoritmo}** (n = {n:,}): mais rapido com entrada "
            f"*{melhor_tipo}* e mais lento com entrada *{pior_tipo}* - "
            f"variacao de {razao:.1f}x entre os cenarios."
        )

    # --- Quando um O(n^2) e competitivo ---
    linhas.append("")

    quadraticos = [a for a in algoritmos if experimento.info(a)["quadratico"]]
    n_logn = [a for a in algoritmos if not experimento.info(a)["quadratico"]]

    for tipo in tipos:

        for n in sorted(_ordenados(resultados, "n")):

            presentes_q = [a for a in quadraticos if (a, tipo, n) in indice]
            presentes_nl = [a for a in n_logn if (a, tipo, n) in indice]

            if not presentes_q or not presentes_nl:
                continue

            melhor_q = min(
                presentes_q, key=lambda a: indice[(a, tipo, n)].tempo_medio
            )
            melhor_nl = min(
                presentes_nl, key=lambda a: indice[(a, tipo, n)].tempo_medio
            )

            tempo_q = indice[(melhor_q, tipo, n)].tempo_medio
            tempo_nl = indice[(melhor_nl, tipo, n)].tempo_medio

            if tempo_q <= tempo_nl:
                linhas.append(
                    f"- **O(n^2) competitivo:** com entrada *{tipo}* e n = {n:,}, "
                    f"o {melhor_q} ({tempo_q:.6f} s) foi igual ou mais rapido "
                    f"que o {melhor_nl} ({tempo_nl:.6f} s)."
                )

    return "\n".join(linhas)


def gerar_tabelas(caminho_entrada=ARQUIVO_ENTRADA,
                  caminho_saida=ARQUIVO_ANALISE, imprimir=True):

    resultados = experimento.carregar_csv(caminho_entrada)

    partes = [
        "# Analise dos resultados",
        "",
        f"Fonte: `{caminho_entrada}` - {len(resultados)} medicoes, "
        f"media de {resultados[0].repeticoes} execucoes por ponto.",
        "",
        "## Algoritmos avaliados",
        "",
        tabela_markdown(
            ["Algoritmo", "Estrategia", "Melhor", "Medio", "Pior",
             "Espaco", "Estavel"],
            [
                [nome, d["estrategia"], d["melhor"], d["medio"], d["pior"],
                 d["espaco"], "sim" if d["estavel"] else "nao"]
                for nome, d in (
                    (n, experimento.info(n))
                    for n in _ordenados(resultados, "algoritmo")
                )
            ],
        ),
        tabelas_por_metrica(resultados),
        "\n## Crescimento observado x previsto (entrada aleatoria)\n",
        "Razao entre medicoes consecutivas. A coluna Obs./Prev. proxima de "
        "1,0 indica que o experimento seguiu a curva teorica.\n",
        tabela_crescimento(resultados),
        "\n## Sensibilidade ao tipo de entrada\n",
        tabela_sensibilidade(resultados),
        leitura_dos_numeros(resultados),
        "",
    ]

    texto = "\n".join(partes)

    with open(caminho_saida, "w", encoding="utf-8") as arquivo:
        arquivo.write(texto)

    if imprimir:
        print(texto)

    return caminho_saida


# ----------------------------------------------------------------- GRAFICOS

SUPERFICIE = "#fcfcfb"
TEXTO_PRIMARIO = "#0b0b0b"
TEXTO_SECUNDARIO = "#52514e"
GRADE = "#dedcd5"

# Cor por entidade, em ordem fixa - nunca por posicao no ranking
CORES_ALGORITMOS = {
    "Bubble Sort": "#2a78d6",
    "Insertion Sort": "#eb6834",
    "Merge Sort": "#1baf7a",
    "Quick Sort": "#eda100",
    "Quick Sort (pivo ultimo)": "#e87ba4",
}

CORES_TIPOS = {
    "aleatoria": "#2a78d6",
    "ordenada": "#eb6834",
    "inversa": "#1baf7a",
    "parcialmente_ordenada": "#eda100",
}

ROTULOS_METRICAS = {
    "tempo_medio": "Tempo medio de execucao (s)",
    "comparacoes": "Numero de comparacoes",
    "movimentacoes": "Numero de movimentacoes",
}


def _formatar_eixo(valor, _):
    if valor >= 1000:
        return f"{valor:,.0f}".replace(",", ".")
    if valor >= 1:
        return f"{valor:,.0f}"
    return f"{valor:g}"


def _preparar_eixos(titulo, rotulo_y):
    """Eixos em escala log-log.

    Nela uma funcao n^k vira uma reta de inclinacao k, o que torna visivel
    a diferenca entre O(n^2) (inclinacao ~2) e O(n log n) (pouco acima de 1).
    """

    figura, eixo = plt.subplots(figsize=(9, 5.5))

    figura.patch.set_facecolor(SUPERFICIE)
    eixo.set_facecolor(SUPERFICIE)

    eixo.set_title(titulo, color=TEXTO_PRIMARIO, fontsize=13, pad=14, loc="left")
    eixo.set_xlabel("Tamanho da entrada (n)", color=TEXTO_SECUNDARIO, fontsize=10)
    eixo.set_ylabel(rotulo_y, color=TEXTO_SECUNDARIO, fontsize=10)

    eixo.set_xscale("log")
    eixo.set_yscale("log")

    eixo.grid(True, which="major", color=GRADE, linewidth=0.8)
    eixo.grid(True, which="minor", color=GRADE, linewidth=0.4, alpha=0.6)

    eixo.tick_params(colors=TEXTO_SECUNDARIO, labelsize=9)

    for lado in ("top", "right"):
        eixo.spines[lado].set_visible(False)

    for lado in ("left", "bottom"):
        eixo.spines[lado].set_color(GRADE)

    eixo.xaxis.set_major_formatter(FuncFormatter(_formatar_eixo))

    return figura, eixo


def _desenhar_serie(eixo, xs, ys, rotulo, cor):

    eixo.plot(
        xs, ys,
        label=rotulo,
        color=cor,
        linewidth=2,
        marker="o",
        markersize=6,
        markeredgecolor=SUPERFICIE,
        markeredgewidth=1.5,
    )

    # Rotulo direto na ponta da linha: identidade nao depende so da cor
    if xs:
        eixo.annotate(
            rotulo,
            xy=(xs[-1], ys[-1]),
            xytext=(6, 0),
            textcoords="offset points",
            color=TEXTO_SECUNDARIO,
            fontsize=8.5,
            va="center",
        )


def _salvar(figura, eixo, caminho, tamanhos=None):

    # Marca no eixo x exatamente os tamanhos medidos e deixa folga a
    # direita para os rotulos que ficam na ponta das linhas
    if tamanhos:

        tamanhos = sorted(set(tamanhos))

        eixo.set_xticks(tamanhos)
        eixo.set_xticks([], minor=True)
        eixo.xaxis.set_major_formatter(FuncFormatter(_formatar_eixo))
        eixo.set_xlim(min(tamanhos) * 0.85, max(tamanhos) * 2.6)

    eixo.legend(
        frameon=False,
        fontsize=9,
        labelcolor=TEXTO_SECUNDARIO,
        loc="upper left",
    )

    figura.tight_layout()
    figura.savefig(caminho, dpi=150, facecolor=SUPERFICIE)
    plt.close(figura)

    return caminho


def _series(resultados, filtro, chave_serie, campo):
    """{serie: (lista de n, lista de valores)} com valores positivos."""

    agrupado = {}

    for r in resultados:

        if not filtro(r):
            continue

        valor = getattr(r, campo)

        if valor <= 0:
            continue

        agrupado.setdefault(getattr(r, chave_serie), []).append((r.n, valor))

    return {
        serie: ([p[0] for p in sorted(pontos)], [p[1] for p in sorted(pontos)])
        for serie, pontos in agrupado.items()
    }


def graficos_por_metrica(resultados, pasta):
    """Um grafico por (metrica, tipo de entrada), comparando algoritmos."""

    caminhos = []

    tipos = sorted({r.tipo_entrada for r in resultados})

    for campo, rotulo in ROTULOS_METRICAS.items():

        for tipo in tipos:

            series = _series(
                resultados, lambda r, t=tipo: r.tipo_entrada == t,
                "algoritmo", campo
            )

            if not series:
                continue

            figura, eixo = _preparar_eixos(
                f"{rotulo.split('(')[0].strip()} x n - entrada {tipo}", rotulo
            )

            # Ordem fixa das cores, independente do desempenho
            for algoritmo, cor in CORES_ALGORITMOS.items():

                if algoritmo not in series:
                    continue

                xs, ys = series[algoritmo]
                _desenhar_serie(eixo, xs, ys, algoritmo, cor)

            nome = campo.replace("tempo_medio", "tempo")

            tamanhos = sorted({n for xs, _ in series.values() for n in xs})

            caminhos.append(
                _salvar(
                    figura, eixo,
                    os.path.join(pasta, f"{nome}_{tipo}.png"),
                    tamanhos,
                )
            )

    return caminhos


def graficos_de_sensibilidade(resultados, pasta):
    """Um grafico por algoritmo, comparando os tipos de entrada."""

    caminhos = []

    algoritmos = [
        a for a in CORES_ALGORITMOS
        if any(r.algoritmo == a for r in resultados)
    ]

    for algoritmo in algoritmos:

        series = _series(
            resultados, lambda r, a=algoritmo: r.algoritmo == a,
            "tipo_entrada", "tempo_medio"
        )

        if not series:
            continue

        figura, eixo = _preparar_eixos(
            f"{algoritmo}: influencia do tipo de entrada",
            ROTULOS_METRICAS["tempo_medio"],
        )

        for tipo, cor in CORES_TIPOS.items():

            if tipo not in series:
                continue

            xs, ys = series[tipo]
            _desenhar_serie(eixo, xs, ys, tipo, cor)

        arquivo = (
            algoritmo.lower().replace(" ", "_").replace("(", "").replace(")", "")
        )

        tamanhos = sorted({n for xs, _ in series.values() for n in xs})

        caminhos.append(
            _salvar(
                figura, eixo,
                os.path.join(pasta, f"sensibilidade_{arquivo}.png"),
                tamanhos,
            )
        )

    return caminhos


def grafico_comparativo(resultados, pasta):
    """Tempo medio no maior n rodado por todos os algoritmos.

    Usa pontos sobre eixo logaritmico, e nao barras: a diferenca entre os
    algoritmos passa de duas ordens de grandeza, e barra em escala log
    engana (o comprimento deixa de ser proporcional ao valor).
    """

    algoritmos = sorted({r.algoritmo for r in resultados})

    indice = indexar(resultados)

    tamanhos = sorted(
        n for n in {r.n for r in resultados}
        if all((a, "aleatoria", n) in indice for a in algoritmos)
    )

    if not tamanhos:
        return []

    n = tamanhos[-1]

    dados = sorted(
        ((indice[(a, "aleatoria", n)].tempo_medio, a) for a in algoritmos),
        reverse=True,
    )

    figura, eixo = plt.subplots(figsize=(9, 0.75 * len(dados) + 2.4))

    figura.patch.set_facecolor(SUPERFICIE)
    eixo.set_facecolor(SUPERFICIE)

    posicoes = list(range(len(dados)))

    eixo.set_xscale("log")

    for posicao, (tempo, algoritmo) in zip(posicoes, dados):

        eixo.plot(
            [tempo], [posicao],
            marker="o",
            markersize=11,
            color=CORES_ALGORITMOS.get(algoritmo, "#2a78d6"),
            markeredgecolor=SUPERFICIE,
            markeredgewidth=2,
        )

        eixo.annotate(
            f"{tempo:.6f} s",
            xy=(tempo, posicao),
            xytext=(12, 0),
            textcoords="offset points",
            color=TEXTO_SECUNDARIO,
            fontsize=9.5,
            va="center",
        )

    eixo.set_yticks(posicoes)
    eixo.set_yticklabels([a for _, a in dados], color=TEXTO_PRIMARIO, fontsize=10)
    eixo.set_ylim(-0.6, len(dados) - 0.4)

    eixo.set_title(
        f"Tempo medio com entrada aleatoria (n = {n:,})",
        color=TEXTO_PRIMARIO, fontsize=13, pad=14, loc="left",
    )
    eixo.set_xlabel(
        ROTULOS_METRICAS["tempo_medio"] + " - escala logaritmica",
        color=TEXTO_SECUNDARIO, fontsize=10,
    )

    menor = min(t for t, _ in dados)
    maior = max(t for t, _ in dados)

    eixo.set_xlim(menor / 2.5, maior * 6)

    eixo.grid(True, axis="x", which="major", color=GRADE, linewidth=0.8)
    eixo.grid(True, axis="x", which="minor", color=GRADE, linewidth=0.4, alpha=0.6)
    eixo.set_axisbelow(True)

    eixo.tick_params(colors=TEXTO_SECUNDARIO, labelsize=9)

    for lado in ("top", "right", "left"):
        eixo.spines[lado].set_visible(False)

    eixo.spines["bottom"].set_color(GRADE)

    figura.tight_layout()

    caminho = os.path.join(pasta, "comparativo_pontos.png")
    figura.savefig(caminho, dpi=150, facecolor=SUPERFICIE)
    plt.close(figura)

    return [caminho]


def gerar_graficos(caminho_entrada=ARQUIVO_ENTRADA, pasta=PASTA_GRAFICOS,
                   verboso=True):

    os.makedirs(pasta, exist_ok=True)

    resultados = experimento.carregar_csv(caminho_entrada)

    caminhos = (
        graficos_por_metrica(resultados, pasta)
        + graficos_de_sensibilidade(resultados, pasta)
        + grafico_comparativo(resultados, pasta)
    )

    if verboso:
        for caminho in caminhos:
            print(f"grafico gerado: {caminho}")

    return caminhos


if __name__ == "__main__":

    gerar_tabelas(imprimir=False)
    print(f"tabelas geradas: {ARQUIVO_ANALISE}")

    gerar_graficos()
