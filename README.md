# ADA

### a desktop IDE for running legacy programming languages

![Python](https://img.shields.io/badge/Python-3.13-blue?style=flat-square&logo=python)
![PyQt6](https://img.shields.io/badge/PyQt6-6.11-green?style=flat-square)
![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)

> a desktop IDE that brings dead programming languages back to life. built to preserve computer culture, one language at a time.

---

## languages

| Language | Year | Status |
|----------|------|--------|
| BASIC | 1964 | ✅ supported |
| Pascal | 1970 | ✅ supported |
| COBOL | 1959 | ✅ supported |
| Fortran | 1957 | ✅ supported |
| Ada | 1980 | ✅ supported |
| ALGOL | 1958 | coming soon |
| LISP | 1958 | coming soon |
| Smalltalk | 1972 | coming soon |

---

## themes

ADA ships with 6 built-in themes, switchable live from the Theme menu:

| Theme | Inspiration |
|-------|-------------|
| Lovelace | creme, black, crimson — Ada Lovelace herself |
| Sakura | soft pink, deep rose |
| Mint | #c7f0d8 and #43523d |
| Military | dark forest green |
| iBook | early 2000s Mac sea blue |
| Nokia | deep navy, cyan |

---

## why

programming languages die. the environments that ran them disappear. the knowledge encoded in decades of legacy code becomes unrunnable, unreadable, and eventually lost.

ADA exists to keep that code alive. not as a museum exhibit — as a working interpreter you can run on your machine today.

named after Ada Lovelace, 1815. the first programmer who ever lived.

---

## quickstart

```bash
git clone https://github.com/reemaotaibi/ADA.git
cd ADA

pip install PyQt6

python main.py
```

---

## structure

```
ADA/
├── main.py                   # UI + theme engine
├── interpreter.py            # BASIC interpreter
├── pascal_interpreter.py     # Pascal interpreter
├── cobol_interpreter.py      # COBOL interpreter
├── fortran_interpreter.py    # Fortran interpreter
├── ada_interpreter.py        # Ada interpreter
├── languages.py              # language registry
└── examples.py               # example programs
```

---

## roadmap

- [ ] ALGOL support
- [ ] LISP support
- [ ] Smalltalk support
- [ ] Modula-2 support
- [ ] file open/save
- [ ] syntax error highlighting
- [ ] package as .exe for Windows

---

## license

MIT — use it, build on it, keep the past alive.

---

<p align="center">named after Ada Lovelace, 1815</p>
