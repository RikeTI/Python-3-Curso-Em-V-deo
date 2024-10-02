"""
Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extensão, de zero até vinte.
Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.

#Desafio extra: faça o programa perguntar novamente até que o usuário queira sair.
"""
# Lógica de Programação

# Criação de uma tupla com os números por extenso

# Criação de uma tupla com os números arábicos

# Comparar a posição dos elementos das 2 tuplas

# Criação de um laço para repetir a comparação n vezes

    # O laço deve verificar se o número digitado está entre 0 e 20

'''
n1 = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
n2 = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20)

import time

while True:
    n = int(input('Digite um nº entre [0 e 20]: '))
    if n > 20 or n < 0:
        print('Inválido')
    else:
        print('Verificando...')
        time.sleep(1)
        print('='*40)
        if 0 <= n <= 20:
            for c in range(0, 21):
                if c == n:
                    print(f'{n} = {n1[c]}')
        break
print('Fim do Programa.')
'''


# Protótipo para uma entrada específica (no caso, o 0)
'''if n == n2[0]:
    print(f'Você digitou {n}.')
    print('Comparando...')
    time.sleep(2)
    print(n1[0])'''


# Funcionando a comparação e a busca
# Falta a restrição para repetir a entrada sempre que um valor inválido foi digitado
'''
print('Verificando...')
time.sleep(1)
print('='*40)
if 0 <= n <= 20:
    for c in range(0, 21):
        if c == n:
            print(f'{n} = {n1[c]}')
else:
    print('Inválido. Tente novamente.')
    '''



#Resolução do Professor
cont = ('zero', 'um', 'dois', 'três', 'quatro', 
        'cinco', 'seis', 'sete', 'oito', 'nove', 
        'dez', 'onze', 'doze', 'treze', 'catorze', 
        'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
    núm = int(input('Digite um número entre 0 e 20: '))
    if 0 <= núm <= 20:
        break
    print('Tente novamente. ', end='')
print(f'Você digitou o número {cont[núm]}')

