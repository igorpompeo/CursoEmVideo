'''
Melhore o EXERCÍCIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos.
O programa encerra quando ele disser que quer mostrar 0 TERMOS
'''
print('*!Gerando PA!*')
print('*-*-*-*'*10)
primeiro = int(input("Digite um valor para calculo de PA: "))
razao = int(input("Digite o valor da razao: "))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while cont <= total:
        print('{} → '.format(termo), end='')
        termo += razao
        cont += 1
    print("\033[1;33mPAUSA\033[m")
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print('Progressão finalizada com \033[1;33m{}\033[m termos mostrados.'.format(total))
print("\033[1;33mACABOU!\033[m")
