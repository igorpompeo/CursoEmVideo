times = ('Flamengo', 'Fluminense', 'Atlético', 'São Paulo',
         'Grêmio', 'Corinthians', 'Palmeiras', 'Internacional',
         'Sport Recife', 'Cruzeiro', 'América-MG', 'Botafogo',
         'Vasco da Game', 'EC Vitória', 'Bahia', 'Santos',
         'Atlético-PR', 'Chapecoense', 'Ceará SC', 'Paraná')
print('-=' * 15)
print(f'Lista de times: {times}')
print('-=' * 15)
print(f'Os 5 primeiros são {times[0:5]}')
print('-=' * 15)
print(f'Os 4 últimos são {times[-4:]}')
print('-=' * 15)
print(f'Times em ordem alfabética: {sorted(times)}')
print('-=' * 15)
print(f'E o clube Chapeconese está na {times.index("Chapecoense")+1} posição!')
