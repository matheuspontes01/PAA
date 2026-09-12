"""Insertion Sort - estrategia: incremental (constroi o prefixo ordenado).

Complexidade de tempo:
    melhor caso   O(n)    -> entrada ja ordenada (1 comparacao por elemento)
    caso medio    O(n^2)
    pior caso     O(n^2)  -> entrada inversamente ordenada
Complexidade de espaco: O(1) (ordenacao in-place)
Estavel: sim
Observacao: nao realiza trocas, e sim deslocamentos; por isso "trocas" e
sempre 0 e o custo de escrita aparece em "movimentacoes".
"""


def insertion_sort(lista):
    comparacoes = 0
    trocas = 0
    movimentacoes = 0

    for i in range(1, len(lista)):

        chave = lista[i]

        j = i - 1

        while j >= 0:

            comparacoes += 1

            if lista[j] > chave:

                lista[j + 1] = lista[j]

                movimentacoes += 1

                j -= 1

            else:
                break

        lista[j + 1] = chave

        movimentacoes += 1

    return {
        "comparacoes": comparacoes,
        "trocas": trocas,
        "movimentacoes": movimentacoes
    }


# Teste
if __name__ == "__main__":

    lista = [5, 3, 8, 1, 2]

    resultado = insertion_sort(lista)

    print("Lista ordenada:", lista)
    print("Metricas:", resultado)
