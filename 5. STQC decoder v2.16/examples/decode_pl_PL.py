# Przykładowy program w Pythonie dekodujący numer obszaru z dziesiętnej reprezentacji sekwencji

# Zaimportuj wymagane moduły
from sys import argv, exit

# Pobierz dziesiętną reprezentację sekwencji; jeśli nie podano, wyświetl pomoc
try:
	to_decode = int(argv[1])
	if not (0 <= to_decode <= 4095):
		print("Sekwencja musi mieścić się w zakresie 0-4095!")
		exit(2)
except IndexError:
	# Wyświetl pomoc i wyjdź
	print("Poprawne użycie: python3 decode_pl_PL.py <dziesiętna_sekwencja>")
	exit(0)
except ValueError:
	# To nie jest poprawna liczba!
	print("To nie jest poprawna liczba!")
	exit(2)

# Wyświetl wynik
print((to_decode // 64) * 100 + (to_decode % 64))