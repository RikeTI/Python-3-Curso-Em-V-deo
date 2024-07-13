"""
Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50
"""
'''for i in range(1, 50+1): #50 laços
    #print('.', end='')
    if i % 2 == 0:
        print(i, end=' ')'''

#Mais eficiente que o de cima. 
#Não fará diferença alguma no presente momento devido a simplicidade do programa, mas para códigos maiores, isso faz diferença
for i in range(2, 51, 2): #25 laços
    if i % 2 == 0:
        print(i, end=' ')           
