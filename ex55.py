'''
faça um programa que leia o peso de cinco pessoas. no final, mostre qual foi
o maior e o menor peso lidos
'''
biggest = 0
lower = 0
for person in range(1, 6):
    weight = float(input("Digite o seu peso da {}ª pessoa: ".format(person)))
    if person == 1:
        biggest = weight
        lower = weight
    else:
        if weight > biggest:
            biggest = weight
        if weight < lower:
            lower = weight
print("O maior peso lido foi de {} KG!".format(biggest))
print("O menor peso lido foi de {} KG".format(lower))
