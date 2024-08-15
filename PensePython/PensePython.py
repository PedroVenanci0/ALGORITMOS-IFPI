def main():
    resultado = is_abecedarian()
    print(resultado)

def is_abecedarian():

    iglesio = False

    palavra = input()

    primeiro_termo = ord(palavra[0])

    for elemenst in range(1, len(palavra)):

        segundo_termo = ord(palavra[elemenst])

        if (primeiro_termo == segundo_termo - 1) or primeiro_termo == segundo_termo:
            primeiro_termo = segundo_termo
            iglesio = True

        else: iglesio = False
        
    return iglesio            
main()