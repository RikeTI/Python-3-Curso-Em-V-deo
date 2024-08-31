"""
Escreva um programa que leia um número n inteiro qualquer e mostre na tela os n primeiros elementos de uma Sequênia de Fibonacci.
Ex.: 0 -> 1 -> 1 -> 2 -> 3 -> 5 -> 8
"""
'''print('>>> Sequência de Fibonacci <<<')
import time
n = int(input('Informe quantos números inteiros você quer ver? '))
print('{} número(s), né? Beleza!\nCarregando...'.format(n))
time.sleep(2)
t1 = 0
t2 = 1
t3 = t1 + t2
print('{} ↦ {} ↦ {}'.format(t1, t2, t3), end='')
for i in range(0, n-3):
    print(' ➝  ', end='')
    t1 = t2
    t2 = t3
    t3 = t1 + t2
    print(t3, end='')
print(' ➜  FIM!')
'''
#Resolução do Professor
n = int(input('Quantos termos você quer mostrar? '))
t1 = 0
t2 = 1
print('{} ➝  {}'.format(t1, t2), end='')
cont = 3
while cont <= n:
    t3 = t1 + t2
    print(' ➝  {}'.format(t3), end='')
    t1 = t2
    t2 = t3
    cont += 1
print(' ➜  FIM!')

