frase = 'Curso em Vídeo Python'
print(frase)
print(frase[0])#Pega o caracter da posição 0, que é o 1º elemento
print(frase[9:13])#Pega os caracteres da posição até a posição 12 
print(frase[9:21])#Pega os caracteres de 9 a 20
print(frase[9:21:2])#Pega os caracteres de 9 a 20, pulando de 2 em 2
print(frase[:5])#Da posição 0 até a posição 5
print(frase[15:])#Da posição 15 até o final
print(frase[9::3])#Da posição 9 até o final, pulando de 3 em 3
print('~'*60)

#Análise
print('Há {} caracteres (incluindo os espaços em branco)'.format(len(frase)))
print(frase[-1])#Elemento na última posição
print('A letra "{}" aparece {} veze(s) nesta string/cadeia de caracteres'.format('o', frase.count('o')))
print('A letra "{}" aparece {} veze(s) neste intervalo'.format('o', frase.count('o', 0, 13)))#Realiza a contagem das aparições da letra "o" dentro do intervalo especificado -- de 0 a 13.
print(frase.find('deo'))#Comando para encontrar a posição do termo espeficidado -- ele retornará a posição da 1ª aparição (ou onde começou), mesmo se houver repetidos
print(frase.find('Android'))#Retorna "-1" se não encontrar nada
print('Curso' in frase)#"in" é um Operador que retorna True ou False SE O TERMO ESPECIFICADO existir na variável => "'Curso' 'existe' em frase?" True
print('~'*60)

#Transformação
frase = frase.replace('Python', "Android")
print(frase)
print(frase.upper())#Maiúsculos
print(frase.lower())
print(frase.capitalize())
print(frase.title())
print('-'*10)
frase = 'Aprendenda Python'
print('"{}" tem {} caracteres (incluindo espaços em branco)'.format(frase, len(frase)))
frase = '   Aprendenda Python  '#Foram adicionar 5 espaços (3 no início e 2 no final)
print('"{}" tem {} caracteres (incluindo espaços em branco)'.format(frase, len(frase)))
print(frase.rstrip())#Right-Strip => Elimina os espaços à direita
print(frase.lstrip())#Left-Strip => Elimina os espaços à esquerda
frase = frase.strip()#Elimina os espaços no início e no fim
print(frase)
print('~'*60)

#Divisão
frase = 'Curso em Vídeo Python'
print(frase)
frase = frase.split()#Divide uma string em listas, em tantos quanto forem os espaços em branco internos
print(frase)
frase = '-'.join(frase)#Junta as diferentes strings ou listas com o caracter entre aspas simples (que no caso foi o traço)
print(frase)
print()
print('Há {} letra(s) "{}" na frase {}.\nPorém, há {} "{}" na mesma frase, pois o Python diferencia maiúsculas de minúsculas.'.format(frase.count(frase[4]), frase[4], frase, frase.count(frase[4].upper()), frase[4].upper()))
print(frase.upper().count(frase[0]))
print(frase.replace('Python', 'Android'))
print()
frase = 'Curso em Vídeo Android'
print(frase)
print(frase[0])
frase = frase.split()
print(frase)
print(frase[0])
print(frase[0][0])
print()
print("""Lorem Ipsum é simplesmente um texto fictício da indústria de impressão e composição tipográfica. Lorem Ipsum tem sido o texto fictício padrão da indústria desde 1500, quando um impressor desconhecido pegou uma prova de tipos e a misturou para fazer um livro de espécimes de tipos. Ela sobreviveu não apenas a cinco séculos, mas também ao salto para a composição tipográfica eletrônica, permanecendo essencialmente inalterada. Foi popularizado na década de 1960 com o lançamento de folhas Letraset contendo passagens de Lorem Ipsum e, mais recentemente, com software de editoração eletrônica como Aldus PageMaker, incluindo versões de Lorem Ipsum.""")



