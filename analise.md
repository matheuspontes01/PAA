# Analise dos resultados

Fonte: `resultados.csv` - 96 medicoes, media de 3 execucoes por ponto.

## Algoritmos avaliados

| Algoritmo | Estrategia | Melhor | Medio | Pior | Espaco | Estavel |
|---|---|---|---|---|---|---|
| Bubble Sort | Forca bruta (comparacao par a par) | O(n) | O(n^2) | O(n^2) | O(1) | sim |
| Insertion Sort | Incremental | O(n) | O(n^2) | O(n^2) | O(1) | sim |
| Merge Sort | Divisao e conquista | O(n log n) | O(n log n) | O(n log n) | O(n) | sim |
| Quick Sort | Divisao e conquista (pivo = mediana de tres) | O(n log n) | O(n log n) | O(n^2) | O(log n) | nao |

## Tempo medio (s)


### Entrada: aleatoria

| Algoritmo | n = 100 | n = 500 | n = 1,000 | n = 5,000 | n = 10,000 | n = 50,000 | n = 100,000 |
|---|---|---|---|---|---|---|---|
| Bubble Sort | 0.000309 | 0.008524 | 0.037689 | 1.046601 | 4.216614 | - | - |
| Insertion Sort | 0.000151 | 0.004010 | 0.016111 | 0.474119 | 1.761111 | - | - |
| Merge Sort | 0.000108 | 0.000609 | 0.001379 | 0.008401 | 0.017855 | 0.104730 | 0.223572 |
| Quick Sort | 0.000076 | 0.000488 | 0.001134 | 0.006922 | 0.014552 | 0.086562 | 0.184794 |

### Entrada: ordenada

| Algoritmo | n = 100 | n = 500 | n = 1,000 | n = 5,000 | n = 10,000 | n = 50,000 | n = 100,000 |
|---|---|---|---|---|---|---|---|
| Bubble Sort | 0.000003 | 0.000018 | 0.000040 | 0.000223 | 0.000440 | - | - |
| Insertion Sort | 0.000006 | 0.000033 | 0.000074 | 0.000407 | 0.000841 | - | - |
| Merge Sort | 0.000079 | 0.000492 | 0.001083 | 0.007107 | 0.014738 | 0.085074 | 0.176935 |
| Quick Sort | 0.000047 | 0.000308 | 0.000695 | 0.004522 | 0.009488 | 0.054979 | 0.115182 |

### Entrada: inversa

| Algoritmo | n = 100 | n = 500 | n = 1,000 | n = 5,000 | n = 10,000 | n = 50,000 | n = 100,000 |
|---|---|---|---|---|---|---|---|
| Bubble Sort | 0.000398 | 0.010803 | 0.047568 | 1.410157 | 5.442679 | - | - |
| Insertion Sort | 0.000285 | 0.007567 | 0.032349 | 0.860424 | 3.481293 | - | - |
| Merge Sort | 0.000079 | 0.000509 | 0.001099 | 0.006726 | 0.014280 | 0.083597 | 0.172843 |
| Quick Sort | 0.000073 | 0.000624 | 0.001501 | 0.010073 | 0.022357 | 0.138782 | 0.301911 |

### Entrada: parcialmente_ordenada

| Algoritmo | n = 100 | n = 500 | n = 1,000 | n = 5,000 | n = 10,000 | n = 50,000 | n = 100,000 |
|---|---|---|---|---|---|---|---|
| Bubble Sort | 0.000199 | 0.005250 | 0.024714 | 0.664679 | 2.702157 | - | - |
| Insertion Sort | 0.000034 | 0.000941 | 0.003808 | 0.100983 | 0.402970 | - | - |
| Merge Sort | 0.000084 | 0.000577 | 0.001224 | 0.007687 | 0.016736 | 0.095066 | 0.202363 |
| Quick Sort | 0.000060 | 0.000430 | 0.001065 | 0.006276 | 0.013652 | 0.081317 | 0.172933 |

## Comparacoes


### Entrada: aleatoria

| Algoritmo | n = 100 | n = 500 | n = 1,000 | n = 5,000 | n = 10,000 | n = 50,000 | n = 100,000 |
|---|---|---|---|---|---|---|---|
| Bubble Sort | 4,775 | 124,479 | 498,590 | 12,492,979 | 49,989,839 | - | - |
| Insertion Sort | 2,386 | 61,795 | 246,478 | 6,252,755 | 24,856,051 | - | - |
| Merge Sort | 540 | 3,849 | 8,707 | 55,201 | 120,367 | 718,185 | 1,536,439 |
| Quick Sort | 728 | 4,864 | 11,275 | 70,306 | 148,915 | 893,295 | 1,912,179 |

