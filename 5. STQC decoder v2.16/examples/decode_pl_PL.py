# Przykładowy program w Pythonie dekodujący numer obszaru z sekwencji STQC

# Zaimportuj wymagane moduły
from sys import argv, exit
import re

# Funkcja konwertująca sekwencję STQC do Base10
def stqc_to_base10(stqc:str)->int:
	# Zastąp wszystkie cyfry 4 powtórzonymi znakami
    replaced = re.sub(r"([0-3])4",r"\1\1","0"+stqc)
    # Przekonwertuj z Base4 na Base10
    return int(replaced, 4)

# Odczytaj sekwencję; jeśli nie została podana, wyświetl pomoc
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

# Odczytaj 2 części sekwencji
area1_sq = to_decode[:4]
area2_sq = to_decode[4:]

# Zdekoduj te części
try:
    area1 = stqc_to_base10(area1_sq)
    area2 = stqc_to_base10(area2_sq)
except ValueError:
	# Niepoprawna sekwencja
	print("Niepoprawna sekwencja!")
	exit(2)

# Wyświetl wynik
print(int(f"{area1}{area2:02d}"))