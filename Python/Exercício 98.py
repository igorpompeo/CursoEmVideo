def contador(ini, fim, passo):
    if passo == 1:
        print(f'{ini} \t')
        while ini != fim:
            print(ini + passo)
            ini += 1
    elif passo == 2:
        print(f'{ini} \t')
        while ini != fim:
            print(ini - passo)
            ini -= 2
    else:
        print(f'{ini} \t')
        while ini != fim:
            print(ini + passo)
            ini += 1
    print('=-=' * 20)

print('=-=' * 20)
inicio = int(input('Digite os seguintes valores: [1], [10] ou até [99999]. '))
fim = int(input('Digite os seguintes valores: [10], [0] ou até [999999]. '))
passo = int(input('Digite os seguintes valores: [1], [2] ou até [99999]. '))
contador(inicio, fim, passo)

from time import sleep

def contador(i, f, p):
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    print('-=' * 15)
    print(f'Contagem de {i} até {f} de {p} em {p}')
    sleep(2.5)


    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont} ', end='', flush=True)
            sleep(0.5)
            cont += p
        print('FIM')
    else:
        cont = i
        while cont >= f:
            print(f'{cont} ', end='', flush=True)
            sleep(0.5)
            cont -= p
        print('FIM')

contador(1, 10, 1)
contador(10, 0, 2)
print('Agora é a sua vez de personalizar a contagem:')
ini = int(input('Inicio: '))
fim = int(input('Fim: '))
pas = int(input('Passo: '))
contador(ini, fim, pas)