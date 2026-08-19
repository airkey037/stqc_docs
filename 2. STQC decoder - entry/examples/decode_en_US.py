# An example Python program that can decode command and unit ID from a decimal representation of 2nd STQC sequence

# Import required modules
from sys import argv, exit

# Define command list
CMDS = {
	0: "KASUJ",
	1: "ALARM",
	2: "PAGER",
	3: "TEST",
	4: "MAKRO",
	5: "OC.GR",
	6: "AI.OC1",
	7: "AI.OC2",
	8: "AI.OC3",
	9: "FONIA"
}

# Try to get decimal representation of 2nd sequence
try:
	sq_dec = int(argv[1])
except IndexError:
	# Display help message
	print("Usage: python3 decode_en_US.py <decimal 2nd sequence>")
	exit(0)
except ValueError:
	# Invalid number
	print("Invalid input number!")
	exit(2)

# Sequence can't be bigger than 9999 and can't be negative. Check it
if sq_dec < 1 or sq_dec > 9999:
	print("Input number have to fit in range 1-9999")
	exit(2)

# Calculate unit ID and command
unit = sq_dec % 1000
cmd = CMDS[int(sq_dec / 1000)]

# Display result
print(f"Unit ID: {unit}\nCommand: {cmd}")