# Podstawy języka Python - Rozszerzone przykłady

# -------------------------
# Zmienne i typy danych
# -------------------------
liczba_calkowita = 42
liczba_zmiennoprzecinkowa = 3.14
tekst = "Witaj, świecie!"
wartosc_logicza = True
lista = [1, 2, 3, "Python", True]
krotka = (1, 2, 3, "Tuple")
zestaw = {1, 2, 3, "Set"}
slownik = {"klucz": "wartość", "wiek": 25}

print("Liczba całkowita:", liczba_calkowita)
print("Lista:", lista)

# -------------------------
# Operacje matematyczne
# -------------------------
suma = 5 + 3
roznica = 10 - 7
iloczyn = 4 * 2
iloraz = 10 / 3
modulo = 10 % 3
potega = 2 ** 3

print("Suma:", suma)
print("Potęga:", potega)

# -------------------------
# Instrukcje warunkowe
# -------------------------
x = 10
y = 20

if x > y:
    print("x jest większe niż y")
elif x == y:
    print("x jest równe y")
else:
    print("x jest mniejsze niż y")

# -------------------------
# Pętle
# -------------------------
# Pętla for
for liczba in range(5):
    print("Liczba:", liczba)

# Pętla while
licznik = 0
while licznik < 3:
    print("Licznik:", licznik)
    licznik += 1

# -------------------------
# Funkcje
# -------------------------
def dodaj(a, b):
    return a + b

wynik = dodaj(5, 7)
print("Wynik dodawania:", wynik)

# -------------------------
# Klasy i obiekty
# -------------------------
class Samochod:
    def __init__(self, marka, model):
        self.marka = marka
        self.model = model

    def przedstaw_sie(self):
        return f"Samochód: {self.marka} {self.model}"

moj_samochod = Samochod("Toyota", "Corolla")
print(moj_samochod.przedstaw_sie())

# -------------------------
# Metody specjalne
# -------------------------
class Punkt:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # definicja serializacji obiektu Punkt do typu string
    def __str__(self):
        return f"Punkt({self.x}, {self.y})"

    # definicja dodawania dwóch obiektów Punkt
    def __add__(self, other):
        return Punkt(self.x + other.x, self.y + other.y)

punkt1 = Punkt(2, 3)
punkt2 = Punkt(4, 5)
suma_punktow = punkt1 + punkt2
print(suma_punktow)

# -------------------------
# Obsługa wyjątków
# -------------------------
try:
    wynik = 10 / 0
except ZeroDivisionError:
    print("Nie można dzielić przez zero!")
finally:
    print("Koniec obsługi wyjątków.")

# -------------------------
# Operacje na plikach
# -------------------------
with open("przyklad.txt", "w") as plik:
    plik.write("Witaj, pliku!")

with open("przyklad.txt", "r") as plik:
    zawartosc = plik.read()
    print("Zawartość pliku:", zawartosc)

# -------------------------
# List comprehension
# -------------------------
kwadraty = [x**2 for x in range(10)]
print("Kwadraty:", kwadraty)

# -------------------------
# Importowanie modułów
# -------------------------
import math

pierwiastek = math.sqrt(16)
print("Pierwiastek z 16:", pierwiastek)

# -------------------------
# Zagnieżdżone struktury danych
# -------------------------
dane = {
    "osoby": [
        {"imie": "Ania", "wiek": 30},
        {"imie": "Piotr", "wiek": 25}
    ]
}

for osoba in dane["osoby"]:
    print(f"Imię: {osoba['imie']}, Wiek: {osoba['wiek']}")
