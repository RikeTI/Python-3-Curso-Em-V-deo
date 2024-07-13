"""
Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
*Equilátero: todos os lados iguais
*Isóscelees: 2 lados iguais
*Escaleno: todos os lados diferentes
"""
import time
l1 = float(input('Informe o tamanho de um lado: '))
l2 = float(input('Informe o tamanho de outro lado: '))
l3 = float(input('Informe o tamanho do último lado: '))
if (l1 < l2 + l3) and (l2 < l1 + l3) and (l3 < l1 + l2):
    print('Analisando...')
    time.sleep(1)
    if l1 == l2 == l3:
        print('Todos os segmentos são iguais -> \033[35mTriângulo Equilátero\033[m')
    elif l1 == l2 or l1 == l3 or l2 == l3:
        print('Dois dos três segmentos são iguais - > \033[34mTriângulo Isósceles\033[m')
    else:
        print('Todos os segmentos são diferentes -> \033[32mTriângulo Escaleno\033[m')
else:
    print('\033[31mOs segmentos informados NÃO FORMAM um Triângulo!\033[m')
