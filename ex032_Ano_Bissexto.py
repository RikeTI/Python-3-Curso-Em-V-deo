"""
Faça um programa que leia um ano qualquer e mostre se ele é bissexto.
"""
from datetime import date
ano = int(input('Informe um ano qualquer para verificação: [Digite 0 para pegar o ano atual] '))
#print('Bissexto' if ano % 4 == 0 else 'Não é bissexto')
#Ano Bissexto: ocorre a cada 4 anos, exceto os anos que são múltiplos 100, mas não são múltiplos de 400.
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} é BISSEXTO'.format(ano))
else:
    print('O ano {} não é BISSEXTO'.format(ano))

