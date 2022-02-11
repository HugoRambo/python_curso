
from datetime import date
atual = date.today().year
nasc = int(input('Qual a data do seu nascimento ?'))
valorc = (atual - nasc) - 18
if nasc < 2004:
    print('Você passou da idade de servir o quartel {} anos, hoje tem a idade de {}'.format(valorc, atual - nasc))
elif nasc > 2004:
    print('Voce ainda não esta na idade de servir o quartel falta {} anos'.format((nasc - atual) + 18))
elif nasc == 2004:
    print('Parabens, voce pode pintar o meio fio.')
