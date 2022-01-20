a = input('informe seu nome completo: ')
print(a.upper())
print(a.lower())
b = len(a.strip())-a.count(' ')
print('o nome {} contem {} letras.'.format(a,b))
a=a.split()
print('o primeiro nome é {}'.format(a[0]))


