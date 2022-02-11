# Exercício Python 45: Crie um programa que faça o computador jogar Jokenpô com você.
import random
print('\033[1;31m Joguinho de jokenpo')
itens = ('Pedra', 'Papel', 'Tesoura')
computador = random.randint(0, 2)

print('''****Opções****
    [0] PEDRA
    [1] PAPEL
    [2] TESOURA ''')
print('\033[1;37m-=' * 15)
jogada = int(input('Qual é sua jogada :'))
print('-=' * 15)
print('\033[1;31mComputador jogou {}'.format(itens[computador]))
print('Você jogou {}'.format(itens[jogada]))
print('\n')
if computador == 0:  # computador jogou pedra
    if jogada == 0:
        print('Voces empataram')
    elif jogada == 1:
        print('Voce venceu')
    elif jogada == 2:
        print('Voce perdeu')
    else:
        print('Nenhuma jogada valida')
if computador == 1:
    if jogada == 0:
        print('Voce perdeu. ')
    elif jogada == 1:
        print('Voces empataram !')
    elif jogada == 2:
        print('Voce venceu. ')
    else:
        print('Nenhuma opção valida')
if computador == 2:
    if jogada == 0:
        print('Você venceu')
    if jogada == 1:
        print('Voce perdeu')
    if jogada == 2:
        print('Voces empataram')
    else:
        print('Nenhuma opção valida')
else:
    print('Nenhuma opção valida')