#Exercício Python 65: Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
# O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.


numero = 0
valor = 0
quantidade = 0
numeros = 0
maior = 0
menor = 0
cont = str(input('Quer iniciar o programa: [S/N]')).upper().strip()[0] #removendo espaços e deixando tudo para maiscula
while cont == 'S':
    num = int(input('Digite um numero : '))
    cont = str(input('Quer continuar [S/N]')).upper().strip()[0] #removendo espaços e deixando tudo para maiscula
    numero = numero + num
    valor = valor + 1
    quantidade = quantidade + 1
    if quantidade ==1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num

print('Voce digitou {} numeros, e medida foi {}'.format(quantidade, numero / valor))
print('O maior valor foi {}, e o menor valor {}'.format(maior, menor))