# Entry to the STQC alarm sirens control system

This documention is describing, how exactly STQC is used in OSP.

The sequence used to send command to the receiver is constructed from 7 tones (100ms each one), 200ms break and 8 tones (100ms each one). Whole sequence is exactly 1.7s long.

Example:

```text
1234123 12341234
```

## Radio specs

OSP is using those VHF radio frequencies to send and exchange commands:

```text
148.725 MHz - TX
148.825 MHz - RX
```

* Modulation: **NFM** (Narrowband Frequency Modulation)
* Channel bandwidth: 12.5 kHz

You can use a radio receiver, like RTL-SDR v4, and try to receive those signals. **Remember, that transmitting is forbidden and illegal!!**