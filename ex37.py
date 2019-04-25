# coding=utf-8
'''
escreva um programa que leia um número inteiro qualquer e peça para o usuário
escolher qual será a base de conversão:
1 - binário; 2 - octal; 3 - hexadecimal;
'''
Ndecimal = int(input('Digite um número inteiro: '))
op1 = int(input('Iremos fazer a conversão para você, se desejar binário digite 1, se for octal digite 2, '
                'e se for hexadecimal digite 3!'))
if op1 == 1:
    Nbin = bin(Ndecimal)
    print('O valor que você digitou, em binário é assim: {}'.format(Nbin[2:]))
elif op1 == 2:
    Noct = oct(Ndecimal)
    print('O valor que você digitou, em octal é assim: {}'.format(Noct[2:]))
elif op1 == 3:
    Nhex = hex(Ndecimal)
    print('O valor que você digitou, em hexadecimal é assim: {}'.format(Nhex[2:]))
else:
    print('Digitou uma opção inválida!')