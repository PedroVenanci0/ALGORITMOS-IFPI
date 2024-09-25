import funcionalidades as func

def ler_arquivo():

    arquivo = open("enem2014.txt.csv", encoding='cp1252')

    matriz = []

    for linha in arquivo:
        linha = linha.strip() 
        valores = linha.split(';')  
        matriz.append(valores) 
    
    return matriz

def menu():

    matriz = ler_arquivo()
    
    print("""

    > ENEM POR ESCOLA - 2014 < 
=====================================
            
       > Menu de Consulta <
-------------------------------------  
1 - Top N Brasil (todas as áreas)
2 - Top N Brasil por Área
3 - Top N por Estado
4 - Top N por Estado e Rede (pública ou privada)
5 - Media Nacional por Área
6 - Melhor escola por Área e Estado ou BR
7 - Listas Escolas por Estado Ordenada Por Renda
8 - Busca escola específica por parte  Nome
9 - Ranking ENEM por Estado
10 - Ranking ENEM por Região do País
          
0 - sair
--------------------------------------
""")   
    
    try:
        opcao = int(input("> "))

    except ValueError:
        print("\nErro: Por favor, insira um número válido.")
        input("\nPressione Enter para voltar ao menu...")
        menu()

    match opcao:
        case 1:
            func.top_brasil(matriz)
        case 2:
            func.top_brasil_area(matriz)
        case 3:
            func.top_estado(matriz)
        case 4:
            func.top_estado_publica_privada(matriz)
        case 5:
            func.media_nacional(matriz)
        case 6:
            pass
            #melhor_escola()
        case 7:
            pass
            #lista_escolas_estado_renda()
        case 8:
            pass
            #escola_por_nome()
        case 9:
            pass
            #ranking_por_estado()
        case 10:
            pass
            #ranking_por_regiao()
        case 0:
            print("fim...")
            return
        case _:
            print("\nInforme um número correspondente as opções!!!")
            input("\npressione Enter para voltar ao menu...")
            menu()


def main():
    menu()
main()