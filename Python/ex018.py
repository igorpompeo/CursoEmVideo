from math import radians, sin, cos, tan
#exercício de seno, cosseno e tangente
ang = float(input('Digite o ângulo que você deseja: '))
seno = sin(radians(ang))
print('O ângulo de {} tem o SENO de {:.2f}'.format(ang, seno))
cos = cos(radians(ang))
print('O ângulo de {} tem o COSSENO de {:.2f}'.format(ang, cos))
tan = tan(radians(ang))
print('O ângulo de {} tem a TANGENTE de {:.2f}'.format(ang, tan))