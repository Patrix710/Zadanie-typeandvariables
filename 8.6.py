# Wprowadź dane
>>> distance = int(input("Podaj odległość w km: "))
Podaj odległość w km: 50
>>> fuel_price = float(input("Podaj cenę paliwa za litr: "))
Podaj cenę paliwa za litr: 15
>>> fuel_consumption = float(input("Podaj zużycie paliwa w litrach na 100 km: "))
Podaj zużycie paliwa w litrach na 100 km: 25
# Oblicz zużycie paliwa i koszt
>>> total_fuel_consumption = (fuel_consumption * distance) / 100
>>> total_cost = total_fuel_consumption * fuel_price
# Wyświetl wyniki
>>> print(f"Całkowite zużycie paliwa: {total_fuel_consumption:.2f} litrów")
Całkowite zużycie paliwa: 12.50 litrów
>>> print(f"Całkowity koszt transportu: {total_cost:.2f} zł")
Całkowity koszt transportu: 187.50 zł