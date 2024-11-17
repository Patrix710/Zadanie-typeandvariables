# BMI Calculator

height = input('Enter your height in cm: ')  # Pobieranie wzrostu użytkownika
weight = input('Enter your weight in kg: ')  # Pobieranie wagi użytkownika
height = int(height)  # Konwersja wzrostu na liczbę całkowitą
weight = int(weight)  # Konwersja wagi na liczbę całkowitą
bmi = weight / (height / 100) ** 2  # Obliczenie BMI
bmi = round(bmi, 2)  # Zaokrąglenie BMI do dwóch miejsc po przecinku
print('Your BMI is', bmi)  # Wyświetlenie BMI
print('Check on the Internet if your BMI is ok!!')  # Zasugerowanie, żeby sprawdzić wynik w Internecie

C:\Users\Patryk>cd C:\Users\Patryk\Desktop\Zadanko
C:\Users\Patryk\Desktop\Zadanko>py bmi.py
Enter your height in cm: 180
Enter your weight in kg: 70
Your BMI is 21.6
Check on the Internet if your BMI is ok!!

