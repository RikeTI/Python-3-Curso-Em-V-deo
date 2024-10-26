"""
Crie um programa onde o usuário possa digitar 5 valores numércios e cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.
"""
#Resolução do Professor
lista = []
for c in range(0, 3):
    n = int(input('Digite um valor: '))
    if c == 0 or  n > lista[-1]:
        lista.append(n)
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                break
            pos += 1
print('-=' * 30)
print(f'Os valores digitados em ordem foram {lista}')



"""
#Incompleto
valores = []
for i in range(0,3):
    valores.append(int(input('Digite um número: '))) 
    if i == 0:
        temp = valores[i]                 # temp = valores[0]
        pos1 = valores.index(valores[i])
    else:
       for pos in range(len(valores)):
            if valores[i] < valores[pos]: # valores[1] < valores[0]
                valores[pos] = valores[i] # valores[0] = valores[1]
                valores[i] = temp         # valores[1] = temp
                temp = valores[i]
print('=-'*20)
print(valores)
"""
 
"""Rascunho
valores = []
for i in range(0,2):
    valores.append(int(input('Digite um número: '))) 
    if i == 0:
        temp = valores[i]
        pos1 = valores.index(valores[i])
    else:
       for pos in range(len(valores)):
           print(f'Na posição {pos}, encontrei o valor {valores[i]}')
       ''' if valores[i] < temp: #valores[0]
            valores[pos1] = valores[i]
            valores[i] = temp
            temp = valores[i]'''   
print('=-'*20)
print(valores)
#for c, v in enumerate(valores):
    #print(f'Na posição {c}, encontrei o valor {v}')
#print(f'Valor: {valores[0]}')
#print(f'Posição: {pos1}')
"""

   
'''
num = [9, 4, 5]
print(num)
num.insert(2, 3)
print(num)
pos = num.index(3)
print(pos)
num.insert(pos, 11) # Inserte é para ADICIONAR, não substituir
print(num)
print(len(num))
num[4] = 6
print(num)
#>>> [9, 4, 5]
#>>> [9, 4, 3, 5]
#>>> 2
#>>> [9, 4, 11, 3, 5]
#>>> 5
#>>> [9, 4, 11, 3, 6]
'''