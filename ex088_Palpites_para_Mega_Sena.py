
"""
Faça um programa que ajude um jogador da MEGA SENA a criar palpites. O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.
"""

'''from random import randint
from time import sleep
matriz = [[], [], []]


#x = int(input('Quantos jogos gostaria de gerar? '))
for i in range(0, 3):
    for j in range(0, 6):
        n = randint(1, 19)
        #if n not in matriz:        # Error!
        #    matriz[i].append(n)    # Error!
        # matriz[i].append(randint(1, 60))
#print(matriz)

for i in range(0, 3):
    for j in range(0, 6):
        print(f'[{matriz[i][j]:^3}]', end='')
    #sleep(0.5)
    print()
'''


#Resolução do Professor
from random import randint
from time import sleep
lista = list()
jogos = list()
print('-' * 30)
print('      JOGA NA MEGA SENA     ')
print('-' * 30)
quant = int(input('Quantos jogos você quer que eu sorteie? '))
tot = 1
while tot <= quant:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
print(f'-=' * 3, f' SORTEANDO {quant} JOGOS ', '-=' * 3)
for i, l in enumerate(jogos):
    sleep(1)
    print(f'Jogo {i+1}: {l}')
print('-=' * 5, '< BOA SORTE! >', '-=' * 5)
