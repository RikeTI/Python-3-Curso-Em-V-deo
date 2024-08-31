"""
Melhore o jogo do Desafio 028 onde o computador vai "pensar" em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites forem necessários para vencer.
"""

'''
import random
palpite = 1
pc = random.randint(1,2)
print('Pensei em um número. Quer adivinhar qual? ')
usuário = int(input('Escolha um número de 1 a 4: '))
while usuário != pc:
    palpite += 1
    print('Eu pensei no número {} e o número informado foi {}'.format(pc, usuário))
    print('\033[31mVocê errou!\033[m Tente novamente!')
    usuário = int(input('Escolha um número de 1 a 4: '))

#print('Eu pensei no número {} e o número informado foi {}'.format(pc, usuário))
print('Você acertou! \033[1;33mParabéns\033[m!')
print('Foram necessários {} palpite(s)'.format(palpite))
'''


#Resolução do Professor
from random import randint
computador = randint(0, 10)
print('Sou seu computaodr... Acabei de pensar em um número entre 0 e 10')
print('Será que você consegue adivinhar qual foi?')
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual é o seu palpite? '))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais... Tente mais uma vez')
        elif jogador > computador:
                print('Menos... Tente mais uma vez')
print('Acertou com {} tentativas. Parabéns!'.format(palpites))