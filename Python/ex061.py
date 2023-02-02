'''
Refaça o EXERCÍCIO 51, lendo o primeiro termo e a razão de uma PA, mostrando os 10
primeiros termos da progressão usando a estrutura while.
'''
print('*!Gerando PA!*')
print('-*-*-'*10)
primeiro = int(input("Digite um valor para calculo de PA: "))
razao = int(input("Digite o valor da razao: "))
termo = primeiro
cont = 1
while cont <= 10:
    print('{} → '.format(termo), end='')
    termo += razao
    cont += 1
print("\033[1;33mACABOU\033[m")
