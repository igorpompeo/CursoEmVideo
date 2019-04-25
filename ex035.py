# analisando triângulo
cores = {'limpa':'\033[m' ,
         'verde':'\033[1;34m'}
print('-='*20)
print('Analisando triângulos')
print('-='*20)
r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima {}PODEM FORMAR{} um triângulo!'.format(cores['verde'],cores ['limpa']))
else:
    print('Os segmentos acima {}NÃO PODEM FORMAR{} um triângulo!'.format(cores['verde'],cores ['limpa']))