### Entrada: ordenada

| Algoritmo | n = 100 | n = 500 | n = 1,000 | n = 5,000 | n = 10,000 | n = 50,000 | n = 100,000 |
|---|---|---|---|---|---|---|---|
| Bubble Sort | 99 | 499 | 999 | 4,999 | 9,999 | - | - |
| Insertion Sort | 99 | 499 | 999 | 4,999 | 9,999 | - | - |
| Merge Sort | 356 | 2,272 | 5,044 | 32,004 | 69,008 | 401,952 | 853,904 |
| Quick Sort | 669 | 4,263 | 9,520 | 60,678 | 131,343 | 782,782 | 1,665,551 |

### Entrada: inversa

| Algoritmo | n = 100 | n = 500 | n = 1,000 | n = 5,000 | n = 10,000 | n = 50,000 | n = 100,000 |
|---|---|---|---|---|---|---|---|
| Bubble Sort | 4,950 | 124,750 | 499,500 | 12,497,500 | 49,995,000 | - | - |
| Insertion Sort | 4,950 | 124,750 | 499,500 | 12,497,500 | 49,995,000 | - | - |
| Merge Sort | 316 | 2,216 | 4,932 | 29,804 | 64,608 | 382,512 | 815,024 |
| Quick Sort | 851 | 6,843 | 15,995 | 108,443 | 242,135 | 1,504,807 | 3,259,375 |

### Entrada: parcialmente_ordenada

| Algoritmo | n = 100 | n = 500 | n = 1,000 | n = 5,000 | n = 10,000 | n = 50,000 | n = 100,000 |
|---|---|---|---|---|---|---|---|
| Bubble Sort | 4,639 | 119,518 | 494,512 | 12,468,251 | 49,959,749 | - | - |
| Insertion Sort | 622 | 14,766 | 57,159 | 1,438,326 | 5,760,634 | - | - |
| Merge Sort | 494 | 3,542 | 8,092 | 52,787 | 115,475 | 692,603 | 1,485,631 |
| Quick Sort | 748 | 5,212 | 13,694 | 79,165 | 175,170 | 1,030,492 | 2,296,615 |

## Movimentacoes


### Entrada: aleatoria

| Algoritmo | n = 100 | n = 500 | n = 1,000 | n = 5,000 | n = 10,000 | n = 50,000 | n = 100,000 |
|---|---|---|---|---|---|---|---|
| Bubble Sort | 4,579 | 122,601 | 490,970 | 12,495,525 | 49,692,119 | - | - |
| Insertion Sort | 2,388 | 61,799 | 246,484 | 6,252,762 | 24,856,059 | - | - |
| Merge Sort | 1,344 | 8,976 | 19,952 | 123,616 | 267,232 | 1,568,928 | 3,337,856 |
| Quick Sort | 686 | 4,487 | 10,777 | 65,383 | 137,413 | 861,987 | 1,791,569 |

### Entrada: ordenada

| Algoritmo | n = 100 | n = 500 | n = 1,000 | n = 5,000 | n = 10,000 | n = 50,000 | n = 100,000 |
|---|---|---|---|---|---|---|---|
| Bubble Sort | 0 | 0 | 0 | 0 | 0 | - | - |
| Insertion Sort | 99 | 499 | 999 | 4,999 | 9,999 | - | - |
| Merge Sort | 1,344 | 8,976 | 19,952 | 123,616 | 267,232 | 1,568,928 | 3,337,856 |
| Quick Sort | 252 | 1,020 | 2,044 | 11,808 | 23,616 | 131,068 | 262,140 |

### Entrada: inversa

| Algoritmo | n = 100 | n = 500 | n = 1,000 | n = 5,000 | n = 10,000 | n = 50,000 | n = 100,000 |
|---|---|---|---|---|---|---|---|
| Bubble Sort | 9,900 | 249,500 | 999,000 | 24,995,000 | 99,990,000 | - | - |
| Insertion Sort | 5,049 | 125,249 | 500,499 | 12,502,499 | 50,004,999 | - | - |
| Merge Sort | 1,344 | 8,976 | 19,952 | 123,616 | 267,232 | 1,568,928 | 3,337,856 |
| Quick Sort | 936 | 7,672 | 18,168 | 125,784 | 281,088 | 1,763,200 | 3,826,464 |

### Entrada: parcialmente_ordenada

