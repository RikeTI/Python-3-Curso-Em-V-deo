"""
Faça um programa que leia o ano de nascimento de um jovem e informe de acordo com sua idade:
*Se ele ainda vai se alistar ao serviço militar.
*Se é a hora de se alistar.
*Se já passou do tempo do alistamento.

Seu programa tambem deve mostrar o tempo que falta ou que passou do prazo.
"""

import datetime
#print(datetime.date.today().year)#Ano atual
anoAtual = datetime.date.today().year
ano = int(input('Digite o ano de nascimento: '))
idade = anoAtual - ano
if idade < 18:
    print('Você têm {} ano(s) de idade. Ainda resta(m) {} ano(s) para se alistar.'.format(idade, 18 - idade))
    print('Você irá se alistar em {}.'.format(anoAtual + (18 - idade)))

elif idade == 18:
    print('Você têm 18 anos. É tempo de se alistar.')
else:
    print('Você têm {} anos. Seu alistamento ocorreu há {} ano(s).'.format(idade, idade - 18))

