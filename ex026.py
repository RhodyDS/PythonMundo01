a = input('insiraa uma frase:')
print('aparece a letra A {} vezes'.format(a.lower().count('a')))
b = a.lower().find('a')
print('aparece a primeira letra A na posição {}'.format(int(b+1)))
c = a.lower().rfind('a')
print('aparece a ultima  letra A na posição {}'.format(int(c+1)))