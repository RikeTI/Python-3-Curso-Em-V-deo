"""
Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200km e R$0,45 para viagens mais longas.
"""
viagem = float(input('Informe a distância da viagem (em Kms): '))
if viagem <= 200:
    print('A viagem será de {}kms, portanto, o preço por quilômetro é de R$0,50.\nO total a se pagar será de R${:.2f}'.format(viagem, viagem * 0.5))
else:
    print('A viagem será de {}kms, portanto, o preço por quilômetro é de R$0,45.\nO total a se pagar será de R${:.2f}'.format(viagem, viagem * 0.45))
  
'''
#if Simplificado
preço = viagem * 0.5 if viagem <= 200 else viagem * 0.45
print('O preço da passagem será de R${:.2f}'.format(preço))
'''
