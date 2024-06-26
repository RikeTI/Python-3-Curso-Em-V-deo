"""
Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados
Ex.: 1834 => uni: 4 ; dez: 3 ; cen: 8 ; mil: 1
"""


n = int(input('Informe um número de 0 a 9999: '))
#Exemplo: n = 1834
u = n % 10#1000, 800 e 30 são múltiplos de 10; Resto = 4
d = n // 10 % 10#183 => 100 e 80 são múltiplos de 10; Resto = 3
c = n // 100 % 10#18 => 10 é múltiplo de 10; Resto = 8
m = n // 1000 % 10#1 => não há múltiplo de 10; Resto = 1
print('Unidade: {}'.format(u))
print('Dezena: {}'.format(d))
print('Centena: {}'.format(c))
print('Milhar: {}'.format(m))


'''#Separando os valores da maneira string de ser (porém ocorrerá erro se houver menos de 4 digítos)
n = input('Informe um número de 0 a 9999: ')
print('Unidade: {}'.format(n[3]))
print('Dezena: {}'.format(n[2]))
print('Centena: {}'.format(n[1]))
print('Milhar: {}'.format(n[0]))'''

