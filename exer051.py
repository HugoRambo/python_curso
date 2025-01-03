# Exercício Python 51: Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
# No final, mostre os 10 primeiros termos dessa progressão.
print('\33[1;32m 10 TERMOS DE UMA PA ')
print(30 * '=') 8ecB5CtPoc
a = int(input('Digite o primeiro termo:'))
b = int(input('Digite a razao da PA :'))
decimo = a + (10 - 1) * b
for c in range(a, decimo + b, b):
    print('\33[1;31m{}'.format(c), end='   ->  ')
print('\nACABOU')