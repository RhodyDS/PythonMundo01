a = input('insira o nome de uma cidade')
a = a.lower().split()

if 'santo' in a[0]:
    print('essa cidade começa com a palavra SANTO')
else:
    print('essa cidade NÃO começa com a palavra SANTO')