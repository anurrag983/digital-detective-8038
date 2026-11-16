# Mission 2 — Become comfortable with the Terminal

## 1. Task / objective
Practice basic terminal navigation and file commands, test redirecting output, use command flags and pipes, and understand package managers.

## 2. Work completed
- Practiced running basic commands like `pwd`, `ls`, `cd`, `mkdir`, `cp`, `mv`, and `cat`.
- Created a `terminal-practice` folder and practiced writing lines to a file with `>` and `>>`.
- Tested flags like `ls -lah` and piped the result into `head -n 5`.
- Checked Homebrew package manager on my Mac.

## 3. Commands / tools used
- `pwd`, `ls`, `cd`, `mkdir`, `echo`, `cp`, `mv`, `cat`, `head`, `|`, `brew`.

## 4. My understanding

### Task 2.1 — Terminal operations
| Operation / command name | What it does | What I observed |
| :--- | :--- | :--- |
| **Current-directory display (`pwd`)** | Prints the folder path I am currently in | `/Users/[redacted]/digital-detective-8038` |
| **Directory listing (`ls`)** | Lists files and folders in my current folder | Showed all my mission folders and README.md |
| **Detailed listing (`ls -l`)** | Shows permissions, file size, owner, and date | Showed lines like `drwxr-xr-x` with details |
| **Change directory (`cd ..`)** | Moves one folder up | Prompt changed to the parent folder |
| **Create directory (`mkdir test`)** | Makes a new folder | A new folder was created immediately |
| **Create empty file (`touch file.txt`)** | Makes a blank file | File created with 0 bytes size |
| **Copy file (`cp file.txt copy.txt`)** | Makes a duplicate copy | Now had two identical files |
| **Move / rename file (`mv copy.txt renamed.txt`)** | Renames or moves a file | The copied file was renamed |
| **Display file contents (`cat file.txt`)** | Prints the text inside a file to the screen | Showed the text directly in the terminal |

### Task 2.2 — Practicing file changes
- **Difference between replacing and adding text:** Using `>` wipes out whatever was inside the file and writes the new text. Using `>>` adds the new text to the bottom of the file without deleting existing lines.
- **Difference between copying and moving:** Copying (`cp`) leaves the original file where it was and makes a second copy. Moving (`mv`) takes the original file to a new location or changes its name, so only one file remains.
- **What `pwd` tells you:** It gives you the full absolute path from the root `/` to where your terminal is currently sitting, so you don't get lost in folders.
- **Why `ls` is useful:** It lets you see what is inside a folder before trying to open or edit files, and helps check if a command worked.

### Task 2.3 — Flags and pipes
- Flags change how commands behave. For example, `ls` just shows names, but `ls -lah` gives a detailed list (`-l`), shows hidden files (`-a`), and shows sizes in easy-to-read KB/MB (`-h`).
- **Pipes (`|`):** In `ls -lah | head -n 5`, the pipe symbol takes the big list that `ls -lah` would print, and feeds it straight into `head -n 5`, which cuts it down to just the first 5 lines.

### Task 2.4 — Package managers
Homebrew is installed on my Mac (`Homebrew 7.0.13`). A package manager is super helpful because instead of downloading a installer from a browser and dragging it to Applications, I can just type a single command like `brew install <tool>` and it automatically downloads, installs, and keeps it updated.

## 5. Difficulties faced
When I first tried adding a second line to my text file, I accidentally used a single `>` instead of `>>`, which deleted my first line.

## 6. How I resolved them
I quickly realized my mistake, recreated the file with line 1, and then used `echo "line 2" >> practice.txt` to append without overwriting.

## 7. Evidence / files
- `terminal-practice/practice.txt`
- `terminal-practice/notes_backup.txt`

## 8. Commit details
- Commit message: `Complete Terminal and file management mission`
