from time import sleep
def maior(* núm):
    cont = maior = 0
        print(f'{valor} ', end=''
    print('+=' * 30)
    print('Analisando os valores passados...')
    for valor in núm:, flush=True)
        sleep(0.3)
        if cont == 0:
            miaor = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print(f'Foram informados {cont} valores ao todo.')
    print(f'O maior valor informado foi {maior}.')


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 8)
maior(1, 9)
maior(8)
maior()