# Przykładowy program w Pythonie dekodujący numer województwa i powiatu z sekwencji STQC

# Zaimportuj wymagane moduły
from sys import argv, exit
import re

# Funkcja konwertująca sekwencję STQC do Base10
def stqc_to_base10(stqc:str)->int:
	# Zastąp wszystkie cyfry 4 powtórzonymi znakami
    replaced = re.sub(r"([0-3])4",r"\1\1","0"+stqc)
    # Przekonwertuj z Base4 na Base10
    return int(replaced, 4)

# Odczytaj sekwencję; jeśli nie podano, wyświetl wiadomość z pomocą
try:
	to_decode = argv[1]
except IndexError:
	# Wyświetl pomoc i wyjdź
	print("Poprawne użycie: python3 decode_pl_PL.py <sekwencja>")
	exit(0)

# Sprawdź długość sekwencji
if len(to_decode) != 7:
	# Wyświetl wiadomość z błędem
	print("Sekwencja musi mieć 7 znaków!")
	exit(2)

# Pobierz pierwsze 4 znaki (województwo) i ostatnie 3 (powiat)
vvdsq = to_decode[:4]
pwtsq = to_decode[4:]

# Zdekoduj województwo i powiat
try:
	vvd = stqc_to_base10(vvdsq)
	pwt = stqc_to_base10(pwtsq)
except ValueError:
	# Niepoprawna sekwencja
	print("Niepoprawna sekwencja!")
	exit(2)

# Wyświetl wyniki
print(f"Województwo: {vvd}\nPowiat: {pwt}")