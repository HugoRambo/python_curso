# Exercício Python 46: Faça um programa que mostre na tela uma contagem
    # regressiva para o estouro de fogos de artifício, indo de 10 até 0, com uma pausa de 1 segundo entre eles.
import emoji
import time
for c in range(11, 0, -1):
    print('Contagem regressiva... {} '.format(c - 1))
    time.sleep(0.5)
print('Buuum estourou ')