# Program, który wypisuje numer telefonu składający się z 9 cyfr,
# podzielony na trzy grupy po 3 cyfry, oddzielone myślnikiem.

>>> phone = input('Wprowadź numer telefonu: ')
Wprowadź numer telefonu: 777 777 710
>>> formatted_phone = phone[:3] + '-' + phone[3:6] + '-' + phone[6:]
>>> print(f'Numer telefonu: {formatted_phone}')
Numer telefonu: 777- 77-7 710