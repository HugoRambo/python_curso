# Exercício Python 57: Faça um programa que leia o sexo de uma pessoa,
# mas só aceite os valores ‘M’ ou ‘F’. Caso esteja errado, peça a digitação novamente até ter um valor correto.
sexo = 0
pessoa = 0
while sexo != 1:
    c = str(input('Digite seu sexo, [F/M]')).strip().upper()[0]
    if c == 'F':
        print('Sexo {}'.format(c))
        pessoa = pessoa + 1
        return print('Seu sexto é {}'.format(c))
    elif c == 'M':
        print('Sexo {}.'.format(c))
        pessoa = pessoa + 1
        return print('Seu sexto é {}'.format(c))
    else:
        print('Sexo não existe, digitar um valor valido')