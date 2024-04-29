def main():
    cor = tabela_de_cor()

def tabela_de_cor():
    
    cor = 'cor'
    print (f'''
   >>>> NÚMEROS PARA CORES DOS RESULTADOS <<<<
           
           CINZA        >>>        \033[30m{cor} = 30\033[m
           VERMELHOR    >>>        \033[31m{cor} = 31\033[m
           VERDE        >>>        \033[32m{cor} = 32\033[m
           AMARELO      >>>        \033[33m{cor} = 33\033[m
           AZUL ESCURO  >>>        \033[34m{cor} = 34\033[m
           ROSA         >>>        \033[35m{cor} = 35\033[m
           AZUL CIANO   >>>        \033[36m{cor} = 36\033[m

''')
    
main()