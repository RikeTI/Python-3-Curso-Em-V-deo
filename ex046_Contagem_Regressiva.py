"""
Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artício, indo de 10 até 0, com uma pausa de 1 segundo entre eles
"""
import time

for c in range(10, -1, -1):
    print(c)
    time.sleep(0.25)#1/4 de segundo
print('KABOOM!!!')

#print('hello')
#time.sleep(1)
#print('world')
