"""
Crie um programa que leia um número real qualquer pelo teclado e mostre na tela a sua porção inteira
Ex.: 6.127 => 6
"""
import math
num = float(input('Digite um valor: '))
print('O valor digitado foi {} e a sua porção inteira é {}'.format(num, math.trunc(num)))


'''#Realização do exercício sem importação
num = float(input('Digite um valor: '))
print('O valor digitado foi {} e a sua porção inteira é {}'.format(num, int(num)))'''