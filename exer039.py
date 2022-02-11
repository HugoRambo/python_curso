 # Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade,
    # se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento.
    # Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

idade = int(input('Qual sua idade  ?'))
if idade < 18:
    print('Falta para voce se alistar {} anos'.format(18 - idade))
elif idade > 18:
    print('Voce já passou da epoca de se alistar {} anos'.format(idade - 18))
elif idade == 18:
    print('Uhul, chegou o grande dia, voce pode se alistar')