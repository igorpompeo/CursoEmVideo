'''
Reescreva a função leiaInt() que fizemos no desafio 104, incluindo agoa a possibilidade da digitação de um número
de tipo inválido. Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.
Se o usuário não digitar o valor (CTRL+C), o retorno deverá ser o número 0 para ambas funções.
'''
def leiaInt(msg):
    '''
    Função que válida se o dado informado é um número inteiro
    :param msg: dado informado pelo usuário
    :return: dado que foi digitado
    '''
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[0;31mERRO! Digite um número inteiro válido. \033[m')
            continue
        except (KeyboardInterrupt):
            print('\n\033[31mUsuário preferiu não digitar esse número.\033[m')
            return 0
        else:
            return n

def leiaFloat(msg):
    '''
    Função que válida se o dado informado é um número real
    :param msg: dado informado pelo usuário
    :return: dado que foi digitado
    '''
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print('\033[0;31mERRO! Digite um número inteiro válido. \033[m')
            continue
        except (KeyboardInterrupt):
            print('\n\033[31mUsuário preferiu não digitar esse número.\033[m')
            return 0
        else:
            return n


n1 = leiaInt('Digite um Inteiro: ')
n2 = leiaFloat('Digite um Real: ')
print(f'O valor inteiro digitado foi {n1} e o real foi {n2}')
