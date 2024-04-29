import time

def main():
    numero_N = 100
    
        # Método 1: Usando um loop for para imprimir os números pares

    start_time = time.time()
    for i in range(1, numero_N + 1):
        if i % 2 == 0:
            print(i)
    end_time = time.time()
    print("Tempo usando loop for:", end_time - start_time)

       # Método 2: Usando list comprehension e filter para obter os números pares

    start_time = time.time()
    lista_numeros = [i for i in range(numero_N + 1)]
    filtro_par = list(filter(lambda i: i % 2 == 0, lista_numeros))
    print("Números pares usando list comprehension e filter:", filtro_par)
    end_time = time.time()
    print("Tempo usando list comprehension e filter:", end_time - start_time)
main()