'''
teste = list()
teste.append('Rike')
teste.append(26)
galera = list()
galera.append(teste[:])
print(galera)

teste[0] = 'Maria'
teste[1] = 22
galera.append(teste)
print(galera)
'''

'''
galera = [['João', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]
print(galera)
print(galera[1])
print(galera[2][0])
print('-=' * 20)
for p in galera:
    print(p) #Vai imprimir todas as listas internas
print('-=' * 20)

for q in galera:
    print(q[0])#Vai imprimir somente o 1º elemento de cada lista    
print('-=' * 20)

for r in galera:
    print(f'{r[0]} tem {r[1]} anos de idade')
'''

totmai = totmen = 0
galera = list()
dado = list()
for c in range(0, 3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:]) #Cria uma cópia do conteúdo da lista 'dado' na lista 'galera'
    dado.clear()#Limpa a lista
print(galera)
print('-=' * 20)
for p in galera:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade.')
        totmai += 1
    else:
        print(f'{p[0]} é menor de idade.')
        totmen += 1
print(f'Temos {totmai} maiores e {totmen} menores de idade.')
