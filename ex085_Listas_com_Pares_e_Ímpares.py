"""
Crie um programa onde o usuário possa digitar 7 valores numéricos e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.
"""
#Resolução do Professor
núm = [[], []]#Iniciar uma lista com 2 listas internas
valor = 0
for c in range(1, 8):
    valor = int(input(f'Digite o {c}º valor: '))
    if valor % 2 == 0:
        núm[0].append(valor)#Adiciona na 1ª sublista
    else:
        núm[1].append(valor)#Adiciona na 2ª sublista
print('-=' * 30)
núm[0].sort()
núm[1].sort()
print(f'Os valores pares digitados foram: {núm[0]}')
print(f'Os valores ímpares digitados foram: {núm[1]}')
