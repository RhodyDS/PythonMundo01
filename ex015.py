d = int(input('quantos dias alugado?'))
k = int(input('quantos km rodados'))
pagar = (d*60) + (k*0.15)
print('o valor a ser pago é de R${:.2f}'.format(pagar))