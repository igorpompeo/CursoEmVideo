from ex107 import moeda

v = float(input('Digite um preço: R$ '))
print(f'A metade de {v} é {moeda.metade(v)}')
print(f'O dobro de {v} é {moeda.dobro(v)}')
print(f'Aumentado 10%, temos {moeda.aumentar(v, 10)}')
print(f'Reduzindo 10%, temos {moeda.reduzir(v, 10)}')
