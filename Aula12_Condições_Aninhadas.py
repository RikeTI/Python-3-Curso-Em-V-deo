nome = str(input('Qual é seu nome? ')).title()
if nome == 'Rike':
    print('Que nome bonito!')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo':
    print('Seu nome é bem popular no Brasil.')
elif nome in 'Ana Mavis Luisa July':
    print('Belo nome feminino')
print('Tenha um bom dia, {}!'.format(nome))







