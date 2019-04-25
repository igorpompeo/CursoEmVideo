# coding:  utf-8

# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
# O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos
# ele vai pagar. Calcule o valor da prestação mensal, sabendo que ela não pode
# exceder 30% do salário ou então o empréstimo será negado.

sal = float(input('Digite o seu salário: '))
casa = float(input('Digite o valor da casa que quer comprar: '))
anos = float(input('Digite a quatidade de anos que quer pagar a casa? '))
valor_mensal = casa / anos
emprestimo_analise = sal + (sal * 30/100)
if valor_mensal > emprestimo_analise:
    print('O valor do seu salário não é confiável, o custo das prestações estão muito altos, emprestimo foi negado!')
else:
    print('O seu emprestimo está liberado, esperamos que seja muito feliz com sua casa nova!')