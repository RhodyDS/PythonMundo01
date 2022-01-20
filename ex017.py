import math

a = float(input('insira o valor do cateto oposto'))
b = float(input('insira o valor do cateto adjacente'))
c=math.hypot(a,b)
print('o comprimento da hipotenusa é {}'.format(c))