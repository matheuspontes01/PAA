# Analise dos resultados

Fonte: `completo.csv` - 112 medicoes, media de 3 execucoes por ponto.

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
| Bubble Sort | 0.001005 | 0.030115 | 0.129053 | 3.892340 | 16.373086 | 432.266949 | 1686.363383 |
| Insertion Sort | 0.000506 | 0.011879 | 0.051482 | 1.471646 | 5.873240 | 156.774371 | 690.796208 |
| Merge Sort | 0.006161 | 0.005454 | 0.004972 | 0.028305 | 0.105115 | 0.330726 | 0.700057 |
| Quick Sort | 0.007547 | 0.001720 | 0.003980 | 0.024344 | 0.050553 | 0.305159 | 0.643772 |

### Entrada: ordenada

| Algoritmo | n = 100 | n = 500 | n = 1,000 | n = 5,000 | n = 10,000 | n = 50,000 | n = 100,000 |
|---|---|---|---|---|---|---|---|
| Bubble Sort | 0.000013 | 0.000068 | 0.000141 | 0.000707 | 0.001491 | 0.007304 | 0.014936 |
| Insertion Sort | 0.000022 | 0.000123 | 0.000269 | 0.001384 | 0.002932 | 0.016708 | 0.031054 |
| Merge Sort | 0.000347 | 0.001741 | 0.003855 | 0.022404 | 0.047318 | 0.272890 | 0.567150 |
| Quick Sort | 0.000189 | 0.001042 | 0.002307 | 0.014863 | 0.031327 | 0.182995 | 0.382742 |

### Entrada: inversa

| Algoritmo | n = 100 | n = 500 | n = 1,000 | n = 5,000 | n = 10,000 | n = 50,000 | n = 100,000 |
|---|---|---|---|---|---|---|---|
| Bubble Sort | 0.001474 | 0.040368 | 0.172982 | 4.752913 | 19.411177 | 509.529474 | 2288.864650 |
| Insertion Sort | 0.001316 | 0.026438 | 0.103221 | 2.885878 | 11.321627 | 291.626901 | 1264.737554 |
| Merge Sort | 0.000274 | 0.001673 | 0.003785 | 0.022375 | 0.046784 | 0.261272 | 0.554790 |
| Quick Sort | 0.000370 | 0.002400 | 0.005983 | 0.039250 | 0.091527 | 0.539961 | 1.161648 |

### Entrada: parcialmente_ordenada

| Algoritmo | n = 100 | n = 500 | n = 1,000 | n = 5,000 | n = 10,000 | n = 50,000 | n = 100,000 |
|---|---|---|---|---|---|---|---|
| Bubble Sort | 0.000587 | 0.017375 | 0.088901 | 2.307057 | 10.080857 | 232.119670 | 928.480754 |
| Insertion Sort | 0.000184 | 0.003307 | 0.022717 | 0.425802 | 1.493073 | 37.176723 | 138.428532 |
| Merge Sort | 0.000305 | 0.001899 | 0.004284 | 0.025969 | 0.055078 | 0.352796 | 0.679314 |
| Quick Sort | 0.000223 | 0.001498 | 0.003636 | 0.022007 | 0.047634 | 0.287696 | 0.607230 |

## Comparacoes


### Entrada: aleatoria

| Algoritmo | n = 100 | n = 500 | n = 1,000 | n = 5,000 | n = 10,000 | n = 50,000 | n = 100,000 |
|---|---|---|---|---|---|---|---|
| Bubble Sort | 4,775 | 124,479 | 498,590 | 12,492,979 | 49,989,839 | 1,249,964,281 | 4,999,868,357 |
| Insertion Sort | 2,386 | 61,795 | 246,478 | 6,252,755 | 24,856,051 | 625,537,186 | 2,502,206,219 |
| Merge Sort | 540 | 3,849 | 8,707 | 55,201 | 120,367 | 718,185 | 1,536,439 |
| Quick Sort | 728 | 4,864 | 11,275 | 70,306 | 148,915 | 893,295 | 1,912,179 |

### Entrada: ordenada

| Algoritmo | n = 100 | n = 500 | n = 1,000 | n = 5,000 | n = 10,000 | n = 50,000 | n = 100,000 |
|---|---|---|---|---|---|---|---|
| Bubble Sort | 99 | 499 | 999 | 4,999 | 9,999 | 49,999 | 99,999 |
| Insertion Sort | 99 | 499 | 999 | 4,999 | 9,999 | 49,999 | 99,999 |
| Merge Sort | 356 | 2,272 | 5,044 | 32,004 | 69,008 | 401,952 | 853,904 |
| Quick Sort | 669 | 4,263 | 9,520 | 60,678 | 131,343 | 782,782 | 1,665,551 |

