"""
A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
*Até 9 anos: MIRIM.
*Até 14 anos: INFANTIL.
*Até 19 anos: JÚNIOR
*Até 25 anos: SÊNIOR
*Acima: MASTER
----------
Cores: Cinza -> Vermelho -> Verde -> Amarelo -> Azul -> Roxo -> Ciano -> Branco
"""


ano = int(input('Informe o ano de nascimento do atleta: '))
from datetime import date
idade = abs(ano - (date.today().year))
if idade <= 9:
    print('{} anos.\nCategoria \033[33mMIRIM.\033'.format(idade))
elif 9 < idade <= 14:
    print('{} anos.\nCategoria \033[34mINFANTIL.\033[m'.format(idade))
elif idade <= 19:
    print('{} anos.\nCategoria \033[35mJÚNIOR.\033[m'.format(idade))
elif idade <= 25:
    print('{} anos.\nCategoria\033[36m SÊNIOR.\033[m'.format(idade))
else:
    print('{} anos.\nCategoria \033[7;37mMASTER.\033[m'.format(idade))
