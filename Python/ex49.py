# coding=utf-8
from __future__ import print_function
'''
refaça o desafio 09, mostrando a tabuado de um número que o usuário escolher,
só que agora utilizando um laço for
'''
num = int(input('Digite um número para ver a tabuada: '))
for c in range(0,11,):
    print('{} x {:2} = {}'.format(num,c, num*c))