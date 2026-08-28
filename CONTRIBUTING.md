# How to contribute to the STQC documentation

If you want to contribute and help me creating this documentation, you're welcome! In this file you can find all types of contribution that I'll appreciate and rules, that your code should have to be merged to the **main** branch.

---

## Improving documentation

1. **Add more translations**. Currently, documentation is only available in Polish and English. If you know other languages, then you're welcome to contributions! Here are some rules, that your new documentation should follow:
    * **Don't modify format**. The format of documentation should be the same in all languages. You should only translate text, but formatting (like **bolds**, *italic*, codespaces) should remain unchanged.
    * **Translate only comments (for programs)**. If you are translating example programs, only change comments and printed messages. **DO NOT CHANGE** variable names or other code parts.
2. **Add examples also in other programming languages**. Currently, examples are only available in Python. If you know other languages, like C++, C, Java, ... - then you can add working examples in those languages too. Here are some rules, that you need to follow:
    * **Comments**. Add comments to your code quite frequently. This may help other people understand, what the code is doing.
    * **Don't make example programs too big**. Example files are only the **examples**, so they should be as short as possible. For example, if you are creating program that encodes number to a STQC sequence, your program should be doing **only** this thing.

---

## Improving programs

If you want to create whole program for all possible STQC operations (like *pystqc.py*) in other programming language, you can do it! Here are some rules, that you need to follow:
- **OOP style**. Code program in OOP style instead of procedural style to make it easier to use the source code in other projects
- **Add instructions**. Add all instructions to use your program. For example, create detailed *--help* instruction. If your program have to be compiled, attach **Makefile**.

---

## How to send your code

To do so, please make fork of this repository on GitHub. After finishing your work, make Pull Request. Then, I'll review it, and if the changes are good - your work will be merged to my repository, and your nick will be added to the *CREDITS* file!