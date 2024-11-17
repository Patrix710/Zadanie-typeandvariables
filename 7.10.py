>>> import random
# KOMPUTER RZUCA KOSTKĄ
>>> computer = random.randint(1, 6)
# UŻYTKOWNIK ZGADUJE LICZBĘ
>>> you = int(input('Zgadnij liczbę wyrzuconą przez komputer (1-6): '))
Zgadnij liczbę wyrzuconą przez komputer (1-6): 5
# SPRAWDZENIE, CZY UŻYTKOWNIK TRAFIŁ
>>> won = you == computer
>>> print(f'Komputer wyrzucił: {computer}')
Komputer wyrzucił: 3
>>> print(f'Trafiłeś: {won}')
Trafiłeś: False