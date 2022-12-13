#Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.

print('Calculadora de graus que transfoma graus celcius em fahrenheit')
print('Forneça a temperatura em graus celcius: ')
graus_c = float(input())
graus_f = (graus_c * 1.8) + 32

print('A temperatura {0} graus em Celcius é igual a {1} em graus Fahrenheit'.format(graus_c, graus_f))
