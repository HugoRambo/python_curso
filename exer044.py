# Exercício Python 44: Elabore um programa que calcule o valor a ser pago por um produto,
    # considerando o seu preço normal e condição de pagamento:
    # – à vista dinheiro/cheque: 10% de desconto
    # – à vista no cartão: 5% de desconto
    # – em até 2x no cartão: preço formal
    # – 3x ou mais no cartão: 20% de juros
print('Nossa loja tem um valor variavel do preço dos produtos.')
valor = float(input('Digite o valor  do produto :'))
print('''Qual modelo de pagamento vai querer.
    [1] à vista dinheiro/cheque: 10% de desconto
    [2] à vista no cartão: 5% de desconto
    [3] em até 2x no cartão: preço normal
    [4] 3x ou mais no cartão: 20% de juros
    ''')
opcao = int(input('Qual opção vai querer ?'))
if opcao == 1:
    a = ((valor * 10) / 100)
    print('Valor do desconto é de  {:.1f}R$, o valor  depois do desconto é de {:.1f}'.format(a, valor - a, 'R$'))
elif opcao == 2:
    b = ((valor * 5) / 100)
    print('Valor do desconto é de {:.1f}R$, o valor depois do descnto é de {:.1f}'.format(b, valor - b, 'R$'))
elif opcao == 3:
    print('Valor nessa opção tem preço normal {:.1f}'.format(valor))
    print('parcela custara {}R$'.format(valor / 2))
elif opcao == 4:
    c = ((valor * 20) / 100)
    perguntar = int(input('Quantas parcelas seram ? '))
    print(
        'nessas condições não tem desconto, sistema ganha um aumento de 20%, acresentando o valor de  {:.1f}  tornando a custar {:.1f}'.format(
            c, valor + c, 'R$'))
    print('As parcelas nessa opção em {} vezes, custara {} mensal.'.format(perguntar, (valor + c) / perguntar))
else:
    print('Não tem essa opção')