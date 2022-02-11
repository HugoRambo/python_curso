# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
import math
angulo = float(input('Digite o angulo que você deseja'))
seno = math.sin(math.radians(angulo))
print('Seno desse algulo é {}'.format(seno))