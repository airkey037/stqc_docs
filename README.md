# STQC Documentation

***NOTE:** English version below*

---

W tym repozytorium znajdziesz pełną dokumentację standardu STQC, czyli systemu selektywnego wywoływania używanego przez strażaków w OSP do aktywacji syren alarmowych.

Źródła danych można znaleźć w pliku **CREDITS**.

Niektóre programy zawarte w repozytorium wymagają programu [FFmpeg](https://ffmpeg.org/) do poprawnego działania.

Projekt jest udostępniony na licencji GNU GPL 3.0. Jej pełny zapis możesz znaleźć w pliku **LICENSE**.

## SUROWO ZABRONIONE JEST UŻYWANIE PONIŻSZEJ DOKUMENTACJI ORAZ PROGRAMÓW DO NIELEGALNEGO URUCHAMIANIA SYREN ALARMOWYCH!!! Autorzy programu są ZWOLNIENI Z ODPOWIEDZIALNOŚCI za jakiekolwiek nielegalne użycia - ta dokumentacja została stworzona dla strażaków i innych ludzi, którzy chcą otrzymywać powiadomienia o alarmach w pobliskich jednostkach OSP. Autorzy mają nadzieję, że będzie ona używana JEDYNIE do tego celu.

Projekt jest podzielony na kilka folderów w celu łatwiejszej nawigacji:

1. **STQC encoding and decoding** - dokumentacje w tym folderze są poświęcone stricte samemu standardowi STQC, czyli temu, jak enkodować i dekodować liczby do odpowiednich tonów. Dokumentacja dostępna w językach: Polski, Angielski. W podfolderze *examples/* znajdują się programy w Pythonie umożliwiające enkodowanie i dekodowanie liczb do/z odpowiednich sekwencji STQC. [Źródło informacji](https://github.com/sq5bpf/multimon-ng-stqc)
2. **STQC decoder - entry** - wprowadzenie do metod enkodowania i dekodowania informacji przekazywanych syrenom alarmowym. W tym folderze znajdziesz również metodę, której używa [Dekoder STQC Bartka (serwerbartka.pl)](https://serwerbartka.pl/dekoder-stqc/) w wersjach 2.10, 2.15 i 2.16 do ustalenia numeru jednostki i komendy. Są one wszystkie wrzucone do jednego folderu, ponieważ są takie same dla każdej wersji, i zwyczajnie nie byłoby sensu opisywać tego samego w trzech różnych folderach.
3. **STQC decoder v2.10** - w tym folderze znajdują się (krótkie) informacje, jak [Dekoder STQC Bartka (serwerbartka.pl)](https://serwerbartka.pl/dekoder-stqc/) w wersji 2.10 wyznacza numer powiatu.
4. **STQC decoder v2.15** - w tym folderze znajdują się informacje, w jaki sposób [Dekoder STQC Bartka (serwerbartka.pl)](https://serwerbartka.pl/dekoder-stqc/) wyznacza numer województwa oraz powiatu.
5. **STQC decoder v2.16** - w tym folderze znajdują się informacje, w jaki sposób [Dekoder STQC Bartka (serwerbartka.pl)](https://serwerbartka.pl/dekoder-stqc/) wyznacza numer obszaru.

Program **pystqc.py** to pełny i kompletny program pozwalający na dekodowanie, transkodowanie, generowanie oraz enkodowanie wszystkich powyższych formatów. Aby dowiedzieć się więcej, uruchom go z opcją *--help*:

```bash
python3 pystqc.py --help
```

---

***NOTE:** I apologise if my English isn't perfect. I hope that you'll understand this documentation \:)*

In this repository you can find full documentation of STQC - a system used by Polish firefighters to remotely enable and disable alarm sirens.

You can find all data sources that I used to create this documentation in the **CREDITS** file.

Some programs in this repo require [FFmpeg](https://ffmpeg.org/) to work.

Project is shared under terms of GNU GPL 3.0 licence. You can whole license in the **LICENSE** file.

## IT IS FORBIDDEN TO USE THIS DOCUMENTATION AND PROGRAMS TO ILLEGALLY ENABLE ALARM SIRENS!!! Program authors ARE NOT RESPONSIBLE for any illegal usage of this program - it was created for firefighters and other people to allow them receiving notifications about alarms in nearby OSP units, and authors hope, that it will be used ONLY for this purpose.

Project is divided into folders for easier navigation:

1. **STQC encoding and decoding** - documentations in this folder are focused stricte on the STQC standard - detailed instructions about encoding and decoding numbers to specific tones. Documentation is available in those languages: Polish, English. In the *examples/* subfolder you can find Python programs that can encode/decode numbers to/from STQC sequences. [Information source](https://github.com/sq5bpf/multimon-ng-stqc)
2. **STQC decoder - entry** - methods of encoding and decoding informations used to control alarm sirens. You can also find documented method, that [Bartek's STQC decoder (serwerbartka.pl)](https://serwerbartka.pl/dekoder-stqc/) in version 2.10, 2.15 and 2.16 is using to determine unit number and command. I put them into one folder, because they are the same for all versions, so there is no need to put the same stuff in 3 folders.
3. **STQC decoder v2.10** - in this folder you can find (short) documentation, how [Bartek's STQC decoder](https://serwerbartka.pl/dekoder-stqc/) in version 2.10 is decoding "powiat*" number.
4. **STQC decoder v2.15** - in this folder you can find documentation, how [Bartek's STQC decoder](https://serwerbartka.pl/dekoder-stqc/) is decoding voivodeship and "powiat*" number.
5. **STQC decoder v2.16** - in this folder you can find documentation, how [Bartek's STQC decoder](https://serwerbartka.pl/dekoder-stqc/) is decoding area number.

\* I can't translate "powiat" to English, because I don't know any good word that matches exactly its meaning. Generally Voivodeships in Poland are divided into smaller administration regions called "powiats".

**pystqc.py** program is a full and powerful utility to encode, decode, transcode and generate all formats mentioned above. If you want to learn more, run:

```bash
python3 pystqc.py --help
```