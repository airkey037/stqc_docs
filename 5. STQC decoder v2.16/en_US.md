# Bartek's STQC decoder unofficial documentation

[Source](https://serwerbartka.pl/dekoder-stqc/)

This documentation applies to the following versions of Bartek's STQC decoder:
* 2.16

---

## Decoding area number

First of all, we need to decode the first sequence:

**4013241** -> **489**

Then, we need to use this formula:

$$a = \lfloor \frac{s}{64} \rfloor \cdot 100 + s \bmod 64$$

Where:
* a -> area number
* s -> decimal representation of the first sequence (must fit in range **0 - 4095**)

Plug the values:

$$a = \lfloor \frac{489}{64} \rfloor \cdot 100 + 489 \bmod 64$$
$$a = \lfloor 7,640625 \rfloor \cdot 100 + 41$$
$$a = 7 \cdot 100 + 41$$
$$a = 741$$

Result: **741**

---

## Encoding area number

To encode the area number, we need to ensure, that the area number satisfies this:

$$(a \bmod 100) \in ([0; 63] \cap \mathbb{N}) \wedge \lfloor \frac{a}{100} \rfloor \in ([0; 63] \cap \mathbb{N})$$

In simple words, first two numbers and last two numbers have to fit in range 0-63.

Then, we can use this formula, to convert the area number to the sequence's decimal representation:

$$s = \lfloor \frac{a}{100} \rfloor \cdot 64 + (a \bmod 100)$$

Where:
* s -> decimal representation of the first sequence
* a -> area number

Let's try to encode area number **1832**.

Plug the values:

$$s = \lfloor \frac{1832}{100} \rfloor \cdot 64 + (1832 \bmod 100)$$
$$s = \lfloor 18,32 \rfloor \cdot 64 + 32$$
$$s = 18 \cdot 64 + 32$$
$$s = 1184$$

Result: **1184**

---

In the *examples/* folder you can find example Python program that can decode/encode area number to a ready STQC sequence.