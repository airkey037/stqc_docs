# Nieoficjalna dokumentacja dekodera STQC Bartka

[Źródło](https://serwerbartka.pl/dekoder-stqc/)

Dokumentacja dla wersji **2.16**

---

## Dekodowanie numeru obszaru

Aby zdekodować numer obszaru, bierzemy pierwszą sekwencję i dzielimy ją na 2 części o długościach 4 i 3 cyfry:

**4014342** -> **4014** oraz **342**

Następnie dekodujemy każdą z nich używając metody z folderu 1:

**4014** -> **5**
**342** -> **62**

Na końcu łączymy te dwa wyniki w celu uzyskania numeru obszaru. W tym przypadku wynik to **562**.

### Ważna informacja!

Każda z tych części **musi** zmieścić się w zakresie 0-63, ponieważ są to liczby **6-bitowe**. Dozwolone zakresy to:

* 0-63
* 100-163
* 200-263
...
* 6300-6363

---

W folderze *examples/* możesz znaleźć przykładowe programy w Pythonie, które mogą enkodować i dekodować numer obszaru do sekwencji STQC.