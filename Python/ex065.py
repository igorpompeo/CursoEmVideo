'''
Crie um programa que leia vários números inteiros pelo teclado.
No final da execução, mostre a média entre todas os valores e qual foi o maior e o menor valores lidos.
O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.
'''
aux = cont = 0
n = int(input('Digite um número: '))
opção = str(input('Quer continuar a digitar mais números? [S/N] ')).upper()
while opção != 'N':
    aux = n
    n = input('Digite outro número: ')
    cont += 1
    opção = str(input('Quer continuar a digitar mais números? [S/N] ')).upper()
media = (n + aux) / cont
if n > aux:
    print('O maior número digitado foi: {}'.format(n))
if aux < n:
    print('O menor valor digitado foi: {}'.format(aux))
print('A média dos valor é: {}'.format(media))
