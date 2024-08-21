import random
import os\

def main():

    OpcaoMenuInicial = int(input(Menu() + "> "))

    match OpcaoMenuInicial:

        case 1:
            Valores = GerarDadosAutomaticos()
            print(f"\n{Valores}")
        case 2:
            Valores = InserirManualmente()
            print(f"\n{Valores}")
        case 3:
            Valores = InserirArquivo()
            print(f"\n{Valores}")
    
    MenuGeral()
    OpcoesMenuGeral = int(input("> "))

    while OpcoesMenuGeral != 15:

        match OpcoesMenuGeral:

            case 1:
                MostrarValores(Valores)
            case 2:
                pass
            case 3:
                QuantidadeVetores(Valores)
            case 4:
                MaiorMenorVetor(Valores)
            case 5:
                SomatorioValores(Valores)
            case 6:
                MediaValores(Valores)
            case 7:
                QtdValoresPositivos(Valores)
            case 8:
                QtdValoresNegativos(Valores)
            case 9:
                Regras(Valores)
            case 10:
                AddNovosValores(Valores)
                pass
            case 11:
                Valores = RemoverPorValor(Valores)
                print(Valores)
            case 12:
                Valores = RemoverPorIndex(Valores)
                print(Valores)
                pass
            case 13:
                EditarPorPosicao(Valores)
                pass
            case 14:
                #SalvarArquivo()
                pass

        input("\n| Pressione Enter para CONTINUAR: |")
        clear_screen()
        MenuGeral()
        OpcoesMenuGeral = int(input("> "))
            
            

def MenuGeral():
    opcoes = """
======================================
        >>> Menu PlayNumber <<<
======================================
| 1 | - Mostrar todos os Vetores
| 2 | - Resetar Valor
| 3 | - Ver quantidades de itens do vetor
| 4 | - Ver menor e maior valores e suas posições
| 5 | - Sómatorio de Valores
| 6 | - Média de Valores
| 7 | - Mostrar Valores Positivos e Quantidades
| 8 | - Mostrar Valores Negativos e suas Quantidades
| 9 | - Atualizar Todos os Valores segundo as regras a seguir
| 10| - Adicionar Novos Valores
| 11| - Remover Itens por um Valor exato
| 12| - Remover por Posição 
| 13| - Editar Valores Especificos por Posição
| 14| - Salvar Valores em Arquivo
| 15| - Sair
=====================================
"""
    print(opcoes) 

def Menu():
    opcao_menu = """
======================================
    >>> Inicialização de Vetores <<<
======================================
| 1 | - Inicializar Dados Automaticos
| 2 | - Inserir Valores 
| 3 | - Inserir Arquivo
======================================
"""
    return opcao_menu

def GerarDadosAutomaticos():

    tamanho = int(input("\nInsira o Número de dados > "))
    min_ = int(input("\nInsira o Menor valor onde os dados se encontram > "))
    max_ = int(input("\nInsira o Maior valor onde os dados se encontram > "))

    ListaDados = []

    for i in range(tamanho):
        ListaDados.append(random.randint(min_,max_))

    return ListaDados

def InserirManualmente():

    ListaDados = []

    tamanho = int(input("\nInsira o dado > "))

    for elements in range(tamanho):

        Dados = int(input(f"Dado [{elements + 1}] > "))
        ListaDados.append(Dados)
    
    return ListaDados
     

def InserirArquivo():

    NomeArquivo = input("Insira o Nome do arquivo > ")
    Arquivo = open(f"{NomeArquivo}").split()

def MostrarValores(valores):
    print(valores)

def QuantidadeVetores(valores):

    qtdVetores = 0
    
    for elements in range(len(valores)):
        qtdVetores += 1

    print(f"\nA quantidade de vetores presentes é {qtdVetores} unidades")

def MaiorMenorVetor(valores):

    MenorVetor = valores[0]
    MaiorVetor = 0

    contador = 0

    posicaoMenorVetor = 0
    posicaoMaiorVetor = 0

    for elements in valores:
        if elements > MaiorVetor:
            MaiorVetor = elements
            posicaoMaiorVetor = contador + 1 
        if elements < MenorVetor:
            MenorVetor = elements
            posicaoMenorVetor = contador + 1
        
        contador += 1

    print(f"""
====================================
| >> Maior Valor: {MaiorVetor} na {posicaoMaiorVetor}° Posição |
| >> Menor Valor: {MenorVetor} na {posicaoMenorVetor}° Posição |
====================================
""")
    
