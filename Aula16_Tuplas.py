#Tuplas são IMUTÁVEIS
# () Tupla
# [] Lista
# {} Dicionário


#lanche = (' Hambúrguer', 'Suco', 'Pizza', 'Pudim') #Tupla
#print(lanche)


lanche = 'Hambúrguer', 'Suco', 'Pizza', 'Pudim', 'Batata Frita' # Também é Tupla




"""

'''for comida in lanche:
    print(f'Eu vou comer {comida}')
print('Comi pra caramba!')'''

#Exibe a tupla com seus respectivos indíces
'''for cont in range(0, len(lanche)):
    print(f'{cont} : {lanche[cont]}')
print('Comi pra caramba!')'''

#Exibe a tupla com seus respectivos indíces
for pos, comida in enumerate(lanche):
    #print(f'Eu vou comer {comida} na posição {pos}')
    print(f'{pos} : {comida}')
print('Comi pra caramba!')

"""
#print(lanche)
#print(sorted(lanche))


'''a = (2, 5, 4)
b = (5, 8, 1, 2)
print(f'a: {a}\nb: {b}')
c = a + b
d = b + a
print(f'\nc: {c}\nd: {d}')

#print(len(f'Tamanho de C: {c}')) #Comando errado com resultado confuso
print(f'\nTamanho de C: {len(c)}')
print(f'Ocorrências de 5 em C: {c.count(5)}')
print(f'8 está na posição: {c.index(8)} (a contar de 0)')

print(f'\n2 está na posição: {c.index(2, 4)} (a contar de 4)')'''


pessoa = ('Rike', 25, 'M', 83.5)
print(pessoa)
del(pessoa) # Deleta a tupla inteira
# Uma tupla é imutável, mas ela por si é apagável
print(pessoa) # Neste ponto, a tupla "pessoa" não existe mais7
