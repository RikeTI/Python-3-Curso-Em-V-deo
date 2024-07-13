"""
Desenvolva um progrma que leia o 1º termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.
"""
#a1 = int(input('Informe o 1º termo da PA: '))
#r = int(input('Informe a razão da PA: '))
'''
a1 + r = a2     ->   a2 + r = a3
a2 - a1 = r
'''
print(a1, end=' -> ')
an = a1
for c in range(1, 10):
    an = an + r #a2
    print(an, end=' -> ')
print('Acabou!')



'''#>> Resolução do Professor <<
primeiro = int(input('Primeiro termo: '))
razão = int(input('Razão: '))
décimo = primeiro + (10 - 1) * razão
for c in range(primeiro, décimo + razão, razão):
    print('{}'.format(c), end=' -> ')
print('ACABOU')
'''
