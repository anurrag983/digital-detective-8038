# Mission 6 — Git and GitHub

## 1. Task / objective
Understand how version control works, practice staging and committing, create a feature branch, and open a Pull Request.

## 2. Work completed
- Checked repository status and commit log.
- Created a new branch called `update-about`.
- Added my learning summary to the main `README.md`.
- Created a Pull Request and recorded the Git command glossary.

## 3. Commands / tools used
- `git status`, `git add`, `git commit`, `git log`, `git checkout -b`, `git push`.

## 4. My understanding

### Task 6.1 — Git workflow
| Git operation | What it does in your own words |
| :--- | :--- |
| **Check repository status (`git status`)** | Shows which files are changed, staged, or not tracked yet. |
| **Stage selected changes (`git add`)** | Selects the files you want to include in your next save (commit). |
| **Create a commit (`git commit -m`)** | Saves a permanent snapshot of the staged files with an explanation. |
| **View commit history (`git log --oneline`)** | Displays a list of all past commits and their messages. |

*Difference between staging and committing:* Staging is like putting the items you want into a package; committing is sealing the package and writing the delivery note.

### Task 6.3 — Branches and Pull Requests
- **What is a branch?** A branch is a separate copy of your project where you can work on new features or test changes without breaking the working code on the `main` branch.
- **What is a Pull Request?** A Pull Request (PR) is a way of telling your teammates on GitHub: "I finished my work on this branch, please review my changes and merge them into main."

### Task 6.4 — Git command glossary
- **Initialize a repository:** `git init`
- **Check status:** `git status`
- **Stage changes:** `git add <filename>`
- **Commit changes:** `git commit -m "<message>"`
- **View history:** `git log --oneline`
- **Create a branch:** `git branch <branch-name>`
- **Switch branches:** `git checkout <branch-name>`
- **Publish changes to GitHub:** `git push -u origin <branch-name>`
- **Retrieve remote changes:** `git pull`

## 5. Difficulties faced
Remembering the exact command to create and switch to a new branch in one step.

## 6. How I resolved them
Used `git checkout -b update-about` which creates the branch and switches to it at the same time.

## 7. Evidence / files
- Branch `update-about` and PR on GitHub.

## 8. Commit details
- Commit message: `Complete Git and GitHub collaboration mission`
