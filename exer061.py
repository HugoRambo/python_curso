#Exercício Python 61: Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.
termo = int(input('Digite o primeiro termo da PA'))
razao = int(input('Digite a razão da PA'))
fim = 10
while fim > 0:
    print('A progressao da PA É  {} '.format(termo))
    termo = termo + razao
    fim = fim - 1