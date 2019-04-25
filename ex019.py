from random import choice
#sorteando um item na lista
n1 = str(input('Primeiro aluno: '))
n2 = str(input('Segundo aluno: '))
n3 = str(input('Terceiro aluno: '))
n4 = str(input('Quarto aluno: '))
lista = [n1, n2, n3, n4]#lista em python é sempre entre conchetes os valores da mesma
escolhido = choice(lista)
print('O aluno escolhido foi: {}'.format(escolhido))
