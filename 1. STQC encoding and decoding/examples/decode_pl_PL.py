# Przykładowy program w Pythonie dekodujący liczby z sekwencji STQC (Wersja w języku Polskim)

# Zaimportuj wymagane moduły
from sys import argv, exit
import re

# Odczytaj sekwenję. Jeżeli nie została podana, wyświetl pomoc
try:
	to_decode = argv[1]
except IndexError:
	# Wyświetl pomoc i wyjdź
	print("Poprawne użycie: python3 decode_pl_PL.py <sekwencja>")
	exit(0)

# Zregeneruj powtórzone znaki używając wyrażeń regularnych
replaced = re.sub(r"([0-3])4",r"\1\1","0"+to_decode)

# Przekształć liczbę spowrotem na Base10
try:
	final = int(replaced, 4)
except ValueError:
	# Wyjątek ValueError zostanie rzucony, gdy na wejściu znajdzie się niepoprawna sekwencja
	print("Podana sekwencja jest niepoprawna!")
	exit(2)

# Wyświetl zdekodowaną liczbę
print(final)