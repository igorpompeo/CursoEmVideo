# coding=utf-8
'''
desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu imc
e mostre seu status, de acordo com a tabela abaixo:
abaixo de 18,5 - abaixo do peso; entre 18,5 a 25 - peso ideal, 25 até 30 - sobrepeso
acima de 40 - obesidade mórbida.
'''
peso = float(input('Qual é seu peso? (Kg) '))
altura = float(input('Qual é a sua altura? (m) '))
imc = peso / (altura ** 2)
print('O IMC dessa pessoa é de {:.1f}'.format(imc))
if imc < 18.5:
    print('Você está ABAIXO DO PESO normal')
elif 18.5 <= imc < 25:
    print('Parabéns, você está na faixa de PESO NORMAL')
elif 25 <= imc < 30:
    print('Você está em SOBREPESO')
elif 30 <= imc <40:
    print('Você está em OBESIDADE, cuidado!')
else:
    print ('Você está em OBESIDADE MÓRBIDA, cuidado!!')
