'''
Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros
elementos de uma Sequência de Fibonacci.
Ex: 0 -> 1 -> 1 -> 2 -> 3 -> 5 -> 8
'''
print('-'*30)
print('Fibonacci')
print('-'*30)
n = int(input('Quantos termos você quer mostrar? '))
t1 = 0
t2 = 0
print('='*30)
print('{} - {}'.format(t1, t2), end = '')
cont = 3
while cont <= n:
    t3 = t1 + t2
    print(' - {}'.format(t3), end = '')
    t1 = t2
    t2 = t3
    cont += 1
'''def fib(n):
    a, b = 0, 1
    print(a)
    while (b < n):
        a, b = b, a + b
        print(a)
fib(10)'''