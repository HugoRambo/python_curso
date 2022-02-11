#Exercício Python 62: Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerrará quando ele disser que quer mostrar 0 termos.
termo = int(input('Digite o primeiro termo da PA'))
razao = int(input('Digite a razão da PA'))
fim = 10

while fim > 0:
    print('A progressao da PA É  {} '.format(termo))
    termo = termo + razao
    fim = fim - 1
    mais = int(input('Quantos termos você quer mostrar a mais nessa pa ? '))
while mais > 0 :
    print('A progressão da PA É {}'.format(termo))
    termo = termo + razao
    mais = mais -1