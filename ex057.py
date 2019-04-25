'''
faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'.
Caso esteja errado, peça a digitação novamente até ter um valor correto.
'''
sexo = input('Digite o seu sexo: ').upper()
while sexo not in 'MF':
    sexo = input('Digite um valor aceitável [M/F]! Digite seu sexo novamente: ').strip().upper()
print('Obrigado pela informação! Seu sexo é {}!'.format(sexo))
