'''
Melhore o jogo do EXERCÍCIO 28 onde o computador vai 'pensar' em um número entre 0 e 10.
Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites
foram necessários para vencer
'''
from random import randint
computador = randint(0, 10)
print('Olá, sou seu computador, vamos jogar? ')
print('Estou pensando em um número de 0 a 10, será que você consegue adivinhar? ')
acertou = False
palpite = 0
while not acertou:
    jogador = int(input('Qual o seu palpite? '))
    palpite += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais... Tente de novo. ')
        elif jogador > computador:
            print('Menos... Tente de novo. ')
print('Acertou com {} tentativas. \33[32mParabéns!'.format(palpite))
