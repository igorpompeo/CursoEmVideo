# coding=utf-8
'''
desenvolva um programa que leia o primeiro termo e a razão de uma PA. no final
mostre os 10 primeiros termos dessa progressão.
'''
num = int(input("digite um valor para calculo de PA: "))
razao = int(input("digite o valor da razao: "))
decimo = num + (10 - 1) * razao
for c in range(num, decimo + razao, razao):
    print('{} '.format(c), end='-> ')
print('ACABOU')
