# coding=utf-8
'''
faça um programa que calcule a soma entre todos os números impares
que são múltiplos de três e que se encontram no intervalo de 1 até 500
'''
soma = 0
cont = 0
for i in range (1, 501, 2):
    if i % 3 == 0:
        soma = soma + i
        cont = cont + 1
print('Entre todos os número temos {} e a soma é {}'.format(cont,soma))
