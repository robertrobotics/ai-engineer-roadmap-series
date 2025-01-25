"""
Skrypt zbierający wydatki użytkownika i prezentujący statystyki finansowe
"""

# Importujemy potrzebne moduły
import statistics

# Funkcja do zebrania wydatków od użytkownika
def zbierz_wydatki():
    wydatki = []
    print("Podaj swoje wydatki z ostatnich 7 dni (w zł). Wpisz 'stop', aby zakończyć.")
    
    for dzien in range(1, 8):
        while True:
            try:
                wydatek = input(f"Dzień {dzien}: ")
                if wydatek.lower() == 'stop':
                    return wydatki
                wydatek = float(wydatek)
                if wydatek < 0:
                    print("Wydatek nie może być ujemny. Spróbuj ponownie.")
                    continue
                wydatki.append(wydatek)
                break
            except ValueError:
                print("Nieprawidłowy format. Wprowadź liczbę.")
    return wydatki

# Funkcja do obliczenia i wyświetlenia statystyk
def pokaz_statystyki(wydatki):
    if not wydatki:
        print("Brak danych do analizy.")
        return

    suma = sum(wydatki)
    srednia = statistics.mean(wydatki)
    mediana = statistics.median(wydatki)
    min_wydatek = min(wydatki)
    max_wydatek = max(wydatki)

    print("\nStatystyki finansowe z ostatnich 7 dni:")
    print(f"Łączna suma wydatków: {suma:.2f} zł")
    print(f"Średni wydatek dzienny: {srednia:.2f} zł")
    print(f"Mediana wydatków: {mediana:.2f} zł")
    print(f"Najmniejszy wydatek: {min_wydatek:.2f} zł")
    print(f"Największy wydatek: {max_wydatek:.2f} zł")

# Główna część programu
def main():
    print("Witaj w analizatorze wydatków!")
    wydatki = zbierz_wydatki()
    pokaz_statystyki(wydatki)

# Uruchomienie programu
if __name__ == "__main__":
    main()