### Entrada: inversa

| Algoritmo | n = 100 | n = 500 | n = 1,000 | n = 5,000 | n = 10,000 | n = 50,000 | n = 100,000 |
|---|---|---|---|---|---|---|---|
| Bubble Sort | 4,950 | 124,750 | 499,500 | 12,497,500 | 49,995,000 | 1,249,975,000 | 4,999,950,000 |
| Insertion Sort | 4,950 | 124,750 | 499,500 | 12,497,500 | 49,995,000 | 1,249,975,000 | 4,999,950,000 |
| Merge Sort | 316 | 2,216 | 4,932 | 29,804 | 64,608 | 382,512 | 815,024 |
| Quick Sort | 851 | 6,843 | 15,995 | 108,443 | 242,135 | 1,504,807 | 3,259,375 |

### Entrada: parcialmente_ordenada

| Algoritmo | n = 100 | n = 500 | n = 1,000 | n = 5,000 | n = 10,000 | n = 50,000 | n = 100,000 |
|---|---|---|---|---|---|---|---|
| Bubble Sort | 4,639 | 119,518 | 494,512 | 12,468,251 | 49,959,749 | 1,249,510,916 | 4,999,578,768 |
| Insertion Sort | 622 | 14,766 | 57,159 | 1,438,326 | 5,760,634 | 144,947,862 | 575,734,504 |
| Merge Sort | 494 | 3,542 | 8,092 | 52,787 | 115,475 | 692,603 | 1,485,631 |
| Quick Sort | 748 | 5,212 | 13,694 | 79,165 | 175,170 | 1,030,492 | 2,296,615 |

## Movimentacoes


### Entrada: aleatoria

| Algoritmo | n = 100 | n = 500 | n = 1,000 | n = 5,000 | n = 10,000 | n = 50,000 | n = 100,000 |
|---|---|---|---|---|---|---|---|
| Bubble Sort | 4,579 | 122,601 | 490,970 | 12,495,525 | 49,692,119 | 1,250,974,391 | 5,004,212,457 |
| Insertion Sort | 2,388 | 61,799 | 246,484 | 6,252,762 | 24,856,059 | 625,537,195 | 2,502,206,228 |
| Merge Sort | 1,344 | 8,976 | 19,952 | 123,616 | 267,232 | 1,568,928 | 3,337,856 |
| Quick Sort | 686 | 4,487 | 10,777 | 65,383 | 137,413 | 861,987 | 1,791,569 |

### Entrada: ordenada

| Algoritmo | n = 100 | n = 500 | n = 1,000 | n = 5,000 | n = 10,000 | n = 50,000 | n = 100,000 |
|---|---|---|---|---|---|---|---|
| Bubble Sort | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| Insertion Sort | 99 | 499 | 999 | 4,999 | 9,999 | 49,999 | 99,999 |
| Merge Sort | 1,344 | 8,976 | 19,952 | 123,616 | 267,232 | 1,568,928 | 3,337,856 |
| Quick Sort | 252 | 1,020 | 2,044 | 11,808 | 23,616 | 131,068 | 262,140 |

### Entrada: inversa

| Algoritmo | n = 100 | n = 500 | n = 1,000 | n = 5,000 | n = 10,000 | n = 50,000 | n = 100,000 |
|---|---|---|---|---|---|---|---|
| Bubble Sort | 9,900 | 249,500 | 999,000 | 24,995,000 | 99,990,000 | 2,499,950,000 | 9,999,900,000 |
| Insertion Sort | 5,049 | 125,249 | 500,499 | 12,502,499 | 50,004,999 | 1,250,024,999 | 5,000,049,999 |
| Merge Sort | 1,344 | 8,976 | 19,952 | 123,616 | 267,232 | 1,568,928 | 3,337,856 |
| Quick Sort | 936 | 7,672 | 18,168 | 125,784 | 281,088 | 1,763,200 | 3,826,464 |

### Entrada: parcialmente_ordenada

| Algoritmo | n = 100 | n = 500 | n = 1,000 | n = 5,000 | n = 10,000 | n = 50,000 | n = 100,000 |
|---|---|---|---|---|---|---|---|
| Bubble Sort | 1,047 | 28,534 | 112,320 | 2,866,656 | 11,501,271 | 289,795,728 | 1,151,269,011 |
| Insertion Sort | 622 | 14,766 | 57,159 | 1,438,327 | 5,760,634 | 144,947,863 | 575,734,505 |
| Merge Sort | 1,344 | 8,976 | 19,952 | 123,616 | 267,232 | 1,568,928 | 3,337,856 |
| Quick Sort | 416 | 3,290 | 7,913 | 50,080 | 113,315 | 716,251 | 1,469,607 |

## Trocas


### Entrada: aleatoria

