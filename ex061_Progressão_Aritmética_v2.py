"""
Refaça o Desafio 051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.
"""
import time
a1 = int(input('Informe o 1º termo da PA: '))
r = int(input('Informe a Razão da PA: '))
c = 2
a = a1 + r
print('~'*54)
print('PA de 10 Termos com \033[1;33m A1 = {}\033[m e \033[1;33mRazão = {}\033[m'.format(a1, r))
print('Calculando...') 
print('~'*54)
time.sleep(1)
print('{}'.format(a1), end=' -> ')
while c < 10:
    print('{}'.format(a), end=' -> ')
    a = a + r  
    c += 1
print('{}'.format(a))



'''a1 = 2
r = 3
c = 2
a = a1 + r  
print('a1 = {}'.format(a1))
while c < 11:
    print('a{} = {}'.format(c, a))
    a = a + r  
    c += 1'''
