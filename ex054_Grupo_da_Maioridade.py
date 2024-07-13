"""
Crie um programa que leia o ano de nascimento de 7 pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
"""
import datetime
anoAtual = datetime.date.today().year
maior = menor = 0
for c in range(1, 8):
    ano = int(input('Informe o ano de nascimento: '))
    if anoAtual - ano < 18:
        menor += 1
    else:
        maior += 1
print('{} pessoas são maior idade!'.format(maior))
print('{} pessoas são menor idade'.format(menor))


'''    idade = anoAtual - ano
    if idade < 18:
        print('{} anos.'.format(idade))
        print('Menor de idade!')
    else:
        print('{} anos'.format(idade))
        print('Maior de idade!')'''