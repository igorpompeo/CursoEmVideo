def aumentar(preço=0, taxa=0, formato=False):

    '''
    -> Calcula o aumento de um determinado preço,
    retornando o resultado com ou sem formatação.
    :param preço: o preço que se quer reajustar
    :param taxa: qual é a porcentagem do aumento
    :param formato: quer a saída formatada ou não?
    :return: o valor reajustado, com ou sem formato
    '''

    res = preço + (preço * taxa/100)
    return res if formato is False else moeda(res)


def diminuir(preço=0, taxa=0, formato=False):

    '''
    -> Calcula a redução de um determinado preço,
    retornando o resultado com ou sem formatação
    :param preço: o preço que se quer reajustar
    :param taxa: qual é a porcentagem da redução
    :param formato: quer a saída formatada ou não?
    :return: o valor reajustado, com ou sem formato
    '''

    res = preço - (preço * taxa/100)
    return res if formato is False else moeda(res)


def dobro(preço=0, formato=False):

    '''
    -> Calcula o dobro de um determinado preço,
    retornando o resultado com ou sem formataçào.
    :param preço: o preço que se quer reajustar
    :param formato: quer a saída formatada ou não?
    :return: o valor reajustado, com ou sem formato
    '''

    res = preço * 2
    return res if formato is False else moeda(res)


def metade(preço=0, formato=False):

    '''
    -> Calcula a metada de um determinado preço,
    retornando o resultado com ou sem formatação.
    :param preço: o preço que se quer reajustar
    :param formato: quer a saída formatada ou não?
    :return: o valor reajustado, com ou sem formato
    '''

    res = preço / 2
    return res if formato is False else moeda(res)


def moeda(preço=0, moeda='R$'):

    '''
    -> Formatação de moeda
    :param preço: o preço que se quer reajustar
    :param moeda: a moeda que se quer formatar
    :return: o valor reajustado, com ou sem formato
    '''

    return f'{moeda}{preço:>.2f}'.replace('.', ',')

def resumo(preço=0, taxaa=10, taxar=5):

    '''
    -> Resumo de funções
    :param preço: o preço que se quer reajustar
    :param taxaa: a taxa de aumento
    :param taxar: a taxa de redução
    :return: o valor reajustado, com ou sem formato
    '''

    print('-' * 30)
    print('RESUMO DO VALOR'.center(30))
    print('-' * 30)
    print(f'Preço analisado: \t{moeda(preço)}')
    print(f'Dobro do preço: \t{dobro(preço, True)}')
    print(f'Metado do preço: \t{metade(preço, True)}')
    print(f'{taxaa}% de aumento: \t{aumentar(preço, taxaa, True)}')
    print(f'{taxar}% de redução: \t{diminuir(preço, taxar, True)}')
    print('-' * 30)
