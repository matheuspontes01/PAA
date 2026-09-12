"""Motor do experimento: catalogo, entradas, medicao e execucao.

Dividido em quatro secoes:

    CATALOGO   quais algoritmos entram no experimento e a teoria de cada um
    ENTRADAS   geracao dos quatro cenarios de entrada
    MEDICAO    coleta das metricas de uma execucao e a media das repeticoes
    EXECUCAO   percorre a grade (algoritmo x entrada x tamanho) -> CSV

Os algoritmos em si ficam cada um em seu arquivo (bubble_sort.py,
insertion_sort.py, merge_sort.py, quick_sort.py). Cada funcao de ordenacao
recebe uma lista, ordena IN-PLACE e devolve um dicionario com as chaves
comparacoes, trocas e movimentacoes.

Uso direto:
    python experimento.py
Ou pela linha de comando principal:
    python main.py run --sizes 100,1000,10000 --repeats 5
"""

import csv
import gc
import random
import statistics
import sys
import time
from dataclasses import dataclass, asdict, fields

from bubble_sort import bubble_sort
from insertion_sort import insertion_sort
from merge_sort import merge_sort
from quick_sort import quick_sort, quick_sort_ultimo


# ----------------------------------------------------------------- CATALOGO

ALGORITMOS = {
    "Bubble Sort": {
        "funcao": bubble_sort,
        "estrategia": "Forca bruta (comparacao par a par)",
        "melhor": "O(n)",
        "medio": "O(n^2)",
        "pior": "O(n^2)",
        "espaco": "O(1)",
        "estavel": True,
        "quadratico": True,
        "padrao": True,
    },
    "Insertion Sort": {
        "funcao": insertion_sort,
        "estrategia": "Incremental",
        "melhor": "O(n)",
        "medio": "O(n^2)",
        "pior": "O(n^2)",
        "espaco": "O(1)",
        "estavel": True,
        "quadratico": True,
        "padrao": True,
    },
    "Merge Sort": {
        "funcao": merge_sort,
        "estrategia": "Divisao e conquista",
        "melhor": "O(n log n)",
        "medio": "O(n log n)",
        "pior": "O(n log n)",
        "espaco": "O(n)",
        "estavel": True,
        "quadratico": False,
        "padrao": True,
    },
    "Quick Sort": {
        "funcao": quick_sort,
        "estrategia": "Divisao e conquista (pivo = mediana de tres)",
        "melhor": "O(n log n)",
        "medio": "O(n log n)",
        "pior": "O(n^2)",
        "espaco": "O(log n)",
        "estavel": False,
        "quadratico": False,
        "padrao": True,
    },
    # Variante didatica: so entra com --with-variants.
    # Serve para evidenciar o pior caso O(n^2) do Quick Sort.
    "Quick Sort (pivo ultimo)": {
        "funcao": quick_sort_ultimo,
        "estrategia": "Divisao e conquista (pivo = ultimo elemento)",
        "melhor": "O(n log n)",
        "medio": "O(n log n)",
        "pior": "O(n^2)",
        "espaco": "O(log n)",
        "estavel": False,
        "quadratico": True,
        "padrao": False,
    },
}


def nomes(incluir_variantes=False):
    """Nomes dos algoritmos a serem executados."""
    return [
        nome for nome, dados in ALGORITMOS.items()
        if dados["padrao"] or incluir_variantes
    ]


def info(nome):
    """Dados teoricos de um algoritmo do catalogo."""
    return ALGORITMOS[nome]


# ----------------------------------------------------------------- ENTRADAS

# Fracao de elementos fora de ordem no cenario parcialmente ordenado
DESORDEM_PARCIAL = 0.10

SEMENTE_PADRAO = 42


def aleatoria(n, semente=SEMENTE_PADRAO):
    """Ordem totalmente aleatoria - representa o caso medio."""
    gerador = random.Random(semente)
    return [gerador.randint(0, 10 * n) for _ in range(n)]


def ordenada(n, semente=SEMENTE_PADRAO):
    """Ja em ordem crescente - melhor caso de varios algoritmos."""
    return list(range(n))


