"""
Crie uma preenchida com os 20 primeiros colocados da Tabela Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
a) Apenas os 5 primeiros colocados.
b) Os últimos 4 colocados da tabela.
c) Uma lista com os times em ordem alfabética.
d) Em que posição na tabela está o time da Chapecoense?
"""

times = ('Corinthians', 'Palmeiras', 'Santos', 'Grêmio', 'Cruzeiro', 'Flamengo', 'Vasco', 'Chapecoense', 'Atlético', 'Botafogo', 'Atlético-PR', 'Bahia', 'São Paulo', 'Fluminese', 'Sport Recife', 'EC Vitória', 'Curitiba', 'Avaí', 'Ponte Preta', 'Atlético-GO')

# INCOMPLETO
# Letra (a)
#print('Os 5 primeiros colocados:  ', end='')
#for a in range(0, 5):
#    print(f'>> \033[1;35m{times[a]}\033[m', end=' << ')
#print()
# Letra (b)
#print('Os 4 últimos colocados: ', end='')
#for b in range(-1, -5, -1):
#    print(f'>> \033[1;32m {times[b]} \033[m', end=' << ')
#print()
# Letra (c)
#print(sorted(times))


#Resolução do Professor
print('-='*15)
print(f'Lista de times do Brasileirão: {times}')
print('-='*15)
print(f'Os 5 primeiros são {times[0:5]}')
print('-='*15)
print(f'Os 4 últimos são {times[-4:]}')
print('-='*15)
print(f'Times em ordem alfabética: {sorted(times)}')
print('-='*15)
print(f'O Chapecoense está na {times.index("Chapecoense")+1}ª posição')

