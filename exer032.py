# Faça um programa que leia um ano qualquer e mostre se ele é bissexto.
ano = int(input('Qual ano você quer descobrir que é bissextos ? '))
if ano % 4 == 0:
    print('Esse ano é bissexto {}'.format(ano))
else:
    print('Esse ano, não é bissexto {}'.format(ano))