# Example Python program to encode voivodeship and powiat number to ready STQC sequence

# Import required libraries
from sys import argv, exit

# Function that converts from Base10 (digits 0-9) to Base4 (digits 0-3, like in STQC)
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

# Get voivodeship and powiat number; if not presented, display help message
try:
	voivodeship = int(argv[1])
	powiat = int(argv[2])
except IndexError:
	# Display help message and exit
	print("Usage: python3 encode_en_US.py <voivodeship> <powiat>")
	exit(0)
except ValueError:
	# One of those values is not a correct number
	print("One of given values is not a correct decimal number!")
	exit(2)

# Check, are those numbers in 0-63 range
if voivodeship < 0 or voivodeship > 63:
	print("Voivodeship ID have to fit in range 0-63!")
	exit(2)
if powiat < 0 or powiat > 63:
	print("Powiat ID have to fit in range 0-63!")
	exit(2)

# Use the formula to calculate and print the decimal representation of the sequence
print(64 * voivodeship + powiat)