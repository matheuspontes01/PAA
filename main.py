"""Linha de comando do trabalho de analise empirica de algoritmos de ordenacao.

Exemplos:

    python main.py start                     roda os experimentos, gera as
                                             tabelas e os graficos
    python main.py start --quick             versao curta, para conferir
    python main.py run --sizes 100,1000,10000 --repeats 5
    python main.py run --with-variants       inclui o Quick Sort com pivo
                                             no ultimo elemento (pior caso)
    python main.py tables                    so refaz as tabelas do CSV
    python main.py charts                    so refaz os graficos do CSV
    python main.py algorithms                mostra o catalogo e a teoria

Organizacao do projeto:

    bubble_sort.py  insertion_sort.py  merge_sort.py  quick_sort.py
                    um algoritmo por arquivo
    experimento.py  catalogo, entradas, medicao e execucao -> resultados.csv
    relatorio.py    tabelas (analise.md) e graficos (graficos/)
    main.py         esta linha de comando
"""

import argparse
import sys

import experimento
import relatorio


def _lista_de_inteiros(texto):
    return [int(parte) for parte in texto.split(",") if parte.strip()]


def _lista_de_textos(texto):
    return [parte.strip() for parte in texto.split(",") if parte.strip()]


def construir_parser():

    parser = argparse.ArgumentParser(
        prog="main.py",
        description="Analise empirica de algoritmos de ordenacao",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )

    comandos = parser.add_subparsers(dest="comando", required=True)

    # --- opcoes compartilhadas por 'start' e 'run' ---
    opcoes_execucao = argparse.ArgumentParser(add_help=False)

    opcoes_execucao.add_argument(
        "--sizes", type=_lista_de_inteiros,
        default=experimento.TAMANHOS_PADRAO,
        help="tamanhos de entrada separados por virgula "
             f"(padrao: {','.join(str(n) for n in experimento.TAMANHOS_PADRAO)})",
    )
    opcoes_execucao.add_argument(
        "--inputs", type=_lista_de_textos,
        default=experimento.tipos_de_entrada(),
        help="tipos de entrada "
             f"(padrao: {','.join(experimento.tipos_de_entrada())})",
    )
    opcoes_execucao.add_argument(
        "--repeats", type=int, default=experimento.REPETICOES_PADRAO,
        help="execucoes por ponto, das quais se tira a media "
             f"(padrao: {experimento.REPETICOES_PADRAO})",
    )
    opcoes_execucao.add_argument(
        "--quadratic-limit", type=int, default=experimento.LIMITE_QUADRATICO,
        help="maior n aplicado aos algoritmos O(n^2) "
             f"(padrao: {experimento.LIMITE_QUADRATICO})",
    )
    opcoes_execucao.add_argument(
        "--with-variants", action="store_true",
        help="inclui a variante Quick Sort com pivo no ultimo elemento",
    )
    opcoes_execucao.add_argument(
        "--quick", action="store_true",
        help="perfil curto (n ate 2.000) para verificar se esta tudo certo",
    )
    opcoes_execucao.add_argument(
        "--csv", default=experimento.ARQUIVO_SAIDA,
        help=f"arquivo de resultados (padrao: {experimento.ARQUIVO_SAIDA})",
    )

    comandos.add_parser(
        "start", parents=[opcoes_execucao],
        help="executa os experimentos, gera tabelas e graficos",
    )
    comandos.add_parser(
        "run", parents=[opcoes_execucao],
        help="so executa os experimentos e grava o CSV",
    )

    tabelas = comandos.add_parser(
        "tables", help="gera as tabelas a partir do CSV existente"
    )
    tabelas.add_argument("--csv", default=experimento.ARQUIVO_SAIDA)
    tabelas.add_argument("--output", default=relatorio.ARQUIVO_ANALISE)

    graficos = comandos.add_parser(
        "charts", help="gera os graficos a partir do CSV existente"
    )
    graficos.add_argument("--csv", default=experimento.ARQUIVO_SAIDA)
    graficos.add_argument("--output-dir", default=relatorio.PASTA_GRAFICOS)

    comandos.add_parser(
        "algorithms", help="mostra o catalogo de algoritmos e a teoria"
    )

    return parser


def _executar(args):

    tamanhos = args.sizes
    limite = args.quadratic_limit

    if args.quick:
        tamanhos = [100, 500, 1000, 2000]
        limite = 2000

    return experimento.rodar(
        tamanhos=tamanhos,
        tipos=args.inputs,
        repeticoes=args.repeats,
        limite_quadratico=limite,
        saida=args.csv,
        com_variantes=args.with_variants,
    )


def main(argv=None):

    args = construir_parser().parse_args(argv)

    if args.comando == "algorithms":

        for nome in experimento.nomes(incluir_variantes=True):

            dados = experimento.info(nome)

            print(f"\n{nome}")
            print(f"  estrategia : {dados['estrategia']}")
            print(f"  tempo      : melhor {dados['melhor']} | "
                  f"medio {dados['medio']} | pior {dados['pior']}")
            print(f"  espaco     : {dados['espaco']}")
            print(f"  estavel    : {'sim' if dados['estavel'] else 'nao'}")
            print(f"  no experimento por padrao: "
                  f"{'sim' if dados['padrao'] else 'nao (use --with-variants)'}")

        return 0

    if args.comando in ("start", "run"):

        _executar(args)

        if args.comando == "start":

            relatorio.gerar_tabelas(args.csv, relatorio.ARQUIVO_ANALISE,
                                    imprimir=False)
            print(f"tabelas geradas: {relatorio.ARQUIVO_ANALISE}")

            relatorio.gerar_graficos(args.csv, relatorio.PASTA_GRAFICOS)

        return 0

    if args.comando == "tables":
        relatorio.gerar_tabelas(args.csv, args.output, imprimir=True)
        return 0

    if args.comando == "charts":
        relatorio.gerar_graficos(args.csv, args.output_dir)
        return 0

    return 1


if __name__ == "__main__":
    sys.exit(main())
