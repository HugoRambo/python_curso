#Exercício Python 67: Faça um programa que mostre a tabuada de vários números,#
# um de cada vez, para cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo


tabuada = 0
valor = 0
num = int(input('Digite um numero que queira tirar a tabuada: '))
if num < 0:
    exit(print('Programa não funciona com numeros abaixo de zero '))
while True:
    valor  = valor +1
    print(f'{valor} x  {num} é igual = {valor * num}')
    tabuada = tabuada +1
    if tabuada == 10:
        exercicio67()
    if num < 0:
        break
print('Programa tabuada encerrado. ')