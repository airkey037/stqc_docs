# Encoding and decoding STQC

In STQC standard we are using 5 tones:

| Tone number | Frequency |
|-------------|-----------|
| 0           | 980 Hz    |
| 1           | 1197 Hz   |
| 2           | 1446 Hz   |
| 3           | 1795 Hz   |
| 4           | 2105 Hz   |

To generate those tones, we can use any program, that supports generating sine wave tone, like *Audacity* or *FFmpeg*:

```bash
# Example: generating tone 0 (980Hz) with length 2s using FFmpeg
ffmpeg -f lavfi -i sine=frequency=980 -t 2 -c:a libmp3lame -ac 1 -ar 44100 -f mp3 tone_0.mp3
```

### Encoding

Let's try encoding number 72. In STQC standard we are operating on numbers with base 4, so we need to convert number with base 10 to base 4 first:

**72** *(10)* = **1020** *(4)*

**IMPORTANT:** When we want our result to be n tones long, we can write additional 0's at the beginning. In "system selektywnego wywoływania" our sequences are 7 and 8 tones long. Let's say, that we want our sequence to be 7 tones long, so we are writing three 0's at the beginning.

**1020** -> **0001020**

Now, we need to find 2 identical numbers located next to each other, and replace 2nd number with **4**. We are doing it, because we want all tones to be exactly 100ms long, so decoder will decode it properly. **If first digit is 0, we are replacing it with 4 first!**

**0001020** -> **4041020**

Now, we can transform all digits to specific tones:

**4041020** -> *2105Hz 980Hz 2105Hz 1197Hz 980Hz 1446Hz 980Hz*

If you want to listen, how this sequence sounds like, you can use the command below to generate it:

```bash
ffmpeg -filter_complex "sine=frequency=980,atrim=duration=0.1,asplit=3[t01][t02][t03];sine=frequency=1197,atrim=duration=0.1[t1];sine=frequency=1446,atrim=duration=0.1[t2];sine=frequency=2105,atrim=duration=0.1,asplit=2[t41][t42];anullsrc,atrim=duration=0.5,asplit=2[start][end];[start][t41][t01][t42][t1][t02][t2][t03][end]concat=v=0:a=1:n=9[aout]" -map "[aout]" -c:a libmp3lame -ar 44100 -ac 1 -f mp3 sequence_4041020.mp3
```

### Decoding

We've got the sequence below:

*2105Hz 980Hz 2105Hz 1197Hz 1795Hz 2105Hz 980Hz*

First of all, we need to transform those tones to their numbers.
**WARNING!** After transforming tones to numbers, we need to add an extra zero at the beginning

*4041340* -> (adding 0) *04041340*

Now, we need to find all 4's and replace them with digits before them:

*04041340* -> *00001330*

Last step: convert base from 4 to 10:

**00001330** *(4)* = **124** *(10)*

Result: **124** was the encoded number.