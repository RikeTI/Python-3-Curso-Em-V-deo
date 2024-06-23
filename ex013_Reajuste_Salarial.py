"""
Faça um algoritmo que leia o salário de um funcionário e mostre o seu novo salário, com 15% de aumento
"""
salário = float(input('Informe o salário do funcionário: R$'))
aumento = salário * 0.15#salario * 15 / 100 => "15 por cento" DE "salario"
print('O novo salário, acrescido de 15%, será R${:.2f}'.format(salário + aumento))
