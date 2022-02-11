# Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra “A”,
# em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.
palavra = str(input('Digite uma frase:')).upper().strip()
print('A letra A aparece {} vezes na frase.'.format(palavra.count('A')))
print('A primeira letra A apareceu na posição {}'.format(palavra.find('A') + 1))
print('A útilma letra A apareceu na posição {}'.format(palavra.rfind('A') + 1))