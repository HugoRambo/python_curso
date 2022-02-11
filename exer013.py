 # Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
salario = int(input('Qual é o seu salário atuamente :'))
aumento = salario * 15 / 100
novo_valor = salario + aumento
print(f'Parabens seu novo salario é de {novo_valor}')