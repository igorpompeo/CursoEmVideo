# explicação
pessoas = {'nome': 'Igor', 'sexo': 'M', 'idade': 27}
print(pessoas)
print(pessoas['nome'])
print(pessoas['idade'])
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos.')
# precisa por dentro de aspas duplas por estar com aspas simples o dicionário
print(pessoas.keys())
# impressão das chaves do dicionário
print(pessoas.values())
# impressão dos valores
print(pessoas.items())
# impressão dos valores (chave e valores)
for k in pessoas.keys():
    print(k)
for k in pessoas.values():
    print(k)
for k, v in pessoas.items():
    print(f'{k} = {v}')
del pessoas['sexo']
# para deletar
pessoas['nome'] = 'Pompeo'
pessoas['peso'] = 88

# exemplo 1
brasil = []
estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}
brasil.append(estado1)
brasil.append(estado2)

print(brasil[0])
print(brasil[1])
print(brasil[0]['uf'])
print(brasil[1]['uf'])
print(brasil[0]['sigla'])

# exemplo 2
estado = dict()
brasil1 = list()
for c in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado'))
    brasil1.append(estado.copy())
    # isso é feito para ficar igual ao fatiamento de uma lista,
    #  pois senão ele pegará somente o último elemento informado
for e in brasil1:
    for k, v in e.items():
        print(f'O campo {k} tem valor {v}')
