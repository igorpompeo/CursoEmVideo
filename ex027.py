#primeiro e último nome de uma pessoa
nome = str(input('Digite seu nome todo: ')).strip()
n = nome.split()
print('Seu primeiro nome é {}'.format(n[0]))
print('Seu último nome é {}'.format(n[len(n)-1]))
