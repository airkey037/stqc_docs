# Enkodowanie i dekodowanie STQC

W standardzie STQC używamy 5 tonów:

| Numer kodu | Częstotliwość |
|------------|---------------|
| 0          | 980 Hz        |
| 1          | 1197 Hz       |
| 2          | 1446 Hz       |
| 3          | 1795 Hz       |
| 4          | 2105 Hz       |

Aby wygenerować poszczególne tony, można użyć jakiegokolwiek programu umożliwiającego generowanie tonu sinusoidalnego o danej częstotliwości, np. *Audacity* lub *FFmpeg*:

```bash
# Przykład: generujemy ton 0 o długości 2s
ffmpeg -f lavfi -i sine=frequency=980 -t 2 -c:a libmp3lame -ac 1 -ar 44100 -f mp3 ton_0.mp3
```

### Przykładowe enkodowanie

Spróbujmy przeprowadzić przykładowy proces enkodowania dla liczby 72. W standardzie STQC używamy podstawy 4, więc najpierw musimy zamienić liczbę z podstawy 10 na 4:

**72** *(10)* = **1020** *(4)*

**WAŻNE:** jeżeli przy enkodowaniu celujemy w konkretną długość sekwencji, jaką chcemy otrzymać (np. 7 i 8 w systemie selektywnego wybierania), dopisujemy na początku tyle zer, aby otrzymać liczbę, której zapis będzie tak długi, ile tonów ostatecznie chcemy otrzymać. Powiedzmy, że w tym przykładzie będzie to 7:

**1020** -> **0001020**

Teraz należy znaleźć dwie takie same liczby obok siebie i zamienić drugą z nich na 4. Robimy to po to, aby nigdy jeden ton nie był dłuższy niż 100ms (bo takiej długości dla każdego tonu używa standard STQC), bo mogłoby to skutkować błędnym zdekodowaniem przez odbiornik. **Jeżli pierwsza cyfra to 0, zamieniamy ją na 4 w pierwszej kolejności!**

**0001020** -> **4041020**

Teraz każdą otrzymaną cyfrę zamieniamy na odpowiedni ton, a każdemu tonowi nadajemy długość 100ms:

**4041020** -> *2105Hz 980Hz 2105Hz 1197Hz 980Hz 1446Hz 980Hz*

Jeżeli chcesz odsłuchać, jak brzmi ta sekwencja, poniższa komenda FFmpeg będzie mogła ją wygenerować:

```bash
ffmpeg -filter_complex "sine=frequency=980,atrim=duration=0.1,asplit=3[t01][t02][t03];sine=frequency=1197,atrim=duration=0.1[t1];sine=frequency=1446,atrim=duration=0.1[t2];sine=frequency=2105,atrim=duration=0.1,asplit=2[t41][t42];anullsrc,atrim=duration=0.5,asplit=2[start][end];[start][t41][t01][t42][t1][t02][t2][t03][end]concat=v=0:a=1:n=9[aout]" -map "[aout]" -c:a libmp3lame -ar 44100 -ac 1 -f mp3 sekwencja_4041020.mp3
```

### Przykładowe dekodowanie

Dostaliśmy taką sekwencję tonów:

*2105Hz 980Hz 2105Hz 1197Hz 1795Hz 2105Hz 980Hz*

Na początku musimy zamienić te dźwięki na numery tonów.
**UWAGA!** Gdy już zamienimy tony na numery, na początku musimy dołożyć 0

*4041340* -> (dokładamy zero) *04041340*

Teraz znajdujemy wszystkie czwórki i zamienimy je na liczbę przed nimi:

*04041340* -> *00001330*

Ostatni krok to zamiana liczby zapisanej czwórkowo na zapis dziesiętny:

**00001330** *(4)* = **124** *(10)*

Zakodowana liczba to **124**.

#### Przykładowe, w pełni udokumentowane, programy w Pythonie można znaleźć w folderze examples/