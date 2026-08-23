# Przykładowy program w Pythonie potrafiący obliczyć dziesiętną reprezentację drugiej sekwencji z numeru jednostki i komendy (wersja po Polsku)

# Zaimportuj wymagane moduły
from sys import argv, exit

# Mapowanie komend na ich numery
CMDS = {
	"KASUJ": 0,
	"ALARM": 1,
	"PAGER": 2,
	"TEST": 3,
	"MAKRO": 4,
	"OC.GR": 5,
	"AI.OC1": 6,
	"AI.OC2": 7,
	"AI.OC3": 8,
	"FONIA": 9
}

# Spróbuj pobrać numer jednostki i komendę
try:
	unit = int(argv[1])
	cmd = CMDS[argv[2].upper()]
except IndexError:
	# Użytkownik nie sprecyzował numeru jednostki lub komendy, wyświetl pomoc
	print(f"Przykład użycia: python3 encode_pl_PL.py <numer jednostki> <komenda>\nDozwolone komendy: {", ".join(CMDS.keys())}")
	exit(0)
except ValueError:
	# Podany numer jednostki nie jest poprawną liczbą
	print("Podany numer jednostki nie jest poprawną liczbą!")
	exit(2)
except KeyError:
	# Niepoprawna komenda
	print(f"Niepoprawna komenda! Dozwolone: {", ".join(CMDS.keys())}")
	exit(2)

# Sprawdź, czy numer jednostki mieści się w przedziale 0-999
if unit < 0 or unit > 999:
	print("Numer jednostki nie mieści się w przedziale 0-999!")
	exit(2)

# Oblicz i wyświetl dziesiętną reprezentację drugiej sekwencji
print(cmd * 1000 + unit)