"""
Crie um programa que leia 2 valores e mostre um menu. Seu programa deverá realizar a operação solicitada em cada caso.
"""
from time import sleep
n1 = int(input('Primerio número: '))
n2 = int(input('Segundo número: '))
opção = 0
maior = n1
while opção != 5:
    print('''    [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novos números
    [ 5 ] sair do programa''')
    opção = int(input('>>> Qual a sua opção? '))
    if opção == 1:
        print('Soma: {} + {} = {}'.format(n1, n2, n1 + n2))
    elif opção == 2:
        print('Multiplicação: {} * {} = {}'.format(n1, n2, n1 * n2))
    elif opção == 3:
        if n2 > n1:
            print('O segundo número é maior: [{}]'.format(n2))
        elif n1 > n2:
            print('O primeiro número é maior: [{}]'.format(n1))
        else:
            print('Os dois números são iguais: [{}]'.format(n1))
    elif opção == 4:
        n1 = int(input('Primerio número: '))
        n2 = int(input('Segundo número: '))
    elif opção == 5:
        break
    else:
        print('Opção Inválida')
    print('=-='*10)
print('Finalizando...')
sleep(1)
print('Fim do Programa')

