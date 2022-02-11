 # Exercício Python 49: Refaça o DESAFIO 9, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.
n = int(input('Digite um numero para nossa tabuada : '))
for c in range(0, 10 + 1):
    print(n, 'x', c, '=', n * c)
