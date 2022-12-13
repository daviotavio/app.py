#C = 5 * ((F-32) / 9).

print('Calculadora de graus que transfoma graus fahrenheit em celcius')
graus_f = float(input('Forneça a temperatura em graus fahrenheit: '))
graus_c = 5 * ((graus_f-32) / 9)

print('A temperatura {0} graus em Fahrenheit é igual a {1} em graus Celsius'.format(graus_f, graus_c))


