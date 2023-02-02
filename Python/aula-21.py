def contador(i, f, p):
    """
    -> Faz uma contagem e mostra na tela
    :param i: início da contagem
    :param f: fim da contagem
    :param p: passo da contagem
    :return: sem retorno
    Função criada por Gustavo Guanabara do canal CursoemVideo
    """
    c = i
    while c <= f:
        print(f'{c}', end='..')
        c += p
    print('FIM!')
contador(0, 100, 10)

def somar(a=0, b=0, c=0):
    """
    -> Faz a soma de três valores e mostra o resultado na tela
    :param a: o primeiro valor
    :param b: o segundo valor
    :param c: o terceiro valor
    :return: sem retorno
    """
    s = a + b + c
    return s
resp = somar(3, 4, 19)
print(f'O resultado da soma é: {resp}', end='\n')

# aula prática
def fatorial(n = 1):
    f = 1
    for c in range(n, 0, -1):
        f *= c
    return f

f0 = int(input('Digite um número: '))
f1 = fatorial(5)
f2 = fatorial(4)
f3 = fatorial()
print(f'O fatorial de {fatorial(f0)}, {f1}, {f2}, {f3}')
