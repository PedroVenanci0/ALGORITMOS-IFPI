def UtilizandoRecursividade():

    print("""
> Opeções de Tarefas:
_________________________________
          
> (1) < Calcular o Fatorial de um número N.
> (2) < Imprimir uma Sequência Fibonacci de comprimento C.
> (3) < Função que imprime uma Sequência Simples de A até B.
> (4) < Calcular o Produto (multiplicação) nas forma de somas sucessivas.
> (5) < Calcular Exponencial de um Número N elevado a expoente E.
> (6) < Dado um intervalo A e B, calcular o somatório de um Vetor de N Elementos Aleatórios.
> (7) < Contar Vogais e Consoantes de Frase.
_________________________________
""")
    
    opcoes = int(input("> "))

    match opcoes:
        case 1:
            FatorialRecursividade()
        case 2:
            FibonacciRecursividade()
        case 3:
            SequenciaRecursividade()
        case 4:
            ProdutoSomaSucessivasRecursividade()
        case 5:
            ExponencialRecursividade()
        case 6:
            SomatorioAleatorioRecursividade()
        case 7:
            ContarVogaisConsoantesRecursividade()


def FatorialRecursividade():
    pass

def FibonacciRecursividade():
    pass

def SequenciaRecursividade():
    pass

def ProdutoSomaSucessivasRecursividade():
    pass

def ExponencialRecursividade():
    pass

def SomatorioAleatorioRecursividade():
    pass

def ContarVogaisConsoantesRecursividade():
    pass

            

