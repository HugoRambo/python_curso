# Exercício Python 54: Crie um programa que leia o ano de nascimento de sete pessoas.
# No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores
from datetime import date
atual = date.today().year
contadormaior = 0  # contandor ajuda altos, bom pra tratar informação
contadormenor = 0
for pess in range(1, 8):
    nasc = int(input('Qual sua data de nascimento:'))
    idade = atual - nasc
    if idade >= 18:
        contadormaior += 1
    else:
        contadormenor += 1
print('Ao total tivemos {}, pessoas maiores de idade'.format(contadormaior))
print('Ao total tivemos {}, pessoas menores de idade'.format(contadormenor))