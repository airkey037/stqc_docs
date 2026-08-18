# Informacje o użyciu STQC jako systemu kontroli syren alarmowych

Ta dokumentacja opisuje, jak STQC jest używany w OSP.

Sekwencja użyta do wysłania komend jest zbudowana z 7 tonów (100ms każdy), 200ms ciszy i 8 tonów (100ms każdy). Całe wywołanie trwa 1.7s.

Przykład:

```text
1234123 12341234
```

## Specyfikacja radiowa

Straż używa tych częstotliwości do wysyłania i wymiany informacji:

```text
148.725 MHz - TX
148.825 MHz - RX
```

* Modulacja: **NFM** (Narrowband Frequency Modulation)
* Szerokość kanału: 12.5 kHz

Możesz użyć jakiegokolwiek odbiornika na pasmo VHF, jak RTL-SDR v4, i próbować odbierać te sygnały. **Pamiętaj, że nadawanie jest nielegalne i zabronione!!**