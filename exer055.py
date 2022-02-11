# Exercício Python 55: Faça um programa que leia o peso de cinco pessoas.
# No final, mostre qual foi o maior e o menor peso lidos
valores = list()
for p in range(1, 6):
    valores.append(float(input('Digite o peso :')))

print('Maior valor digitado é {}'.format(max(valores)))
print('Menor valor digitado foi {}'.format(min(valores)))