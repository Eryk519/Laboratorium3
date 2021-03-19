import numpy as np
import random
from Ciagi import *
import math

#ZAD1
a = [1-x for x in range(1,10)]
b = [4**i for i in range(8)]
c = [x for x in a if x % 2 == 0]
print(a)
print(b)
print(c)

#ZAD2

Lista1 = random.sample(range(1, 100), 10)
for i in range(0,5):
    n = random.randint(1,100)
Lista1.append(n)

parzyste = [n for n in Lista1 if n % 2 == 0]
print(parzyste)

#ZAD3

skroty = {"Jajka": "Sztuki",
 "Cukier": "Kilogranmy",
 "Mleko": "Litry"}

odwrocone2 = {value: key for key, value in skroty.items()}
print(odwrocone2)

#ZAD4
def trojkat_prostokatny(a,b,c):
    if (a**2 + b**2) == c**2:
        return ("Trójkąt jest prostokątny")
    else:
        return ("Trójkąt nie jest prostokątny")
print(trojkat_prostokatny(2,4,5))

#ZAD5
def pole_trapezu(a=2, b=4, h=5):
    pole_trapezu = ((a+b)/2)*h
    return pole_trapezu
print(pole_trapezu())

#ZAD6
def ciagGeometryczny(a, b, ile):
    for i in range(ile):
        a = a*b

    return a

print(ciagGeometryczny(1, 4, 10))

#ZAD7
def ciagGeometryczny(a, b, ile):
    for i in range(ile):
        a *= b

    return a

print(ciagGeometryczny(1, 4, 10))


#ZAD8
def produkt(** produkty):
    suma = 0
    ile_produktow = 0
    for key, value in produkty.items():
        suma += value
        ile_produktow += 1

    return suma, ile_produktow

print(produkt(maslo=3, ser=8, szynka=12, mleko=2))

#ZAD10
plik = open("liczby.txt", "w")

for i in range(101):
    if i%4 == 0:
        liczba = i
        plik.write(str(i))
        plik.write("\n")
#ZAD11
plik = open("liczby.txt", "r")

for wiersz in plik:
    print(wiersz)
