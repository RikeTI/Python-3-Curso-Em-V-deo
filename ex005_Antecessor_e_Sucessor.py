"""
Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e seu antecessor
"""
n = int(input('Digite um número: '))
#suc = n + 1
#ant = n - 1
print('''O nº informado é {}.
Seu antecessor é {}.
Seu sucessor é {}.'''.format(n, (n-1), (n+1)))
