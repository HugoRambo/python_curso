 # Exercício Python 10: Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.
carteira = int(float(input('Quanto de dinheiro você tem na carteira R$ ? ')))
conversor = carteira / 5.90
print('Com esse valor de', (carteira), 'R$', 'você pode comprar', (conversor), 'dolares')
