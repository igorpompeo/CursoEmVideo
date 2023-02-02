'''
Crie um programa que leia dois valores e mostre um menu na tela:
[1] somar; [2] multiplicar; [3]maior;[4] novos números e [5]sair do programa
Seu programa deverá realizar a operação solicitada em cada caso.
'''
n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
op = int
print('-=-'*20)
while op != 5:
    op = int(input('''Digite sua opção:
    [ 1 ] somar; 
    [ 2 ] multiplicar; 
    [ 3 ] maior; 
    [ 4 ] novos números 
    [ 5 ] sair '''))
    if op == 1:
        soma = int(n1+n2)
        print('A soma é: {}'.format(soma))
    elif op == 2:
        mult = int(n1*n2)
        print('A multiplicação é: {}'.format(mult))
    elif op == 3:
        if n1 > n2:
            maior = int(n1)
            print('O número maior é: {}'.format(maior))
        else:
            print('O número maior é: {}'.format(n2))
    elif op == 4:
        print('Opção de novos valores, favor informar:')
        n1 = int(input('Digite um novo primeiro valor: '))
        n2 = int(input('Digite um novo segundo valor: '))
print('-=-'*20)
