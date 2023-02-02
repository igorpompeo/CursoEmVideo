#passagem de viagem
km = int(input('Digite quantos KM será o percurso de sua viagem: '))
p1 = float(0.50)
p2 = float(0.45)
if km <= 200:
    calc = int(200 - km) * p1
    print('O valor da sua passagem é: R$ {:.2f}'.format(calc))
else:
    calc = int(km - 200) * p2
    print('O valor da sua passagem é: R$ {:.2f}'.format(calc))
print('Boa Viagem!')
