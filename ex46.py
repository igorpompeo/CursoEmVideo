# coding=utf-8
from time import sleep
'''faça um programa que mostre na tala uma contagem regressiva
para o estouro de fogos de artificio, indo de 10 até 0, com uma pausa de
1 segundo entre eles'''
print('Contagem regressiva para os fogos começarem!')
for i in range(10,-1, -1):
    print(i)
    sleep(0.5)
print('Feliz Ano NOVO')
print('POW! POW! BOOOM!')