# Exercício Python 006: Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.
numero = int(input('Digite um valor que queria saber --o dobro--, --o triplo-- e a --raiz quadrada-- '))
dobro = numero * 2
triplo = numero * 3
raiz = numero ** (1 / 2)
print(f'o Dobro do numero {numero}, é {dobro},\n O triplo é {triplo},\n E a raiz quadrada é {raiz}')
