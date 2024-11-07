"""
Aprimore o desafio anterior, mostrando no final:
a) A soma de todos os valores pares digitados;
b) A soma dos valores da 3ª coluna;
c) O maior valores da segunda linha.
"""
pares = coluna3 = maior = 0

#        1ª Linha / 2ª Linha / 3ª Linha 
#matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for i in range(0, 3):
    for j in range(0, 3): # Na 1ª linha vai rodar as 3 colunas; em seguida, na 2ª linha, as próximas 3 colunas 
        matriz[i][j] = int(input(f'Digite um valor para a posição [{i}, {j}]: '))

#matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
#matriz = [[1, 2], [3, 9]]
#Exibir os itens da lista
for i in range(0, 3):       # for i -> Laço das Linhas
    for j in range(0, 3):   # for j -> Laço das Colunas
        if matriz[i][j] % 2 == 0: 
            pares += matriz[i][j]   # Soma dos Pares
        print(f'[{matriz[i][j]:^5}]', end=' ')
        if i == 0:
            maior = matriz[1][j]
        else:
            if matriz[1][j] > maior:
                maior = matriz[1][j]
    coluna3 += matriz[i][2] #Soma de todos os elementos da 3ª Coluna (For i)
    print()
print(f'A soma de todos os valores pares é {pares}')
print(f'A soma de todos os valores da 3ª coluna é {coluna3}')
print(f'O maior valor da 2ª Linha é {maior}')



