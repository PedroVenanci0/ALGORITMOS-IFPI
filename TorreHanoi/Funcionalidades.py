from utils import red,green,darkblue,lightblue

def tutorial():

    print(f"""

====================================
> Bem Vindo a Torre de Hanoi ({red("R")}{green("G")}{darkblue("B")}) <
====================================

- Hanói Rogério Gordinho Bonito --> Hanói RGB

============
> controle <
============

- {red("R")}G (Dá pilha 'R' para a torre 'G')
- RB (Dá pilha 'R' para a torre 'B')
- GR (Dá pilha 'G' para a torre 'R')
- GB (Dá pilha 'G' para a torre 'B')
- BG (Dá pilha 'B' para a torre 'G')
- BR (Dá pilha 'B' para a torre 'R')

============
 > Regras <
============

- Somente é possível inserir e remover itens no Topo das Torres.

- Vence o Jogador que completar todas as Torres com seus itens correspondentes em menos jogadas

- Em caso de Empate, a vitoria será daquele que completou em menos tempo

- O jogo Encerrar ao alocar corretamente os itens 
________________________________________

""")

def menu():

    print("""


     > Menu Inicial <
==========================
(1) Start Game
(2) Tutorial
(3) Historico de Vitorias
(4) Quit Game
=========================
""")

    opcoes = int(input("> "))
    match opcoes:
        caso 1:
            StarGame()
        caso 2:
            Tutorial()
        caso 3:
            HistoricoVitoria()
        caso 4:
