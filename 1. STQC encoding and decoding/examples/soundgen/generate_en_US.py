# An example Python program that can encode STQC sequence to .mp3 file
# FFmpeg is required: https://ffmpeg.org/

# Import required modules
from math import sin, pi
import subprocess
from sys import argv, exit
from os import remove

# Get STQC sequence
argv.pop(0)
sequence = " ".join(argv)

# If sequence is empty, display help message
if len(sequence) == 0:
	print("Usage: python3 generate_en_US.py <sequence>")
	exit(0)

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
filename = f"sequence_{sequence.replace(" ","_").strip("_")}.mp3"

# Start FFmpeg
try:
	ffmpeg = subprocess.Popen(["ffmpeg","-loglevel","quiet","-y","-f","s16le","-ac","1","-ar",str(SAMPLE_RATE),"-i","-","-c:a","libmp3lame","-ac","1","-ar","48000","-b:a","64k","-f","mp3",filename],stdin=subprocess.PIPE)
except FileNotFoundError:
	# FFmpeg is not installed
	print("FFmpeg is not installed or not in your PATH!")
	exit(19)

# Start loop that comes through every tone
for tone in sequence:
	# Create a blank array for every sample
	pcm = bytearray()
	# Check, is it tone or break
	if tone == " ":
		# This is break, add silence
		for _ in range(int(SAMPLE_RATE * BREAK_LENGTH)):
			# Add 2 bytes of silence
			pcm.append(0)
			pcm.append(0)
	else:
		# This is tone, add it
		for sn in range(int(SAMPLE_RATE * TONE_LENGTH)):
			# Generate sample using math functions
			sample = sin(2 * pi * FREQS[tone] * sn / SAMPLE_RATE)
			# Multiply calculated sample to be in typical s16le range
			value = int(sample * 32767)
			# Add calculated sample to the list in little endian format
			pcm.extend(value.to_bytes(2, byteorder="little", signed=True))
	# Check, is process still alive
	if ffmpeg.poll() is not None:
		print(f"FFmpeg process finished unexpected with code {ffmpeg.returncode}")
		remove(filename)
		exit(19)
	# Try to write samples to FFmpeg's stdin
	try:
		ffmpeg.stdin.write(pcm)
	except BrokenPipeError:
		# FFmpeg died in the middle of writing
		print(f"FFmpeg died during writing samples to stdin! Exit code: {ffmpeg.returncode}")
		remove(filename)
		exit(19)

# Close stdin and wait for FFmpeg to finish encoding
ffmpeg.stdin.close()
ffmpeg.wait()