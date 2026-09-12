# Analise empirica de algoritmos de ordenacao

Trabalho de Projeto e Analise de Algoritmos. Compara quatro algoritmos de
ordenacao medindo tempo, comparacoes, trocas e movimentacoes sobre quatro
tipos de entrada e sete tamanhos, e confronta o resultado com a
complexidade teorica.

## Instalacao

Os experimentos, o CSV e as tabelas usam **apenas a biblioteca padrao do
Python** (3.9+). O `matplotlib` e necessario so para os graficos.

**Com ambiente virtual**:

```bash
python -m venv .venv
source .venv/bin/activate         
pip install -r requirements.txt
```
## Como rodar

```bash
python main.py start             # experimentos + tabelas + graficos
python main.py start --quick     # versao curta (n ate 2.000), para conferir
python main.py algorithms        # catalogo e complexidades
python main.py start --quadratic-limit 100000 --csv completo.csv #Roda o buble e o insertion incluindo os 100.000 elementos
python main.py run --sizes 100,1000,10000 --repeats 5   # escolhendo tamanhos e repeticoes
python main.py run --with-variants                      # inclui o Quick Sort de pior caso
python main.py tables                                   # so refaz analise.md
python main.py charts                                   # so refaz os graficos

```

| Comando | O que faz |
|---|---|
| `start` | roda os experimentos e gera tabelas e graficos |
| `run` | so roda os experimentos e grava o CSV |
| `tables` | refaz `analise.md` a partir do CSV existente |
| `charts` | refaz a pasta `graficos/` a partir do CSV existente |
| `algorithms` | mostra o catalogo de algoritmos e suas complexidades |

| Opcao de `start` / `run` | O que faz |
|---|---|
| `--sizes 100,1000` | tamanhos de entrada, separados por virgula |
| `--inputs aleatoria,inversa` | quais cenarios de entrada rodar |
| `--repeats 5` | execucoes por ponto, das quais se tira a media |
| `--quadratic-limit 5000` | maior n aplicado a Bubble e Insertion |
| `--with-variants` | inclui o Quick Sort com pivo no ultimo elemento |
| `--quick` | perfil curto, para verificar se esta tudo certo |
| `--csv arquivo.csv` | onde gravar (ou de onde ler) os resultados |

## Estrutura

Um arquivo por algoritmo; o restante agrupado por etapa do trabalho:

```
bubble_sort.py  insertion_sort.py  merge_sort.py  quick_sort.py
                um algoritmo por arquivo
experimento.py  catalogo + entradas + medicao + execucao -> resultados.csv
relatorio.py    tabelas (-> analise.md) e graficos (-> graficos/)
python main.py start --quadratic-limit 100000 --csv
main.py         linha de comando
```

`experimento.py` e `relatorio.py` sao divididos em secoes comentadas
(CATALOGO / ENTRADAS / MEDICAO / EXECUCAO e TABELAS / GRAFICOS), entao da
para achar cada etapa sem precisar de um arquivo separado para cada uma.

Cada algoritmo e independente dos demais modulos: ordena a lista in-place
e devolve `{"comparacoes", "trocas", "movimentacoes"}`. Rode qualquer um
sozinho com `python bubble_sort.py`.

## Os algoritmos

| Algoritmo | Estrategia | Melhor | Medio | Pior | Espaco | Estavel |
|---|---|---|---|---|---|---|
| Bubble Sort | forca bruta | O(n) | O(n²) | O(n²) | O(1) | sim |
| Insertion Sort | incremental | O(n) | O(n²) | O(n²) | O(1) | sim |
| Merge Sort | divisao e conquista | O(n log n) | O(n log n) | O(n log n) | O(n) | sim |
| Quick Sort | divisao e conquista | O(n log n) | O(n log n) | O(n²) | O(log n) | nao |

A escolha cobre tres estrategias de projeto diferentes e dois patamares de
complexidade. Isso permite comparar quadraticos contra linearitmicos e,
dentro de cada par, isolar o efeito da estrategia: dois O(n²) que diferem
no numero de trocas, e dois O(n log n) que diferem no uso de memoria e na
estabilidade do pior caso.

Os numeros abaixo sao do experimento deste repositorio: n = 10.000 para os
quadraticos e n = 100.000 para os linearitmicos (ver `analise.md`).

---

### Bubble Sort — `bubble_sort.py`

**Como funciona.** Percorre a lista comparando cada par de vizinhos e
trocando-os quando estao fora de ordem. A cada passagem o maior elemento
restante "flutua" ate o fim, entao apos a i-esima passagem as i ultimas
posicoes ja estao definitivas. A implementacao guarda uma flag
`houve_troca`: se uma passagem inteira termina sem nenhuma troca, a lista
ja esta ordenada e o laco para.

