# Exercício Python 28: Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 e
# peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
# O programa deverá escrever na tela se o usuário venceu ou perdeu.
print('Vou pensar um numero de 0 a 5, tente adivinhar')
numero = int(input('Digite o numero: '))
numero_correto = 4
if numero == 4:
    print('Parabéns você ganhou o numero correto é {}'.format(numero))
else:
    print('Você perdeu o numero correto é {}'.format(numero_correto))