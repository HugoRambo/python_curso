# Exercício Python 7: Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.
nota = int(input('Digite sua nota: '))
nota1 = int(input('Digite outra nota sua, para podermos calcular sua media: '))
soma = nota + nota1
media = soma / 2
print(f'Bom amigo, sua média é  {media}')