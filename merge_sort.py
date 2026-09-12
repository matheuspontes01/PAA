"""Merge Sort - estrategia: divisao e conquista.

Complexidade de tempo:
    melhor caso   O(n log n)
    caso medio    O(n log n)
    pior caso     O(n log n)  -> nao depende da ordem da entrada
Complexidade de espaco: O(n) (vetores auxiliares na intercalacao)
Estavel: sim
Observacao: nao faz trocas; toda escrita de elemento e contada em
"movimentacoes", incluindo as copias para os vetores auxiliares.
"""


def merge_sort(lista):
    comparacoes = 0
    trocas = 0
    movimentacoes = 0

    def merge(inicio, meio, fim):

        nonlocal comparacoes
        nonlocal movimentacoes

        esquerda = lista[inicio:meio + 1]
        direita = lista[meio + 1:fim + 1]

        # Copiar para os vetores auxiliares tambem e movimentacao
        movimentacoes += len(esquerda) + len(direita)

        i = 0
        j = 0
        k = inicio

        # Junta as duas partes ordenadas
        while i < len(esquerda) and j < len(direita):

            comparacoes += 1

            if esquerda[i] <= direita[j]:

                lista[k] = esquerda[i]
                i += 1

            else:

                lista[k] = direita[j]
                j += 1

            movimentacoes += 1

            k += 1

        # Copia o que sobrou da esquerda
        while i < len(esquerda):

            lista[k] = esquerda[i]

            movimentacoes += 1

            i += 1
            k += 1

        # Copia o que sobrou da direita
        while j < len(direita):

            lista[k] = direita[j]

            movimentacoes += 1

            j += 1
            k += 1

    def ordenar(inicio, fim):

        if inicio < fim:

            meio = (inicio + fim) // 2

            # Divide
            ordenar(inicio, meio)
            ordenar(meio + 1, fim)

            # Conquista
            merge(inicio, meio, fim)

    ordenar(0, len(lista) - 1)

    return {
        "comparacoes": comparacoes,
        "trocas": trocas,
        "movimentacoes": movimentacoes
    }


# Teste
if __name__ == "__main__":

    lista = [5, 3, 8, 1, 2]

    resultado = merge_sort(lista)

    print("Lista ordenada:", lista)
    print("Metricas:", resultado)
