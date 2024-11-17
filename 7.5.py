>>> car_number = input('Podaj numer rejestracyjny samochodu: ')
Podaj numer rejestracyjny samochodu: KK67890
>>> is_krakow = car_number[:2] in ["KR", "KK"]
>>> print(f'Samochód jest z Krakowa: {is_krakow}')
Samochód jest z Krakowa: True

>>> car_number = input('Podaj numer rejestracyjny samochodu: ')
Podaj numer rejestracyjny samochodu: SK12345
>>> is_krakow = car_number[:2] in ["KR", "KK"]
>>> print(f'Samochód jest z Krakowa: {is_krakow}')
Samochód jest z Krakowa: False