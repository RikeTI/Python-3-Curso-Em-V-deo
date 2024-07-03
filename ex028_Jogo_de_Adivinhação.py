"""
Escreva um progrma que faça o computador 'pensar' em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.
"""
import random
from time import sleep
pc = random.randint(0, 5)
#print(pc)
print('Vou pensar em um número entre 0 e 5. Tente adivinhá-lo!')
player = int(input('Digite sua resposta: '))
print('LOADING...')
sleep(1)
print('Player: {}\nPC: {}'.format(player, pc))
print('-'*20)
print('Acertou!' if pc == player else 'Errou!')
