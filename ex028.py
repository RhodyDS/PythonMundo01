import random,time

a = random.randint(0, 5)

b = int(input('tente advinhar o numero que estou pensando de 0 a 5:\n'))
print('processando...')
time.sleep(3)
if a == b:
    print('parabens eu pensei no numero {} e você digitou o numero {}!!'.format(a, b))
else:
    print('você errou!! eu pensei no numero {}'.format(a))
