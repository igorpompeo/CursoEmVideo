numero = [[], []]
valor = 0
print('*-*'*30)
for c in range(1, 8):
    valor = int(input('Digite um número: '))
    if valor % 2 == 0:
        numero[0].append(valor)
    elif valor % 2 == 1:
        numero[1].append(valor)
print('*-*'*30)
numero[0].sort()
numero[1].sort()
print(f'Os valores pares digitados foram: {numero[0]}')
print(f'Os valores ímpares digitados foram: {numero[1]}')
print('*-*'*30)
print('Fim do programa')
