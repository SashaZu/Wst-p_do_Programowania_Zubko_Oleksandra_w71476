#Zadanie 1
"""
import math
def PoleKola(r):
    if r<=0:
        print("Kolo o takim promieniu nie istnieje")
    else:
        p=r*r*math.pi
        return round(p,2)

print(PoleKola(4))
"""

#Zadanie 2
'''
def pole_trapezu(a, b, h):
    if a>0 and b>0 and h>0:
        return((a+b)*h)/2
    else:
        return "nie mogę poloczyć"

a = float(input("Podaj a: "))
b = float(input("Podaj b: "))
h = float(input("Podaj h: "))
pole_trapezu(a, b, h)
print(f"pole trapezu o podstawach {a} i {b}, oraz wysokosci {h} wynosi {pole_trapezu(a, b, h)}.")
'''

#Zadanie 3
'''
def Dodatna(a):
    if a>0:
        print("Liczba jest dodatna.")
    elif a==0:
        print("Liczba równa się 0.")
    else:
        print("Liczba jest ujemna.")
a=float(input("Wprowadź liczbę: "))   
Dodatna(a)
'''

#Zadanie 4
'''
def oblicz_bmi(waga, wzrost):
    if wzrost <= 0 or waga <= 0:
        return"Waga i wzrost muszą być większ od zera."
    bmi = waga/(wzrost**2)

    if bmi < 18.5:
        zakres = "Niedowaga"
    elif 18.5 <= bmi <= 24.9:
        zakres = "Waga prawidłowa"
    elif 25.0 <= bmi <= 29.0:
        zakres = "Nadwaga"
    else:
        zakres = "Otyłość"

    return round(bmi, 2), zakres

waga = float(input("Podaj soją wage w kilogramach: "))
wzrost = float(input("Podaj swój wzrost w metrach: "))
wynik = oblicz_bmi(waga, wzrost)

if isinstance(wynik, tuple):
    print(f"Twoje BMI wynosi: {wynik[0]}. Znajdujesz się w zakresie: {wynik[1]}.")
else:
    print(wynik)
'''

#Zadanie 5
'''
def oblicz_średnią (lista_liczb):
    if not lista_liczb:
        return None
    return sum(lista_liczb)/len(lista_liczb)
lista_liczb = [10, 20, 30, 40, 50]
śriednia = oblicz_średnią(lista_liczb)
print(śriednia)
'''

#Zadanie 6
'''
imię = input("Podaj imię: ")
wiek = int(input("Podaj wiek: F"))

def info(imię, wiek = 20):
    """
    Funkcja przyjmuje dwa parametry imię oraz wiek.
    Wiek ma wartość domyślna 20.
    Funkcja wypisuje te wartości na ekranie.
    """
    print(f"Imię: {imię}, Wiek: {wiek}")
    
print(info.doc)
info(imię, wiek)
'''

#Zadanie 7
'''
import math

def pole_trójkąta(a, b, c):
    if not all(isinstance(i, (int, float)) for i in [a, b, c]):
        return "Boki muszą być liczbami rzeczywistymi."
    if a <= 0 or b <= 0 or c <= 0:
        return "Boki muszą być liczbami dodatnimi."
    
    if a + b <= c or a + c <= b or b + c <= a:
        return "Podane boki nie tworzą trójkąta."
    
    try:
        s = (a + b + c) / 2
        pole_obliczane = s * (s - a) * (s - b) * (s - c)
        if pole_obliczane <= 0:
            return "Nie można obliczyć pola: boki są nieprawidłowe."
        pole = math.sqrt(pole_obliczane)
        return pole
    except Exception as e:
        return f"Wystąpił błąd podczas obliczania pola: {e}"

a = 4
b = 4
c = 5
wynik = pole_trójkąta(a, b, c)
if isinstance(wynik, (int, float)):
    print(f"Pole trójkąta wynosi: {wynik}")
else:
    print(f"Błąd: {wynik}")
'''

#Zadanie 8
'''
def PowR(a, n):
    if n>=0:
        if n==0:
            return 1
        elif n==1:
            return a
        else:
            return a * PowR(a, n-1)
    else:
        return "nie w tej funkcji"

a = float(input("Podaj a: "))
n = float(input("Podaj n: "))
print(PowR(a, n))
'''

#Zadanie 9
'''
def  Fib(n):
    if n == 1 or n == 2 :
        return 1
    else:
        return Fib(n-1) + Fib(n-2)

print(Fib(1))
print(Fib(2))
print(Fib(3))
print(Fib(4))
print(Fib(5))
print(Fib(6))
print(Fib(7))
'''

