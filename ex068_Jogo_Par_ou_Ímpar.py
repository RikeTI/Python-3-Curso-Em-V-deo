"""
Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador PERDER, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
"""

'''import random
cont = 0
print('>> VAMOS JOGAR PAR OU ÍMPAR? <<')
while True:
    print('-'*24)
    jogador = str(input('Par ou Impar? ')).strip().title()

    if jogador == 'Par':
        computador = 'Impar'
    elif jogador == 'Impar':
        computador = 'Par'
    print(f'Jogador: {jogador}')
    print(f'Computador: {computador}')
    print('='*20)
    choice = random.randint(0,1)
    if choice == 0:
        rodada = 'Par'
        print(f'Rodada: {rodada}')
    else:
        rodada = 'Impar'
        print(f'Rodada: {rodada}')

    print('='*20)

    if rodada == jogador:
        print('Vitória do Jogador')
        cont +=1
    else:
        print('Vitória do Computador')
        break
print('~~'*13)
print(f'Você ganhou {cont} rodada(s)!')
'''

#Resolução do Professor
from random import randint
v = 0
while True:
    jogador = int(input('Diga u valor: '))
    computador = randint(0, 10)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Ímpar? [P/I] ')).strip().upper()[0]
    print(f'Você jogou {jogador} e o computador {computador}. Total de {total}')
    print('DEU PAR' if total % 2 == 0 else 'DEU ÍMPAR')
    if tipo == 'P':
        if total % 2 == 0:
            print('Você VENCEU!')
            v += 1
        else:
            print('Você PERDEU!')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('Você VENCEU!')
            v += 1
        else:
            print('Você PERDEU!')
            break
    print('Vamos jogar novamente...')
print(f'GAME OVER! Você venceu {v} vezes')



