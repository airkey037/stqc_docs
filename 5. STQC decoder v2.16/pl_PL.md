# Nieoficjalna dokumentacja dekodera STQC Bartka

[Źródło](https://serwerbartka.pl/dekoder-stqc/)

Dokumentacja dla wersji:
* 2.16

---

## Dekodowanie numeru obszaru

Na początek dekodujemy sekwencję:

**4013241** -> **489**

Później używamy tego wzoru:

$$a = \lfloor \frac{s}{64} \rfloor \cdot 100 + s \bmod 64$$

Gdzie:
* a -> wynik, numer obszaru
* s -> dziesiętna reprezentacja sekwencji (musi zmieścić się w zakresie **0 - 4095**)

Podstawiamy wartości:

$$a = \lfloor \frac{489}{64} \rfloor \cdot 100 + 489 \bmod 64$$
$$a = \lfloor 7,640625 \rfloor \cdot 100 + 41$$
$$a = 7 \cdot 100 + 41$$
$$a = 741$$

Wynik: **741**

---

## Enkodowanie numeru obszaru

Zanim zaczniemy, musimy upewnić się, że numer obszaru, który chcemy zakodować, spełnia:

$$(a \bmod 100) \in ([0; 63] \cap \mathbb{N}) \wedge \lfloor \frac{a}{100} \rfloor \in ([0; 63] \cap \mathbb{N})$$

W prostych słowach, pierwsze 2 cyfry i ostatnie 2 cyfry muszą mieścić się w zakresie 0-63.

Później do faktycznego przekształcenia używamy tego wzoru:

$$s = \lfloor \frac{a}{100} \rfloor \cdot 64 + (a \bmod 100)$$

Gdzie:
* s -> wynik, dziesiętna reprezentacja sekwencji
* a -> numer obszaru

Spróbujmy zakodować numer obszaru **1832**.

Podstawiamy:

$$s = \lfloor \frac{1832}{100} \rfloor \cdot 64 + (1832 \bmod 100)$$
$$s = \lfloor 18,32 \rfloor \cdot 64 + 32$$
$$s = 18 \cdot 64 + 32$$
$$s = 1184$$

Wynik: **1184**

---

W folderze *examples/* możesz znaleźć przykładowe programy w Pythonie, które mogą enkodować i dekodować numer obszaru do sekwencji STQC.