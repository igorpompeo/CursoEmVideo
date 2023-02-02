#jogo da adivinhação v.1.0
import random
from time import sleep
print('-=-' * 20)
n = int(input('Estou pensando em um número de 0 a 5, tente adivinhar! '))
print('PROCESSANDO...')
sleep(2)
print('-=-' * 20)
pc = random.randint(0, 5)
if n == pc:
    print('Você acertou, meus parabéns!')
else:
    print('Você não conseguiu, perdeu!')
print('---------------------FIM DE JOGO-----------------------')
