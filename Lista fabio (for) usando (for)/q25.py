# 25. Em uma eleição presidencial existem 3 (três) candidatos. Os votos são informados através de códigos.
# Os dados utilizados para a contagem dos votos obedecem à seguinte codificação:
# · 1, 2, 3 = voto para os respectivos candidatos;
# · 9 = voto nulo;
# · 0 = voto em branco;
# Escreva um algoritmo que leia o código votado por N eleitores. Ao final, calcule e escreva:
# a) total de votos para cada candidato;
# b) total de votos nulos;
# c) total de votos em branco;
# d) quem venceu a eleição.

import os

def main():
    print ('\n>>>>>>>>>>> ELEIÇÕES ADS MURAL <<<<<<<<<<<')
    print ('==========================================\n')
    
    print('''
          
· 1, 2, 3 = voto para os respectivos candidatos
· 9 = voto nulo
· 0 = voto em branco

''')
    
    LucasLopes = 0
    Patro = 0
    rogerio = 0
    nulo = 0
    voto_branco = 0
    
    opcao_voto = int(input('Qual sua opção de voto: '))
    
    if opcao_voto == 1:
        
        LucasLopes += 1
    
    elif opcao_voto == 2:
        
        Patro += 1
    
    elif opcao_voto == 3:
        
        rogerio += 1 
    
    elif opcao_voto == 9:
        
        nulo += 1
    
    elif opcao_voto == 0:
        
        voto_branco += 1
        
    print(f'''
          
========================================================================
                    >>>>> RESULTADO DAS ELEIÇÕES <<<<<
========================================================================
. Número de votos >> Candidato Patro           -----------> {Patro}
. Número de votos >> Candidato LucasLopes      -----------> {LucasLopes}
. Número de votos >> Candidatos Rogerio        -----------> {rogerio}
. Número de votos >> Nulos                     -----------> {nulo}
. Número de votos >> brancos                   -----------> {voto_branco} 
=======================================================================

''')
    
    
def LimparTela():
    
    os.system('cls' if os.name == 'nt' else 'clear')



def aguarde(segundos):
    
    
    
main()