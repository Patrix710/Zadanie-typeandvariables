# Wprowadź kod SWIFT
>>> swift = input("Podaj kod SWIFT: ")
Podaj kod SWIFT: 12345678
# Wyodrębnij kod banku i kraju
>>> bank_code = swift[:4]
>>> country_code = swift[4:6]
# Wyświetl wyniki
>>> print(f"Bank Code: {bank_code}")
Bank Code: 1234
>>> print(f"Country Code: {country_code}")
Country Code: 56