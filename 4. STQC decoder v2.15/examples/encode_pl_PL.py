# Przykładowy program w Pythonie enkodujący numer województwa i powiatu do gotowej sekwencji STQC

# Zaimportuj wymagane moduły
from sys import argv, exit

# Funkcja konwertująca Base10 na Base4
def base10_to_base4(base10:int)->str:
	if base10 < 0:
		return None
	binsgn = bin(base10)[2:]
	if len(binsgn) % 2 != 0:
		binsgn = "0" + binsgn
	it = iter(binsgn)
	numbers = []
	for d1, d2 in zip(it, it):
		numbers.append(str(int(d1+d2,2)))
	return "".join(numbers)

# Odczytaj numer powiatu i województwa
try:
	voivodeship = int(argv[1])
	powiat = int(argv[2])
except IndexError:
	# Wyświetl wiadomość z pomocą
	print("Poprawne użycie: python3 encode_pl_PL.py <województwo> <powiat>")
	exit(0)
except ValueError:
	# Jedna z tych liczb nie jest poprawna
	print("Jedna z podanych wartości nie jest poprawną liczbą!")
	exit(2)

# Sprawdź, czy te liczby mieszczą się w zakresie 0-63
if voivodeship < 0 or voivodeship > 63:
	print("Numer województwa musi mieścić się w zakresie 0-63!")
	exit(2)
if powiat < 0 or powiat > 63:
	print("Numer powiatu musi mieścić się w zakresie 0-63!")
	exit(2)

# Oblicz i wyświetl wynik na podstawie wzoru
print(64 * voivodeship + powiat)