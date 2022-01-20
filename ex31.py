a = float(input('qual a distancia da viagem em km: '))
if a<= 200:
    print('o preço da passagem é de R${}'.format(a*0.50))
else:
    print('o preço da passagem é de R${}'.format(a*0.45))