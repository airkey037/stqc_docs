# Bartek's STQC decoder unofficial documentation

[Source](https://serwerbartka.pl/dekoder-stqc)

This documentation applies to the following versions of Bartek's STQC decoder:
* 2.15

---

## Decoding Voivodeship number

**IMPORTANT:** The voivodeship numbers aren't corresponding to the real administration divison in Poland (for example, units with different voivodeship numbers can practically be physically located the same one)

First of all, we need to decode the first sequence:

**4013241** -> **489**

Then, we need to use this formula:

$$v = \lfloor \frac{s}{64} \rfloor$$

Where:
* v -> voivodeship number
* s -> decimal representation of the first sequence

Plug the values:

$$v = \lfloor \frac{489}{64} \rfloor$$

$$v = 7$$

Result: **7**

**NOTE:** Voivodeship number have to fit in range 0-63

---

## Decoding powiat number

**IMPORTANT:** The powiat numbers aren't corresponding to the real administration divison in Poland (for example, units with different powiat numbers can practically be physically located the same one)

First of all, we need to decode the first sequence:

**4013241** -> **489**

Then, we are using this formula:

$$p = s \bmod 64$$

Where:
* p -> calculated powiat number
* s -> decimal representation of the first sequence

Plug the values:

$$p = 489 \bmod 64$$

$$p = 41$$

Result: **41**

**NOTE:** Powiat number have to fit in range 0-63.

---

## Encoding Voivodeship and Powiat number

In order to do this, we must get Voivodeship and Powiat number in decimal (both within range 0-63). Example:

Voivodeship: **31**
Powiat: **14**

Then, we are using this formula to get full decimal sequence:

$$s = 64 \cdot v + p$$

Where:
* s -> decimal sequence
* v -> voivodeship number (0-63)
* p -> powiat number (0-63)

Plug the values:

$$s = 64 \cdot 31 + 14$$

$$s = 1998$$

Finally, we are encoding this number using STQC (remember to force the output to be exactly 7 tones long):

**1998** -> **4134032**

---

In the *examples/* folder you can find Python programs that can encode/decode STQC sequence and determine Voivodeship and powiat number.