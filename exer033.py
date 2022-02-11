# Faça um programa que leia três números e mostre qual é o maior e qual é o menor
print('Vamos ver qual é o numero maior, e o menor entre 3 numeros')
primeiro = int(input('Digite o primeiro numero:'))
segundo = int(input('Digite o segundo numero: '))
terceiro = int(input('Digite o terceiro numero:'))
if primeiro < segundo and primeiro < terceiro:
    menor = primeiro
if segundo < primeiro and segundo < terceiro:
    menor = segundo
if terceiro < primeiro and terceiro < segundo:
    menor = terceiro
if primeiro > segundo and primeiro > terceiro:
    maior = primeiro
if segundo > primeiro and segundo > terceiro:
    maior = segundo
if terceiro > primeiro and terceiro > primeiro:
    maior = terceiro
print('O maior  valor digitado foi {}'.format(maior))
print('O menor valor digitado foi {}'.format(menor))