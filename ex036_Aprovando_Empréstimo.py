"""
Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.
"""
import time
salário = float(input('Qual o seu salário? R$'))
casa = float(input('Qual o valor da casa? R$'))
anos = int(input('Em quantos anos pretende pagar? '))
prestações = anos * 12
prestação_mensal = casa / prestações
print('Seu salário é de R${:.2f}'.format(salário))
print('A casa que pretende comprar custa R${:.2f}'.format(casa))
print('O empréstimo foi solicitado para ser pago em {} ano(s), o que seria em {} prestações'.format(anos, prestações))
print('O valor de cada prestação foi fixado em R${:.2f}'.format(prestação_mensal))
print('Analisando sua solicitação...')
time.sleep(2)
if prestação_mensal > 0.3 * salário:
    print('\033[31mEMPRÉSTIMO NEGADO!\033[m')
else:
    print('\033[32mEMPRÉSTIMO CONCEDIDO!\033[m')




