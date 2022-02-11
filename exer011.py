# Exercício Python 11: Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área
    # e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.
largura = float(input('Digite a largura da sua parede:'))
altura = float(input('Digite a altura da sua parede:'))
calcu = largura * altura
print(calcu, 'M2')
tinta = calcu / 2
print(f'\nPara pintar a sua parede, que tem o tamanho de {calcu}', 'm2.', f'\nÈ necessário a quantidade de {tinta}','Litros De tinta')