# Przykładowy program w Pythonie dekodujący numer województwa i powiatu z sekwencji STQC

# Zaimportuj wymagane moduły
from sys import argv, exit

# Odczytaj dziesiętną reprezentację sekwencji; jeśli nie podano, wyświetl wiadomość z pomocą
try:
	to_decode = int(argv[1])
	if to_decode < 0 or to_decode > 4095:
		print("Dziesiętna reprezentacja sekwencji musi mieścić się w zakresie 0-4095!")
		exit(2)
except IndexError:
	# Wyświetl pomoc i wyjdź
	print("Poprawne użycie: python3 decode_pl_PL.py <dziesiętna sekwencja>")
	exit(0)
except ValueError:
	print("To nie jest poprawna liczba!")
	exit(2)

# Wyświetl wyniki
print(f"Województwo: {to_decode // 64}\nPowiat: {to_decode % 64}")