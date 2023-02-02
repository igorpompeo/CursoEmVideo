# coding=utf-8
'''
desenvolva um programa que leia sei números inteiros e mostre a soma apenas
daqueles que forem pares. se o valor digitado for impar desconsidere-o
'''
soma = 0
cont = 0
for c in range(1, 7):
    num = int(input('Digite o {}º valor: '.format(c)))
    if num % 2 == 0:
        soma += num
        cont += 1
print("Você informou {} número(s) PARE(S) e a soma foi {}".format(cont, soma))
