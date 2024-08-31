"""
Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999 (flag), que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).
"""
acc = cont = 0
while True:
    n = int(input('Digite um número [999 p/ parar]: '))
    if n == 999:
        break
    else:
        cont += 1
        acc += n
print('{} números foram digitados'.format(cont))
print('A soma de todos os números foi {}'.format(acc))


'''#Resolução do Professor
núm = cont = soma = 0
núm = int(input('Digite um número [999 para parar]: '))
while núm != 999:
    soma += núm
    cont += 1
    núm = int(input('Digite um número [999 para parar]: '))
print('Você digitou {} números e a soma entre eles foi {}'.format(cont, soma))'''
