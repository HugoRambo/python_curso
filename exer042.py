# Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
    # Exercício Python 35: Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.
    # Regra do triangulo, o resultado da soma de dois lados, não pode ser maior que um dos lados. '''
r1 = float(input('Digite a primeira medida : '))
r2 = float(input('Digite a segunda medida : '))
r3 = float(input('Digite a terceira medida :'))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Esses numeros, PODEM FORMAR um triangulo', end=' ')
    if r1 == r2 == r3:
        print('Equilatero')
    elif r1 != r2 != 3 != r1:
        print('ESCALENO')
    else:
        print('ISÓSCELES')
else:
    print('Não pode formar nenhum triangulo')
