#Exercício Python 68: Faça um programa que jogue par ou ímpar com o computador.
# O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo
import random
num = random.randint(1,10)
valor = int(input('Diga um valor'))
escolha = str(input('Par ou ímpar [P/I]')).upper().strip()
if escolha == 'P':
    computador = num + valor
    resto = computador % 2
    while resto == 0:
        print(f'Deu par Você venceu{computador}')
        break
if escolha == 'I':
    computador = num + valor
    resto = computador % 2
    while resto == 1:
        print(f'Deu impar voce perdeu {computador}')
        break