sal = float(input('Qual é o salário do funcionário? R$ '))
x = sal + (sal * 15 / 100)
print('O funcionário ganhava {:.2f}, com 15% de aumento irá receber R$ {:.2f}'.format(sal, x))
