'''
Crie um programa que leia vários números inteiros pelo teclado.
O programa só vai para quando o usuário digitar o valor 999, que é a condição de parada.
No final mostre quantos números foram digitados e qual foi a soma entre eles.
(desconsiderando o flag (999))
'''
n = contador = soma = 0
n = int(input('Digite os números por favor: [999 para parar]'))
while n != 999:    
    contador += 1
    soma += n
    n = int(input('Digite os números por favor: [999 para parar]'))
print('Você digitou \033[4;31m{}\033[m'.format(contador))
print('A soma dos números é: \033[4;35;41m{}\033[m'.format(soma))
