# Exercício Python 58: Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10.
# Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.
import random
import time
numeros = random.randint(0, 10)
contador = 1
n = int(input('Digite um numero, tente adivinhar o numero que computador pensou:'))

if n > numeros:
    print('Numero muito maior, digite de 0 a 10 ')
time.sleep(0.5), print('\033[4;32mPensado...')
while n != numeros:
    n = int(input('tente de novo, digite outro numero'))
    contador = contador + 1
    if n > numeros:
        print('Numero muito maior, digite de 0 a 10 ')
print('\033[1;35mParabens voce acertou  o numero coreto é {}, voce usou  {} tentativas.'.format(n, contador))