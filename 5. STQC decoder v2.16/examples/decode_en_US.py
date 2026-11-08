# An example Python program to decode an area number from a decimal representation of the sequence

# Import required libraries
from sys import argv, exit

# Get a decimal sequence; if not presented, display help message
try:
	to_decode = int(argv[1])
	if not (0 <= to_decode <= 4095):
		print("Sequence have to fit in range 0-4095!")
		exit(2)
except IndexError:
	# Display help message and exit
	print("Usage: python3 decode_en_US.py <sequence>")
	exit(0)
except ValueError:
	# Invalid number
	print("This is not a decimal number!")
	exit(2)

# Print the result
print((to_decode // 64) * 100 + (to_decode % 64))