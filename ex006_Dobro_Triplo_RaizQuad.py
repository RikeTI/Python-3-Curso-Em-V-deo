"""
Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada
"""
n = int(input('Digite um número: '))
d = n * 2
t = n * 3
r = pow(n,(1/2))#r = n ** (1/2)
print('O número informado é {}.\nO dobro vale {}, o triplo vale {} e a raiz quadrada vale {:.2f}.'.format(n, d, t, r))
