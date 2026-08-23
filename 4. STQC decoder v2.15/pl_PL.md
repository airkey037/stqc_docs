# Nieoficjalna dokumentacja dekodera STQC Bartka

[Źródło](https://serwerbartka.pl/dekoder-stqc)

Dokumentacja dla wersji **2.15**

---

## Dekodowanie numeru województwa

Bierzemy pierwsze 4 cyfry pierwszej sekwencji:

**4024031** -> **4024**

Następnie dekodujemy je (używając metody z folderu 1). Tak otrzymamy numer województwa:

**4024** -> **00022**

**00022** *(4)* = **10** *(10)*

Wynik: **10**

Numer województwa musi być w zakresie 0-63.

---

## Dekodowanie numeru powiatu

Bierzemy ostatnie 3 cyfry pierwszej sekwencji:

**4024031** -> **031**

I dekodujemy ją, używając metody z folderu 1:

**031** -> **0031**

**0031** *(4)* = **13** *(10)*

Wynik: **13**

Numer powiatu musi zmieścić się w zakresie 0-63

---

W folderze *examples/* możesz znaleźć przykładowy program w Pythonie, który może enkodować/dekodować te informacje do/z gotowej sekwencji