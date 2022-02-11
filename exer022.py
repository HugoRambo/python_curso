# Crie um programa que leia o nome completo de uma pessoa e mostre:      #lower = diminuir      upeer aumentar
nome = input('Digite seu nome completo :').strip()
print('Analisando seu nome...')
print('Seu nome minusculo é {}'.format(nome.lower()))
print('Seu nome maisculo é {}'.format(nome.upper()))
print('A quantidade de palavras do seu nome é de {}'.format(len(nome) - nome.count(' ')))
print('Seu primeiro nome tem a quantidade de {} letras'.format(nome.find(' ')))