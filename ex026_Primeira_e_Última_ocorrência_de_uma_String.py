"""
Faça um programa que leia uma frase pelo teclado e mostre:
*Quantas vezes aparece a letra 'A'
*Em que posição ela aparece a primeira vez
*Em que posição ela aparece a última vez
"""
frase = str(input('Digite uma frase qualquer: ')).strip()
print('A letra "A" aparece {} vez(es) na frase informada pelo usuário.'.format(frase.upper().count('A')))
print('A letra "A" aparece pela primeira vez na {}ª posição.'.format(frase.upper().find('A')+1))
print('A letra "A" aparece pela última vez na {}ª posição.'.format(frase.upper().rfind('A')+1))

