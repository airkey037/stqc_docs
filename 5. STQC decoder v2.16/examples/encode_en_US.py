# An example Python program that encodes an area number to a decimal representation of the sequence

# Import required modules
from sys import exit, argv

# Get an area number
try:
	area = int(argv[1])
except IndexError:
	# Display help message
	print("Usage: python3 encode_en_US.py <area>")
	exit(2)
except ValueError:
	# Incorrect decimal number
	print("This is not a correct number!")
	exit(2)

# Ensure that the area number has a correct format
# To be honest: I didn't think that De Morgan's Laws would be useful, until today ;)
if not ((0 <= (area // 100) <= 63) and (0 <= (area % 100) <= 63)):
	print("Invalid area number!")
	exit(2)

# Output the result
print((area // 100) * 64 + (area % 100))