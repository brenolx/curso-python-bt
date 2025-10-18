
def mensagem():
    return 'Treinado (import) de funções do curso!'


def fatorial(num):
    fat = num

    while(num != 1):
        fat = fat * (num - 1) # 3x2
        num -= 1              # 6x1
    return fat                #
