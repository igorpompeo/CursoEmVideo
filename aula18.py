# primeiro modo de declaração;
teste = list()
teste.append('Igor')
teste.append(28)
galera = list()
galera.append(teste[:])
teste[0] = 'Pompeo'
teste[1] = 28
galera.append(teste[:])
print('Impressão de todos os elementos da lista!')
print(galera)
# segundo modo de declaração;
galera2 = [['Igor', 28], ['Pompeo', 28], ['Tavares', 28], ['Souza', 28]]
print(galera2[2][1])
for p in galera2:
    # todos
    print('Todos de uma vez!')
    print(p)
    # todos os nomes
    print('Todos os nomes!')
    print(p[0])
    # todas as idades
    print('Todas as idades!')
    print(p[1])
    # formatado
    print('Todos os elementos formatados!')
    print(f'{p[0]} tem {p[1]} anos de idade!')
# criação de lista e um for para incluir valores nelas
galera3 = list()
dado = list()
totmai = totmen = 0
for c in range(0, 2):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera3.append(dado[:])
    dado.clear()
print(galera3)

# também posso colocar validação
for p in galera3:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade.')
        totmai += 1
    else:
        print(f'{p[0]} é menor de idade!')
        totmen += 1
print(f'Temos {totmai} maiores e {totmen} menores de idade.')