def SomatorioValores(valores):

    somatorio = 0

    for elements in valores:
        somatorio += elements
    
    print(f"\nO somatorio dos valores é {somatorio}")   

def MediaValores(valores):

    somatorio = 0
    qtdValores = 0

    for elements in valores:
        somatorio += elements
        qtdValores += 1
    
    media = somatorio / qtdValores

    print(f"|A média dos Valores >> {media}|")

    
def QtdValoresPositivos(valores):

    ListaPositivos = []

    contadorPositivos = 0

    for elements in valores:
        if elements >= 0:
            ListaPositivos.append(elements)
            contadorPositivos += 1

    print(f"""
======================
{ListaPositivos}

|Quantidade >> {contadorPositivos}|
======================
""")

def QtdValoresNegativos(valores):
        
    ListaNegativos = []

    contadorNegativos = 0

    for elements in valores:
        if elements >= 0:
            ListaNegativos.append(elements)
            contadorNegativos += 1

    print(f"""
======================
{ListaNegativos}

|Quantidade >> {contadorNegativos}|
======================
""")

def Regras(valores):
    opcoes = """
======================================
    >>> Atualizando Valores <<<
======================================
| 1 | - Multiplicar Por Um Valor
| 2 | - Elevar a Um Valor
| 3 | - Reduzir a uma fração
| 4 | - Substituir valores negativos por um número aleatórios da uma faixa(min, max)
| 5 | - Ordenar valores
| 6 | - Embaralhar valores
======================================
"""

    print(opcoes)
    opcoesMenu = int(input("> "))

    # clear_screen()
    
    match opcoesMenu:
        case 1:
            MultiplicarValores(valores)
        case 2: 
            ElevarValor(valores)
            pass
        case 3:
            ReduzirAhFracao(valores)
            pass
        case 4:
            # SubstituirValoresNegativos(valores)
            pass
        case 5:
            # OrdenarValores(valores)
            pass
        case 6:
            # EmbaralharValores(valores)
            pass
        


def clear_screen():
    # Verifica o sistema operacional
    if os.name == 'posix':  # Linux/macOS
        os.system('clear')
    elif os.name == 'nt':   # Windows
        os.system('cls')

def MultiplicarValores(valores):

    #Reseter Valores para sua forma original

    valor = int(input('Informe um valor para os termos serem multiplicados > '))

    for elements in range(len(valores)):
        valores[elements] = valores[elements] * valor

    print(valores)

def ElevarValor(valores):

    #Reseter Valores para sua forma original

    valor = int(input('Informe um valor para os termos serem Elevados > '))

    for elements in range(len(valores)):
        valores[elements] = valores[elements] ** valor

    print(valores)

def ReduzirAhFracao(valores):
    pass

def AddNovosValores(valores):
    
    opcoes = """
======================================
    >>> Adicionando Valores <<<
======================================
| 1 | - Inicializar Dados Automaticos
| 2 | - Inserir Valores Manualmente
| 3 | - Inserir Arquivo
============================
"""
    print(opcoes)

    entrada = int(input("\n> "))

    match entrada:
        case 1:
            valores += GerarDadosAutomaticos()
        case 2:
            valores += InserirManualmente()
        case 3:
            valores += InserirArquivo()

def RemoverPorValor(valores):

    valor = int(input("Informe o valor a ser excluido > "))

    ListaNova = []

    for elements in valores:
        if elements == valor:
            continue
        
        ListaNova.append(elements)

    valores = ListaNova

    return valores
    
def RemoverPorIndex(valores):

    valor = int(input("Informe o index a ser excluido > "))

    ListaNova = []

    for elements in range(len(valores)):
        if elements + 1 == valor:
            continue
            
        ListaNova.append(valores[elements])

    valores = ListaNova

    return valores

def EditarPorPosicao(valores):

    indexEditado = int(input("Informe o index a ser editado > "))
    valorInserido = int(input("Informe o valor a ser Inserido > "))

    valores[indexEditado - 1] = valorInserido

    print(f"O valor {valores[indexEditado]} foi inserido no Posição [{indexEditado}]!!")

    print(f"\nA nova Lista de vetores Consiste em {valores}")

main()



