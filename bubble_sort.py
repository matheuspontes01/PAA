"""Bubble Sort - estrategia: forca bruta / comparacao par a par.

Complexidade de tempo:
    melhor caso   O(n)    -> entrada ja ordenada (para na 1a passagem)
    caso medio    O(n^2)
    pior caso     O(n^2)  -> entrada inversamente ordenada
Complexidade de espaco: O(1) (ordenacao in-place)
Estavel: sim
"""


def bubble_sort(lista):
    comparacoes = 0
    trocas = 0
    movimentacoes = 0

    n = len(lista)

    for i in range(n - 1):
        houve_troca = False

        for j in range(n - 1 - i):

            comparacoes += 1

            if lista[j] > lista[j + 1]:

                lista[j], lista[j + 1] = lista[j + 1], lista[j]

                trocas += 1
                movimentacoes += 2

                houve_troca = True

        # Se nenhuma troca aconteceu,
        # a lista ja esta ordenada
        if not houve_troca:
            break

    return {
        "comparacoes": comparacoes,
        "trocas": trocas,
        "movimentacoes": movimentacoes
    }


# Teste
if __name__ == "__main__":

    lista = [5, 3, 8, 1, 2]

    resultado = bubble_sort(lista)

    print("Lista ordenada:", lista)
    print("Metricas:", resultado)
