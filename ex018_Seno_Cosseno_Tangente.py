"""
Fçaa um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo
"""
#from math import radians, sin, cos, tan
import math
ang = float(input('Informe um ângulo qualquer: '))
seno = math.sin(math.radians(ang))#Converte o ângulo informado pelo usuário para 'radianos' e a partir dele verifica qual o seno, pois a fórmula 'math.sin()' só aceita valores em radianos
cosseno = math.cos(math.radians(ang))
tangente = math.tan(math.radians(ang))
print('O ângulo de {}º tem {:.2f} de Seno, {:.2f} de Cosseno e {:.2f} de Tangente'.format(ang, seno, cosseno, tangente))
