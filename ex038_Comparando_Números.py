"""
Escreva um programa que leia 2 números inteiros e compare-os, mostrando na tela uma mensagem:
*O primeiro valor é MAIOR
*O segundo valor é MAIOR
*Não existe valor MAIOR, os dois são iguais.
"""
n1 = int(input('Informe o 1º número: '))
n2 = int(input('Informe o 2º número: '))
if n1 > n2:
    print('O primeiro valor, {}, é MAIOR!'.format(n1))
elif n2 > n1:
    print('O segundo valor, {}, é MAIOR!'.format(n2))
else:
    print('Não existe valor MAIOR, os dois são iguais!')

