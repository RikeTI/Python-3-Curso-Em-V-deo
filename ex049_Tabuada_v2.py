"""
Refaça o Desafio 009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço FOR.
"""
#n = int(input('Digite um número para ver a sua tabuada: '))
n=9
print('='*13)
for c in range(1, 11):
    m = n * c
    print('{:<2} x {:>2} = {}'.format(n, c, m))
print('='*13)
