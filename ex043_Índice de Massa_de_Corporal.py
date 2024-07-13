"""
Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status de acordo com a tabela abaixo:
*Abaixo de 18.5: Abaixo do Peso
*Entre 18.5 e 25: Peso Ideal
*25 até 30: Sobrepeso
*Acima de 40: Obesidade Mórbida
"""
peso = float(input('Informe o seu peso (em Kg): '))
altura = float(input('Informe a sua altura (em metros): '))
imc = (peso) / (altura * altura)
if imc < 18.5:
    print('Seu peso é de {}\nSua altura é de {}\nSeu IMC resultou em {:.2f} -> \033[35mAbaixo do Peso\033[m'.format(peso, altura, imc))
elif 18.5 <= imc < 25:
    print('Seu peso é de {} kg\nSua altura é de {} m\nSeu IMC resultou em {:.2f} -> \033[32mPeso Ideal\033[m'.format(peso, altura, imc))
elif 25 <= imc < 30:
    print('Seu peso é de {} kg\nSua altura é de {} m\nSeu IMC resultou em {:.2f} -> \033[4;32mSobrepeso\033[m'.format(peso, altura, imc))
elif 30 <= imc <= 40:
    print('Seu peso é de {} kg\nSua altura é de {} m\nSeu IMC resultou em {:.2f} -> \033[33mObesidade\033[m'.format(peso, altura, imc))
else: # imc > 40
    print('Seu peso é de {} kg\nSua altura é de {} m\nSeu IMC resultou em {:.2f} -> \033[31mObesidade Mórbida\033[m'.format(peso, altura, imc))