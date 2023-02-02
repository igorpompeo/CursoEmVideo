'''ex - 66
crie um programa que leia varios numeros inteiros pelo teclado. 
O programa so vai parar quando o usuario digitar o valor 999, que e a condicao de parada. 
No final, mostre quantos numeros foram digitados e qual foi a soma entre eles (desconsiderando a flag).
'''
n = contador = soma = 0
while True:    
	n = int(input('Digite os números por favor: [999 para parar]'))
    if n == 999:
		  break
	contador += 1
  soma += n
print(f'Você digitou \033[4;31m{contador}\033[m')
print(f'A soma dos números é: \033[4;35;41m{soma}\033[m')
