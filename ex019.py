import random
a = []
for y in range(0,4):
    x=input('insira o nome do aluno {}\n'.format(y+1))
    a.append(x)
    y+1

print('o aluno sorteado é {}'.format(a[random.randint(0,3)]))
