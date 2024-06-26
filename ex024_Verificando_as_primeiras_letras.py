"""
Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome 'SANTO'.
"""
cidade = str(input('Informe o nome de uma cidade: ')).strip().upper().split()
#print(cidade)
print('SANTO' in cidade[0])
print('SANTO' == cidade[0])
cidade = ' '.join(cidade)
#print(cidade)
print(cidade[:5] == 'SANTO')
#Todas as opções acima cumprem o pedido

