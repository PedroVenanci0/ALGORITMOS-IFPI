
def menu():
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
            top_brasil()
        case 2:
            top_brasil_area()
        case 3:
            top_estado()
        case 4:
            top_estado_publica_provada()
        case 5:
            media_nacional()
        case 6:
            melhor_escola()
        case 7:
            lista_escolas_estado_renda()
        case 8:
            escola_por_nome()
        case 9:
            ranking_por_estado()
        case 10:
            ranking_por_regiao()
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