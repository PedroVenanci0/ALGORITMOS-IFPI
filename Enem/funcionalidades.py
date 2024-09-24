from utils import clear_screen

def top_brasil():

    matriz_valores = ler_arquivo()
    numero_escolas = int(input("\nInforme o número de escolas a serem classficadas: "))
    clear_screen()
    print(f"\n----- Top {numero_escolas} Escolas do Brasil ----- \n")

    lista_melhores = []
    contador = 0

    for i in range(numero_escolas):
        for elements in matriz_valores[i]:
            lista_melhores.append(matriz_valores[i][1])
            break

    for escolas in lista_melhores:
        contador += 1
        print(f"{contador} - {escolas}")


def top_brasil_area():

    matriz_valores = ler_arquivo()
    numero_escolas = int(input("\nInforme o número de escolas a serem classficadas: "))
    clear_screen()
    print("""

> ÁREA DICIPLINARES <
---------------------
1 - LINGUAGENS
2 - MATEMÁTICA
3 - CIÊNCIAS HUMANAS
4 - CIÊNCIAS DA NATUREZA
5 - REDAÇÃO
---------------------
""")

    try:
        opcao = int(input("Informe a área diciplicar para analise: "))
    except ValueError:
        print("\nErro: Por favor, insira um número válido.")
        top_brasil_area()
    match opcao:
        case 1:
            ordenacao_linguagens(matriz_valores)
        case 2:
            ordenacao_matematica(matriz_valores)
        case 3:
            ordenacao_humanas(matriz_valores)
        case 4:
            ordenacao_natureza(matriz_valores)
        case 5:
            ordenacao_redacao(matriz_valores)



    clear_screen()





def ler_arquivo():

    arquivo = open("enem2014.txt.csv")

    matriz = []  # Cria a matriz (lista de listas)

    for linha in arquivo:
        linha = linha.strip() 
        valores = linha.split(';')  
        matriz.append(valores) 
    
    return matriz

    # for elements in matriz:
    #     print(elements)
    #     print()

top_brasil()
