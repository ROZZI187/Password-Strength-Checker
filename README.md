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
## Konwersacja do pliku exe
Aby skonwertować aplikację do pliku exe (github nie pozwala na dodanie zbyt dużego pliku) należy:

1. **Uruchomić CMD w folderze w którym jest aplikacja**
2. **Instalujemy pyinstallera**:
```bash
pip install pyinstaller
```
4. **Zastosować następującą komendę:**
```bash
pyinstaller --onefile --windowed --add-data "hasla.txt;." main.py
```
3. **Plik exe znajdować się będzie w nowym folderze **dist** i można go uruchomić (trzeba zezwolić na uruchomienie jeśli antywirus nie pozwala)**

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
## Jak aplikacja wygląda?
1. **Pierwsze uruchomienie**
![image](https://github.com/user-attachments/assets/683e4b22-3f3a-4a0d-bfb9-fba0cce88fbb)

2. **Sprawdzenie hasła które nie spełnia wymogów**
![image](https://github.com/user-attachments/assets/0dbd2d7a-d6cd-4b06-b3c2-1a07a166f721)

3. **Generowanie silnego hasła z możliwością skopiowania**
![image](https://github.com/user-attachments/assets/b5ac42ec-01c5-4d8b-99bf-fc8f7ae9d587)

4. **Sprawdzenie hasła które jest klasyfikowane jako silne**
![image](https://github.com/user-attachments/assets/c5bc6873-8dc1-4d6a-845c-11734b86f9c7)

## Licencja
Projekt dostępny na licencji MIT.


