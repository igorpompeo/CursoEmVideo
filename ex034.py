# aumentos múltiplos
salário = float(input('Qual é o seu salário? R$'))
if salário <= 1250:
    novo = salário + (salário * 15 / 100)
else:
    novo = salário + (salário * 10 / 100)
print('Antigo salário era R$ {:.2f} agora recebe R$ {:.2f} agora.'.format(salário, novo))