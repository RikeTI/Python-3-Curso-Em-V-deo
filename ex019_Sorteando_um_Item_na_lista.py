"""
Um professor quer sortear um dos seus 4 alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido.
"""
from random import choice
a1 = str(input('Nome do 1º aluno: '))
a2 = str(input('Nome do 2º aluno: '))
a3 = str(input('Nome do 3º aluno: '))
a4 = str(input('Nome do 4º aluno: '))
lista = [a1, a2, a3, a4]
escolhido = choice(lista)
print('O aluno escolhido foi {}'.format(escolhido))