def inversa(n, semente=SEMENTE_PADRAO):
    """Ordem decrescente - pior caso de varios algoritmos."""
    return list(range(n, 0, -1))


def parcialmente_ordenada(n, semente=SEMENTE_PADRAO, desordem=DESORDEM_PARCIAL):
    """Lista ordenada com `desordem` * n posicoes trocadas aleatoriamente."""

    gerador = random.Random(semente)

    lista = list(range(n))

    quantidade_trocas = int(n * desordem)

    for _ in range(quantidade_trocas):

        i = gerador.randrange(n)
        j = gerador.randrange(n)

        lista[i], lista[j] = lista[j], lista[i]

    return lista


GERADORES = {
    "aleatoria": aleatoria,
    "ordenada": ordenada,
    "inversa": inversa,
    "parcialmente_ordenada": parcialmente_ordenada,
}


def gerar_entrada(tipo, n, semente=SEMENTE_PADRAO):
    """Gera uma entrada do tipo pedido.

    As entradas sao reprodutiveis: a mesma semente gera sempre a mesma
    lista, entao todos os algoritmos recebem exatamente os mesmos dados.
    """

    if tipo not in GERADORES:
        raise ValueError(
            f"Tipo de entrada desconhecido: {tipo}. "
            f"Use um de: {', '.join(GERADORES)}"
        )

    return GERADORES[tipo](n, semente)


def tipos_de_entrada():
    return list(GERADORES)


# ------------------------------------------------------------------ MEDICAO

# Metricas registradas, com a mesma definicao para todos os algoritmos:
#
#     tempo         tempo de parede da ordenacao, em segundos
#                   (time.perf_counter, coletor de lixo desligado)
#     comparacoes   comparacoes entre elementos da entrada
#     trocas        permutas de dois elementos do vetor
#     movimentacoes escritas de elementos em posicoes de vetor
#                   (uma troca conta como 2 movimentacoes)


@dataclass
class Resultado:
    algoritmo: str
    tipo_entrada: str
    n: int
    repeticoes: int
    tempo_medio: float
    tempo_minimo: float
    tempo_maximo: float
    desvio_tempo: float
    comparacoes: float
    trocas: float
    movimentacoes: float


CAMPOS = [campo.name for campo in fields(Resultado)]


def esta_ordenada(lista):
    return all(lista[i] <= lista[i + 1] for i in range(len(lista) - 1))


def executar_uma_vez(funcao, lista):
    """Ordena uma copia da lista e devolve (metricas, tempo em segundos)."""

    copia = list(lista)

    coletor_ligado = gc.isenabled()
    gc.disable()

    try:
        inicio = time.perf_counter()
        contadores = funcao(copia)
        fim = time.perf_counter()

    finally:
        if coletor_ligado:
            gc.enable()

    if not esta_ordenada(copia):
        raise AssertionError(
            f"{funcao.__name__} nao ordenou corretamente uma lista "
            f"de {len(copia)} elementos"
        )

    return contadores, fim - inicio


def medir(algoritmo, funcao, tipo_entrada, n, repeticoes=3,
          semente=SEMENTE_PADRAO):
    """Executa o algoritmo `repeticoes` vezes e devolve a media das metricas.

    Cada repeticao usa uma semente diferente, de modo que a media reduz
    tanto o ruido da maquina quanto o efeito de uma entrada particular.
    """

    tempos = []
    comparacoes = []
    trocas = []
    movimentacoes = []

    for repeticao in range(repeticoes):

        lista = gerar_entrada(tipo_entrada, n, semente + repeticao)

        contadores, tempo = executar_uma_vez(funcao, lista)

        tempos.append(tempo)
        comparacoes.append(contadores["comparacoes"])
        trocas.append(contadores["trocas"])
        movimentacoes.append(contadores["movimentacoes"])

    return Resultado(
        algoritmo=algoritmo,
        tipo_entrada=tipo_entrada,
        n=n,
        repeticoes=repeticoes,
        tempo_medio=statistics.fmean(tempos),
        tempo_minimo=min(tempos),
        tempo_maximo=max(tempos),
        desvio_tempo=statistics.pstdev(tempos) if len(tempos) > 1 else 0.0,
        comparacoes=statistics.fmean(comparacoes),
        trocas=statistics.fmean(trocas),
        movimentacoes=statistics.fmean(movimentacoes),
    )


