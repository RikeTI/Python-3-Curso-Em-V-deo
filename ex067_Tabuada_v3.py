"""
Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo.
"""
while True:
    n = int(input('Qual o número você quer ver a tabuada? '))
    if n < 0:
        break
    print('='*20)
    for i in range(1, 11):
        print(f'{n:^5} x {i:^3} = {n*i:^4}')
    print('='*20)
print('Número negativo informado. Fim do Loop!')
