#Exercício Python 69: Crie um programa que leia a idade e o sexo de várias pessoas.
# A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
print('-' * 58)
print('Cadastre um pessoa')
print('-' * 58)
idadetotal = 0
mulher = 0          #toda vez que escolhe F aumenta 1
mulhermenor = 0     # toda vez que mulher tem menos de 20 aumenta 1
homem = 0
home_menor = 0
while True:
    idade= int(input('Idade :'))
    sexo = str(input('Sexo: [M/F]')).strip().upper()[0]
    if sexo == 'F':
        mulher = mulher + 1
        if idade > 18:
            idadetotal = idadetotal+1
        elif idade < 20:
            mulhermenor = mulhermenor +1
    elif sexo == 'M':
        homem = homem +1
        if idade > 18:
            idadetotal = idadetotal +1
        else:
            home_menor = home_menor +1

    pergunta = str (input('Quer continuar [S/N]')).upper().strip() [0]
    print('Cadastre um pessoa')
    if pergunta == 'N':
        break


print(f' Total de pessoas com mais de 18 anos é {idadetotal} ')
print(f' Ao total temos {homem} homens cadastrado')
print(f' E temos {mulhermenor} mulheres com menos de 20 anos')