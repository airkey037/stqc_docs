# Example Python program to decode voivodeship and powiat number from STQC sequence

# Import required libraries
from sys import argv, exit

# Get a decimal representation of the sequence; if not presented, display help message
try:
	to_decode = int(argv[1])
	if to_decode < 0 or to_decode > 4095:
		print("The decimal representation of the sequence have to fit in range 0-4095!")
		exit(2)
except IndexError:
	# Display help message and exit
	print("Usage: python3 decode_en_US.py <decimal sequence>")
	exit(0)
except ValueError:
	print("This is not a correct number!")
	exit(2)

# Print the results
print(f"Voivodeship: {to_decode // 64}\nPowiat: {to_decode % 64}")