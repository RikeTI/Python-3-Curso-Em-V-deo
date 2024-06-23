"""
Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar
US$1,00 = R$5,41 (cotação 13/06/2024)


---------------------------------------------------
Tarefa Extra: Conversão de outras moedas (Cotação 14/06/2024)
Dólar   | Estados Unidos (USD)  | US$   | R$5,41
Iene    | Japão (JPY)           | ¥     | R$0,034
Peso    | Argentina (ARS)       | $     | R$0,0059
Dinar   | Kwait (KWD)           | د.ك   | R$17,49

"""
real = float(input('Quanto dinheiro você tem? R$'))
dolar = 5.41
iene = 0.034
peso = 0.0059
dinar = 17.49

print('Com R${:.2f} você pode comprar até US${:.4f} (dolár americano)'.format(real, real/dolar))
print('Com R${:.2f} você pode comprar até ¥{:.4f} (iene japonês)'.format(real, real/iene))
print('Com R${:.2f} você pode comprar até ${:.4f} (peso argentino)'.format(real, real/peso))
print('Com R${:.2f} você pode comprar até د.ك {:.4f} (dinar kwaitiano)'.format(real, real/dinar))

