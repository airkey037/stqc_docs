# Example Python program that encodes area number to a ready STQC sequence

# Import required modules
from sys import exit, argv
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
def genstqc(sq:int, characters:int=None,add_leading_0=True)->str:
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
	# If first digit is a 0, replace it with 4 (if add_leading_0 argument is True)
	if as_list[0] == "0" and add_leading_0:
		as_list[0] = "4"
	# Replace repeated characters using Regex
	final = re.sub(r"([0-3])\1",r"\g<1>4","".join(as_list))
	# Return the final result
	return final

# Get area number
try:
	area = f"{int(argv[1]):04d}"
except IndexError:
	# Display help message
	print("Usage: python3 encode_en_US.py <area>")
	exit(2)
except ValueError:
	# Invalid area number
	print("Invalid area number!")
	exit(2)

# Get 2 parts of an area number
area1 = int(area[:2])
area2 = int(area[2:])

# Check, are both values in range 0-63
if area1 < 0 or area1 > 63:
	print(f"First part of an area number have to fit in range 0-63! ({area1} given)")
	exit(2)
if area2 < 0 or area2 > 63:
	print(f"Second part of an area number have to fit in range 0-63! ({area2} given)")
	exit(2)

# Calculate output sequence
area1_sq = genstqc(area1, 4)
area2_sq = genstqc(area2, 3, add_leading_0=False)

# Output the sequence
print(area1_sq + area2_sq)