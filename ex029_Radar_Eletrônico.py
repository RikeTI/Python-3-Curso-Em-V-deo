"""
Escreva um programa que leia a velcodiade de um carro. Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada km acima do limite.
"""
import math
msg = 'Radar Eletrônico em Funcionamento'
limite = 80
print('[{:^40}]'.format(msg))
print('A velocidade máxima permitida neste trecho é {}km/h.'.format(limite))
vel = float(input('Qual a velocidade do carro? (Em Km/h): '))
if vel > limite:
    multa = vel - limite
    print('Você está {}km/h acima do limite de velocidade! Você deverá pagar uma multa de R${:.2f}.'.format(multa, multa * 7))
else:
    print('Você está dentro do limite de velocidade! Siga em frente.')
