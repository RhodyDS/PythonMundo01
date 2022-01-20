import random
a = []
for y in range(0,4):
    x=input('insira o nome do aluno {}\n'.format(y+1))
    a.append(x)
    y+1

random.shuffle(a)
for k in range(0,4):
    print('o sorteado n°{} foi o {}'.format(k+1,a[k]))
    k+1



