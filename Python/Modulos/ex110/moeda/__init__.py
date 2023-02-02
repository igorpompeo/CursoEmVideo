def aumentar(v, n, h):
    '''
    -> Calcula o aumento de um determinado preço,
    retornando o resultado com ou sem formatação.
    :param preço: o preço que se quer reajustar;
    :param taxa: qual é a porcentagem do aumento;
    :param formato: quer a saída formatada ou não?
    :return: o valor reajustado, com ou sem formato
    '''
    b = True
    if h != True:
        b = h
    if b == True:
        a = format((v + (v * (n / 100)) * 1), '.2f')
        return 'R$ ' + a
    a = (v + (v * (n / 100)) * 1)
    return a

def dobro(v, h):
    b = True
    if h != True:
        b = h
    if b == True:
        d = format((v * 2), '.2f')
        return 'R$ ' + d
    d = v * 2
    return d

def formatar(v):
    b = True
    if b == True:
        f = format(v, '.2f')
        return 'R$ ' + f
    f = v
    return f

def metade(v, h):
    b = True
    if h != True:
        b = h
    if b == True:
        m = format((v / 2), '.2f')
        return 'R$ ' + m
    m = v / 2
    return m

def reduzir(v, n, h):
    b = True
    if h == True:
        r = format((v - (v * (n / 100)) * 1), '.2f')
        return 'R$ ' + r
    else:
        r = (v - (v * (n / 100)) * 1)
        return r

def resumo(preço=0, taxaa=10, taxar=5):
    print('-' * 30)
    print('RESUMO DO VALOR'.center(30))
    print('-' * 30)
    print(f'Preço analisado: {moeda(preço)}')