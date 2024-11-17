>>> # Program sprawdza, czy rzucona liczba jest specjalna (1 lub 6)
>>> import random
>>> dice_roll = random.randint(1, 6)
>>> is_special = dice_roll in [1, 6]
>>> print(f'Wyrzucona liczba: {dice_roll}')
Wyrzucona liczba: 3
>>> print(f'Jest specjalna: {is_special}')
Jest specjalna: False