'''
Condicionais pode ser: SIMPLES, COMPOSTO, ENCADEADO
'''

nota1 = nota2 = 0.0
media = 0

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

# calculando a média artimética
media = (nota1 + nota2) / 2
if (media >= 7):
  print('O aluno está aprovado!')

elif (media < 7 and media >=6):
  print('O aluno está de recuperação!')
else:
  print('O aluno não foi aprovado!')

print('Sua média é: {}'.format(media))