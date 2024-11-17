>>> # Definiujemy dane
>>> total = 8000000000  # Całkowita populacja świata (8 miliardów)
>>> north = 7200000000  # Populacja półkuli północnej (7,2 miliarda)
>>> south = total - north  # Populacja półkuli południowej (8 miliardów - 7,2 miliarda)
>>>
>>> # Obliczanie procentowego udziału
>>> north_percentage = (north / total) * 100  # Procent mieszkańców półkuli północnej
>>> south_percentage = (south / total) * 100  # Procent mieszkańców półkuli południowej
>>>
>>> # Wyświetlanie wyników
>>> print("World population: ", total)
World population:  8000000000
>>> print("Northern Hemisphere: ", north)
Northern Hemisphere:  7200000000
>>> print("Northern Hemisphere in %: ", round(north_percentage, 2))  # Procent półkuli północnej
Northern Hemisphere in %:  90.0
>>> print("Southern Hemisphere: ", south)
Southern Hemisphere:  800000000
>>> print("Southern Hemisphere in %: ", round(south_percentage, 2))  # Procent półkuli południowej
Southern Hemisphere in %:  10.0