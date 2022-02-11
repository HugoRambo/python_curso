# Exercício Python 34: Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários superiores a R$1250,00,
# calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.
print('Vamos calcular um aumento do seu salario ')
salario = float(input('Digite seu salario'))
if salario <= 1250.00:
    aumento = (15 * salario) / 100
    print('Seu aumento foi de {}'.format(aumento))
    print('Apartir de agora ele é de {}'.format(salario + aumento))
else:
    aumento = (10 * salario) / 100
    print('Seu salaário aumentou {}'.format(aumento))
    print('Apartir de agora ele é de {}'.format(salario + aumento))