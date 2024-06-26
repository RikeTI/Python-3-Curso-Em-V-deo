"""
Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o última nome separadamente.
Ex.: Ana Maria de Souza
Primeiro: Ana
Último: Souza
"""
nome = str(input('Digite o seu nome completo: ')).strip().title().split()
print('Nome completo: {}'.format(nome))
print('Primeiro nome: {}'.format(nome[0]))
print('Sobrenome: {}'.format(nome[-1]))
#print('Sobrenome: {}'.format(nome[len(nome)-1]))#Mesmo resultado que a linha acima

