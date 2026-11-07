# Bartek's STQC decoder unofficial documentation

[Source](https://serwerbartka.pl/dekoder-stqc)

This documentation applies to the following versions of Bartek's STQC decoder:

* 2.10
* 2.15
* 2.16

As you can see, this applies to all versions, so that's why I put this in one file.

This page contains informations, how **Bartek's STQC decoder** is parsing unit ID and command.

This information is encoded only in **the second sequence**, so if you want to decode them, you don't need to parse the first one.

---

## Decode unit ID

To decode the unit ID, after extracting the decimal number from the STQC sequence, use the **modulo** function.

$$u = s \bmod 1000$$

Where:
* u - unit number (range 0-999)
* s - decoded sequence

Let's say, that the decoded 2nd sequence is **1082**:

$$u = s \bmod 1000$$

Plug the values:

$$u = 1082 \bmod 1000$$

$$u = 82$$

Result: **82**

---

## Decode alarm siren's command

To get this command, we are dividing the input sequence by 1000 and rounding it down. Example for **1082**:

$$c = \lfloor \frac{s}{1000} \rfloor$$

$$c = \lfloor \frac{1082}{1000} \rfloor$$

$$c = \lfloor 1.082 \rfloor$$

$$c = 1$$

When you have the command code, plug it to this table to get the command name:

| Result | Name   |
|--------|--------|
| 0      | KASUJ  |
| 1      | ALARM  |
| 2      | PAGER  |
| 3      | TEST   |
| 4      | MAKRO  |
| 5      | OC.GR  |
| 6      | AI.OC1 |
| 7      | AI.OC2 |
| 8      | AI.OC3 |
| 9      | FONIA  |

**NOTE:** Please don't ask me, what these commands are doing - I don't have this information :(

Result: 1 -> **ALARM**

---

## Encode unit ID and alarm siren's command

First of all, to encode this information, you need both unit ID and command. Unit ID is a number from the range 0-999. To get the command ID, please see the table in the section above.

Example:
* Unit ID: 519
* Command: *TEST* -> 3

To get the decimal number of the result, use this formula:

$$s = 1000 \cdot c + u$$

Where:
* s - decimal representation of the sequence
* c - command ID
* u - unit ID

Plug the values:

$$s = 1000 \cdot 3 + 519$$

$$s = 3519$$

Result: **3519**

---

In the *examples/* folder you can find the example Python programs that are able to encode and decode unit ID and command.