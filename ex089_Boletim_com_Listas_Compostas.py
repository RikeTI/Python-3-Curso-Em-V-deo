"""
Crie um programa que leia o nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final, mostre um boletim contendo a média de cada um e permita que o usuário posssa mostrar as notas de cada aluno individualmente.
"""

"""
# LÓGICA DE PROGRAMAÇÃO 
# Leia: Nome; N1; N2;
# Guardar nome e notas em lista composta
#   [[nome1, notaA1, notaA2], [nome2, notaB1, notaB2], [nome3, notaC1, notaC2]...]
# Escreva: Nome; Média
# Boletim = [[nome1, média1], [nome2, média2], [nome3, média3]...]


#nome = []
#notas = []
aluno = list()
discentes = list()
#boletim = [[], []]

#lista_exemplo = [['Rike', 7.4, 8], ['Brett', 9, 5.8]]
#print(f'{lista_exemplo[0]}\n{lista_exemplo[1]}')



aluno.append(str(input('Informe o nome do aluno: ')).title())
aluno.append(float(input('Informe a 1ª nota do aluno: ')))
aluno.append(float(input('Informe a 2ª nota do aluno: ')))
discentes.append(aluno[:])
aluno.clear()



while True:
    op = str(input('Continuar? [S/N] ')).upper()
    if op == 'N':
        break
    elif op == 'S':
        aluno.append(str(input('Informe o nome do aluno: ')).title())
        aluno.append(float(input('Informe a 1ª nota do aluno: ')))
        aluno.append(float(input('Informe a 2ª nota do aluno: ')))
        discentes.append(aluno[:])
        aluno.clear()

print(discentes)
#print(aluno)

"""



#Resolução do Professor
ficha = list()
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media])
    resp = str(input('Quer continuar? [S/N] '))
    if resp in 'Nn':
        break
print('-=' * 30)
print(f'{"No.":<4}{"Nome":<10}{"MÉDIA":>8}')
print('-' * 26)
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    print('-' * 35)
    opc = int(input('Mostrar notas de qual aluno ? (999 interrompe): '))
    if opc == 999:
        print('FINALIZANDO...')
        break
    if opc <= len(ficha) - 1:
        print(f'Notas de {ficha[opc][0]} são {ficha[opc][1]}')
print('<<< VOLTE SEMPRE >>>')





