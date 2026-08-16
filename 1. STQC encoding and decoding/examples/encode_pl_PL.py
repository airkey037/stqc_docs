# Przykładowy program w Pythonie enkodujący liczby zgodnie ze standardem STQC (Wersja w języku Polskim)

# Zaimportuj wymagane moduły
from sys import argv, exit
import re

# Funkcja konwertująca liczby o podstawie 10 do podstawy 4
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

# Odczytaj liczbę wejściową. Jeżeli nie została podana, wyświetl wiadomość z pomocą
try:
	to_encode = int(argv[1])
except IndexError:
	# Wyświetl wiadomość z pomocą
	print("Poprawne użycie: python3 encode_en_US.py <liczba> <długość wyjścia (opcjonalnie)>")
	exit(0)
except ValueError:
	# Wartość wejściowa nie jest liczbą
	print("Wartość wejściowa nie jest liczbą!")
	exit(2)

# Zamień wejściową liczbę na podstawę 4
transformed = base10_to_base4(to_encode)

# Sprawdź, czy liczba wejściowa nie jest ujemna
if transformed is None:
	print("Liczba musi być dodatnia!")
	exit(2)

# Przekształć łańcuch na listę
as_list = list(transformed)

# Dodaj zera na początku, jeśli drugi parametr został podany
try:
	total_digits = int(argv[2])
	# Sprawdź, czy żądana długość nie jest mniejsza niż to możliwe
	if total_digits < len(as_list):
		# To nie jest dozwolone, wyświetl wiadomość o błędzie
		print(f"Żądana długość wyjściowa jest niemożliwa do zrealizowania! Wymagane jest {len(as_list)} znaków, a w parametrze zostało podane {total_digits}")
		exit(2)
	# Jeżeli wszystko jest poprawne, dodaj zera na początku
	as_list = ['0'] * (total_digits - len(as_list)) + as_list
except IndexError:
	# Możemy to zignorować - błąd pojawi się, gdy drugi parametr nie zostanie podany
	pass
except ValueError:
	# Wartość w drugim parametrze nie jest liczbą
	print("Wartość w drugim parametrze nie jest liczbą!")
	exit(2)

# Jeżeli pierwsza cyfra to zero, zamień ją na 4 (dekoder potrzebuje tej zamiany)
if as_list[0] == "0":
	as_list[0] = "4"

# Używając wyrażeń regularnych zamień drugą powtarzającą się liczbę na 4
final = re.sub(r"([0-3])\1",r"\g<1>4","".join(as_list))

# Wyświetl wynik
print(final)