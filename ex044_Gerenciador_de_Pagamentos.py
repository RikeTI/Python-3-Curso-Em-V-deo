"""
Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição e pagamento:
*À vista dinheiro/cheque: 10% de desconto.
*À vista no cartão: 5% de desconto.
*Em até 2x no cartão: Preço Normal.
*3x ou mais no cartão: 20% de juros.
"""
preço = float(input('Informe o preço do produto: R$'))
print('''Há 4 modalidades de pagamento:
[ 1 ]: À vista no dinheiro ou cheque -> \033[34m10% de desconto\033[m
[ 2 ]: À vista no cartão -> \033[36m5% de desconto\033[m
[ 3 ]: Em até 2x no cartão -> \033[32mPreço Normal\033[m
[ 4 ]: 3x ou mais no cartão -> \033[33m20% de juros\033[m''')
pag = int(input('Como gostaria de pagar? '))

'''
if pag == 1:
    print('O produto custa {}R${:.2f}{}, mas devido a opção de pagamento será aplicado um desconto de 10% ao preço final\nO novo valor será fixado em {}R${:.2f}{}'.format('\033[36m', preço, '\033[m', '\033[36m', preço * 0.90, '\033[m'))
elif pag == 2:
    print('O produto custa {}R${:.2f}{}, mas devido a opção de pagamento será aplicado um desconto de 5% ao preço final\nO novo valor será fixado em {}R${:.2f}{}'.format('\033[36m', preço, '\033[m', '\033[36m', preço * 0.95, '\033[m'))
elif pag == 3:
    print('O preço do produto será fixado em {}R${:.2f}{}\nSem desconto '.format('\033[36m', preço, '\033[m',))
elif pag == 4:
    parcelas = int(input('Em quantas parcelas? '))

    print('O produto custa {}R${:.2f}{}, mas devido a opção de pagamento será aplicada uma taxa de 20% de juros ao preço final\nO novo valor será fixado em {}R${:.2f}{}'.format('\033[36m', preço, '\033[m', '\033[31m', preço * 1.2, '\033[m'))


print('>>> \033[32mObrigado pela preferência! Volte Sempre!\033[m')
'''
#Resolução do Professor (continuação da linha 14)
if pag == 1:
    total = preço - (preço * 10 / 100)
elif pag == 2:
    total = preço - (preço * 5 / 100)
elif pag == 3:
    total = preço
    parcela = total / 2
    print('Sua compra será parcelada em 2x de R${:.2f} SEM JUROS'.format(parcela))
elif pag == 4:
    total = preço + (preço * 20 / 100)
    totparc = int(input('Quantas parcelas? '))
    parcela = total / totparc
    print('Sua compra será parcelada em {}x de R${:.2f} COM JUROS'.format(totparc, parcela))
else:
    total = 0
    print('\033[31mOpção Inválida!\033[m Tente novamente')

print('Sua compra de {}R${:.2f}{} vai custar {}R${:.2f}{} no final.'.format('\033[1m', preço, '\033[m', '\033[33m', total, '\033[m'))

