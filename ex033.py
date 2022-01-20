a = int(input('insira um valor'))
b = int(input('insira outro valor'))
c = int(input('insira mais outro valor'))

if a > b and a > c:
    print('o maior valor é {}'.format(a))
elif b > a and b > c:
    print('o maior valor é {}'.format(b))
elif c > a and c > b:
    print('o maior valor é {}'.format(c))
elif a == b == c:
    print('os numeros são iguais')
