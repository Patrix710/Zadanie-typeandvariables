>>> age = int(input('Podaj wiek: '))
Podaj wiek: 20
>>> no_tax = age <= 26 # na podstawie wieku (wiek ≤ 26)
>>> print(f'zwolnienie z podatków:{no_tax}')
zwolnienie z podatków:True

>>> age = int(input('Podaj wiek: '))
Podaj wiek: 38
>>> no_tax = age <= 26 # na podstawie wieku (wiek ≤ 26)
>>> print(f'Zwolnienie z podatków: {no_tax}')
Zwolnienie z podatków: False