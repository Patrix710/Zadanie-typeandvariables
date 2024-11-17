>>> # Program generuje 3 rzuty kostką i ich sumę
>>> import random
>>> dice_roll_1 = random.randint(1, 6)
>>> dice_roll_2 = random.randint(1, 6)
>>> dice_roll_3 = random.randint(1, 6)
>>> total = dice_roll_1 + dice_roll_2 + dice_roll_3
>>> print(f'Rzuty: {dice_roll_1}, {dice_roll_2}, {dice_roll_3}')
Rzuty: 3, 2, 3
>>> print(f'Suma rzutów: {total}')
Suma rzutów: 8