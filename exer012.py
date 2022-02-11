 # Exercício Python 12: Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
# 1500*10/100
# a conta a cima seria, 10% de 1500
print('__Estamos com uma promoção de 5% de desconto__')
preço = float(input('Digite o preço do produto, que vou te dar desconto na hora:'))
portencagem = preço * 5 / 100
novo_preço = preço - portencagem
print(f'5% de {preço}, dara de desconto para você de {portencagem}')

print(f'Valor do produto na promoção éde {novo_preço}')