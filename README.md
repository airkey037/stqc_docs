# STQC Documentation

***NOTE:** English version below*

---

W tym repozytorium znajdziesz pełną dokumentację standardu STQC, czyli systemu selektywnego wywoływania używanego przez strażaków w OSP do aktywacji syren alarmowych.

Źródła danych można znaleźć w pliku **CREDITS**.

Niektóre programy zawarte w repozytorium wymagają programu [FFmpeg](https://ffmpeg.org/) do poprawnego działania.

Projekt jest udostępniony na licencji GNU GPL 3.0. Jej pełny zapis możesz znaleźć w pliku **LICENSE**.

## Surowo zabronione jest używanie poniższej dokumentacji oraz programów do nielegalnego uruchamiania syren alarmowych!!

Projekt jest podzielony na kilka folderów w celu łatwiejszej nawigacji:

1. **STQC encoding and decoding** - dokumentacje w tym folderze są poświęcone stricte samemu standardowi STQC, czyli temu, jak enkodować i dekodować liczby do odpowiednich tonów. Dokumentacja dostępna w językach: Polski, Angielski. W podfolderze *examples/* znajdują się programy w Pythonie umożliwiające enkodowanie i dekodowanie liczb do/z odpowiednich sekwencji STQC. [Źródło informacji](https://github.com/sq5bpf/multimon-ng-stqc)
2. **STQC decoder - entry** - wprowadzenie do metod enkodowania i dekodowania informacji przekazywanych syrenom alarmowym. W tym folderze znajdziesz również metodę, której używa [Dekoder STQC Bartka (serwerbartka.pl)](https://serwerbartka.pl/dekoder-stqc/) w wersjach 2.10, 2.15 i 2.16 do ustalenia numeru jednostki i komendy.

---

In this repository you can find full documentation of STQC - a system used by Polish firefighters to remotely enable and disable alarm sirens.

You can find all data sources that I used to create this documentation in the **CREDITS** file.

Some programs in this repo require [FFmpeg](https://ffmpeg.org/) to work.

Project is shared under terms of GNU GPL 3.0 licence. You can whole license in the **LICENSE** file.

## It is forbidden to use this documentation and programs to illegally enable alarm sirens!!

Project is divided into folders for easier navigation:

1. **STQC encoding and decoding** - documentations in this folder are focused stricte on the STQC standard - detailed instructions about encoding and decoding numbers to specific tones. Documentation is available in those languages: Polish, English. In the *examples/* subfolder you can find Python programs that can encode/decode numbers to/from STQC sequences. [Information source](https://github.com/sq5bpf/multimon-ng-stqc)2. **STQC decoder - entry** - methods of encoding and decoding informations used to control alarm sirens. You can also find documented method, that [Bartek's STQC decoder (serwerbartka.pl)](https://serwerbartka.pl/dekoder-stqc/) in version 2.10, 2.15 and 2.16 is using to determine unit number and command.