"""
Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar. No final, mostre:
a) Qual é o total gasto na compra?
b) Quantos produtos custam mais de R$1.000,00?
c) Qual é o nome do produto mais barato?
"""

'''total_custo = qtd1000 = barato = cont = 0
while True:
    nome_prod = str(input('Nome do produto: ')).title()
    preço_prod = float(input('Preço: R$'))
    total_custo += preço_prod
    if preço_prod >= 1000:
        qtd1000 += 1

    if cont == 0:                   #Se ainda for a primeira compra,
        barato = preço_prod         #a variável "barato" receberá o mesmo valor da primeira entrada
        nome_barato = nome_prod
    else:                           #Se não for a primeira repetição,
        if barato > preço_prod:     #"barato" fará uma comparação para ver qual é o menor valor.
            barato = preço_prod
            nome_barato = nome_prod
    cont += 1
    repet = ' '
    while repet not in 'SN':
        repet = str(input('Gostaria de continuar? [S/N] ')).strip().upper()
    if repet[0] == 'N':
        break

print('='*40)
print(f'O total da compra foi de R${total_custo:.2f}')
print(f'Há {qtd1000} produto(s) que custa(m) mais de R$1000,00') 
print(f'O produto mais barato foi {nome_barato} e custou R${barato:.2f}')
    '''


#Resolução do Professor
total = totmil = menor = cont = 0
barato = ''
while True:
    produto = str(input('Nome do produto: '))
    preço = float(input('Preço do produto: R$'))
    cont += 1
    total += preço
    if preço > 1000:
        totmil += 1
    if cont == 1 or preço < menor:
        menor = preço
        barato = produto
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print('{:-^40}'.format(' FIM DO PROGRAMA '))
print(f'O total da compra foi R${total:.2f}')
print(f'Temos {totmil} produtos custando mais de R$ 1000.00')
print(f'O produto mais barato foi {barato} que custa R${menor:.2f}')
