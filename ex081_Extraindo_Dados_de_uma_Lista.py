"""
Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
a) Quantos números foram digitados;
b) A lista de valores, ordenada de forma decrescente;
c) Se o valor 5 foi digitado e está ou não na lista.
"""
lista = []
lista.append(int(input('Digite um valor: ')))
while True:
    op = input('Quer continuar? [S/N] ').upper()
    if op == 'N':
        break
    elif op == 'S':
        lista.append(int(input('Digite um valor: ')))
    else:
        print('Opção Inválida!')  
print(f'Foram digitados {len(lista)} elementos ao todo.')
lista.sort(reverse=True)
print(lista)
print('5 se encontra na lista' if 5 in lista else '5 não se encontra na lista')  
