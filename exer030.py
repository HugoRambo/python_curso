# Exercício Python 30: Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.
numero = int(input('digite um numero:'))
resultado = numero % 2
if resultado == 0:
    print('Numero é par {}'.format(resultado))
else:
    print('Numero impar {}'.format(resultado))