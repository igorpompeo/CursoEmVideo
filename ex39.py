# coding=utf-8
from datetime import date
'''
faça um programa que leia o ano de nascimento de um jovem e informe, de acordo
com sua idade:
se ele ainda vai se alistar ao serviço militar; Se é a hora de se alistar;
Se já passou do tempo do alistamento.
Seu programa também deverá mostrar o tempo que faltou ou que passsou do prazo.
'''
atual = date.today().year
nasc = int(input('Ano de nascimento: '))
idade = atual - nasc
print('Quem nasceu em {} tem {} anos em {}.'.format(nasc, idade, atual))
if idade == 18:
    print('Você tem que se alistar IMEDIATAMENTE!')
elif idade < 18:
    saldo = 18 - idade
    print('Você ainda não tem 18 anos, ainda faltam {} anos para o alistamento'.format(saldo))
    ano = atual + saldo
    print('Seu alistamento será em {}'.format(ano))
else:
    saldo = idade - 18
    print('Você já deveria ter se alistado há {} ano(s)'.format(saldo))
    ano = atual - saldo
    print('Seu alistamento foi em {}'.format(ano))
