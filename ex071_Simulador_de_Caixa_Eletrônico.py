"""
Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues.
Obs.: Considere que o caixa possui cédulas de R$50, R$20, R$10, e R$1.
"""

'''import time
print('~~'*20)
print('{:^40}'.format('>>> SIMULADOR DE CAIXA <<<'))
print('~~'*20)

cash = int(input('Quanto dinheiro você vai querer sacar? R$'))
print(f'R${cash:.2f} solicitado!')
print('Processando...')
time.sleep(1.5)

print('='*42)
nota50 = cash // 50     #Quantidade de notas de R$50
print(f'Sua solicitação contém {nota50} nota(s) de R$50,00')
resto = cash - nota50 * 50
print(f'Resta R${resto:.2f} para ser processado')

print('-'*15)
print('Processando...')
time.sleep(1)
print('-'*15)

nota20 = resto // 20    #Quantidade de notas de R$20
print(f'Sua solicitação contém {nota20} nota(s) de R$20,00')
resto -= (nota20 * 20)
print(f'Resta R${resto:.2f} para ser processado')

print('-'*15)
print('Processando...')
time.sleep(1)
print('-'*15)

nota10 = resto // 10    #Quantidade de notas de R$10
print(f'Sua solicitação contém {nota10} nota(s) de R$10,00')
resto -= (nota10 * 10)
print(f'Resta R${resto:.2f} para ser processado')

print('-'*15)
print('Processando...')
time.sleep(1)
print('-'*15)

print(f'Sua solicitação contém {resto} nota(s) de R$1,00')'''
 

#Resolução do Professor
print('='*30)
print('{:^30}'.format('BANCO CEV'))
print('='*30)
valor = int(input('Que valor você quer sacar? R$'))
total = valor
céd = 50
totcéd = 0
while True:
    if total >= céd:
        total -= céd
        totcéd += 1
    else:
        if totcéd > 0:
            print(f'Total de {totcéd} cédulas de R${céd}')
        if céd == 50:
            céd = 20
        elif céd == 20:
            céd = 10
        elif céd == 10:
            céd = 1
        totcéd = 0
        if total == 0:
            break
print('=' * 30)
print('Volte sempre ao BANCO CEV! Tenha um bom dia!')
