# Wprowadź wzrost w cm
>>> cm = int(input("Podaj wzrost w cm: "))
Podaj wzrost w cm: 187
# Oblicz wysokość w stopach i calach
>>> feet = cm // 30.48
>>> inches = (cm % 30.48) / 2.54
# Wyświetl wyniki
>>> print(f"Twój wzrost to {cm} cm, czyli {int(feet)} stóp i {int(inches)} cali.")
Twój wzrost to 187 cm, czyli 6 stóp i 1 cali.