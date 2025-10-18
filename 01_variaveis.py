# Conveções para craição de variáveis
nome_usuario = 'Breno'
# print(nome_usuario)

# ---------
media = 0
n1 = n2 = n3 = n4 = 0.0

# ---------
nome, idade = 'Breno', 27
estado = True 

# TIPO DE DADOS type() ----- tipos primitivos
print(type(media)) # <class> inteiro
print(type(n1)) # <> float
print(type(nome)) # #string
print(type(estado)) # booleano / lógico
print(type(1+2j)) # complex -- números complexos

# Função isinstance() - True false
a = 10
b = 'sol'

# Verificando se a var 'a' é de um tipo numerico seja int ou float
print(isinstance(a, (float, int)))