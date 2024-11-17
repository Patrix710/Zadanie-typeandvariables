>>> # Manipulacja ciągiem znaków
>>> #
>>> movie = "The Lord of the Rings: The Return of the King"
>>>
>>> # wypisz liczbę znaków w tytule
>>> print('Liczba znaków: ', len(movie))
Liczba znaków:  45
>>>
>>> # wypisz tytuł wielkimi literami
>>> print(movie.upper())
THE LORD OF THE RINGS: THE RETURN OF THE KING
>>>
>>> # wypisz tytuł małymi literami
>>> print(movie.lower())
the lord of the rings: the return of the king
>>>
>>> # wypisz, ile razy litera "e" pojawia się w tytule
>>> print(movie.count('e'))
5
>>>
>>> # wypisz, gdzie w tekście znajduje się słowo "Lord"
>>> print(movie.find('Lord'))
4
>>>
>>> # wypisz, gdzie w tekście znajduje się słowo "dragon"
>>> print(movie.find('dragon'))
-1