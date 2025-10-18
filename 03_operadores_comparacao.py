"""
OPERADOR | OPERAÇÃO
    ==        Igual a
    !=        Difertente de
     >       Maior que
     <        Menor que
    >=       Maior ou igual a
    <=        Menor ou igual a
"""
x = y = z = False
n1 = n2 = 0

n1 = int(input('Digite um numero:'))
n2 = int(input('Digite outro numero:'))

x = n1 == n2
print('São iguais?', x, '\n')

z = n1 > n2
print(n1, 'é maior que', n2, '?', z, '\n')

y = n1 != n2
print('São diferentes ' + str(y)) # casting (bool to string)