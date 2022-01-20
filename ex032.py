from datetime import date
a = int(input('informe o ano:'))
if a == 0:
    a = date.today().year
if a % 4 == 0 and a % 100 != 0 or a % 400 == 0:
    print('esse ano é bissexto')
else:
    print('o ano não é bissexto')
