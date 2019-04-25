#Analisador de Textos
nome = str(input('Digite seu nome completo: ')).strip()
print('Seu nome em maiusculo é {}: '.format(nome.upper()))
print('Seu nome em minusculo é {}: '.format(nome.lower()))
print('Seu nome contém {} letras: '.format(len(nome)-nome.count(' ')))
#print('Seu primeiro nome contém {} letras'.format(nome.find(' ')))
separa = nome.split()
print('Seu primeiro nome contém {} letras'.format(separa[0]), len(separa[0]))