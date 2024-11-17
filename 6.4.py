>>> # Program do wyświetlania szczegółowych informacji o pracowniku
>>> #
>>> employee = "Mr. John May, born on 1998-02-16"
>>> # Imię zaczyna się od indeksu 4 i kończy na 8
>>> print(f'Imię: {employee[4:8]}')
Imię: John
>>> # Nazwisko zaczyna się od indeksu 9 i kończy na 13
>>> print(f'Nazwisko: {employee[9:13]}')
Nazwisko: May,
>>> # Data urodzenia zaczyna się od indeksu 21 i kończy na 31
>>> print(f'Data urodzenia: {employee[21:31]}')
Data urodzenia:  1998-02-16
>>> # Inicjały: pierwsza litera imienia i nazwiska
>>> print(f'Inicjały: {employee[4]}{employee[9]}')
Inicjały: JM