# Exercício Python 37: Escreva um programa em Python que leia um número inteiro qualquer e peça para o
# usuário escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.
numero = int(input('Digite um numero inteiro :'))
print('''Qual tipo de base de conversão:  
    [1] Binario
    [2] Octal
    [3] Hexadecimal''')
opção = int(input('Qual sua opção:'))
if opção == 1:
    print('O numero convertido para binario é {}'.format(bin(numero)))
elif opção == 2:
    print('O numero convertido para octal {}'.format(oct(numero)))
elif opção == 3:
    print('O numero convertido para Hexadecial é {}'.format(hex(numero)))
else:
    print('conversão escolhida não é valida')