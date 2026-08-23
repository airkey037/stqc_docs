# An example Python program with ability to encode unit ID and command to a decimal representation of 2nd sequence

# Import required modules
from sys import argv, exit

# Define some variables
CMDS = {
	"KASUJ": 0,
	"ALARM": 1,
	"PAGER": 2,
	"TEST": 3,
	"MAKRO": 4,
	"OC.GR": 5,
	"AI.OC1": 6,
	"AI.OC2": 7,
	"AI.OC3": 8,
	"FONIA": 9
}

# Try to get unit ID and command
try:
	unit = int(argv[1])
	cmd = CMDS[argv[2].upper()]
except IndexError:
	# User haven't specified either unit or cmd, display help message
	print(f"Usage: python3 encode_en_US.py <unit id> <command>\nAllowed commands: {", ".join(CMDS.keys())}")
	exit(2)
except ValueError:
	# Specified unit ID is not a correct number
	print("Specified unit ID is not a valid number!")
	exit(2)
except KeyError:
	# Invalid command
	print(f"Specified command is not a valid command! Allowed: {", ".join(CMDS.keys())}")
	exit(2)

# Check, does unit ID fit in range 0-999
if unit < 0 or unit > 999:
	print("Unit ID have to fit in range 0-999!")
	exit(2)

# Calculate and display the decimal representation of 2nd sequence
print(cmd * 1000 + unit)