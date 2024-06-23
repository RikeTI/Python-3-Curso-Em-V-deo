"""
Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros
km hm dam m dm cem mm
   /10 <- 1 -> *10
"""
medida = float(input('Informe a medida em metros: '))
print('{}m equivale a {}cm'.format(medida, medida*100))
print('{}m equivale a {}mm'.format(medida, medida*1000))
