'''
desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. no final
do programa, mostre: a média de idade do grupo
qual é o nome do homem mais velho
quantas mulheres têm menos de 20 anos
'''
agemedia = 0
sumage = 0
majorageman = 0
eldername = ''
totwoman20 = 0
for person in range (1, 5):
    print('------- {}ª PESSOA ------'.format(person))
    sex = chr(input("Digite seu sexo [M/F] : ")).strip()
    name = str(input("Digite seu nome: ")).strip()
    age = int(input("Digite sua idade: "))
    sumage += age
    if person == 1 and sex in 'Mm':
        majorageman = age
        eldername = name
    if sex in 'Mm' and age > majorageman:
        majorageman = age
        eldername = name
    if sex in 'Ff' and age < 20:
        totwoman20 += 1
agemedia = sumage / 4
print('A media de idade do grupo é de {} anos'.format(agemedia))
print('O homem mais velho tem {} anos e se chama {}.'.format(majorageman, eldername))
print('Ao todo são {} mulheres com menso de 20 anos'.format(totwoman20))
