"""
Desenvolva um programa que leia 6 números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.
"""
s  = cont = 0
for c in range(1, 7):
    n = int(input('Digite um número: '))
    if n % 2 == 0:
        s += n
        cont += 1
print('Quantidade de Pares: {}'.format(cont))
print('Soma dos Pares: {}'.format(s))