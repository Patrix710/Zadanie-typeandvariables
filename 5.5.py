>>> # Program do obliczania ceny po rabacie
>>> price_string = input('Enter price: ')  # Wczytanie ceny
Enter price: 77
>>> discount_string = input('Enter discount %: ')  # Wczytanie procentu rabatu
Enter discount %: 50
>>> price = float(price_string)  # Konwersja ceny na float
>>> discount = float(discount_string)  # Konwersja rabatu na float
>>> # Obliczanie ceny po rabacie
>>> discount_amount = price * (discount / 100)  # Kwota rabatu
>>> price_with_discount = price - discount_amount  # Cena po rabacie
>>> # Drukowanie wyników
>>> print(f'Price with discount: {price_with_discount:.2f}')
Price with discount: 38.50
>>>
>>> print(f'Reduction: {discount_amount:.2f}')
Reduction: 38.50