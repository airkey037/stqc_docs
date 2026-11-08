# Entry to the STQC alarm sirens control system

This documention is describing, how exactly STQC is used in OSP.

The sequence used to send commands to the receiver is constructed from 7 tones (100ms each one), 200ms break and 8 tones (100ms each one). The whole sequence is exactly 1.7s long.

Example:

```text
1234123 12341234
```

## Radio specs

Firefighters in Poland are using those VHF radio frequencies to send and exchange commands:

```text
148.725 MHz - TX
148.825 MHz - RX
```

**NOTE:** Those channels are used **only** to exchange commands between sirens - the voice channels are completely separated, and their frequency depends on the region.

* Modulation: **NFM** (Narrowband Frequency Modulation)
* Channel bandwidth: 12.5 kHz

You can use a radio receiver, like RTL-SDR v4, and try to receive those signals. According to the [Prawo komunikacji elektronicznej](https://isap.sejm.gov.pl/isap.nsf/download.xsp/WDU20240001221/T/D20241221L.pdf):

```text
1. Nie wymaga pozwolenia używanie urządzeń radiowych przeznaczonych wyłącznie do odbioru.
```

**Remember, that transmitting is forbidden and illegal!!**