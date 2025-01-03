# Exercício Python 43: Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC)
    # e mostre seu status, de acordo com a tabela abaixo:
    # IMC abaixo de 18,5: Abaixo do Peso
    # Entre 18,5 e 25: Peso Ideal
    # 25 até 30: Sobrepeso
    # 30 até 40: Obesidade
    # Acima de 40: Obesidade Mórbida
print('Vamos calcula seu IMC')
altura = float(input('Digite sua altura :'))
peso = float(input('Digite seu peso : '))
calculo = peso / (altura * altura)
if calculo <= 18.5:
    print('Voce esta abaixo do peso, seu IMC é de {:.1f}'.format(calculo))
elif calculo <= 18.5 or calculo <= 25:
    print('Voce esta no peso ideal {:.1f}.'.format(calculo))
elif calculo <= 25 or calculo <= 30:
    print('Voce esta com sobre peso {:.1f}'.format(calculo))
elif calculo <= 30 or calculo <= 40:
    print('Voce tem obesidade :/ {:.1f}'.format(calculo))
else:
    print('Você tem obesidade Mórbida')
