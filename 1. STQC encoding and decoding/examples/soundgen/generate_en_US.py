# An example Python program that can encode STQC sequence to .mp3 file
# FFmpeg is required: https://ffmpeg.org/

# Import required modules
import math
import subprocess
from sys import argv, exit

# Get STQC sequence
argv.pop(0)
sequence = " ".join(argv)

# Define some variables
SAMPLE_RATE = 48000  # 48kHz sampling rate
TONE_LENGTH = 0.1    # 100ms <- single tone duration
BREAK_LENGTH = 0.2   # 200ms <- break length
FREQS = {            # Define tone frequencies
	"0": 980,
	"1": 1197,
	"2": 1446,
	"3": 1795,
	"4": 2105
}

# Check, is this a correct sequence
for tone in sequence:
	if tone not in FREQS.keys() and tone != " ":
		# This isn't a correct STQC sequence!
		print(f"{tone} is not a valid STQC tone! Allowed options: {", ".join(FREQS.keys())}, SPACE (break)")
		exit(2)

# Create file name
filename = f"sequence_{sequence.replace(" ","_")}.mp3"