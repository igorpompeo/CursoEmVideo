#Procurando uma string dentro de outra
nome = str(input('Qual o seu nome? ')).strip()
print('Seu nome tem Silva? {}'.format('SILVA' in nome.upper()))