**Por que e O(n²).** Sao n-1 passagens e ate n-1 comparacoes em cada uma,
o que da n(n-1)/2 comparacoes — em n = 10.000, cerca de 50 milhoes. A flag
so ajuda quando a entrada ja esta (quase) ordenada: em uma unica passagem
sem trocas ele sai, o que da o melhor caso O(n).

**No experimento.**

| Entrada | Tempo | Comparacoes | Trocas |
|---|---|---|---|
| aleatoria | 4,217 s | 49.989.839 | 24.846.060 |
| ordenada | 0,000440 s | 9.999 | 0 |
| inversa | 5,443 s | 49.995.000 | 49.995.000 |
| parcialmente ordenada | 2,702 s | 49.959.749 | 5.750.635 |

Foi o **pior algoritmo em entrada aleatoria** — 290x mais lento que o
Quick Sort — e o **mais sensivel ao tipo de entrada**: 12.379x de diferenca
entre ordenada e inversa. Repare que em entrada parcialmente ordenada o
tempo caiu pela metade mas as comparacoes quase nao mudaram: o ganho veio
das trocas, que sao a operacao cara, nao das comparacoes.

**Quando usar.** Praticamente nunca em producao. Vale como referencia
didatica e para listas minusculas ou ja quase ordenadas, onde a parada
antecipada o torna O(n) — e ai ele venceu ate o Quick Sort no experimento.

---

### Insertion Sort — `insertion_sort.py`

**Como funciona.** Estrategia incremental: mantem um prefixo ordenado e
insere nele um elemento por vez. Para cada elemento, guarda seu valor na
variavel `chave` e desloca para a direita todos os elementos maiores do
prefixo, abrindo o buraco onde a chave entra. E o mesmo gesto de ordenar
cartas na mao.

**Por que e O(n²).** No pior caso cada elemento precisa atravessar todo o
prefixo, dando novamente n(n-1)/2 comparacoes. Mas em uma entrada
aleatoria a chave para, em media, no meio do prefixo — por isso fez
**metade** das comparacoes do Bubble Sort (24,9 M contra 50,0 M) e foi 2,4x
mais rapido, mesmo os dois sendo O(n²).

**Detalhe das metricas.** Ele nao faz trocas, e sim deslocamentos: por isso
`trocas` e sempre 0 e o custo de escrita aparece todo em `movimentacoes`.
Um deslocamento e uma escrita; uma troca sao duas. Essa e a razao de ele
ganhar do Bubble Sort no mesmo n.

**No experimento.**

| Entrada | Tempo | Comparacoes | Movimentacoes |
|---|---|---|---|
| aleatoria | 1,761 s | 24.856.051 | 24.856.059 |
| ordenada | 0,000841 s | 9.999 | 9.999 |
| inversa | 3,481 s | 49.995.000 | 50.004.999 |
| parcialmente ordenada | 0,403 s | 5.760.634 | 5.760.634 |

O caso parcialmente ordenado e o mais revelador: **4,4x mais rapido que em
entrada aleatoria**, porque o custo real dele e proporcional ao numero de
inversoes da entrada, nao a n². Com 10% de desordem, ha poucas inversoes.

**Quando usar.** E o melhor dos quadraticos na pratica: entradas pequenas
(dezenas de elementos) ou quase ordenadas, e como caso-base dentro de
algoritmos hibridos — bibliotecas reais trocam para Insertion Sort quando
a particao fica menor que umas dezenas de elementos.

---

### Merge Sort — `merge_sort.py`

**Como funciona.** Divisao e conquista. Divide a lista ao meio
recursivamente ate sobrarem pedacos de um elemento (trivialmente
ordenados) e depois intercala os pedacos dois a dois: a funcao `merge`
copia as duas metades para vetores auxiliares e vai escolhendo, a cada
passo, o menor entre as duas frentes.

**Por que e O(n log n) sempre.** A divisao gera log₂n niveis de recursao, e
cada nivel intercala no total n elementos. Como a divisao e sempre pela
metade — independente dos valores — **nao existe pior caso**: a arvore de
recursao tem a mesma forma para qualquer entrada. Foi o unico algoritmo com
movimentacoes constantes (3.337.856) nos quatro cenarios, o que mostra isso
de forma direta.

**O preco.** Os vetores auxiliares custam O(n) de memoria extra, e cada
elemento e escrito duas vezes por nivel (uma na copia para o auxiliar,
outra na volta). Por isso ele tem **mais movimentacoes que o Quick Sort**
(3,3 M contra 1,8 M) e perdeu no tempo, apesar de fazer **menos
comparacoes** (1,5 M contra 1,9 M).

**No experimento.**

| Entrada | Tempo | Comparacoes | Movimentacoes |
|---|---|---|---|
| aleatoria | 0,224 s | 1.536.439 | 3.337.856 |
| ordenada | 0,177 s | 853.904 | 3.337.856 |
| inversa | 0,173 s | 815.024 | 3.337.856 |
| parcialmente ordenada | 0,202 s | 1.485.631 | 3.337.856 |

