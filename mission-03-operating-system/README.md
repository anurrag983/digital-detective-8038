# Mission 3 — Understand the operating system

## 1. Task / objective
Inspect system details, learn about running processes and PIDs, understand file permissions and paths, and explain the main jobs of an operating system.

## 2. Work completed
- Checked macOS system specs, user identity, disk space, and memory.
- Looked at running processes using `ps` and noted how PIDs work.
- Checked permissions on files and explained absolute vs relative paths.
- Completed the OS responsibilities table with simple explanations and examples.

## 3. Commands / tools used
- `uname -srm`, `whoami`, `df -h /`, `top -l 1`, `chmod`.

## 4. My understanding

### Task 3.1 — Exploring my system
| Information explored | What it tells you | Your observation (privacy-safe) |
| :--- | :--- | :--- |
| **Operating system details** | Kernel version and CPU type | `Darwin 27.2.0 arm64` (macOS on Apple Silicon) |
| **Current account identity** | Logged in username | `[redacted]` |
| **Available and used storage** | Total disk space and how much is left | `Size: 926Gi, Used: 13Gi, Avail: 808Gi (2% used)` |
| **System activity snapshot** | Number of running tasks and memory usage | `Processes: ~628 total, CPU: ~76% idle, RAM: 15GB used` |

### Task 3.2 — Processes
- **What is a process?** A process is simply a program that is currently running in memory (RAM).
- **What does the PID column mean?** PID stands for Process ID. It is a unique number that the operating system gives to every running program so it can keep track of it.
- **Two process examples:** `zsh` (my terminal shell) and `Google Chrome` (my web browser).

### Task 3.3 — Paths and permissions
- **Difference between paths:**
  - *Absolute path:* The complete address starting all the way from the root `/` folder. Example: `/Users/[redacted]/digital-detective-8038/README.md`.
  - *Relative path:* The address starting from where you currently are. Example: `mission-03-operating-system/README.md`.
- **Permissions:** A file showing `-rw-r--r--` means:
  - The owner has read (`r`) and write (`w`) permissions.
  - Group and others only have read (`r`) permission.
  - Nobody has execute (`x`) permission because it's a text file, not a runnable script.

### Task 3.4 — Operating system responsibilities
| OS responsibility | Your explanation | Example |
| :--- | :--- | :--- |
| **Process management** | Decides which running program gets to use the CPU and for how long. | Running my code while Chrome plays music in the background. |
| **Memory management** | Gives RAM to apps that need it and cleans it up when they close. | Freeing up memory when I quit a heavy app. |
| **Device management** | Connects and talks to hardware devices using drivers. | Sending print jobs to my Wi-Fi printer. |
| **File management** | Keeps all files and folders organized on the drive. | Saving files inside my assignment folders. |
| **User interface / shell** | Gives humans a visual desktop or terminal to interact with the computer. | The macOS desktop and the Zsh terminal window. |
| **Security and permissions** | Makes sure one user or app cannot damage system files or read private data. | Asking for my password/TouchID before installing software. |

## 5. Difficulties faced
When I ran `ps aux`, it printed hundreds of lines on the screen all at once and it was hard to read.

## 6. How I resolved them
I piped the command into `head -n 10` (`ps aux | head -n 10`) so I could easily see just the first few lines and the column headers.

## 7. Evidence / files
- System observation tables above.

## 8. Commit details
- Commit message: `Document operating system and file management`
