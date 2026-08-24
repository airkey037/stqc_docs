# Example Python program to encode voivodeship and "powiat" number to ready STQC sequence

# Import required libraries
from sys import argv, exit
import re

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

# Function that outputs ready STQC sequence
def genstqc(sq:int, characters:int=None)->str:
	# Transform sequence from Base10 to Base4
	transformed = base10_to_base4(sq)
	# Check, was input number a negative number
	if transformed is None:
		raise ValueError("Input number can't be a negative number!")
	# Convert string to list
	as_list = list(transformed)
	# Add 0's at the beginning, if user specified amount of digits
	if characters is not None:
		# Check, is total digits less then minimum required
		if characters < len(as_list):
			# This isn't allowed, report an error
			raise ValueError(f"Output length set by the user is too short! {len(as_list)} required, {characters} wanted")
		# If everything is correct, expand list with 0's
		as_list = ['0'] * (characters - len(as_list)) + as_list
	# Return the final result
	return "".join(as_list)

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

# Generate sequence from voivodeship ID and powiat ID
voivodeship_sq = genstqc(voivodeship, 4)
powiat_sq = genstqc(powiat, 3)

# Replace repeated characters using Regex
final = re.sub(r"([0-3])\1",r"\g<1>4","0"+voivodeship_sq+powiat_sq)[1:]

# Print the result
print(final)