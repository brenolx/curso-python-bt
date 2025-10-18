# n1 = 1

# Enquanto o n1 for menor= a 10 faça
# while (n1 != 0):
#     print(f'{n1}')
#     n1 += 1

nome = None

while (True):
    nome = input('Digite seu nome ou \'x\' pra parar:')
    
    if nome == 'x' or nome == 'X':
        break # finaliza imediatamente o laço
    print(f'O nome é: {nome}')

print('Até logo!')