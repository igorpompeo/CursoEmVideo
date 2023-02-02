largura = float(input('Digite a largura em metros: '))
altura = float(input('Digite a altura em metros: '))
metros = largura*altura
tinta = metros / 2
print('A área quadrada que você tem é de {:.1f}x{:.1f} m²!'.format(largura,altura))
print('Para pintar você vai precisar de {:.1f}l para pintar {:.1f}m²'.format(tinta,metros))