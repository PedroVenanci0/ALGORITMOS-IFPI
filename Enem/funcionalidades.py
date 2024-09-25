from utils import clear_screen
import funcionalidade_utils as func_utils

DinicionarioAreas = {
    "linguagens": 8,
    "matematica": 9,
    "humanas": 10,
    "natureza": 11,
    "redacao": 12

}

def top_brasil(matriz):

    numero_escolas = int(input("\nInforme o número de escolas a serem classficadas: "))
    clear_screen()
    print(f"\n----- Top {numero_escolas} Escolas do Brasil ----- \n")

    lista_melhores = []

    for i in range(numero_escolas):
        for elements in matriz[i]:
            lista_melhores.append(matriz[i][1])
            break

    for i in range(len(lista_melhores)):
        print(f"{i+1} - {lista_melhores[i]}")


def top_brasil_area(matriz):

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
            media_area = func_utils.quick_sort(matriz,"linguagem")
        case 2:
            media_area = func_utils.quick_sort(matriz,"matematica")
        case 3:
            media_area = func_utils.quick_sort(matriz,"humanas")
        case 4:
            media_area = func_utils.quick_sort(matriz,"natureza")
        case 5:
            media_area = func_utils.quick_sort(matriz,"redacao")
    
    numero_escolas = int(input("\nInforme o número de escolas a serem classficadas: "))

    for i in range(numero_escolas):
        print(f"{i+1} - {media_area[i][1]}")

def top_estado(matriz):

    matriz_escolas = []
    estado_analisado = input("Informe o estado a ser analisado: ").upper()

    for i in range(len(matriz)):
        if str(matriz[i][3]) == estado_analisado:
            matriz_escolas.append(matriz[i])
    

    media_area = func_utils.quick_sort(matriz_escolas,7)


    numero_escolas = int(input("\nInforme o número de escolas a serem classficadas: "))

    for i in range(numero_escolas):
        print(f"{i+1} - {media_area[i][1]}")

def top_estado_publica_privada(matriz):

    matriz_escolas = []
    estado_analisado = input("Informe o estado a ser analisado: ").upper()

    for i in range(len(matriz)):
        if matriz[i][3] == estado_analisado:
            matriz_escolas.append(matriz[i])

    rede_analisada = int(input("(1) - Municipal | (2) - Federal | (3) - Federal | (4) - Privada: "))

    match rede_analisada:
        case 1:
            rede_escolar = "Municipal"
        case 2:
            rede_escolar = "Estadual"
        case 3:
            rede_escolar = "Federal"
        case 4:
            rede_escolar = "Privada"

    matriz_rede = []
    
    for i in range(len(matriz_escolas)):
        if matriz_escolas[i][4] == rede_escolar:
            matriz_rede.append(matriz_escolas[i])

    matriz_rede = func_utils.quick_sort(matriz_rede,7)

    numero_escolas = int(input("\nInforme o número de escolas a serem classficadas: "))

    for i in range(numero_escolas):
       print(f"{i+1} - {matriz_rede[i][1]}")
    
def media_nacional(matriz):
    
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
        media_nacional()

    
    match opcao:

        case 1:
            media_area = func_utils.media_nacional_area(matriz,8)
        case 2:
            media_area = func_utils.media_nacional_area(matriz,"matematica")
        case 3:
            media_area = func_utils.media_nacional_area(matriz,"humanas")
        case 4:
            media_area = func_utils.media_nacional_area(matriz,"natureza")
        case 5:
            media_area = func_utils.media_nacional_area(matriz,"redacao")

    
    print(f"A media da area escolhida é {media_area:.2f}")
        


