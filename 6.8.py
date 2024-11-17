>>> first = input('Wprowadź pierwszą literę: ')
Wprowadź pierwszą literę: a
>>> last = input('Wprowadź drugą literę: ')
Wprowadź drugą literę: d
>>>
>>> first_letter_code = ord(first)
>>> last_letter_code = ord(last)
>>> number_of_letters = abs(last_letter_code - first_letter_code) - 1
>>> print(f'Pomiędzy literami {first} i {last} są {number_of_letters} litery')
Pomiędzy literami a i d są 2 litery
>>>