>>> password = input('Podaj hasło: ')
Podaj hasło: university
>>> password_ok = len(password) >= 8
>>> print(f'Hasło poprawnej długości: {password_ok}')
Hasło poprawnej długości: True

>>> password = input('Podaj hasło: ')
Podaj hasło: anna333
>>> password_ok = len(password) >= 8
>>> print(f'Hasło poprawnej długości: {password_ok}')
Hasło poprawnej długości: False