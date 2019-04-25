#conversor de moedas
real = float(input('Quanto de dinheiro você tem na carteira? R$ '))
dolar = real / 3.31
euro = real / 3.77
print("Com R$ {:.2f} você pode comprar US$ {:.2f}".format(real,dolar))
print("Com R$ {:.2f} você pode comprar EU$ {:.2f}".format(real,euro))
