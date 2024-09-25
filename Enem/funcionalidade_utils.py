def ler_arquivo():

    arquivo = open("enem2014.txt.csv", encoding='cp1252')

    matriz = []  # Cria a matriz (lista de listas)

    for linha in arquivo:
        linha = linha.strip() 
        valores = linha.split(';')  
        matriz.append(valores) 
    return matriz

matriz = ler_arquivo()


def quick_sort(matriz,key):

    if len(matriz) <= 1:
        return matriz

    pivot = matriz[len(matriz) // 2]
    left = []
    right = []

    for i in range(len(matriz)):
        if matriz[i][key] > pivot[key]:
            left.append(matriz[i])
        elif matriz[i][key] < pivot[key]:
            right.append(matriz[i])
    
    # Concatenando as listas corretamente
    return quick_sort(left,key) + [pivot] + quick_sort(right,key)

def media_nacional_area(matriz,key):

    notas = []
    somatorio = 0

    for i in range(len(matriz)):
        notas.append(matriz[i][key])
        somatorio += matriz[i][key]

    qtd_notas = len(notas)
    media = somatorio/qtd_notas

    return media 


