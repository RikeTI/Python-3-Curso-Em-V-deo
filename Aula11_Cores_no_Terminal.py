'''
\033[Style;Text;Backm => [Estilo:Texto:Fundom]
Style:
0 => None (Sem estilo
1 => Bold (Negrito)
4 => Underline (Sublinhado)
7 => Negative (inverte as cores de texto e fundo

Text:
30 => Cinza  | 31 => Vermelho | 32 => Verde | 33 => Amarelo | 34 => Azul | 35 => Roxo | 36 => Ciano | 37 => Branco 

Back:
40 => Cinza | 41 => Vermelho | 42 => Verde | 43 => Amarelo | 44 => Azul | 45 => Roxo | 46 => Ciano | 47 => Branco
'''


'''#Negrito e Vermelho
print('\033[1;31mHello, world!\033[m')
#Finalize com '\033' para que a formatação seja limitada ao que estiver dentro do código 033.
print()
a = 3
b = 5

print('Os valores são \033[33m{}\033[m e \033[36m{}\033[m!!!'.format(a, b))
'''
#nome = input('Digite o seu nome: ').title()
#print('Muito prazer em te conhecer, {}{}{}!'.format('\033[4;34m', nome, '\033[m'))
'''
Fundo Vermelho, Fonte Branca
Fundo Azul, Fonte Amarela
Fundo Amarelo, Fonte Roxa
Fundo Verde, Fonte Branca
Fundo Preto, Fonte Branca
Fundo Branco, Fonte Preta
'''
#Acrescendo um espaço vazio antes e depois do "Teste"
print('\033[1;30;41m Teste \033[m')
print('\033[4;33;44m Teste \033[m')
print('\033[1;35;43m Teste \033[m')
print('\033[4;37;42m Teste \033[m')
print('\033[1;37m Teste \033[m')
print('\033[4;47m Teste \033[m')

