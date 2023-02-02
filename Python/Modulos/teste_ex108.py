from ex108 import moeda

v = float(input('Digite um preço: R$ '))
print(f'A metade de {moeda.formatar(v)} é {moeda.formatar(moeda.metade(v))}')
print(f'O dobro de {moeda.formatar(v)} é {moeda.formatar(moeda.dobro(v))}')
print(f'Aumentado 10%, temos {moeda.formatar(moeda.aumentar(v, 10))}')
print(f'Reduzindo 20%, temos {moeda.formatar(moeda.reduzir(v, 20))}')
