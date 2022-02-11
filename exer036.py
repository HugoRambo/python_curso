# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
# A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.
print('Vamos calcular se você pode financia sua casa.')
casa = float(input('Qual o valor da casa R$ :'))  # valor da casa
salario = float(input('Qual é o seu salário : '))  # salario mensal
tempo = int(input('Quantos anos voce quer pagar você quer pagar :'))  # Tempo que quer pagar
prestacao = casa / (tempo * 12)  # valor casa divido  pelo tempo vezes 12
minimo = salario * 30 / 100  # tirou os 30% do salario
if prestacao <= minimo:
    print('Você pode comprar a casa, pagara por mes {}'.format(minimo))
else:
    print('Negado a compra')