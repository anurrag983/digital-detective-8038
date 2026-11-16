# Mission 5 — Numbers and data

## 1. Task / objective
Convert numbers by hand between decimal, binary, and hexadecimal; check them in Python; build a working number converter script; and learn how text is stored.

## 2. Work completed
- Did all 7 number conversions by hand showing the steps.
- Checked my answers using Python functions like `bin()`, `hex()`, and `int()`.
- Wrote `number_converter.py` and tested it with 3 numbers.
- Answered questions about ASCII and UTF-8.

## 3. Commands / tools used
- `python3`
- `python3 mission-05-numbers-data/number_converter.py`

## 4. My understanding

### Task 5.1 — Manual Conversions (My Steps)
1. **Decimal 13 to binary:**
   - 13 / 2 = 6 (remainder 1)
   - 6 / 2 = 3 (remainder 0)
   - 3 / 2 = 1 (remainder 1)
   - 1 / 2 = 0 (remainder 1)
   - Writing remainders from bottom to top gives: **`1101`**

2. **Decimal 25 to binary:**
   - 25 / 2 = 12 (remainder 1)
   - 12 / 2 = 6 (remainder 0)
   - 6 / 2 = 3 (remainder 0)
   - 3 / 2 = 1 (remainder 1)
   - 1 / 2 = 0 (remainder 1)
   - Writing remainders from bottom to top gives: **`11001`**

3. **Binary 1010 to decimal:**
   - (1 × 8) + (0 × 4) + (1 × 2) + (0 × 1) = 8 + 0 + 2 + 0 = **`10`**

4. **Binary 1101 to decimal:**
   - (1 × 8) + (1 × 4) + (0 × 2) + (1 × 1) = 8 + 4 + 0 + 1 = **`13`**

5. **Hexadecimal A to decimal:**
   - A is just **`10`** in decimal.

6. **Hexadecimal 1F to decimal:**
   - (1 × 16) + (F × 1) = 16 + 15 = **`31`** (since F = 15)

7. **Binary 1111 to hexadecimal:**
   - In decimal, 1111 is 8 + 4 + 2 + 1 = 15.
   - In hexadecimal, 15 is written as **`F`**.

### Task 5.2 — Verifying in Python
| Expression | Python Output | Did it match? |
| :--- | :--- | :--- |
| `bin(13)` | `'0b1101'` | Yes, matches 1101 |
| `bin(25)` | `'0b11001'` | Yes, matches 11001 |
| `int('1010', 2)` | `10` | Yes, matches 10 |
| `int('1101', 2)` | `13` | Yes, matches 13 |
| `int('A', 16)` | `10` | Yes, matches 10 |
| `int('1F', 16)` | `31` | Yes, matches 31 |
| `hex(0b1111)` | `'0xf'` | Yes, matches F |

### Task 5.3 — Testing `number_converter.py`
| Test number | Binary output | Hexadecimal output |
| :--- | :--- | :--- |
| **42** | `0b101010` | `0x2A` |
| **255** | `0b11111111` | `0xFF` |
| **1024** | `0b10000000000` | `0x400` |

*How the functions work:*
- `bin()` takes a normal decimal integer and turns it into binary with a `0b` prefix.
- `hex()` turns a decimal integer into hexadecimal with a `0x` prefix.

### Task 5.4 — Storing text
- ASCII decimal for capital **`A`** is **`65`**.
- ASCII decimal for lowercase **`a`** is **`97`**.
- **Why do computers need an encoding standard?** Computers can only understand 0s and 1s. They cannot save letters directly, so they need a lookup standard (like ASCII) that tells them that the number 65 represents the letter 'A'.
- **Character outside basic ASCII:** The Indian Rupee symbol (**`₹`**) or emojis like **`💻`**, which use UTF-8.

## 5. Difficulties faced
Remembering which letters represent which numbers in hexadecimal (A through F).

## 6. How I resolved them
I wrote a small note for myself: A=10, B=11, C=12, D=13, E=14, F=15.

## 7. Evidence / files
- `number_converter.py`

## 8. Commit details
- Commit message: `Build number converter and practise data representation`
