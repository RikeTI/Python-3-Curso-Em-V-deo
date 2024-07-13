"""
Crie um programa que leia 2 notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
*Média abaixo de 5.0: REPROVADO
*Média entre 5 e 6.9: RECUPERAÇÃO
*Média 7.0 ou superior: APROVADO
"""
n1 = float(input('Informe a primeira nota: '))
n2 = float(input('Informe a segunda nota: '))
média = (n1 + n2) / 2
if média < 5:
    print('Sua média foi: {:.2f} -> \033[4;31mREPROVADO!\033[m'.format(média))
elif 5 <= média < 7:
    print('Sua média foi: {:.2f} -> \033[4;33mRECUPERAÇÃO!\033[m'.format(média))
else:
    print('Sua média foi: {:.2f} -> \033[4;32mAPROVADO!\033[m'.format(média))

#print('\033[1;33mmédia\033[m')

