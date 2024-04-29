# 1. Leia N e escreva todos os números inteiros de 1 a N.

def main():

    num = int(input('Informe um número: '))

    contagem = 0

    while contagem < num: 

        contagem += 1
        print (f'{contagem}')



main()