"""
Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie 2 listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo das 3 listas geradas.
"""
lista = []
par = []
ímpar = []
cont = 0

lista.append(int(input('Digite um valor: ')))
while True:
    op = str(input('Quer continuar? [S/N] ')).upper()
    if op == 'N':
        break
    elif op == 'S':
        lista.append(int(input('Digite um valor: ')))
    else:
        print('Opção Inválida! Tente novamente.')

while cont < len(lista):
    if lista[cont] % 2 == 0:
        par.append(lista[cont])
    else:
        ímpar.append(lista[cont])
    cont += 1
lista.sort()
print(f'Lista Completa: {lista}')
print('-=' * 20)
print(f'Lista de Pares: {par}')
print(f'Lista de Ímpares: {ímpar}')
