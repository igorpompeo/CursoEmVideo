from datetime import date
'''
crie um programa o ano de nascimento de sete pessoas. no final, mostre quantas
pessoas aidna não atingiram a maioridade e quantas já são maiores
'''
atual = date.today().year
totmaior = 0
totmenor = 0
for pessoa in range(1,8):
    nasc = int(input("Em que ano {}º pessoa nasceu? ".format(pessoa)))
    idade = atual - nasc
    if idade >= 21:
        totmaior += 1
    else:
        totmenor += 1
print("Ao todo houve {} pessoas maiores de idade!".format(totmaior))
print("E também houve {} pessoas menores de idade!".format(totmenor))
