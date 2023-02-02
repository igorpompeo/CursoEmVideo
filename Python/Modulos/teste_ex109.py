from ex109 import moeda

v = float(input('Digite o preço: R$ '))
print(f'A metade de {moeda.formatar(v)} é {moeda.metade(v, False)}')
print(f'O dobro de {moeda.formatar(v)} é {moeda.dobro(v, True)}')
print(f'Aumentando 10%, temos {moeda.aumentar(v, 10, True)}')
print(f'Reduzindo 13%, temos {moeda.reduzir(v, 13, True)}')
