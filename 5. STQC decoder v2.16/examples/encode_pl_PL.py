# Przykładowy program w Pythonie enkodujący numer obszaru do sekwencji STQC

# Zaimportuj wymagane moduły
from sys import exit, argv

# Pobierz numer obszaru
try:
	area = int(argv[1])
except IndexError:
	# Wyświetl pomoc
	print("Poprawne użycie: python3 encode_pl_PL.py <obszar>")
	exit(2)
except ValueError:
	print("To nie jest poprawna liczba dziesiętna!")
	exit(2)

# Sprawdź, czy numer obszaru jest poprawny
if not ((0 <= (area // 100) <= 63) and (0 <= (area % 100) <= 63)):
	print("Niepoprawny numer obszaru!")
	exit(2)

# Wyświetl wynik
print((area // 100) * 64 + (area % 100))