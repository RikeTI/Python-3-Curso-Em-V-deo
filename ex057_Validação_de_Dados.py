"""
Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'. Caso esteja errrado, peça a digitação novamente até ter um valor correto.
"""

sexo = str(input('Informe o seu sexo [F/M]: ')).upper().strip()[0]
while sexo not in 'MmFf':
    sexo = str(input('Dados inválidos. Por favor, informe o seu sexo [F/M]: ')).strip().upper()
print('Sexo {} registrado com sucesso'.format(sexo))
