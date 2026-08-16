# Example Python program to encode numbers using STQC (English version)

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

# Get number; if not presented, display help message
try:
	to_encode = int(argv[1])
except IndexError:
	# Display help message and exit
	print("Usage: python3 encode_en_US.py <number> <output n digits (optional)>")
	exit(0)
except ValueError:
	# Input value is not a number
	print("Given number is not a correct decimal number!")
	exit(2)

# Transform entered string to Base4
transformed = base10_to_base4(to_encode)

# Check, was input number a negative number
if transformed is None:
	print("Input number can't be a negative number!")
	exit(2)

# Convert string to list
as_list = list(transformed)

# Add 0's at the beginning, if 2nd parameter is given
try:
	total_digits = int(argv[2])
	# Check, is total digits less then minimum required
	if total_digits < len(as_list):
		# This isn't allowed, report an error
		print(f"Output length set by the user is too short! {len(as_list)} required, {total_digits} wanted")
		exit(2)
	# If everything is correct, expand list with 0's
	as_list = ['0'] * (total_digits - len(as_list)) + as_list
except IndexError:
	# We can ignore it
	pass
except ValueError:
	# Given output length isn't a number
	print("Output length set by the user isn't a correct number!")
	exit(2)

# If first digit is a 0, replace it with 4 (decoder needs this transformation)
if as_list[0] == "0":
	as_list[0] = "4"

# Replace repeated characters using Regex
final = re.sub(r"([0-3])\1",r"\g<1>4","".join(as_list))

# Output the final result
print(final)