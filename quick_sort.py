"""Quick Sort - estrategia: divisao e conquista (particionamento in-place).

Complexidade de tempo:
    melhor caso   O(n log n)  -> pivo divide o vetor ao meio
    caso medio    O(n log n)
    pior caso     O(n^2)      -> pivo sempre extremo (ex.: pivo = ultimo
                                 elemento com entrada ja ordenada)
Complexidade de espaco: O(log n) de pilha de recursao
Estavel: nao

Estrategias de pivo disponiveis:
    "mediana"   mediana de tres (inicio, meio, fim) - padrao, robusto
    "ultimo"    ultimo elemento - expoe o pior caso em entradas ordenadas
    "aleatorio" sorteia o pivo - evita o pior caso de forma probabilistica

A recursao e feita sempre na MENOR particao e a maior e tratada no laco
(eliminacao de recursao de cauda). Isso limita a profundidade da pilha a
O(log n) mesmo no pior caso, evitando estouro de recursao em entradas
grandes ja ordenadas.
"""

import random


def quick_sort(lista, pivo="mediana"):
    comparacoes = 0
    trocas = 0
    movimentacoes = 0

    def trocar(i, j):

        nonlocal trocas
        nonlocal movimentacoes

        if i != j:

            lista[i], lista[j] = lista[j], lista[i]

            trocas += 1
            movimentacoes += 2

    def escolher_pivo(inicio, fim):

        nonlocal comparacoes

        if pivo == "ultimo":
            return fim

        if pivo == "aleatorio":
            return random.randint(inicio, fim)

        # Mediana de tres: primeiro, meio e ultimo
        meio = (inicio + fim) // 2

        a = lista[inicio]
        b = lista[meio]
        c = lista[fim]

        comparacoes += 3

        if (a <= b <= c) or (c <= b <= a):
            return meio

        if (b <= a <= c) or (c <= a <= b):
            return inicio

        return fim

    def particionar(inicio, fim):

        nonlocal comparacoes

        # Coloca o pivo escolhido no fim e particiona (esquema de Lomuto)
        trocar(escolher_pivo(inicio, fim), fim)

        valor_pivo = lista[fim]

        i = inicio - 1

        for j in range(inicio, fim):

            comparacoes += 1

            if lista[j] <= valor_pivo:

                i += 1
                trocar(i, j)

        trocar(i + 1, fim)

        return i + 1

    def ordenar(inicio, fim):

        while inicio < fim:

            q = particionar(inicio, fim)

            # Recursao na menor particao, laco na maior
            if (q - inicio) < (fim - q):

                ordenar(inicio, q - 1)
                inicio = q + 1

            else:

                ordenar(q + 1, fim)
                fim = q - 1

    ordenar(0, len(lista) - 1)

    return {
        "comparacoes": comparacoes,
        "trocas": trocas,
        "movimentacoes": movimentacoes
    }


def quick_sort_ultimo(lista):
    """Variante didatica: pivo fixo no ultimo elemento (pior caso O(n^2)
    em entradas ordenadas e inversamente ordenadas)."""
    return quick_sort(lista, pivo="ultimo")


def quick_sort_aleatorio(lista):
    """Variante com pivo aleatorio."""
    return quick_sort(lista, pivo="aleatorio")


# Teste
if __name__ == "__main__":

    lista = [5, 3, 8, 1, 2]

    resultado = quick_sort(lista)

    print("Lista ordenada:", lista)
    print("Metricas:", resultado)
