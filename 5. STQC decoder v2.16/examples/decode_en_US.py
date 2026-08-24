# Example Python program to decode area number from STQC sequence

# Import required libraries
from sys import argv, exit
import re

# Function that transforms STQC sequence to a decimal number
def stqc_to_base10(stqc:str)->int:
	# Regenerate repeated charactets using Regex
    replaced = re.sub(r"([0-3])4",r"\1\1","0"+stqc)
    # Convert regenerated numbers back to Base10
    return int(replaced, 4)

# Get sequence; if not presented, display help message
try:
	to_decode = argv[1]
except IndexError:
	# Display help message and exit
	print("Usage: python3 decode_en_US.py <sequence>")
	exit(0)

# Check input sequence length
if len(to_decode) != 7:
	# Print error message
	print("Input sequence have to be exactly 7 characters long!")
	exit(2)

# Get 2 parts of a sequence
area1_sq = to_decode[:4]
area2_sq = to_decode[4:]

# Decode those parts
try:
    area1 = stqc_to_base10(area1_sq)
    area2 = stqc_to_base10(area2_sq)
except ValueError:
	# Invalid sequence
	print("Invalid sequence!")
	exit(2)

# Print the result
print(int(f"{area1}{area2:02d}"))