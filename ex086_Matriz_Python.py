"""
Crie um programa que crie uma matriz de dimensão 3x3 e preencha com os valores lidos pelo teclado.
No final, mostre a matriz na tela, com a formatação correta.
"""

'''matriz = [[0, 0], [0, 0]]

for i in range(0, 2):
    for j in range(0, 2):
        matriz[i][j] = int(input(f'Digite um valor para: [{i}, {j}] '))
print(matriz)

'''









#Resolução do Professor
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(0, 3):       #Linhas
    for c in range(0, 3):   #Colunas
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
print('-=' * 30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='') #Centralizado com 5 espaços
    print() #Quebra de linha para deixar as linhas uma embaixo da outra
