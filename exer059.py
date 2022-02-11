# Exercício Python 059: Crie um programa que leia dois valores e mostre um menu na tela:
    # [ 1 ] somar
    # [ 2 ] multiplicar
    # [ 3 ] maior
    # [ 4 ] novos números
    # [ 5 ] sair do programa
    # Seu programa deverá realizar a operação solicitada em cada caso.
valor1 = int(input('Digite o primeiro valor : '))
print('=' * 70)
valor2 = int(input('Digite o segundo valor : '))
opção = 0
while opção != '5':
    print('=' * 70)
    print('''
        [1] SOMAR
        [2] MULTIPLICAR
        [3] MAIOR
        [4] NOVOS NÚMEROS
        [5] SAIR DO PROGRAMA''')
    opção = str(input('digite a operação que queira fazer'))
    if opção == '1':
        a = valor1 + valor2
        print('Voce escolheu somar, {} + {} é igual a {}'.format(valor1, valor2, a))
    elif opção == '2':
        b = valor1 * valor2
        print('Você escolheu multiplicar, {} X {} é igual a {}'.format(valor1, valor2, b ))
    elif opção == '3':
        lista = [valor1, valor2]
        print('Voce escolheu saber quem é o maior ',(max(lista)))
    if opção =='4':
        valor1 = int(input('Digite o primeiro valor : '))
        print('=' * 70)
        valor2 = int(input('Digite o segundo valor : '))
else:
    print('Voce escolheu sair do programa.')