# Exercício Python 041: A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria,
    # de acordo com a idade:
    # Até 9 anos: MIRIM
    # Até 14 anos: INFANTIL
    # Até 19 anos: JÚNIOR
    # Até 25 anos: SÊNIOR
    # Acima de 25 anos: MASTER
from datetime import date
atual = date.today().year
ano = int(input('Digite ano de nascimento :'))
valor = atual - ano
if valor <= 9:
    print('Vocé e da categoria MIRIM, ')
    print(f'Atleta tem {valor} anos')
elif valor > 9 and valor < 14:
    print('Você é da categoria INFANTIL')
    print(f'Atleta tem {valor} anos')
elif valor > 14 and valor < 19:
    print('Você é da categoria Junior')
    print(f'atleta tem idade de {valor}')
elif valor > 19 and valor < 25:
    print('Você é da categoria SÊNIOR ')
    print(f'Atleta tem idade de {valor}')
else:
    print('Você é master manolo. ')