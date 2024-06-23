"""
Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado
"""
km = float(input('Quantos km percorridos? '))
dias = int(input('Quantos dias alugado? '))
#print('{}km(s)\n{} dia(s) alugado(s)'.format(km, dias))
preço_dia = dias * 60
preço_km = km * 0.15
total = preço_dia + preço_km
print('O carro foi alugado por {} dia(s) e o mesmo rodou {} km(s).\nPortanto, o total a pagar será de R${:.2f}'.format(dias, km, total))
