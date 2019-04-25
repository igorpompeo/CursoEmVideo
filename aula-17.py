# aula sobre listas
print('-'*30)
print('Primeiro exemplo de lista')
print('-'*30)

num = [2,5,9,1]
num[2]=3
num.append(7)
num.sort(reverse = True)
num.insert(2,2)
if 5 in num:
    num.remove(5)
else:
    print('Não achei o número 5')
print(num)
print(f'Essa lista tem {len(num)} elementos')

print('-'*30)
print('Segundo exemplo de lista')
print('-'*30)

# segunda lista
valores = list() # outro metodo de criação de lista
# inserção por meio do teclado

'''for cont in range(0,5):
    valores.append(int(input('Digite um valor: ')))'''

valores.append(5)
valores.append(9)
valores.append(4)

for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}!')
print('Cheguei ao final da lista')

print('-'*30)
print('Terceiro exemplo de lista')
print('-'*30)

a = [2,3,4,7]
b = a # isso é uma ligação entre uma lista e a outra
b = a[:] # isso faz uma cópia dos valores da lista a
b[2] = 8 # alterará nas duas listas
print(f'Lista A: {a}')
print(f'Lista B: {b}')