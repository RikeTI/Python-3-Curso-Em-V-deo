"""
Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:
*A média de idade do grupo.
*Qual é o nome do homem mais velho.
*Quantas mulheres têm menos de 20 anos.
"""

'''LÓGICA DE PROGRAMAÇÃO
Ler nome x4
Ler idade x4
Ler sexo x4
qtd = For x4
Média_Idade = (idade1 + idade2 + idade3 + idade4) / qtd 

nome_velho = ''
idade_velho = 0
idade_nova = 0
Para x até 5: Laço FOR
    Ler nome: 'Informe o nome':     String 
    Ler idade: 'Informe a idade':   Int 
    Ler sexo: 'Informe o sexo':     String
    Se sexo == F
        Se idade < 20:
            idade_nova = idade_nova + 1
    Senão, sexo == M:
        Se idade_velho == 0:
            idade_velho = idade
        Senão:
            Se idade > idade_velho:
                idade_velho = idade
'''
idade_velho = idade_nova = somaIdade = 0
for x in range(1, 5):
    nome = str(input('Informe o nome da {}ª pessoa: '.format(x))).title()
    idade = int(input('Informe a idade da {}ª pessoa: '.format(x)))
    sexo = str(input('Informe o sexo da {}ª pessoa [M/F]: '.format(x))).upper()
    somaIdade += idade
    if sexo[0] == 'F':
        if idade < 20:
            idade_nova = idade_nova + 1
    elif sexo[0] == 'M':
        if idade_velho == 0:
            idade_velho = idade
        else:
            if idade > idade_velho:
                idade_velho = idade
                nome_velho = nome
médiaIdade = somaIdade / x
print('O nome do homem mais velho é {}'.format(nome_velho))
print('{} mulheres com menos de 20 anos'.format(idade_nova))
print('A média das idades é {:.2f}'.format(médiaIdade))    
    
#print('~'*15)
#print('Nome: {}\nIdade: {}\nSexo: {}'.format(nome, idade, sexo[0]))
#print('~'*15)


#Resolução do Professor
'''
somaidade = média = maioridadehomem = totmulher20 = 0
nomevelho = ''
for p in range(1, 5):
    print('-----{}ª PESSOA -----'.format(format(p)))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    somaidade += idade
    if p == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        totmulher20 += 1
médiaidade = somaidade / 4
print('A média de idade do grupo é de {} anos'.format(médiaidade))
print('O homem mais velho tem {} anos e se chama {}'.format(maioridadehomem, nome_velho))
print('Ao todo são {} mulheres com menos de 20 anos'.format(totmulher20))
'''

