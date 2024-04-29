# 16. Leia um número N, calcule e escreva os N primeiros termos de seqüência de Fibonacci
# (0,1,1,2,3,5,8,...). O valor lido para N sempre será maior ou igual a 2.

def main():
    
    numero_N = int(input('Digite o número de termos da sequência: '))
    
    while numero_N < 2:
    
        if numero_N < 2:
            
            print('Valor INVÁLIDO!! Tente novamente.')
            numero_N = int(input('Digite o número de termos da sequência: '))
        
    primeiro_termo  = 0
    segundo_termo = 1
    
    ordem = '0 1 '
    
    for contador in range(2, numero_N):
        
        terceiro_termo = primeiro_termo + segundo_termo
        
        primeiro_termo = segundo_termo
        
        segundo_termo = terceiro_termo
        
        ordem += str(terceiro_termo) 
        
        if contador < numero_N - 1: 
            
            ordem += " " 

    print(ordem)
              

main()