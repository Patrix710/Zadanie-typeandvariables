# Program symuluje pięć rzutów kostką.
import random

print("Dice rolling simulator")

for i in range(5):
    dice_roll = random.randint(1, 6)  # Generowanie liczby od 1 do 6
    print(dice_roll, end=" ")  # Wyświetlenie wyniku rzutu


C:\Users\Patryk\Desktop\Zadanko>py dice.py
Dice rolling simulator
6 6 2 1 6