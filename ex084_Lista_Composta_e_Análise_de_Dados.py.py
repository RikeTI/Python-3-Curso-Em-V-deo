"""
Faça um programa que leia o nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
a) Quantas pessoas foram cadastradas;
b) Uma listagem com as pessoas mais pesadas; e, 
c) Uma listagem com as pessoas mais leves.
"""


pessoas = list()
lista_completa = list()
qtd = 1
soma = med = 0
pesado = list() 
leve = list()

pessoas.append(str(input('Informe o nome: ').title()))
pessoas.append(float(input('Informe o peso: ')))
lista_completa.append(pessoas[:])
pessoas.clear()

while True:
    op = str(input('Quer continuar? [S/N] ')).upper()
    if op == 'N':
        break
    elif op == 'S':
        pessoas.append(str(input('Informe o nome: ').title()))
        pessoas.append(float(input('Informe o peso: ')))
        lista_completa.append(pessoas[:])
        pessoas.clear()
        qtd += 1
    else:
        print('Opção Inválida! Tente novamente.')


for p in lista_completa:
    soma += p[1]
med = soma / qtd

for x in range(len(lista_completa)):
    if lista_completa[x][1] > med:
        pesado.append(lista_completa[x]) 
    else:
        leve.append(lista_completa[x])

print('-=' * 30)
print(f'Lista Completa: {lista_completa}.')
print(f'Ao todo foram cadastradas {qtd} pessoas.')
print()
print(f'O peso médio das pessoas cadastradas é {med:.2f}')
print(f'Pessoas pesadas: {pesado}')
print(f'Pessoas leves: {leve}')




'''
#Resolução do Professor
temp = []
princ = []
mai = men = 0
while True:
    temp.append(str(input('Nome: ')))
    temp.append(float(input('Peso: ')))
    if len(princ) == 0:
        mai = men = temp[1]
    else:
        if temp[1] > mai:
            mai = temp[1]
        if temp[1] < men:
            men = temp[1]
    princ.append(temp[:])
    temp.clear()
    resp = str(input('Quer continuar? [S/N] '))
    if resp in 'Nn':
        break
print('-=' * 30)
print(f'Os dados foram {princ}')
print(f'Ao todo, você cadastrou {len(princ)} pessoas.')
print(f'O maior peso foi de {mai}Kg. Peso de ', end='')
for p in princ:
    if p[1] == mai:
        print(f'[{p[0]}] ', end='')
print()
print(f'O menor peso foi de {men}Kg. Peso de ', end='')
for p in princ:
    if p[1] == men:
        print(f'[{p[0]}] ', end='')
print()
'''