# Exercício Python 14: Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.
print('__conversor de temperatura__')
cel = int(input('Digite a tempertura em graus Celsius:'))
conversor = cel * 9 / 5 + cel
print(f'A temperatura em Fahrenheit é de  {conversor}')