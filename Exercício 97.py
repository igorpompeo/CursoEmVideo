def escreva(texto):
    t = texto.__len__() + 4
    print("<" * (t + 1))
    print(f'  {texto}')
    print(">" * (t + 1))

print("Digite qualquer coisa:")
print("-*" * 15)
t = str(input("Digite aqui: "))
escreva(t)
