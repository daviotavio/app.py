#Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
#Para homens: (72.7*h) - 58
#Para mulheres: (62.1*h) - 44.7

altura = float(input('Qual é a sua altura em metros?'))
genero = str(input('Qual seu gênero? M ou F?'))

if genero == 'M' or genero == 'm':
    peso_idealM = (72.7 * altura) - 58
    print('o seu peso ideal é ', peso_idealM)

elif genero == 'F' or genero == 'F':
    peso_idealF = (62.1 * altura) - 44.7
    print('o seu peso ideal é ', peso_idealF)

else:
    input('Algo deu errado.')
