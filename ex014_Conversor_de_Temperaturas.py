"""
Escreva um programa que converta uma temperatura digitada em ºC e converta para ºF
"""
c = float(input('Informe a temperatura em ºC: '))
f = 9 * c / 5 + 32 # <=> ((9 * c) / 5) + 32 | Ordem de Precedência
print('A temperatura de {}ºC equivale a {}ºF'.format(c, f))
