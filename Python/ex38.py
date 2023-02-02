# coding=utf-8
'''
Escreva um programa que leia dois números inteiros e compare-os,
mostrando na tela uma mensagem: o primeiro valor é maior, o segundo é maior,
não existe valor maior, os dois são iguais
'''
a = int(input('Digite um valor maior que zero: '))
b = int(input('Digite outro valor maior que zero: '))
if a > b:
    print('O primeiro valor {} é maior que o segundo {} !'.format(a,b))
elif b > a:
    print('O segundo valor {} é maior que o primeiro {} !'.format(b,a))
else:
    print('Não existe valor maior, os dois são iguais.')
