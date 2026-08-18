# Przykładowy program w Pythonie, który potrafi wygenerować odpowiednie tony STQC do pliku .mp3
# FFmpeg jest wymagany: https://ffmpeg.org/

# Zaimportuj wymagane moduły
from math import sin, pi
import subprocess
from sys import argv, exit
from os import remove

# Odczytaj sekwencję STQC
argv.pop(0)
sequence = " ".join(argv)

# Gdy sekwencja nie została podana, wyświetl pomoc
if len(sequence) == 0:
	print("Poprawne użycie: python3 generate_en_US.py <sekwencja>")
	exit(0)

# Zdefiniuj stałe
SAMPLE_RATE = 48000  # 48kHz częstotliwość próbkowania
TONE_LENGTH = 0.1    # 100ms <- długość pojedynczego tonu
BREAK_LENGTH = 0.2   # 200ms <- długość przerwy
FREQS = {            # Częstotliwości poszczególnych tonów
	"0": 980,
	"1": 1197,
	"2": 1446,
	"3": 1795,
	"4": 2105
}

# Sprawdź, czy podana sekwencja jest poprawnie sformatowana
for tone in sequence:
	if tone not in FREQS.keys() and tone != " ":
		# To nie jest poprawna sekwencja
		print(f"{tone} nie jest poprawnym tonem STQC! Dozwolone tony: {", ".join(FREQS.keys())}, SPACJA (przerwa)")
		exit(2)

# Stwórz nazwę pliku
filename = f"sekwencja_{sequence.replace(" ","_").strip("_")}.mp3"

# Uruchom FFmpeg
try:
	ffmpeg = subprocess.Popen(["ffmpeg","-loglevel","quiet","-y","-f","s16le","-ac","1","-ar",str(SAMPLE_RATE),"-i","-","-c:a","libmp3lame","-ac","1","-ar","48000","-b:a","64k","-f","mp3",filename],stdin=subprocess.PIPE)
except FileNotFoundError:
	# FFmpeg nie jest zainstalowany
	print("FFmpeg nie jest zainstalowany lub nie jest w zmiennej PATH!")
	exit(19)

# Uruchom pętlę, która przechodzi przez każdy ton
for tone in sequence:
	# Utwórz pustą tablicę na próbki dla każdego tonu
	pcm = bytearray()
	# Sprawdź, czy jest to ton, czy przerwa
	if tone == " ":
		# To jest przerwa, dodaj próbki ciszy
		for _ in range(int(SAMPLE_RATE * BREAK_LENGTH)):
			# Dodaj dwa bajty ciszy
			pcm.append(0)
			pcm.append(0)
	else:
		# To jest ton
		for sn in range(int(SAMPLE_RATE * TONE_LENGTH)):
			# Wygeneruj próbkę używając funkcji trygonometrycznych
			sample = sin(2 * pi * FREQS[tone] * sn / SAMPLE_RATE)
			# Pomnóż próbkę, aby była w zakresie dla formatu s16le
			value = int(sample * 32767)
			# Dodaj próbkę do tablicy jako little endian
			pcm.extend(value.to_bytes(2, byteorder="little", signed=True))
	# Sprawdź, czy proces FFmpeg żyje
	if ffmpeg.poll() is not None:
		print(f"FFmpeg niespodziewanie zakończył działanie z kodem {ffmpeg.returncode}")
		remove(filename)
		exit(19)
	# Spróbuj wysłać próbki do FFmpeg
	try:
		ffmpeg.stdin.write(pcm)
	except BrokenPipeError:
		# FFmpeg się zcrashował podczas zapisu
		print(f"Nastąpił crash FFmpeg podczas zapisu próbek! Kod wyjścia: {ffmpeg.returncode}")
		remove(filename)
		exit(19)

# Zamknij stdin i poczekaj, aż zakończy enkodowanie
ffmpeg.stdin.close()
ffmpeg.wait()