# Exercício Python 56: Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: a média de idade do grupo,
# qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.
somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomevelho = ''
totmulher20 = 0
for p in range(1, 5):
    print(f'-------{p}PESSOA----------')
    nome = str(input('Nome : '))
    idade = int(input('Idade : '))
    sexo = str(input('Sexo [M/F] : '))
    somaidade = somaidade + idade
    if p == 1 and sexo in 'Mm':  ##Se a primeira pessoa for... da range, se for M também...
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        totmulher20 = totmulher20 + 1

mediaidade = somaidade / p  # dividi os valores coletados pela range
print('A média de idade do grupo é de {}anos'.format(mediaidade))
print('O Homem mais velho tem {}, anos e se chama {}'.format(maioridadehomem, nomevelho))
print('Ao todo são {} mulheres com menos de 20 anos'.format(totmulher20))