| Algoritmo | n = 100 | n = 500 | n = 1,000 | n = 5,000 | n = 10,000 | n = 50,000 | n = 100,000 |
|---|---|---|---|---|---|---|---|
| Bubble Sort | 2,289 | 61,300 | 245,485 | 6,247,763 | 24,846,060 | 625,487,196 | 2,502,106,229 |
| Insertion Sort | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| Merge Sort | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| Quick Sort | 343 | 2,244 | 5,388 | 32,691 | 68,706 | 430,993 | 895,785 |

### Entrada: ordenada

| Algoritmo | n = 100 | n = 500 | n = 1,000 | n = 5,000 | n = 10,000 | n = 50,000 | n = 100,000 |
|---|---|---|---|---|---|---|---|
| Bubble Sort | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| Insertion Sort | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| Merge Sort | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| Quick Sort | 126 | 510 | 1,022 | 5,904 | 11,808 | 65,534 | 131,070 |

### Entrada: inversa

| Algoritmo | n = 100 | n = 500 | n = 1,000 | n = 5,000 | n = 10,000 | n = 50,000 | n = 100,000 |
|---|---|---|---|---|---|---|---|
| Bubble Sort | 4,950 | 124,750 | 499,500 | 12,497,500 | 49,995,000 | 1,249,975,000 | 4,999,950,000 |
| Insertion Sort | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| Merge Sort | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| Quick Sort | 468 | 3,836 | 9,084 | 62,892 | 140,544 | 881,600 | 1,913,232 |

### Entrada: parcialmente_ordenada

| Algoritmo | n = 100 | n = 500 | n = 1,000 | n = 5,000 | n = 10,000 | n = 50,000 | n = 100,000 |
|---|---|---|---|---|---|---|---|
| Bubble Sort | 523 | 14,267 | 56,160 | 1,433,328 | 5,750,635 | 144,897,864 | 575,634,506 |
| Insertion Sort | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| Merge Sort | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| Quick Sort | 208 | 1,645 | 3,957 | 25,040 | 56,657 | 358,125 | 734,804 |

## Crescimento observado x previsto (entrada aleatoria)

Razao entre medicoes consecutivas. A coluna Obs./Prev. proxima de 1,0 indica que o experimento seguiu a curva teorica.

| Algoritmo | Transicao de n | Classe teorica | Crescimento observado | Crescimento previsto | Obs./Prev. |
|---|---|---|---|---|---|
| Bubble Sort | 100 -> 500 | O(n^2) | 29.96x | 25.00x | 1.20 |
| Bubble Sort | 500 -> 1,000 | O(n^2) | 4.29x | 4.00x | 1.07 |
| Bubble Sort | 1,000 -> 5,000 | O(n^2) | 30.16x | 25.00x | 1.21 |
| Bubble Sort | 5,000 -> 10,000 | O(n^2) | 4.21x | 4.00x | 1.05 |
| Bubble Sort | 10,000 -> 50,000 | O(n^2) | 26.40x | 25.00x | 1.06 |
| Bubble Sort | 50,000 -> 100,000 | O(n^2) | 3.90x | 4.00x | 0.98 |
| Insertion Sort | 100 -> 500 | O(n^2) | 23.46x | 25.00x | 0.94 |
| Insertion Sort | 500 -> 1,000 | O(n^2) | 4.33x | 4.00x | 1.08 |
| Insertion Sort | 1,000 -> 5,000 | O(n^2) | 28.59x | 25.00x | 1.14 |
| Insertion Sort | 5,000 -> 10,000 | O(n^2) | 3.99x | 4.00x | 1.00 |
| Insertion Sort | 10,000 -> 50,000 | O(n^2) | 26.69x | 25.00x | 1.07 |
| Insertion Sort | 50,000 -> 100,000 | O(n^2) | 4.41x | 4.00x | 1.10 |
| Merge Sort | 100 -> 500 | O(n log n) | 0.89x | 6.75x | 0.13 |
| Merge Sort | 500 -> 1,000 | O(n log n) | 0.91x | 2.22x | 0.41 |
| Merge Sort | 1,000 -> 5,000 | O(n log n) | 5.69x | 6.16x | 0.92 |
| Merge Sort | 5,000 -> 10,000 | O(n log n) | 3.71x | 2.16x | 1.72 |
| Merge Sort | 10,000 -> 50,000 | O(n log n) | 3.15x | 5.87x | 0.54 |
| Merge Sort | 50,000 -> 100,000 | O(n log n) | 2.12x | 2.13x | 0.99 |
| Quick Sort | 100 -> 500 | O(n log n) | 0.23x | 6.75x | 0.03 |
| Quick Sort | 500 -> 1,000 | O(n log n) | 2.31x | 2.22x | 1.04 |
| Quick Sort | 1,000 -> 5,000 | O(n log n) | 6.12x | 6.16x | 0.99 |
| Quick Sort | 5,000 -> 10,000 | O(n log n) | 2.08x | 2.16x | 0.96 |
| Quick Sort | 10,000 -> 50,000 | O(n log n) | 6.04x | 5.87x | 1.03 |
| Quick Sort | 50,000 -> 100,000 | O(n log n) | 2.11x | 2.13x | 0.99 |

