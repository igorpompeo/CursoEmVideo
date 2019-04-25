'''ex-70
crie um programa que leia o nome e o preso de varios produtos. 
O programa devera perguntar se o usuario vai continuar. No final, mostre:
a) qual e o total gasto na compra?
b) quantos produtos custam mais de R$ 1000?
c) qual e o nome do produto mais barato?'''

total = totmil = menor = cont = 0
barato = ' '
while True:
    produto = str(input('Nome do produto: '))
    preço = float(input('Preço: R$'))
    cont += 1
    total += preço
    if preço > 1000:
        totmil += 1
    if cont == 1 or preço < menor:
        menor = preço
        barato = produto
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print('{:-^40}'.format('FIM DO PROGRAMA!'))
print(f'O total da compra foi R${total:.2f}')
print(f'Temos {totmil} produtos custando mais de R$ 1000')
print(f'O produto mais barato for {barato} custa R${menor:.2f}')
