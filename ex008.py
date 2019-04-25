medida = float(input('Distancia em metros: '))
km = medida / 1000
hm = medida / 100
dam = medida / 10
m = medida * 1
dm = medida * 10
cm = medida * 100
mm = medida * 1000
print('A medida de {}m corresponde a {}cm e a {}mm'.format(medida,cm,mm))
print('{}km'.format(km))
print('{}hm'.format(hm))
print('{}dam'.format(dam))
print('{}m'.format(m))
print('{:.0f}dm'.format(dm))
print('{:.0f}cm'.format(cm))
print('{:.0f}mm'.format(mm))

