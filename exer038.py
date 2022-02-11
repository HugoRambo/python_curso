# Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:
n1 = int(input('Digite um numero inteiro:'))
n2 = int(input('Digite outro numero inteiro:'))
if n1 > n2:
    print('O numero maior é {} e o menor {}'.format(n1, n2))
elif n2 > n1:
    print('O numero maior é {} e o menor {}'.format(n2, n1))
else:
    print('Não existe valor maior, os dois são iguais')