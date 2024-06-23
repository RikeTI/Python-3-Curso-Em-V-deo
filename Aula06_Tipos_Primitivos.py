#Programa errado. Realiza concatenaçã ao invés de soma.
'''
n1 = input('Digite um número: ')# "n1 = " -> "n1 recebe"
n2 = input('Digite mais um número: ')

s = n1 + n2
print('A soma vale', s)
'''


'''
#Convertendo as strings em numerais inteiros
n1 = int(input('Digite um número: '))
n2 = int(input('Digite mais um número: '))
s = n1 + n2
print('A soma vale {}'.format(s))
#" {} " é uma máscara para realizar a formatação
'''

n1 = input('Digite um valor: ')
print('Inicialmente, ', end='')
print('{} é {}'.format(n1, type(n1)))
n1 = int(n1)
print('Agora,', end=' ')
print('{} é {}'.format(n1, type(n1)))

print()
