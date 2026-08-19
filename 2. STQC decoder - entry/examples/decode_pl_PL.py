# Przykładowy program w Pythonie dekodujący numer jednostki i komendę z dziesiętnej reprezentacji drugiej sekwencji

# Zaimportuj wymagane moduły
from sys import argv, exit

# Lista komend
CMDS = {
	0: "KASUJ",
	1: "ALARM",
	2: "PAGER",
	3: "TEST",
	4: "MAKRO",
	5: "OC.GR",
	6: "AI.OC1",
	7: "AI.OC2",
	8: "AI.OC3",
	9: "FONIA"
}

# Spróbuj pobrać dziesiętną reprezentację drugiej sekwencji
try:
	sq_dec = int(argv[1])
except IndexError:
	# Wyświetl pomoc, gdy to się nie uda
	print("Poprawne użycie: python3 decode_pl_PL.py <druga sekwencja dziesiętnie>")
	exit(0)
except ValueError:
	# Niepoprawna liczba
	print("Niepoprawna liczba wejściowa!")
	exit(2)

# Sprawdź, czy sekwencja mieści się w zakresie 1-9999
if sq_dec < 1 or sq_dec > 9999:
	print("Liczba wejściowa musi zmieścić się w zakresie 1-9999!")
	exit(2)

# Oblicz numer jednostki i komendę
unit = sq_dec % 1000
cmd = CMDS[int(sq_dec / 1000)]

# Wyświetl wynik
print(f"Numer jednostki: {unit}\nKomenda: {cmd}")