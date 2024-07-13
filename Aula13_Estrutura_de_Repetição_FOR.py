'''
print('FOR 0, 6 -> Incremento de 0 a 5, contando de 1 em 1 -> ', end=' ' )
for c in range(0, 6):
    print(c, end=' ')

print()

print('FOR 6, 0, -1 -> Decremento de 6 a 1, contando de 1 em 1 -> ', end=' ' )
for c in range(6, 0, -1):
#O incremento negativo só funciona se deixar explícito. "for c in range(6, 0)" não irá funcionar
    print(c, end=' ')

print()

print('FOR 1, 7, 2 -> Incremento de 1 a 6, contando de 2 em 2 -> ', end=' ' )
for c in range(1, 7, 2):
    print(c, end=' ')
'''


print('>>> Estrutura de Repetição FOR <<<\n > Informe os valores de Início, de Fim e de Contagem (Passo) <')
somador = 0

início = int(input('Início: '))
passo = int(input('Contagem (Passo): '))
fim = int(input('Fim: '))
'''for x in range(início, fim + 1, passo):
    print(x, end=' ')
print('FIM!')'''

#i, p, f = 1, 1, 5
print('A soma de', end=' ')
for x in range(início, fim, passo):#Vai repetir de 1 a 4
    somador = somador + x
    print('{}'.format(x), end=' + ')
print(fim, end=' = ')
print(somador + fim)
#print('A soma de todos os números dentro repetição é {}'.format(somador))






