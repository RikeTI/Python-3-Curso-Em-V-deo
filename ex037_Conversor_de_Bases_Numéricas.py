"""
Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão:
1 para Binário
2 para Octal
3 para Hexadecimal
"""
n = int(input('Digite um número qualquer para conversão: '))
opção = int(input('''Escolha para qual base você gostaria de converter:
[ 1 ]: Binário
[ 2 ]: Octal
[ 3 ]: Hexadecimal
Opção: '''))
if opção == 1:
    print('{} convertido para BINÁRIO é igual a {}'.format(n, bin(n)[2:]))
elif opção == 2:
    print('{} convertido para OCTAL é igual a {}'.format(n, oct(n)[2:]))
elif opção == 3:
    print('{} convertido para HEXADECIMAL é igual a {}'.format(n, hex(n)[2:]))
else:
    print('\033[31mOpção Inválida!\033[m')
