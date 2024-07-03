'''tempo = int(input('Quantos anos tem seu carro? '))
if tempo <= 3:
    print('carro novo')
else:
    print('carro velho')
print('--FIM--')'''

'''#Condição Simplificada
tempo = int(input('Quantos anos tem seu carro? '))
print('carro novo' if tempo <= 3 else 'carro velho')
print('--FIM--')'''

'''nome = str(input('Qual é seu nome? ')).title()
if nome == 'Rike':
    print('Que nome lindo você tem!')
else:
    print('Seu nome é tão normal!')
print('Bom dia, {}!'.format(nome))'''



n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2) / 2
print('A sua média foi {:.1f}'.format(m))
print('PARABÉNS!' if m >= 6 else 'ESTUDE MAIS!')





