a = float(input('insira a velocidade do carro:\n'))
if a > 80:
    print('você foi multado por ultrapassar a velocidade permitida.\nvalor da multa R${}'.format((a-80) * 7))
else:
    print('velocidade dentro do limitee estabelecido. tenha um bom dia.')
