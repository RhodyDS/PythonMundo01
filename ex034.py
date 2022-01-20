a = float(input('qual o valor do seu salario: '))
if a > 1250:
    print('seu salario com o aumento agora é de: R${}'.format(a + (a * 10 / 100)))
else:
    print('seu salario com o aumento agora é de: R${}'.format(a + (a * 15 / 100)))
