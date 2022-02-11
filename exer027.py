# Exercício Python 27: Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.
nome = str(input('Digite seu nome :')).strip().capitalize()
cortado = nome.split()
print('Muito prazer em te conhecer, bonitão !')
print('Seu primeiro nome é {}'.format(cortado[0].capitalize()))
print('Seu segundo nome é {}'.format(cortado[1].capitalize()))
print('Seu terceiro nome é {}'.format(cortado[2].capitalize()))