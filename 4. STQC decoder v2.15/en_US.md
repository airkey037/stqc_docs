# Bartek's STQC decoder unofficial documentation

[Source](https://serwerbartka.pl/dekoder-stqc)

Docs for version **2.15**

---

## Decoding Voivodeship number

We are taking the first sequence, and getting first 4 digits of the sequence:

**4024031** -> **4024**

Then, we are decoding those first 4 digits (like in folder 1) and decoding them to get Voivodeship number:

**4024** -> **00022**

**00022** *(4)* = **10** *(10)*

Result: **10**

Voivodeship number have to fit in range 0-63

---

## Decoding "powiat" number

We are taking last 3 digits of the first sequence:

**4024031** -> **031**

Then, we are decoding it using instructions from folder 1:

**031** -> **0031**

**0031** *(4)* = **13** *(10)*

Result: **13**

Powiat number have to fit in range 0-63.

---

In the *examples/* folder you can find Python programs that can encode/decode STQC sequence and determine Voivodeship and "powiat" number.