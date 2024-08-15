import utils

def main():

    opcão = int(input(menu()))

    if opcão == 1:

        morethan20()

    elif opcão == 2:

        has_no_e()
    
    elif opcão == 3:

        resultado = avoid()
        print(resultado)

    elif opcão == 4:

        resultado = user_only()
        print(resultado)

    elif opcão == 5:

        resultado = uses_all()
        print(resultado)
    

def morethan20():

    arquivo = open('words.txt')

    Lista_20 = []

    for linha in arquivo:
        palavra = linha.strip()
        if len(palavra) >= 20:
            Lista_20.append(palavra)
        
    utils.clear_screen()
        
    for linha in Lista_20:
        print(linha)

def has_no_e():

    arquivo = open('words.txt')

    Lista_no_eh = []

    for linha in arquivo:
        palavra = linha.strip()

        contem_eh = False
        
        for elements in palavra:
            if elements == "e":
                contem_eh = True
                break

        if not contem_eh: 
            Lista_no_eh.append(palavra)

    for elements in Lista_no_eh:
        print(elements)
           
        
def avoid():

    arquivo = open('words.txt')
    cont = 0
    Lista_proibidas = []

    letra_proibida = input("Informe a letra proibida > ")

    for elements in letra_proibida:
        Lista_proibidas.append(elements)

    for linha in arquivo:
        palavra = linha.strip()
        contem_letra_proibida = False

        # Verifica cada letra da palavra
        for letra in palavra:
            for elements in Lista_proibidas:
                if letra == elements:
                    contem_letra_proibida = True
                    break

        # Se a palavra não contém a letra proibida, incrementa o contador
        if not contem_letra_proibida:
            cont += 1

    return cont

def user_only():

    letras_escolhidas = input("Informe as letras  > ")
    palavra_inserida = input("\nInforme a palavra > ")

   
    for letra in palavra_inserida:
        encontrado = False

        for elements in range(len(letras_escolhidas)):
            if letra == letras_escolhidas[elements]:
                encontrado = True
                break
        
        
        if not encontrado:
            return False

    return True  

def uses_all():

    letras_escolhidas = input("Informe as letras  > ")
    palavra_inserida = input("\nInforme a palavra > ")

   
    for letra in palavra_inserida:
        letras_encontradas = 0

        for elements in range(len(letras_escolhidas)):
            if letra == letras_escolhidas[elements]:
                letras_encontradas += 1

        if letras_encontradas == len(letras_escolhidas):
            return True
        
        

def is_abecedaria():

    palavra_inserida = input("\nInforme a palavra > ")

    for letra in palavra_inserida:
        if 

                
def menu():
    opção = """
> QUAL filtro vc deseja ser aplicado em seu arquivo: 

> 1 - Palavras com mais de 20 letras;           >  6 - Palavras com mais de 20 letras;
> 2 - Palavras que nao possuem a letra 'e'      >  7 - Palavras com mais de 20 letras;
> 3 - Palavras com mais de 20 letras;           >  8 - Palavras com mais de 20 letras;
> 4 - Palavras com mais de 20 letras;           >  9 - Palavras com mais de 20 letras;
> 5 - Palavras com mais de 20 letras;           > 10 - Palavras com mais de 20 letras;

>> """
    return opção

main()