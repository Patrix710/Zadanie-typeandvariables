>>> amount_string = input('Enter amount: ') # Wczytanie kwoty
Enter amount: 70
>>> amount = float(amount_string) # Konwersja na liczbę zmiennoprzecinkową

# Obliczanie VAT-u
>>> vat = amount * 0.23

# Drukowanie wyników
>>> print(f'Amount  : {amount:.2f}')
Amount  : 70.00
>>> print(f'VAT 23% : {vat:.2f}')
VAT 23% : 16.10