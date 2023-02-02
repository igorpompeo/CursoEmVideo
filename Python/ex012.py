prod = float(input('Qual o valor do produto em R$? '))
disconto = prod - (prod * 5 / 100)
print('O produto é no valor de R$ {:.2f} e com o desconto de 5% saí R$ {:.2f}'.format(prod, disconto))
