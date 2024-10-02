"""
Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.
"""

feitiços = ('Telecinese', 'Pirocinese', 'Hidrocinese', 'Geocinese', 'Aerocinese', 'Fotocinese', 'Umbracinese')
vogais = ('a', 'e', 'i', 'o', 'u')

for p in feitiços:
    print(p, end=' ')
    for v in vogais:
        if v in p:
            print(v, end=' ')
    print()   


#Resolução do Professor
palavras = ('aprender', 'programar', 'linguagem', 'python', 'curso', 'gratis', 'estudar', 'praticar', 'trabalhar', 'mercado', 'programador', 'futuro')

for p in palavras:
    print(f'\nNa palavra {p.upper()} temos ', end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')