## Sensibilidade ao tipo de entrada

| Algoritmo | n | Tempo: aleatoria | Tempo: ordenada | Tempo: inversa | Tempo: parcialmente_ordenada | Pior / melhor cenario |
|---|---|---|---|---|---|---|
| Bubble Sort | 100,000 | 1686.363383 | 0.014936 | 2288.864650 | 928.480754 | 153245.5x |
| Insertion Sort | 100,000 | 690.796208 | 0.031054 | 1264.737554 | 138.428532 | 40726.9x |
| Merge Sort | 100,000 | 0.700057 | 0.567150 | 0.554790 | 0.679314 | 1.3x |
| Quick Sort | 100,000 | 0.643772 | 0.382742 | 1.161648 | 0.607230 | 3.0x |

## Leitura dos resultados

- **Entrada aleatoria (n = 100,000, maior tamanho rodado por todos):** melhor desempenho do **Quick Sort** (0.643772 s); pior desempenho do **Bubble Sort** (1686.363383 s) - 2619.5x mais lento.
- **Bubble Sort** no maior n medido (n = 100,000, aleatoria): 1686.363383 s, 4,999,868,357 comparacoes, 5,004,212,457 movimentacoes (teorico: O(n^2) no caso medio).
- **Insertion Sort** no maior n medido (n = 100,000, aleatoria): 690.796208 s, 2,502,206,219 comparacoes, 2,502,206,228 movimentacoes (teorico: O(n^2) no caso medio).
- **Merge Sort** no maior n medido (n = 100,000, aleatoria): 0.700057 s, 1,536,439 comparacoes, 3,337,856 movimentacoes (teorico: O(n log n) no caso medio).
- **Quick Sort** no maior n medido (n = 100,000, aleatoria): 0.643772 s, 1,912,179 comparacoes, 1,791,569 movimentacoes (teorico: O(n log n) no caso medio).

- **Bubble Sort** (n = 100,000): mais rapido com entrada *ordenada* e mais lento com entrada *inversa* - variacao de 153245.5x entre os cenarios.
- **Insertion Sort** (n = 100,000): mais rapido com entrada *ordenada* e mais lento com entrada *inversa* - variacao de 40726.9x entre os cenarios.
- **Quick Sort** (n = 100,000): mais rapido com entrada *ordenada* e mais lento com entrada *inversa* - variacao de 3.0x entre os cenarios.
- **Merge Sort** (n = 100,000): mais rapido com entrada *inversa* e mais lento com entrada *aleatoria* - variacao de 1.3x entre os cenarios.

- **O(n^2) competitivo:** com entrada *aleatoria* e n = 100, o Insertion Sort (0.000506 s) foi igual ou mais rapido que o Merge Sort (0.006161 s).
- **O(n^2) competitivo:** com entrada *ordenada* e n = 100, o Bubble Sort (0.000013 s) foi igual ou mais rapido que o Quick Sort (0.000189 s).
- **O(n^2) competitivo:** com entrada *ordenada* e n = 500, o Bubble Sort (0.000068 s) foi igual ou mais rapido que o Quick Sort (0.001042 s).
- **O(n^2) competitivo:** com entrada *ordenada* e n = 1,000, o Bubble Sort (0.000141 s) foi igual ou mais rapido que o Quick Sort (0.002307 s).
- **O(n^2) competitivo:** com entrada *ordenada* e n = 5,000, o Bubble Sort (0.000707 s) foi igual ou mais rapido que o Quick Sort (0.014863 s).
- **O(n^2) competitivo:** com entrada *ordenada* e n = 10,000, o Bubble Sort (0.001491 s) foi igual ou mais rapido que o Quick Sort (0.031327 s).
- **O(n^2) competitivo:** com entrada *ordenada* e n = 50,000, o Bubble Sort (0.007304 s) foi igual ou mais rapido que o Quick Sort (0.182995 s).
- **O(n^2) competitivo:** com entrada *ordenada* e n = 100,000, o Bubble Sort (0.014936 s) foi igual ou mais rapido que o Quick Sort (0.382742 s).
- **O(n^2) competitivo:** com entrada *parcialmente_ordenada* e n = 100, o Insertion Sort (0.000184 s) foi igual ou mais rapido que o Quick Sort (0.000223 s).
