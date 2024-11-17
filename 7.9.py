# Program: Gracz zgaduje wynik rzutu kostką przez komputer
>>> import random
# Rzut komputerowy
>>> computer = random.randint(1, 6)
# Zgadywanie przez użytkownika
>>> guess = int(input('Zgadnij liczbę (1-6): '))
Zgadnij liczbę (1-6): 4
# Sprawdzenie wyniku
>>> you_won = computer == guess
>>> print(f'Rzut komputera: {computer}')
Rzut komputera: 6
>>> print(f'Wygrałeś: {you_won}')
Wygrałeś: False