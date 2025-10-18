# imprtando módulos para aplicação
    # from math import pow, sqrt

# aliás para uma função -->>
    # import math as m
import mod_func as mf

# Só vai executar neste arquivo
if __name__ == '__main__':
    num = int(input('Digite um numero: '))
    fatorial = mf.fatorial(num)

    print(f'O fatorial de {num} é = {fatorial}')