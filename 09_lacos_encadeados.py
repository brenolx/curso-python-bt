# for cont_e in range(1, 6):
#     print(f'\nRodada: {cont_e}')
#     for cont_i in range(5, 0, -1):
#         print(f'valor: {cont_i}')
    
# print('\nFim dos Laços!')

import random

for a in  range(1, 6):
    print(f'\nConjunto: {a}')
    for b in range(5):
        numero = random.randint(1, 100)
        print(f'\tValor: {numero}')