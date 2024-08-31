#Adicionando o comando BREAK para interromper o while
'''n = s = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    s += n
print(f'A soma vale {s}')'''



#Estreantes(? Fstrings): Formatação do Python 3.6+
nome = ' Rike '
idade = 25
salário = 2028.35
print(f'O {nome:-^15} tem {idade} anos e ganhava R${salário:.2f}')


