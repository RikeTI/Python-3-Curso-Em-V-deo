"""
Faça um programa que leia um número qualquer e mostre o seu fatorial. Ex.: 5! = 5 x 4 x 3 x 2 x 1 = 120
"""

'''print('>> Fatorial <<')
n = int(input('Informe um número inteiro qualquer: '))
#n = 5
fat = 1
print('{}'.format(n), end=' ')
while n > 1:
    fat = fat * n
    n -= 1
    print('x {}'.format(n, n-1), end=' ')
print('= {}'.format(fat))
'''


#Resolução do Professor com Módulos
'''from math import factorial
n = int(input('Digite um número para calcular seu Fatorial: '))
f = factorial(n)
print('O fatorial de {} é {}'.format(n, f))'''

#Resolução do Professor de modo tradicional
n = int(input('Digite um número para calcular seu Fatorial: '))
c = n
f = 1
print('Calculando {}! = '.format(n), end='')
while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print('{}'.format(f))
