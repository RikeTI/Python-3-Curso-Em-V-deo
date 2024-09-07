"""
Desenvolva um progrma que leia o 1º termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.
"""
#>> Resolução do Professor <<
'''
primeiro = int(input('Primeiro termo: '))
razão = int(input('Razão: '))
décimo = primeiro + (10 - 1) * razão
for c in range(primeiro, décimo + razão, razão):
    print('{}'.format(c), end=' -> ')
print('ACABOU')
'''



# a_n: a na posição     ;   a_1: a na posição 1     ;   r: é a razão
# n: é um nº inteiro qualquer que representa a quantidade de termos
# O n-ésimo termo de uma PA é:   >>> a_n = a_1 + (n - 1) * r <<<

print('='*30)
print('{:^30}'.format('>> PROGRESSÃO ARITMÉTICA <<'))
print('='*30)
n = int(input('Número de termos: '))
a1 = int(input('Primeiro termo: '))
r = int(input('Razão: '))
a_n = a1 + (n - 1) * r
for c in range(a1, a_n + r, r):
    print(f'{c}', end=' -> ')
print('FIM')
