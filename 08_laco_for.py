# Lista
    # 'lista = [2,6,9,4,0,12,3,7]
    # palavra = 'C urso'

    # for letra in palavra:
    #     print(letra)'

    # for numero in range(1, 11):
    #     print(numero)

    # nome = input('Digite seu nome: ')

    # for x in  range(10):
    #     print(f'{x+1} {nome}')


# função range(valor_inicial, valor_final, incremento)
    # for x  in range(2, 20, 2):
    #     print(x)

# Criando uma tupla = ()
pedras = ('Rubi', 'Esmeralda', 'Quartzo', 'Safira', 'Diamante', 'Turmalina')
for pedra in pedras:
    if pedra == 'Quartzo':
        continue # pula para próxima iteração do laço
    print(pedra)