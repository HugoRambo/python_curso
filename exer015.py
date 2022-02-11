# Exercício Python 15: Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado
print('Bem vindo ao simulador de gastos de alugel de carro')
km = float(input('Quantos quilometros voces percorreu com seu carro ? '))
dia = int(input('Quantos dias você ficou com o carro:'))

custo_km = km * 0.15
custo_dia = dia * 60
print(custo_km)
print(custo_dia)