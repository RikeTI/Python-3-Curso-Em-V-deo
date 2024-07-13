"""
Crie um programa que faça o computador jogar Jo-Ken-Pô com você.
"""
import random
import time
print('{:=^40}'.format(' \033[33mVamos jogar um jogo?\033[m '))
time.sleep(1)
print('Que tal Jo-Ken-Pô?')
time.sleep(0.25)
pc = random.randint(1, 3)
player = int(input('''Escolha uma das 3 opções:
[ 1 ]: Pedra
[ 2 ]: Papel
[ 3 ]: Tesoura
Player: '''))
if player == 1 or player == 2 or player == 3:
    time.sleep(0.5)
    print('JO')
    time.sleep(0.5)
    print('KEN')
    time.sleep(0.5)
    print('PÔ!!!')
    if player == 1 and pc == 2:
        print('Vitória do Computador!')
    elif player == 1 and pc == 3:
        print('Vitória do Jogador!')
    elif player == 2 and pc == 1:
        print('Vitória do Jogador!')
    elif player == 2 and pc == 3:
        print('Vitória do Computador!')
    elif player == 3 and pc == 1:
        print('Vitória do Computador!')
    elif player == 3 and pc == 2:
        print('Vitória do Jogador!')
    else:
        print('Empate!')
else:
    print('\033[31mOpção Inválida!\033[m')