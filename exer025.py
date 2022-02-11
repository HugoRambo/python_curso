# Exercício Python 25: Crie um programa que leia o nome de uma pessoa e diga se ela tem “SILVA” no nome.
nome = str(input('Qual é seu nome completo ? ')).strip()
print('Seu nome tem silva ? {} '.format('SILVA' in nome.upper())