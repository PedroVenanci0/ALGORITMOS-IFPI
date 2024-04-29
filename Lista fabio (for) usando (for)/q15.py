# 15. Leia N, calcule e escreva os N primeiros termos de seqüência (1, 3, 6, 10, 15,...).

def main():

    numero_de_termos = int(input('Informe o número de termos: '))

    valor = 1

    ordem = ''

    sequencia = []

    for contador in range(2, numero_de_termos + 1):

        valor = valor + contador

        sequencia.append(str(valor))

    ordem = ', '.join(sequencia)

    print (f'A ordem de termos da sequência é (1, {ordem})')
main()