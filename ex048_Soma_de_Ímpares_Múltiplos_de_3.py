"""
Faça um programa que calcule a soma entre todos os números ímpares que são múltiplos de 3 e que se encontram no intervalo de 1 até 500.
"""
soma = cont = 0
for x in range(1, 500+1, 2):
    if x % 3 == 0:
        cont += 1
        soma += x
        #print(x, end=' ')
print('A soma de todos {} valores solicitados é {}'.format(cont, soma))


