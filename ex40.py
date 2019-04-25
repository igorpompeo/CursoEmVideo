# coding=utf-8
'''
crie um programa que leia duas notas de um aluno e calcule sua média, mostrando
uma mensagem no final, de acordo com a média atingida:
média abaixo de 5.0 - reprovado
média entre 5.0 e 6.9 recuperação
média 7.0 ou superior aprovado
'''
nota1 = float(input('Digite sua primeira nota: '))
nota2 = float(input('Digite sua segunda nota: '))
media = (nota1 + nota2)/2
print('Tirado {:.1f} e {:.1f}, a média do aluno é {:.1f}'.format(nota1, nota2, media))
if media < 5:
    print('REPROVADO!')
elif 7 > media >= 5:
    print('RECUPERAÇÃO!')
else:
    print('APROVADO')