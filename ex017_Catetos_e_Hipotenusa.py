"""
Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa
"""

from math import hypot
ca = float(input('Informe o Cateto Adjacente: '))
co = float(input('Informe o Cateto Oposto: '))
#hi = (ca ** 2 + co ** 2) ** (1 / 2)#Hipotenusa = Raiz Quadrada da Soma dos Catetos elevados ao Quadrado
hi = hypot(co, ca)
print('A hipotenusa vai medir {:.2f}'.format(hi))

