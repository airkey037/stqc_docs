# Example Python program to decode numbers from STQC sequence (English version)

# Import required libraries
from sys import argv, exit
import re

# Get number; if not presented, display help message
try:
	to_decode = argv[1]
except IndexError:
	# Display help message and exit
	print("Usage: python3 decode_en_US.py <sequence>")
	exit(0)

# Regenerate repeated charactets using Regex
replaced = re.sub(r"([0-3])4",r"\1\1","0"+to_decode)

# Convert regenerated numbers back to Base10
try:
	final = int(replaced, 4)
except ValueError:
	# ValueError will be raised when input sequence is invalid
	print("Input sequence is invalid!")
	exit(2)

# Output the final result
print(final)