# Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem,
km = int(input('Qual a distancia da sua viagem ?'))  # cobrando R$0,50 por Km para viagens de até 200Km e
valor = float(0.50)  # R$0,45 parta viagens mais longas.
valor1 = float(0.45)
if km <= 200:
    print('Seu valor para essa viagem é de', km * valor)
if km > 200:
    print('Seu valpr para essa viagem é de', km * valor1)