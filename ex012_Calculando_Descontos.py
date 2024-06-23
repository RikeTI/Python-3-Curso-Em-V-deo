"""
Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto
"""
preço = float(input('Informe o preço do produto: R$'))
desconto = preço*0.05#x * 5 / 100 => 5 por cento de x   
print('O novo preço do produto, com 5% de desconto, será R${:.2f}'.format(preço - desconto))
