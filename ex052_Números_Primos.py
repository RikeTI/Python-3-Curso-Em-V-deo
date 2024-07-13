"""
Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
"""
cont = 0
n = int(input('Informe um número: '))
for c in range(1, n+1):
    if n % c == 0:
        cont +=1
        print('\033[1;31m{}\033[m'.format(c), end=' ')
    else:
        print('\033[33m{}\033[m'.format(c), end=' ')
print()
if cont == 2:
    print('\033[1;32m{}\033[m é Número Primo'.format(n))
else:
    print('\033[1;34m{}\033[m não é Número Primo'.format(n))
