'''
#num = (2, 5, 9, 1) # Tupla -> Imutável
num = [2, 5, 9, 1]
print(num)
num[2] = 3# É possível mudar os elementos
#num[4] = 7# Porém, não é possível add novos por esse método
num.append(7)# Adiciona um novo elemento ao final da lista
num.sort()# Põe os elementos em ordem crescente
print(num)
num.sort(reverse=True)# Ordem decrescente
print(num)
num.insert(2, 0)# Adiciona o elemento "0" na posição 2
print(num)
num.pop()# Remove o último elemento da lista
print(f'Essa lista tem {len(num)} elementos.')
num.insert(2, 2)# .insert(pos, ele) -> Na posição 2, Adicione o elemento 2
print(num)
num.remove(2)# Remove a 1ª ocorrência do elemento, a contar da esquerda para direita
print(num)
if 4 in num:
    num.remove(4)
    print(f'Removi o número 4')
else:
    print('Não achei o número 4')
if 5 in num:
    num.remove(5)
    print(f'Removi o número 5')
    print(num)
else:
    print('Não achei o número 5')
'''

'''
valores = [] #Mesmo resultado -> valores = list()
valores.append(5)
valores.append(9)
valores.append(4)
#print(valores)
#for v in valores:
#    print(f'{v}...', end='')

for cont in range(0, 5):
    valores.append(int(input('Digite um valor: ')))# Serão adicionados elementos ao final da lista; da posição 3 em diante

for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}!')
print('Cheguei ao final da lista.')
'''


a = [2, 3, 4, 7]
b = a # Isso não cria uma cópia da lista, mas sim faz uma ligação entre 2 listas
print(f'Lista A: {a}')
print('='*22)
b[2] = 8# Como resultado, a alteração de uma lista afeta a a outra
print(f'Lista A: {a}')
print(f'Lista B: {b}')
print('='*22)
c = a[:]
c[2] = 9
print(f'Lista A: {a}')
print(f'Lista B: {b}')
print(f'Lista C: {c}')



