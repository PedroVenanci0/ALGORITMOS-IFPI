from utils import escrever_texto
from utils import clear_screen
import time
import random

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
            valor = FatorialRecursividade()
            print(valor)
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
        
    texto = "\nInforme um valor: "
    escrever_texto(texto)
    N = int(input("> "))

    start_time = time.time()

    ValorFinal = FatorialProcessamento(N)

    end_time = time.time()
    execution_time = end_time - start_time

    clear_screen()

    return (f"""
        >>> Fatorial While <<<
========================================
O fatorial {N}!      >   {ValorFinal}
Tempo de execução  >   {execution_time:.6f} segundos
========================================
""")

def FatorialProcessamento (n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * FatorialProcessamento(n - 1)

def FibonacciRecursividade():

    texto = "\nInforme um valor: "
    escrever_texto(texto)
    N = int(input("> "))

    primeiro_termo = 0
    segundo_termo = 1

def FibonacciProcessamento(n,primeiro_termo,segundo_termo):

    if n == (n - (n-2)):
        return

    fibonacci = [primeiro_termo, segundo_termo]

    start_time = time.time()
    
    proximo_termo = primeiro_termo + segundo_termo
    fibonacci.append(proximo_termo)
    
    primeiro_termo = segundo_termo
    segundo_termo = proximo_termo
    
    return sequencia_fibonacci = ", ".join(map(str, fibonacci))
    FibonacciProcessamento(n,primeiro_termo,segundo_termo)


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

            
UtilizandoRecursividade()
