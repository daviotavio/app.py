print('Calculadora de salários')
escolha = input('Voce prefere informar seu salário no mês ou seu valor por hora? Digite "salário" ou "horas"')

if escolha == 'horas' or escolha == 'Horas':
    print('Qual é o seu salário no final do mês?')
    valor1 = float(input())
    print('Quantas horas você trabalhou esse mês? ')
    horas = float(input())
    salario = valor1 / horas
    print('Seu valor por hora é', salario)

elif escolha == 'salario' or escolha =='Salario' or escolha =='Salário' or escolha =='salário':
    print('Quanto você ganha por hora?')
    valor2 = float(input())
    print('e quantas horas você trabalhou esse mês? ')
    qtdHoras = int(input())
    salario_mensal = valor2 * qtdHoras
    print('Seu saláro no fim do mês foi ', salario_mensal)

else:
    print('Algo deu errado, digite "salário" ou "horas"')
