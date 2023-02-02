# coding=utf-8
from datetime import datetime
'''
a confederação nacional de natação precisa de um programa que leia o ano de
nascimento de um atleta e mostre a categoria, de acordo com a idade:
até 9 anos> Mirim; 14 anos> infantil; 19anos> junior; 20 anos> sênior; acima>master
'''
hoje = datetime.now()
ano_sistema = hoje.year
ano = int(input('Digite seu ano de nascimento: '))
aux = ano_sistema - ano
print('O atleta tem {} anos.'.format(aux))
if aux <= 9:
    print('Sua categoria é MIRIM!')
elif aux <= 14:
    print('Sua categoria é INFANTIL!')
elif aux <= 19:
    print('Sua categoria é JUNIOR!')
elif aux <= 25:
    print('Sua categoria é SÊNIOR!')
else:
    print('Sua categoria é MASTER!')
