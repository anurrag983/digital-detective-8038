# Mission 4 — How programs run

## 1. Task / objective
Write and run a simple Python script from terminal, and compare how compiled languages differ from interpreted languages.

## 2. Work completed
- Created a `hello.py` file inside this folder.
- Ran it using `python3 hello.py` and saw the message printed.
- Filled out the compiler vs interpreter comparison table.

## 3. Commands / tools used
- `python3 hello.py`

## 4. My understanding

### Task 4.2 — Compiler vs Interpreter comparison
| Point | Compiler | Interpreter |
| :--- | :--- | :--- |
| **When translation happens** | Translates the whole program into machine code before running it. | Translates and runs the code line by line while the program is running. |
| **Typical output** | A standalone executable file (like a `.exe` or Mac binary). | No separate executable file; output happens directly. |
| **One example** | C or C++ | Python |
| **One advantage** | Runs much faster because the computer already has pure machine code. | Easier to write and test quickly without waiting to compile. |

### Explanation in my own words
A compiler takes your entire code and converts all of it into machine code ahead of time. This means if there is a mistake anywhere, it stops and won't make the file. An interpreter, on the other hand, reads your code line by line as it runs. If line 1 to 5 are fine, it will run them, and then crash only when it reaches a line with an error. Python uses an interpreter, which is why it is so fast and easy to test code in.

## 5. Difficulties faced
I wasn't sure whether to type `python` or `python3` in the terminal on Mac.

## 6. How I resolved them
I ran `python3 --version` to verify and always used `python3` to execute the file.

## 7. Evidence / files
- `hello.py`

## 8. Commit details
- Commit message: `Compare compilers and interpreters`
