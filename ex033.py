first = int(input('Primeiro valor: '))
second = int(input('Segundo valor: '))
thirt = int(input('Terceiro valor: '))
# verificando quem é o menor valor
smaller = first
if second < first and second < thirt:
    smaller = second
if thirt < first and thirt < second:
    smaller = thirt
# verificando quem é o maior valor
bigger = first
if second > first and second > thirt:
    bigger = second
if thirt > second and thirt > first:
    bigger = thirt
print('O menor valor digitado foi: {}'.format(smaller))
print('O maior valor digitado foi: {}'.format(bigger))
