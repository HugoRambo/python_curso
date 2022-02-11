import random
numero = random.randint(0, 5)
print('Pensa um numero de 0 a 5')
numero_pensado = int(input('Digite o numero que pensou'))
print('Processando...')
print('-=-' * 20)
if numero_pensado == numero:
    print('Voce acertou o numero {}'.format(numero))
else:
    print('Voce errou, o numero correoto é {}.'.format(numero))