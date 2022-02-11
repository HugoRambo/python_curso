num = 0
contandor = 0
soma = 0
num = int(input('Digite um número [999 para parar] :'))
while num != 999:

    soma = soma + num
    contandor = contandor +1
    num = int(input('Digite um número [999 para parar] :'))
print('Voce digitou {} números e a soma entre eles foi {}'.format(contandor, soma ))