#Zadanie 10
'''
def Han(n):
    if n == 1:
        return 1
    else: return 2 * Han(n-1) + 1

print(Han(1))
print(Han(2))
print(Han(3))
print(Han(4))
print(Han(5))
print(Han(6))
'''

#Zadanie 11
'''
def reverse_string(s: str) -> str:
    """
    Funkcja odwracająca ciąg znaków.

    Args:
        s (str): Ciąg znaków do odwrócenia.

    Returns:
        str: Odwrócony ciąg znaków.
    """
    return s[::-1]

tekst = "Lubię Rzeszów"
odwrocony_tekst = reverse_string(tekst)
print(odwrocony_tekst)  
'''

#Zadanie 12
'''
def okresl_plec(imie: str) -> str:
    """
    Funkcja określa płeć na podstawie imienia.
    Przyjmuje imię jako argument i zwraca "kobieta" lub "mężczyzna".
    """
    imie = imie.strip().lower()  
    if imie.endswith("a"):  
        return "kobieta"
    else:
        return "mężczyzna"

imiona = ["Anna", "Piotr", "Kasia", "Michał", "Ewa", "Jakub"]

slownik_imiona_plec = {imie: okresl_plec(imie) for imie in imiona}

print(slownik_imiona_plec)
'''

#Zadanie 13
'''
def wspolne_elementy(iterable1, iterable2):
    """
    Funkcja zwraca listę wspólnych elementów dla dwóch obiektów iterowalnych.

    :param iterable1: Pierwszy obiekt iterowalny (np. lista, krotka, string)
    :param iterable2: Drugi obiekt iterowalny (np. lista, krotka, string)
    :return: Lista wspólnych elementów
    """
      
    wspolne = set(iterable1) & set(iterable2)
    return list(wspolne)

lista1 = [1, 2, 3, 4, 5]
lista2 = [4, 5, 6, 7, 8]

print(wspolne_elementy(lista1, lista2))  
'''

#Zadanie 14
'''
def nwd(a: int, b: int) -> int:
    """
    Funkcja zwraca największy wspólny dzielnik (NWD) dwóch liczb całkowitych.
    
    :param a: Pierwsza liczba całkowita
    :param b: Druga liczba całkowita
    :return: Największy wspólny dzielnik (NWD) liczb a i b
    """
    while b != 0:
        a, b = b, a % b
    return abs(a)

print(nwd(48, 18))  
'''

#Zadanie 15
'''
def czy_palindrom(slowo: str) -> bool:
    """
    Funkcja sprawdza, czy podane słowo jest palindromem.
    
    Argumenty:
    slowo (str): Słowo do sprawdzenia.

    Zwraca:
    bool: True, jeśli słowo jest palindromem, w przeciwnym razie False.
    """
    slowo = slowo.lower().replace(" ", "")
    
    return slowo == slowo[::-1]

print(czy_palindrom("kajak"))  
print(czy_palindrom("Anna"))   
print(czy_palindrom("Python")) 
'''

#Zadanie 16
'''
def czy_anagramy(slowo1: str, slowo2: str) -> bool:
    """
    Sprawdza, czy dwa słowa są anagramami.

    :param slowo1: Pierwsze słowo.
    :param slowo2: Drugie słowo.
    :return: True, jeśli słowa są anagramami, w przeciwnym razie False.
    """
    slowo1 = ''.join(slowo1.lower().split())
    slowo2 = ''.join(slowo2.lower().split())

    return sorted(slowo1) == sorted(slowo2)

print(czy_anagramy("Listen", "Silent"))  
print(czy_anagramy("Konik", "Kino"))    
'''

#Zadanie 17
'''
def wyswietl_parametry(*args):
    for i, arg in enumerate(args, start=1):
        print(f"Parametr {i}: {arg}")

wyswietl_parametry(10, 20, 30, "Hello", True)
'''
'''
def znajdz_max(*args):
    if not args: 
        return None
    return max(args)

print(znajdz_max(10, 20, 30, 5))  
print(znajdz_max("a", "z", "g"))  
print(znajdz_max())  
'''
'''
def wyswietl_i_znajdz_max(*args):
    if not args:
        print("Brak parametrów.")
        return None
    
    for i, arg in enumerate(args, start=1):
        print(f"Parametr {i}: {arg}")
    
    max_value = max(args)
    print(f"Wartość maksymalna: {max_value}")
    return max_value

wyswietl_i_znajdz_max(10, 20, 30, -5, 100)
'''