#radar
velocidade = int(input('Digite a velocidade do seu carro: '))
multa = 80
if velocidade >= 80:
    print('Você ultrapassou a velocidade, você será multado!')
    calc = (velocidade - multa) * 7
    print('O custo da multa é de R$ {},00 !'.format(calc))
else:
    print('Parabéns você dirige consciente!')
