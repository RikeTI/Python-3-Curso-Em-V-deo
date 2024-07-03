"""
Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários superiores a R$1.250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.
"""
salário = float(input('Informe o salário do funcionário: R$'))
#print('{:.2f}'.format(salário))
novo = salário * 1.1 if salário > 1250 else salário * 1.15
print('Quem ganha R${:.2f}, passa a ganhar R${:.2f}'.format(salário, novo))
