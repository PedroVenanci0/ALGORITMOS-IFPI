# 13. Leia N e uma lista de N números e escreva o maior número da lista.


def main():

    tamanho_da_lista = int(input('Informe o valor correspondente ao tamnho da lista: '))

    numero = float(input('Digite um numero: '))

    maior_numero = numero

    lista = str(1) + "°" + " " + "-->" + " " + str(numero)

    for contador in range(1, tamanho_da_lista):

        numero = float(input('Digite um numero: '))

        contador += 1

        lista = lista + "\n" + str(contador) + "°" + " " + "-->" + " " + str(numero) 
    
        if numero > maior_numero:

            maior_numero = numero
        
    print ('\n>>>>> Lista de números <<<<<<\n')
    print (lista)
    print ('\n====================================================')
    print (f'O maior número dentre os digitados é {maior_numero}')
    print ('====================================================\n')





main()