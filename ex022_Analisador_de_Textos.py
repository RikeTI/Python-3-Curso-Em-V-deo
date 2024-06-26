"""
Crie um programa que leia o nome completo de uma pessoa e mostre:
*O nome com todas as letras maiúsculas e minúsculas
*Quantas letras ao todo (sem considerar espaços)
*Quantas letras tem o 1º nome
"""
nome = str(input('Digite o nome completo: ')).strip()
print('{}\n{}'.format(nome.upper(), nome.lower()))
espaços = nome.count(' ')
print('O nome "{}" tem ao todo {} letra(s)'.format(nome, len(nome) - espaços))
PrimeiroNome = nome.split()
#print('O 1º nome tem {} letras'.format(len(PrimeiroNome[0])))
#Método alternativo para a 3ª atividade:
print('Seu primerio nome tem {} letras'.format(nome.find(' ')))#Ele vai procurar a 1ª ocorrência de ' ' e assim informar o valor que corresponde a quantidade de letras. Ex.: 'Ana Clara' tem 3 letras no 1º nome e a 1ª ocorrência de ' ' é na posição 3, pois uma lista começa a sua contagem em 0.
      
