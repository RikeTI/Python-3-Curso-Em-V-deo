"""
Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.
Ex.:
APOS A SOPA / A SACADA DA CASA / A TORRE DA DERROTA / O LOBO AMA O BOLO / ANOTARAM A DATA DA MARATONA
"""
'''frase = input('Digite uma frase qualquer: ').upper().strip().split()
print(frase)
print(len(frase))
frase = ''.join(frase)
'''
'''FORA DO EXERCÍCIO, APENAS TESTANDO
frase = ['A', 'B', 'C']
print(frase)
#print(len(frase))
pos = len(frase) - 1
temp = 0
for x in range(0, len(frase)):
    temp = frase[x]
    frase[x] = frase[pos - x]
    frase[pos - x] = temp
print(frase)
'''

#Resolução do Professor
frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
'''inverso = ''
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]'''
inverso = junto[::-1]#:Do início ; :Ao fim ; -1 De trás pra frente
print('O inverso de {} é {}'.format(junto, inverso))
if inverso == junto:
    print('Temos um palíndromo!')
else:
    print('A frase digitada não é um palíndromo!')
