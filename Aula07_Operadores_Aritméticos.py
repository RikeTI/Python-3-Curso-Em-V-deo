"""
Adição          =>      +
Subtração       =>      -
Multiplicação   =>      *
Divisão         =>      /
Divisão Inteira =>      //
Exponenciação   =>      **
Módulo          =>      %
"""

'''
n1 = 5
n2 = 2
print('n1 + n2 = {}'.format(n1 + n2))
print('n1 - n2 = {}'.format(n1 - n2))
print('n1 * n2 = {}'.format(n1 * n2))
print('n1 / n2 = {}'.format(n1 / n2))
print('n1 // n2 = {}'.format(n1 // n2))
print('n1 ** n2 = {}'.format(n1 ** n2))
print('n1 % n2 = {}'.format(n1 % n2))
print('-'*20)
print('4 elevado a 3 é igual a {}'.format(pow(4,3)))
print('81 ** (1/2) => Raiz Quadrada de 81 é igual a {}'.format(81**(1/2)))
print('27 ** (1/3) => Raiz Cúbica de 27 é igual a {}'.format(27**(1/3)))
'''

'''
#Uso de operadores com strings
nome = str(input('Digite o seu nome: ')).capitalize()
print('Prazer em te conhecer, {}!'.format(nome))#Print sem alteração
print('Prazer em te conhecer, {:20}!'.format(nome))#Print com 20 espaços dentro da máscara
#print('Prazer em te conhecer, {:<20}!'.format(nome))#Mesmo resultado que o de cima, pois por padrão o alinhamento é a esquerda
print('Prazer em te conhecer, {:>20}!'.format(nome))#Print com 20 espaços e alinhamento à direita
print('Prazer em te conhecer, {:^20}!'.format(nome))#Print com 20 espaços e alinhamento no centro
print('Prazer em te conhecer, {:=^20}!'.format(nome))#Print com 20 espaços e alinhamento no centro, tendo os '=' preenchendo os espaços vazios
'''


a = int(input('Digite um valor: '))
b = int(input('Digite outro valor: '))
s = a + b
m = a * b
d = a / b
di = a // b
e = a ** b
print('A soma é {}, o produto é {} e a divisão é {}.'.format(s, m, d), end=' >>> ')
print('A divisão inteira é {} e a potência é {}.'.format(di, e))
