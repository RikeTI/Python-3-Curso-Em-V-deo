"""
Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior e menor valor digitado e as suas respectivas posições na lista.
"""
'''
números = []
for n in range(0, 5):
    números.append(int(input(f'Informe um número: ')))
    if n == 0:
        maior = menor = números[n]
    else:
        if maior < números[n]:
            maior = números[n]
            pos_maior = n
        if menor > números[n]:
            menor = números[n]
            pos_menor = n

print(f'Na posição {pos_maior} encontrei o maior valor {maior}')
print(f'Na posição {pos_menor} encontrei o maior valor {menor}')
'''


#Resolução do Professor
listanum = []
for c in range(0, 5):
    listanum.append(int(input(f'Digite um valor para a Posição {c}: ')))
    if c == 0:
        mai = men = listanum[c]
    else:
        if listanum[c] > mai:
            mai = listanum[c]
        if listanum[c] < men:
            men = listanum
print('=-'*30)
print(f'Você digitou os valores {listanum}')
print(f'O maior valor digitado foi {mai} nas posições ', end='')
for i, v in enumerate(listanum):
    if v == mai:
        print(f'{i}... ', end='')
print()
print(f'O menor valor digitado foi {men} nas posições ', end='')
for i, v in enumerate(listanum):
    if v == men:
        print(f'{i}... ', end='')
print()
