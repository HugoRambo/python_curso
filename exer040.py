# Exercício Python 040: Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
# – Média abaixo de 5.0: REPROVADO
# – Média entre 5.0 e 6.9: RECUPERAÇÃO
# – Média 7.0 ou superior: APROVADO
n1 = int(input('Digite sua primeira nota'))
n2 = int(input('Digite sua segunda nota'))
media = (n1 + n2) / 2
if media > 50 and media < 69:
    print('Voce esta de recuperação, sua media é {}'.format(media))
elif media < 49:
    print('Voce esta reprovado, sua media é uma vergonha {}'.format(media))
else:
    print('Parabens voce foi aprovado, sua media é  {}'.format(media))