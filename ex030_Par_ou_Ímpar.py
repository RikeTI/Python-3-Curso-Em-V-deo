"""
Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.
"""
n = int(input('Digite um número inteiro qualquer: '))
if n % 2 == 0:
    print('{} é par'.format(n))
else:
    print('{} é ímpar'.format(n))

