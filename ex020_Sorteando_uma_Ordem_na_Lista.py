"""
O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos 4 alunos e mostre a ordem sorteada.
"""
import random
a1 = input('1º aluno: ')
a2 = input('2º aluno: ')
a3 = input('3º aluno: ')
a4 = input('4º aluno: ')
lista = [a1, a2, a3, a4]
random.shuffle(lista)#Shuffle(lista) => Embaralhar itens de uma lista
print('A ordem de apresentação será {}'.format(lista))
