#Refazendo ex 086 e 087
"""
Crie um programa que crie uma matriz de dimensão 3x3 e preencha com os valores lidos pelo teclado.
No final, mostre a matriz na tela, com a formatação correta.
Aprimore o desafio anterior, mostrando no final:
a) A soma de todos os valores pares digitados;
b) A soma dos valores da 3ª coluna;
c) O maior valores da segunda linha.
"""
linha = list()
coluna = list()
l = int(input('Informe quantas linhas a matriz terá: '))
c = int(input('Informe quantas colunas a matriz terá: '))

for i in range(0,l):
    for j in range(0,c):
        coluna.append(int(input(f'Informe um número para a posição ({i+1}, {j}): ')))
    linha.append(coluna[:])
    coluna.clear()

for i in range(0,l):
    for j in range(0,c):
        print(f'[{linha[i][j]:^5}]', end=' ')
    print()  

