# Bartek's STQC decoder unofficial documentation

[Source](https://serwerbartka.pl/dekoder-stqc)

Docs for following versions:

* 2.10
* 2.15
* 2.16

This page contains informations, how **Bartek's STQC decoder** is reading unit ID and command.

To read those informations, you are using **the second sequence** (the 8-digit one, the one after the break)

---

## Read unit ID

To get unit ID, after converting STQC sequence to a decimal number, use the **modulo** function.

$$u = s \bmod 1000$$

Where:
* u - unit number
* s - decoded sequence

Let's say, that the decoded 2nd sequence is **1082**:

$$u = s \bmod 1000$$

Plug the values:

$$u = 1082 \bmod 1000$$

$$u = 82$$

Result: **82**

---

## Read command

To get command, we are dividing the input sequence by 1000 and rounding it down. Example for **1082**:

$$c = \lfloor \frac{s}{1000} \rfloor$$

$$c = \lfloor \frac{1082}{1000} \rfloor$$

$$c = \lfloor 1.082 \rfloor$$

$$c = 1$$

When you have the command code, plug it to this table to get command name:

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

**NOTE:** Please don't ask me, what those commands are doing - I don't have this information

Result: 1 -> **ALARM**