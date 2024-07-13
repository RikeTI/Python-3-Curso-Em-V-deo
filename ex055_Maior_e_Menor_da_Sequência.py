"""
Faça um programa que leia o peso de 5 pessoas. No final, mostre qual foi o maior e o menor peso lidos.
"""
peso = float(input('Informe o peso da 1ª pessoa: '))
maior = menor = peso
'''print('='*10)
print('Peso: {}\nMaior: {}\nMenor: {}'.format(peso, maior, menor))
print('='*10)'''
for p in range(2, 6):
    peso = float(input('Informe o peso da {}ª pessoa: '.format(p)))
    if peso > maior:
        maior = peso
    if peso < menor:
        menor = peso
print('O maior peso lido foi {:.2f}'.format(maior))
print('O menor peso lido foi {:.2f}'.format(menor))

"""
#LÓGICA DE PROGRAMAÇÃO
peso = 5
maior = 5
menor = 5

*1º laço: peso = 6
if peso > maior:    se 6 > 5:
    maior = 6
if peso < menor:    se 6 < 5:
x
*2º laço: peso = 3
if peso > maior:    se 3 > 6:
if peso < menor:    se 3 < 5:
    menor = 3
x
*3º laço: peso = 10
if peso > maior:    se 10 > 6
    maior = 10
if peso < menor:    se 10 < 3


peso = 10
maior = 10
menor = 3

"""



