# Password Strength Checker

## Opis projektu
"Password Strength Checker" to aplikacja desktopowa napisana w Pythonie z użyciem biblioteki PySide6. Umożliwia ocenę siły hasła, generowanie silnych haseł oraz daje użytkownikowi szczegółowe informacje na temat bezpieczeństwa wprowadzonych haseł.

### Funkcje aplikacji:
1. **Ocena siły hasła**:
   - Sprawdzanie długości hasła.
   - Weryfikacja obecności małych i wielkich liter.
   - Weryfikacja obecności cyfr.
   - Weryfikacja obecności znaków specjalnych.
   - Sprawdzanie, czy hasło nie zawiera popularnych wzorców, korzystając z pliku `hasla.txt`.

2. **Generowanie silnych haseł**:
   - Aplikacja generuje losowe, silne hasła o długości 12 znaków.
   - Wygenerowane hasło można łatwo skopiować do schowka.

3. **Intuicyjny interfejs użytkownika**:
   - Nowoczesny wygląd i łatwość obsługi.
   - Możliwość podglądu wprowadzanego hasła.

---

## Wymagania systemowe
Aby uruchomić aplikację, wymagane jest środowisko Python 3.11 lub nowsze oraz następujące biblioteki:
- `PySide6`

---

## Instrukcja uruchomienia

1. **Zainstaluj Pythona:**
   Pobierz i zainstaluj Python 3.11 lub nowszy z [oficjalnej strony Pythona](https://www.python.org/).

2. **Zainstaluj wymagane biblioteki:**
   Użyj polecenia poniżej, aby zainstalować potrzebne zależności:
   ```bash
   pip install PySide6
   ```

3. **Uruchom aplikację:**
   Pobierz pliki projektu, upewnij się, że plik `hasla.txt` znajduje się w tym samym folderze co `main.py`, a następnie uruchom aplikację:
   ```bash
   python main.py
   ```

---

## Struktura projektu
- `main.py`: Główny plik aplikacji zawierający kod źródłowy.
- `hasla.txt`: Plik zawierający ogromną bazę ** najczęściej używanych haseł**, które są używane do weryfikacji siły hasła.

---

## Jak używać aplikacji
1. Wprowadź swoje hasło w polu "Wprowadź swoje hasło".
2. Kliknij przycisk "Sprawdź siłę hasła", aby otrzymać szczegółową ocenę hasła.
3. Aby wygenerować nowe hasło, kliknij "Wygeneruj silne hasło" i skopiuj je, korzystając z przycisku w nowo otwartym oknie.

---

## Licencja
Projekt dostępny na licencji MIT.


