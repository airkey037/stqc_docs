# Informacje o użyciu STQC jako systemu kontroli syren alarmowych

Ta dokumentacja opisuje, jak STQC jest używany w OSP.

Układ sekwencji do wysłania komend do syren alarmowych jest zbudowana z 7 tonów (100ms każdy), 200ms ciszy i 8 tonów (100ms każdy). Całe wywołanie trwa 1.7s.

Przykład:

```text
1234123 12341234
```

## Specyfikacja radiowa

Straż Pożarna w Polsce używa tych częstotliwości do wysyłania i wymiany informacji:

```text
148.725 MHz - TX
148.825 MHz - RX
```

**INFO:** Te kanały są używane **tylko** do transmisji sekwencji - kanały głosowe są odseparowane w celu uniknięcia zakłóceń, a ich częstotliwości zależą od regionu.

* Modulacja: **NFM** (Narrowband Frequency Modulation)
* Szerokość kanału: 12.5 kHz

Możesz użyć jakiegokolwiek odbiornika na pasmo VHF, jak RTL-SDR v4, i próbować odbierać te sygnały - zgodnie z art. 145 [ustawy Prawo komunikacji elektronicznej](https://isap.sejm.gov.pl/isap.nsf/download.xsp/WDU20240001221/T/D20241221L.pdf):

```text
1. Nie wymaga pozwolenia używanie urządzeń radiowych przeznaczonych wyłącznie do odbioru.
```
**Pamiętaj, że nadawanie jest nielegalne i zabronione!!**