| Algoritmo | n = 100 | n = 500 | n = 1,000 | n = 5,000 | n = 10,000 | n = 50,000 | n = 100,000 |
|---|---|---|---|---|---|---|---|
| Bubble Sort | 1,047 | 28,534 | 112,320 | 2,866,656 | 11,501,271 | - | - |
| Insertion Sort | 622 | 14,766 | 57,159 | 1,438,327 | 5,760,634 | - | - |
| Merge Sort | 1,344 | 8,976 | 19,952 | 123,616 | 267,232 | 1,568,928 | 3,337,856 |
| Quick Sort | 416 | 3,290 | 7,913 | 50,080 | 113,315 | 716,251 | 1,469,607 |

## Trocas


### Entrada: aleatoria

| Algoritmo | n = 100 | n = 500 | n = 1,000 | n = 5,000 | n = 10,000 | n = 50,000 | n = 100,000 |
|---|---|---|---|---|---|---|---|
| Bubble Sort | 2,289 | 61,300 | 245,485 | 6,247,763 | 24,846,060 | - | - |
| Insertion Sort | 0 | 0 | 0 | 0 | 0 | - | - |
| Merge Sort | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| Quick Sort | 343 | 2,244 | 5,388 | 32,691 | 68,706 | 430,993 | 895,785 |

### Entrada: ordenada

| Algoritmo | n = 100 | n = 500 | n = 1,000 | n = 5,000 | n = 10,000 | n = 50,000 | n = 100,000 |
|---|---|---|---|---|---|---|---|
| Bubble Sort | 0 | 0 | 0 | 0 | 0 | - | - |
| Insertion Sort | 0 | 0 | 0 | 0 | 0 | - | - |
| Merge Sort | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| Quick Sort | 126 | 510 | 1,022 | 5,904 | 11,808 | 65,534 | 131,070 |

### Entrada: inversa

| Algoritmo | n = 100 | n = 500 | n = 1,000 | n = 5,000 | n = 10,000 | n = 50,000 | n = 100,000 |
|---|---|---|---|---|---|---|---|
| Bubble Sort | 4,950 | 124,750 | 499,500 | 12,497,500 | 49,995,000 | - | - |
| Insertion Sort | 0 | 0 | 0 | 0 | 0 | - | - |
| Merge Sort | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| Quick Sort | 468 | 3,836 | 9,084 | 62,892 | 140,544 | 881,600 | 1,913,232 |

### Entrada: parcialmente_ordenada

| Algoritmo | n = 100 | n = 500 | n = 1,000 | n = 5,000 | n = 10,000 | n = 50,000 | n = 100,000 |
|---|---|---|---|---|---|---|---|
| Bubble Sort | 523 | 14,267 | 56,160 | 1,433,328 | 5,750,635 | - | - |
| Insertion Sort | 0 | 0 | 0 | 0 | 0 | - | - |
| Merge Sort | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| Quick Sort | 208 | 1,645 | 3,957 | 25,040 | 56,657 | 358,125 | 734,804 |

## Crescimento observado x previsto (entrada aleatoria)

Razao entre medicoes consecutivas. A coluna Obs./Prev. proxima de 1,0 indica que o experimento seguiu a curva teorica.

| Algoritmo | Transicao de n | Classe teorica | Crescimento observado | Crescimento previsto | Obs./Prev. |
|---|---|---|---|---|---|
| Bubble Sort | 100 -> 500 | O(n^2) | 27.57x | 25.00x | 1.10 |
| Bubble Sort | 500 -> 1,000 | O(n^2) | 4.42x | 4.00x | 1.11 |
| Bubble Sort | 1,000 -> 5,000 | O(n^2) | 27.77x | 25.00x | 1.11 |
| Bubble Sort | 5,000 -> 10,000 | O(n^2) | 4.03x | 4.00x | 1.01 |
| Insertion Sort | 100 -> 500 | O(n^2) | 26.59x | 25.00x | 1.06 |
| Insertion Sort | 500 -> 1,000 | O(n^2) | 4.02x | 4.00x | 1.00 |
| Insertion Sort | 1,000 -> 5,000 | O(n^2) | 29.43x | 25.00x | 1.18 |
| Insertion Sort | 5,000 -> 10,000 | O(n^2) | 3.71x | 4.00x | 0.93 |
| Merge Sort | 100 -> 500 | O(n log n) | 5.64x | 6.75x | 0.84 |
| Merge Sort | 500 -> 1,000 | O(n log n) | 2.27x | 2.22x | 1.02 |
| Merge Sort | 1,000 -> 5,000 | O(n log n) | 6.09x | 6.16x | 0.99 |
| Merge Sort | 5,000 -> 10,000 | O(n log n) | 2.13x | 2.16x | 0.98 |
| Merge Sort | 10,000 -> 50,000 | O(n log n) | 5.87x | 5.87x | 1.00 |
| Merge Sort | 50,000 -> 100,000 | O(n log n) | 2.13x | 2.13x | 1.00 |
| Quick Sort | 100 -> 500 | O(n log n) | 6.46x | 6.75x | 0.96 |
| Quick Sort | 500 -> 1,000 | O(n log n) | 2.32x | 2.22x | 1.04 |
| Quick Sort | 1,000 -> 5,000 | O(n log n) | 6.11x | 6.16x | 0.99 |
| Quick Sort | 5,000 -> 10,000 | O(n log n) | 2.10x | 2.16x | 0.97 |
| Quick Sort | 10,000 -> 50,000 | O(n log n) | 5.95x | 5.87x | 1.01 |
| Quick Sort | 50,000 -> 100,000 | O(n log n) | 2.13x | 2.13x | 1.00 |

