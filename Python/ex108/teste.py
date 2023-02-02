from ex108 import moeda

p = float(input('Digite o preço: R$'))
print(f'A metade do {moeda.moeda(p)} é {moeda.metade(p)}')
print(f'O dobro de {moeda.moeda(p)} é {moeda.dobro(p)}')
print(f'Aumentando 10%, temos {moeda.aumentar(p, 10)}')
print(f'Reduzindo 30%, temos {moeda.diminuir(p, 30)}')
