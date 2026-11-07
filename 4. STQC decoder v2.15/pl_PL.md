# Nieoficjalna dokumentacja dekodera STQC Bartka

[Źródło](https://serwerbartka.pl/dekoder-stqc)

Dokumentacja dla wersji **2.15**

---

## Dekodowanie numeru województwa

**WAŻNE:** Numery województw używane przy selektywnym wywoływaniu nie odpowiadają rzeczywistemu podziałowi administracyjnemu w Polsce. Dla przykładu, dwie jednostki leżące fizycznie w tym samym województwie, mogą w rzeczywistości mieć dwa różne logiczne numery województw.

Dekodujemy pierwszą sekwencję:

**4013241** -> **489**

Następnie używamy tego wzoru:

$$v = \lfloor \frac{s}{64} \rfloor$$

Gdzie:
* v -> numer województwa
* s -> dziesiętna reprezentacja sekwencji

Podstawiamy wartości:

$$v = \lfloor \frac{489}{64} \rfloor$$

$$v = 7$$

Wynik: **7**

**NOTE:** Numer województwa musi mieścić się w przedziale 0-63.

---

## Dekodowanie numeru powiatu

**WAŻNE:** Numery powiatów używane przy selektywnym wywoływaniu nie odpowiadają rzeczywistemu podziałowi administracyjnemu w Polsce. Dla przykładu, dwie jednostki leżące fizycznie w tym samym powiecie, mogą w rzeczywistości mieć dwa różne logiczne numery powiatów.

Dekodujemy pierwszą sekwencję:

**4013241** -> **489**

Potem używamy tego wzoru:

$$p = s \bmod 64$$

Gdzie:
* p -> numer powiatu
* s -> dziesiętna reprezentacja pierwszej sekwencji

Podstawiamy wartości:

$$p = 489 \bmod 64$$

$$p = 41$$

Wynik: **41**

**NOTE:** Numer powiatu musi mieścić się w przedziale 0-63.

---

## Enkodowanie numeru województwa i numeru powiatu

Numer powiatu i numer województwa musi mieścić się w przedziale 0-63. Wybierzmy przykładowe liczby i spróbujmy je zakodować:

Województwo: **31**
Powiat: **14**

Póżniej używamy tego wzoru:

$$s = 64 \cdot v + p$$

Gdzie:
* s -> dziesiętna reprezentacja sekwencji
* v -> numer województwa (0-63)
* p -> numer powiatu (0-63)

Podstawiamy wartości:

$$s = 64 \cdot 31 + 14$$

$$s = 1998$$

Wynik: **1998**

---

W folderze *examples/* możesz znaleźć przykładowy program w Pythonie, który może enkodować/dekodować te informacje do/z gotowej sekwencji