## Sensibilidade ao tipo de entrada

| Algoritmo | n | Tempo: aleatoria | Tempo: ordenada | Tempo: inversa | Tempo: parcialmente_ordenada | Pior / melhor cenario |
|---|---|---|---|---|---|---|
| Bubble Sort | 10,000 | 4.216614 | 0.000440 | 5.442679 | 2.702157 | 12379.1x |
| Insertion Sort | 10,000 | 1.761111 | 0.000841 | 3.481293 | 0.402970 | 4141.7x |
| Merge Sort | 100,000 | 0.223572 | 0.176935 | 0.172843 | 0.202363 | 1.3x |
| Quick Sort | 100,000 | 0.184794 | 0.115182 | 0.301911 | 0.172933 | 2.6x |

## Leitura dos resultados

- **Entrada aleatoria (n = 10,000, maior tamanho rodado por todos):** melhor desempenho do **Quick Sort** (0.014552 s); pior desempenho do **Bubble Sort** (4.216614 s) - 289.8x mais lento.
- **Bubble Sort** no maior n medido (n = 10,000, aleatoria): 4.216614 s, 49,989,839 comparacoes, 49,692,119 movimentacoes (teorico: O(n^2) no caso medio).
- **Insertion Sort** no maior n medido (n = 10,000, aleatoria): 1.761111 s, 24,856,051 comparacoes, 24,856,059 movimentacoes (teorico: O(n^2) no caso medio).
- **Merge Sort** no maior n medido (n = 100,000, aleatoria): 0.223572 s, 1,536,439 comparacoes, 3,337,856 movimentacoes (teorico: O(n log n) no caso medio).
- **Quick Sort** no maior n medido (n = 100,000, aleatoria): 0.184794 s, 1,912,179 comparacoes, 1,791,569 movimentacoes (teorico: O(n log n) no caso medio).

- **Bubble Sort** (n = 10,000): mais rapido com entrada *ordenada* e mais lento com entrada *inversa* - variacao de 12379.1x entre os cenarios.
- **Insertion Sort** (n = 10,000): mais rapido com entrada *ordenada* e mais lento com entrada *inversa* - variacao de 4141.7x entre os cenarios.
- **Quick Sort** (n = 100,000): mais rapido com entrada *ordenada* e mais lento com entrada *inversa* - variacao de 2.6x entre os cenarios.
- **Merge Sort** (n = 100,000): mais rapido com entrada *inversa* e mais lento com entrada *aleatoria* - variacao de 1.3x entre os cenarios.

- **O(n^2) competitivo:** com entrada *ordenada* e n = 100, o Bubble Sort (0.000003 s) foi igual ou mais rapido que o Quick Sort (0.000047 s).
- **O(n^2) competitivo:** com entrada *ordenada* e n = 500, o Bubble Sort (0.000018 s) foi igual ou mais rapido que o Quick Sort (0.000308 s).
- **O(n^2) competitivo:** com entrada *ordenada* e n = 1,000, o Bubble Sort (0.000040 s) foi igual ou mais rapido que o Quick Sort (0.000695 s).
- **O(n^2) competitivo:** com entrada *ordenada* e n = 5,000, o Bubble Sort (0.000223 s) foi igual ou mais rapido que o Quick Sort (0.004522 s).
- **O(n^2) competitivo:** com entrada *ordenada* e n = 10,000, o Bubble Sort (0.000440 s) foi igual ou mais rapido que o Quick Sort (0.009488 s).
- **O(n^2) competitivo:** com entrada *parcialmente_ordenada* e n = 100, o Insertion Sort (0.000034 s) foi igual ou mais rapido que o Quick Sort (0.000060 s).
