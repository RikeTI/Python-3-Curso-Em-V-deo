"""
Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente.
"""
valores = []
valores.append(int(input('Digite um número: ')))
op = input('Deseja continuar? [S/N] ').upper()
while True:
    if op == 'S':
        temp = int(input('Digite um número: '))
        if temp not in valores:
            valores.append(temp)
            op = input('Deseja continuar? [S/N] ').upper()
        else:
            print('Este valor já se encontra na lista!')
    elif op == 'N':
        break
    else:
        print('Opção Inválida')
        op = input('Deseja continuar? [S/N] ').upper()
valores.sort()
print(valores)



#Resolução do Professor
'''
números = list()
while True:
    n = int(input('Digite um valor: '))
    if n not in números:
        números.append(n)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado! Não vou adicionar...')
    r = str(input('Quer continuar? [S/N] '))
    if r in 'Nn':
        break
print('-='*30)
print(f'Você digitou os valores {números}')
'''

