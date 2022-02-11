# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triangulo retangulo
    # Calcule e mostre o coprimento da hipotenusa
import math
print('Vou te ajudar com calculo de hipotenusa')
cateto = float(input('Valor do cateto 1  ? '))
cateto2 = float(input('Valor do cateto 2 ?'))
hipotenusa = cateto * cateto
hipotenusa1 = cateto2 * cateto2
resultado = hipotenusa1 + hipotenusa
print(resultado)
raiz = math.sqrt(resultado)
print(f'Valor da sua hiponesua é {raiz} ')