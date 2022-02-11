# Exercício Python 16: Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.
import math
numero = float(input('Digite um numero:'))
numero_convertido = math.ceil(numero)
print(f'Seu numero digitado foi {numero}, a parte inteira dele é {numero_convertido}')