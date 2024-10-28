# print(*objects, sep=' ', end='\n', file=None, flush=False)

"""
imię  = "Oleksandra"
kierunek = "Informatyka"
uczelnia = "WSIZ"

print("Nazywam się " + imię, end=' ')
print("Studiuje na kierunku", kierunek, sep=' ', end=' ')
print("na", uczelnia, sep=' ')
"""

""" 
#4 
print("Jak się nazywasz?") 
name = input() 

print( f"Cześć, {name}, witaj na zajęciach UwU") 
"""

""" 
#5 
bok1 = float(input("Podaj długość boku prostokąta: ")) 
bok2 = float(input("Podaj długość drugiego boku prostokąta: ")) 

obw = ((bok1 + bok2) * 2) 
pole = (bok1 * bok2) 

x = obw 
y = pole 

print("Odwód prostokąta: ", x) 
print("Pole prostokąta: ", y) 
"""

"""
# 6
cena_pal = 6.5

droga = float(input("Podaj drogę pokonaną przez samochód w (km): "))
spalanie = float(input("Podaj średnie spalanie (w litrach na 100 km): "))

zuzycie_paliwa = (droga / 100) * spalanie
koszt_podrozy = zuzycie_paliwa * cena_pal

print(f"Przewidywane zużycie paliwa: {zuzycie_paliwa:.2f} litrów")
print(f"Szacowany koszt podróży: {koszt_podrozy:.2f} zł")
"""

#7

import random

cena_pal = 6.5

spalanie = float(input("Podaj średnie spalanie (w litrach na 100 km): "))

droga = random.randint(50, 500)
print(f"Wylosowana droga: {droga} km")

zuzycie_paliwa = (droga / 100) * spalanie
koszt_podrozy = zuzycie_paliwa * cena_pal

print(f"Przewidywane zużycie paliwa: {zuzycie_paliwa:.2f} litrów")
print(f"Szacowany koszt podróży: {koszt_podrozy:.2f} zł")

"""
Liczby generowane przez random.randint są pseudolosowe. 
To znaczy, że są powtarzalne, gdy używamy tego samego ziarna. 
Prawdziwie losowe liczby są zjawiskami naturalnymi, a te z random są tylko symulowane.
"""