**O mais previsivel dos quatro**: apenas 1,3x de variacao entre o melhor e
o pior cenario, contra 12.379x do Bubble Sort. E estavel (nao troca a ordem
de elementos iguais), porque o `merge` usa `<=` ao escolher da metade
esquerda.

**Quando usar.** Quando o pior caso importa (sistemas com prazo), quando a
estabilidade e necessaria, ou quando os dados nao cabem na memoria —
ordenacao externa e feita com merge. O custo e aceitar O(n) de memoria.

---

### Quick Sort — `quick_sort.py`

**Como funciona.** Tambem divisao e conquista, mas particionando no lugar:
escolhe um pivo, reorganiza o vetor de modo que tudo menor fique a esquerda
e tudo maior a direita (esquema de Lomuto), e chama-se recursivamente nas
duas partes. Diferente do Merge Sort, o trabalho esta na **divisao**, nao na
combinacao — depois do particionamento nao ha nada a juntar.

**Duas decisoes de implementacao importantes:**

1. **Pivo por mediana de tres** (primeiro, meio e ultimo elemento) em vez do
   ultimo elemento. Com pivo fixo no ultimo, uma entrada ja ordenada produz
   particoes de tamanho 0 e n-1 — a recursao vira uma cadeia linear e o
   custo desaba para O(n²).
2. **Recursao so na menor particao**, com a maior tratada no laco `while`
   (eliminacao de recursao de cauda). Isso limita a profundidade da pilha a
   O(log n) mesmo no pior caso, evitando estouro de recursao em n grande.

**Por que e O(n log n) no caso medio e O(n²) no pior.** Se o pivo divide o
vetor em partes equilibradas, ha log₂n niveis de particionamento com n
comparacoes cada. Se o pivo cai sempre num extremo, sao n niveis — dai o
pior caso quadratico. A mediana de tres torna esse cenario improvavel em
entradas reais.

**No experimento.**

| Entrada | Tempo | Comparacoes | Movimentacoes |
|---|---|---|---|
| aleatoria | 0,185 s | 1.912.179 | 1.791.569 |
| ordenada | 0,115 s | 1.665.551 | 262.140 |
| inversa | 0,302 s | 3.259.375 | 3.826.464 |
| parcialmente ordenada | 0,173 s | 2.296.615 | 1.469.607 |

**Foi o mais rapido em entrada aleatoria.** E o mais interessante: ele venceu
o Merge Sort *fazendo mais comparacoes* (1,9 M contra 1,5 M). A vantagem veio
das movimentacoes — 1,8 M contra 3,3 M — porque particiona in-place, sem
copiar para vetores auxiliares. Isso ilustra que contagem de comparacoes
sozinha nao prediz o tempo.

**A variante de pior caso.** O arquivo traz tambem `quick_sort_ultimo`, com
pivo fixo no ultimo elemento, fora do experimento padrao. Rodando
`python main.py run --with-variants`, com entrada **ordenada** e n = 5.000
ela faz **12.497.500 comparacoes** — exatamente n(n-1)/2, a formula do pior
caso — contra 60.678 da mediana de tres. E 130x mais lenta. Serve para
mostrar que a complexidade de pior caso do Quick Sort e real e que a escolha
do pivo e o que a evita.

**Quando usar.** E o padrao para ordenacao em memoria: mais rapido na
media e usa pouca memoria. Evite quando o pior caso for inaceitavel ou
quando a estabilidade for necessaria (ele nao e estavel).

## Experimentos

- **Tamanhos:** 100, 500, 1.000, 5.000, 10.000, 50.000 e 100.000.
  Bubble e Insertion param em 10.000 (`--quadratic-limit`): em n = 100.000
  o custo quadratico levaria horas.
- **Entradas:** aleatoria, ordenada, inversa e parcialmente ordenada
  (10% das posicoes embaralhadas). Sementes fixas, entao todos os
  algoritmos recebem exatamente os mesmos dados.
- **Repeticoes:** 3 execucoes por ponto, com sementes diferentes; grava-se
  a media, o minimo, o maximo e o desvio do tempo.

## Metricas

| Metrica | Definicao usada |
|---|---|
| tempo | `time.perf_counter`, coletor de lixo desligado durante a ordenacao |
| comparacoes | comparacoes entre elementos da entrada |
| trocas | permutas de dois elementos (Insertion e Merge nao fazem trocas) |
| movimentacoes | escritas de elemento em vetor; uma troca conta 2 |

A ordenacao e conferida a cada execucao: se a lista nao sair ordenada, o
experimento falha em vez de registrar um numero errado.

## Saidas

- `resultados.csv` — uma linha por (algoritmo, tipo de entrada, n)
- `analise.md` — tabelas por metrica, crescimento observado x previsto,
  sensibilidade ao tipo de entrada e a leitura dos numeros
- `graficos/` — tempo, comparacoes e movimentacoes x n (log-log), um
  grafico de sensibilidade por algoritmo e o comparativo final
