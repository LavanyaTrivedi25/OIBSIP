# Safe Password Generator (Task 3)

A secure desktop-based password generator application built with Python's `tkinter` GUI framework. It utilizes cryptographic randomness (`secrets` module) to generate highly secure passwords with customizable parameters, clipboard auto-copy, strength analysis, and history tracking.

---

## Tech Stack
- **Language**: Python 3.x
- **GUI Framework**: `tkinter`
- **Security & Randomness**: `secrets`, `string`
- **Clipboard Utility**: `pyperclip`

---

## Key Features
- **Cryptographically Secure**: Utilizes Python's `secrets` module instead of standard pseudo-random number generators to ensure unpredictability.
- **Customizable Options**: 
  - Adjustable password length (minimum 8 characters).
  - Toggles for Uppercase, Lowercase, Numbers, and Symbols.
  - Option to exclude ambiguous characters (`0`, `O`, `l`, `1`).
- **Guaranteed Inclusion**: Ensures that at least one character from each selected pool is present in the final password.
- **Strength Evaluation**: Real-time password strength analyzer (Weak, Medium, Strong) with color-coded feedback.
- **Clipboard Integration**: Automatically copies newly generated passwords to the clipboard via `pyperclip`.
- **History Tracking**: Keeps track of and displays the last 5 recently generated passwords.

---

## Setup & Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/LavanyaTrivedi25/OIRSIP.git
   cd Python-Task3-RandomPasswordGenerator
