def leiaDinheiro(msg):

    '''
    Função que ajusta os dados inseridos pelo usuário, validando se são números e ajusta a ',' se o usuário
    digitar
    :param msg: Função tipo input que receberá os valores do usuário
    :return: Retorno da função em valor real
    '''

    válido = False
    while not válido:
        entrada = str(input(msg)).replace(',', '.').strip()
        if entrada.isalpha() or entrada == '':
            print(f'\033[0;31mERRO: \"{entrada}\" é um preço inválido!\033[m')
        else:
            válido = True
            return float(entrada)
