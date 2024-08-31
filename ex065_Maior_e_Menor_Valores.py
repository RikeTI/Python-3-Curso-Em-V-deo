"""
Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e quais foram o maior e menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.
"""
acc = cont = 0
n = maior = menor = int(input('Digite um número: '))
while True:
    if n > maior:
        maior = n
    if n < menor:
        menor = n
    acc += n
    cont += 1
    flag = str(input('Quer continuar? [S/N] ')).upper().strip()
    if flag[0] == 'S':
        n = int(input('Digite um número: '))
    elif flag[0] == 'N':
        break
média = acc / cont
print('A média dos números informados é {:.2f}'.format(média))
print('O maior valor lido foi {}, enquanto o menor foi {}'.format(maior, menor))



'''#Resolução do Professor
resp = 'S'
soma = quant = média = maior = menor = 0
while resp in 'Ss':
    núm = int(input('Digite um número: '))
    soma += núm
    quant += 1
    if quant == 1:
        maior = menor = núm
    else:
        if núm > maior:
            maior = núm
        if núm < menor:
            menor = núm
    resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
média = soma / quant
print('Você digitou {} números e a média foi {:.2f}'.format(quant, média))
print('O maior valor foi {} e o menor foi {}'.format(maior, menor))'''


