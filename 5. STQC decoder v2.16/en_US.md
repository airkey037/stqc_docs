# Bartek's STQC decoder unofficial documentation

[Source](https://serwerbartka.pl/dekoder-stqc/)

Docs for version **2.16**

---

## Decoding area number

To decode area number, we need to take the input sequence, and divide it to 4-digit and 3-digit part:

**4014342** -> **4014** and **342**

Then, we are decoding each one using method from folder 1:

**4014** -> **5**
**342** -> **62**

Finally, we need to join those two result numbers to get final result. In this case, the result is **562**.

### Important info!

Each one of those parts **have to** fit in range 0-63, since those are **6-bit** numbers. So, allowed ranges are:

* 0-63
* 100-163
* 200-263
...
* 6300-6363

---

In the *examples/* folder you can find example Python program that can decode/encode area number to a ready STQC sequence.