def salvar_csv(resultados, caminho):

    with open(caminho, "w", newline="", encoding="utf-8") as arquivo:

        escritor = csv.DictWriter(arquivo, fieldnames=CAMPOS)
        escritor.writeheader()

        for resultado in resultados:
            escritor.writerow(asdict(resultado))

    return caminho


def carregar_csv(caminho):

    with open(caminho, newline="", encoding="utf-8") as arquivo:

        return [
            Resultado(
                algoritmo=linha["algoritmo"],
                tipo_entrada=linha["tipo_entrada"],
                n=int(linha["n"]),
                repeticoes=int(linha["repeticoes"]),
                tempo_medio=float(linha["tempo_medio"]),
                tempo_minimo=float(linha["tempo_minimo"]),
                tempo_maximo=float(linha["tempo_maximo"]),
                desvio_tempo=float(linha["desvio_tempo"]),
                comparacoes=float(linha["comparacoes"]),
                trocas=float(linha["trocas"]),
                movimentacoes=float(linha["movimentacoes"]),
            )
            for linha in csv.DictReader(arquivo)
        ]


# ----------------------------------------------------------------- EXECUCAO

TAMANHOS_PADRAO = [100, 500, 1000, 5000, 10000, 50000, 100000]

REPETICOES_PADRAO = 3

# Teto de n para os algoritmos O(n^2)
LIMITE_QUADRATICO = 10000

ARQUIVO_SAIDA = "resultados.csv"


def _log(mensagem):
    print(mensagem, file=sys.stderr, flush=True)


def rodar(tamanhos=None, tipos=None, algoritmos=None,
          repeticoes=REPETICOES_PADRAO, limite_quadratico=LIMITE_QUADRATICO,
          saida=ARQUIVO_SAIDA, com_variantes=False, verboso=True):
    """Roda a grade completa de experimentos e grava o CSV de resultados.

    Os algoritmos quadraticos recebem um teto de tamanho: rodar Bubble e
    Insertion com n = 100.000 levaria horas, pois o custo cresce com n^2.
    O teto e um parametro, nao uma regra fixa.
    """

    tamanhos = tamanhos or TAMANHOS_PADRAO
    tipos = tipos or tipos_de_entrada()
    algoritmos = algoritmos or nomes(incluir_variantes=com_variantes)

    resultados = []

    inicio_geral = time.perf_counter()

    for nome in algoritmos:

        dados = info(nome)

        tamanhos_do_algoritmo = [
            n for n in tamanhos
            if not dados["quadratico"] or n <= limite_quadratico
        ]

        ignorados = [n for n in tamanhos if n not in tamanhos_do_algoritmo]

        if verboso and ignorados:
            _log(
                f"[{nome}] tamanhos ignorados (algoritmo quadratico, "
                f"teto = {limite_quadratico}): {ignorados}"
            )

        for tipo in tipos:

            for n in tamanhos_do_algoritmo:

                inicio = time.perf_counter()

                resultado = medir(nome, dados["funcao"], tipo, n, repeticoes)

                resultados.append(resultado)

                if verboso:
                    _log(
                        f"[{nome:<26}] {tipo:<22} n={n:<7} "
                        f"tempo={resultado.tempo_medio:.6f}s  "
                        f"comp={resultado.comparacoes:>12,.0f}  "
                        f"mov={resultado.movimentacoes:>12,.0f}  "
                        f"({time.perf_counter() - inicio:.1f}s)"
                    )

    salvar_csv(resultados, saida)

    if verboso:
        _log(
            f"\n{len(resultados)} medicoes gravadas em {saida} "
            f"({time.perf_counter() - inicio_geral:.1f}s no total)"
        )

    return resultados


if __name__ == "__main__":
    rodar()
