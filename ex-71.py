'''ex-71
crie um programa que simule o funcionamento de um caixa eletronico. 
no inicio, pergunte ao usuario qual sera o valor a ser sacado (numero inteiro) e o programa vai infomrar 
quantas cedulas de cada valor serão entregues.
Obs> considere que o caixa possui cedulas de R$ 50, R$ 20, R$ 10 e R$ 1'''

print('=' * 30)
print('{:30}'.format('BANCO POMPEO'))
print('=' * 30)
valor = int(input('Que valor você quer sacar? R$'))
total = valor
céd = 100
totcéd = 0
while True:
    if total >= céd:
        total -= céd
        totcéd += 1
    else:
        if totcéd > 0:
            print(f'Total de {totcéd} cédulas de R${céd}')
        if céd == 100:
            céd = 50
        elif céd == 50:
            céd = 20
        elif céd == 20:
            céd = 10
        elif céd == 10:
            céd = 5
        elif céd == 5:
            céd = 1
        totcéd = 0
        if total == 0:
            break
print('=' * 30)
print('Volte sempre ao BANCO POMPEO, tenha um bom dia!')
