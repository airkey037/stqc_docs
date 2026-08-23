# Przykładowy program w Pythonie enkodujący numer województwa i powiatu do gotowej sekwencji STQC

# Zaimportuj wymagane moduły
from sys import argv, exit
import re

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

# Funkcja, która zwraca gotową sekwencję STQC
def genstqc(sq:int, characters:int=None,add_leading_0=True)->str:
	# Zamień sekwencję wejściową z Base10 do Base4
	transformed = base10_to_base4(sq)
	# Sprawdź, czy jest to liczba ujemna
	if transformed is None:
		raise ValueError("Input number can't be a negative number!")
	# Zamień string na listę
	as_list = list(transformed)
	# Dodaj 0 na początku, jeżeli użytkownik sprecyzował liczbę cyfr
	if characters is not None:
		# Sprawdź, czy liczba znaków żądanych przez użytkownika nie jest mniejsza niż wymagana
		if characters < len(as_list):
			# To nie jest dozwolone
			raise ValueError(f"Output length set by the user is too short! {len(as_list)} required, {characters} wanted")
		# Jeżeli wszystko jest poprawne, dodaj zera na początku
		as_list = ['0'] * (characters - len(as_list)) + as_list
	# Jeżeli pierwsza cyfra to 0, zamien ją na 4 (gdy podany argument to True)
	if as_list[0] == "0" and add_leading_0:
		as_list[0] = "4"
	# Używając wyrażeń regularnych zamień powtarzające się znaki
	final = re.sub(r"([0-3])\1",r"\g<1>4","".join(as_list))
	# Zwróć wynik
	return final

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

# Wygeneruj sekwencję województwa i powiatu
voivodeship_sq = genstqc(voivodeship, 4)
powiat_sq = genstqc(powiat, 3, add_leading_0=False)

# Wyświetl wynik
print(voivodeship_sq + powiat_sq)