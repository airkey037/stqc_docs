# Nieoficjalna dokumentacja dekodera STQC Bartka

[Źródło](https://serwerbartka.pl/dekoder-stqc)

Dokumentacja obejmuje następujące wersje:

* 2.10
* 2.15
* 2.16

Ta strona opisuje, jak **Dekoder STQC Bartka** odczytuje numer jednostki oraz komendę.

Te informacje są przekazywane w **drugiej sekwencji** (tej ośmiocyfrowej, tej po przerwie), więc to tą sekwencję należy zdekodować.

---

## Numer jednostki

Aby odczytać numer jednostki, po konwersji z sekwencji STQC na liczbę dziesiętną używamy funkcji **modulo** (reszty z dzielenia).

$$u = s \bmod 1000$$

Gdzie:
* u - numer jednostki
* s - zdekodowana sekwencja

Powiedzmy, że zdekodowaną drugą sekwencją jest **1082**:

$$u = s \bmod 1000$$

Podstaw wartości do wzoru:

$$u = 1082 \bmod 1000$$

$$u = 82$$

Wynik: **82**

---

## Read command

Aby odczytać komendę, dzielimy zdekodowaną sekwencję przez 1000 i zaokrąglamy w dół. Znów powiedzmy, że sekwencją jest **1082**:

$$c = \lfloor \frac{s}{1000} \rfloor$$

$$c = \lfloor \frac{1082}{1000} \rfloor$$

$$c = \lfloor 1.082 \rfloor$$

$$c = 1$$

Gdy masz już numer komendy, podstaw ją do tej tabelki, aby uzyskać jej nazwę:

| Wynik | Nazwa  |
|-------|--------|
| 0     | KASUJ  |
| 1     | ALARM  |
| 2     | PAGER  |
| 3     | TEST   |
| 4     | MAKRO  |
| 5     | OC.GR  |
| 6     | AI.OC1 |
| 7     | AI.OC2 |
| 8     | AI.OC3 |
| 9     | FONIA  |

**INFO:** Proszę nie kierować do mnie zapytań, co oznaczają te komendy - nie mam takich informacji.

Wynik: 1 -> **ALARM**