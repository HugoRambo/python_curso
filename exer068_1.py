def exercicio68_1 ():
#Exercício Python 68: Faça um programa que jogue par ou ímpar com o computador.
# O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo
import random
while True:
    jogador = int(input('Diga um valor:'))        # valor, jogador digitar o valor
    computador = random.randint(0,11)             # importação do random
    total = jogador + computador                  # total de valores, entre que escolhi e que computador mandou
    vitoria = 0                                   # vitoria começa com zero, conforme vou ganhando vou somando
    tipo = ' '                                    # tipo iniciou vazio, pois depois ia definir
    derrota = 0
    while tipo not in 'PI':                       # Enquanto ele digitar Par ou Impar vai rodar o codigo
        tipo = str(input('Par ou Ímpar [P/I]')).strip().upper()[0]        #pedindo se ele quer par ou impar, strip retira espaçõs, upper deixa maisculo
    print(f'Voce jogou {jogador} e o computador {computador}, total foi de {total}')   #totais de cada opção
    print('DEU PAR' if total % 2 == 0 else 'DEU IMPAR')                                 #print ocorre, lendo a condição if e else
    if tipo == 'P':                                                                     #if ocorre caso a pessoa escolha par, o if analisa se o valor do total
        if total % 2 == 0:                                                              #é par, se ele for par, printa que venceu e soma + uma vitoria
            print('Voce venceu')
            vitoria = vitoria +1
            print('Vamos jogar novamente...')
        else:
            print('Voce perdeu')
            derrota = derrota +1
            break
    elif tipo == 'I':
        if total % 2 ==0:
            print('Você venceu')
            vitoria = vitoria +1
            print('Vamos jogar novamente...')
        else:
            print('Voce perdeu')
            derrota = derrota + 1
            break

print(f'GAME OVER , você venceu {vitoria} vezes, e perdeu {derrota}')
