'''
crie um programa que leia uma frase qualquer e diga se ela é um palindromo,
desconsiderando os espaços
'''
frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = junto[::-1]
print("O inverso de {} é {}".format(junto, inverso))
if inverso == junto:
    print("É um palíndromo")
else:
    print("Não é um palíndromo")
'''
inverso = ''
for letra in range(len(junto) -1 , -1, -1)
inverso += junto[letra]
'''