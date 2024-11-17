>>> cube_side_string = input('Enter cube side: ') # Wczytanie długości boku sześcianu
Enter cube side: 7
>>> cube_side = int(cube_side_string) # Konwersja na liczbę całkowitą
>>> cube_volume = cube_side ** 3 # Objętość sześcianu: a^3
>>> cube_surface_area = 6 * (cube_side ** 2) # Powierzchnia sześcianu: 6 * a^2
>>> print(f'The volume of a cube with side {cube_side} is {cube_volume}')
The volume of a cube with side 7 is 343
>>> print(f'The surface area of a cube with side {cube_side} is {cube_surface_area}')
The surface area of a cube with side 7 is 294 