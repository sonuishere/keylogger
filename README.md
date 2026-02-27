<div align="center">

# 🔑 Keylogger

### Educational Python Keyboard Event Logger

![Python](https://img.shields.io/badge/Python-3.6%2B-blue?style=flat-square&logo=python)
![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)
![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20Linux%20%7C%20macOS-lightgrey?style=flat-square)

> ⚠️ **For educational and authorized testing purposes only.**

</div>

---

## ⚠️ Legal Notice

> Monitoring someone **without explicit consent** is illegal in many jurisdictions and may violate privacy laws (including India's IT Act 2000).
>
> - ✅ Use only on systems you **own** or have **written permission** to test.
> - ✅ Delete logs after experimentation.
> - ❌ Do **not** deploy on third-party machines.
> - ❌ Do **not** distribute malicious builds.

---

## 📌 Table of Contents

- [Project Overview](#-project-overview)
- [Educational Objectives](#-educational-objectives)
- [Features](#-features)
- [Technical Structure](#-technical-structure)
- [Requirements](#-requirements)
- [Platform-Specific Setup](#-platform-specific-setup)
- [Installation](#-installation)
- [Usage](#-usage)
- [Sample Output](#-sample-output)
- [Limitations](#-limitations)
- [Security & Ethics](#-security--ethics)
- [Responsible Use Guidelines](#-responsible-use-guidelines)
- [Possible Improvements](#-possible-improvements)
- [Contributing](#-contributing)
- [License](#-license)

---

## 📖 Project Overview

`Keylogger.py` is an **educational Python project** designed to demonstrate core programming and cybersecurity concepts including:

- Keyboard event listening
- Keystroke buffering and grouping
- Clipboard interaction
- Timestamped logging
- Multithreaded execution handling

This project is **strictly for learning purposes** in controlled environments.

---

## 🎓 Educational Objectives

This project teaches:

| Concept | Description |
|--------|-------------|
| Global Keyboard Hooks | How OS-level key capture works |
| Event-Driven Programming | Reacting to user input events in Python |
| Buffer Management | Accumulating and flushing data efficiently |
| Thread Separation | Keeping processes stable via multithreading |
| File Logging | Writing structured, timestamped logs to disk |

> 💡 If you are studying cybersecurity, analyze **both** how such tools operate *and* how they are **detected and prevented**.

---

## ✨ Features

### 🔤 Keystroke Grouping
Printable characters are grouped into words instead of individual characters.

```
# Instead of:
h e l l o

# Logs as:
hello
```

---

### 📋 Clipboard Capture
Detects keyboard-triggered clipboard actions:

| Action | Shortcut |
|--------|----------|
| Copy | `Ctrl/Cmd + C` |
| Cut | `Ctrl/Cmd + X` |
| Paste | `Ctrl/Cmd + V` |

Logged in format:
```
[paste: copied_text]
```

> **Note:** Mouse-based copy/paste is **not** captured.

---

### 🕐 Timestamped Logs
Every log entry is prefixed with a timestamp:
```
YYYY-MM-DD HH:MM:SS - data
```

---

### ⌨️ Special Key Handling
Special keys are logged with descriptive labels:

```
[space]  [enter]  [shift]  [backspace]
```

> Basic backspace support is included.

---

### 📝 Append-Only Logging
- Writes to `keylog.txt`
- Never overwrites existing data

---

### 🚪 Graceful Exit
Press `ESC` to safely stop the logger at any time.

---

### 🧵 Threaded Execution
The keyboard listener and clipboard access run in **separate threads** to prevent crashes and ensure stability.

---

## 🏗️ Technical Structure

```
┌─────────────────────────────────────────────┐
│              Keylogger.py                   │
├──────────────────┬──────────────────────────┤
│  Keyboard Thread │  Clipboard Thread        │
│  pynput.Listener │  tkinter clipboard API   │
├──────────────────┴──────────────────────────┤
│             Buffer System                   │
│  Accumulates chars → Flushes on trigger     │
├─────────────────────────────────────────────┤
│           keylog.txt (Append Mode)          │
└─────────────────────────────────────────────┘
```

| Component | Technology Used |
|-----------|----------------|
| Keyboard Listening | `pynput.keyboard.Listener` |
| Clipboard Access | `tkinter` |
| Error Handling | Try/except to prevent crashes |
| Log Output | Append-mode file writes |

---

## 📦 Requirements

| Requirement | Details |
|-------------|---------|
| Python | Version **3.6** or higher |
| `pynput` | `pip install pynput` |
| `tkinter` | Usually bundled with Python |

**Tkinter on Debian/Ubuntu Linux:**
```bash
sudo apt install python3-tk
```

---

## 🖥️ Platform-Specific Setup

### 🪟 Windows
Run Command Prompt as **Administrator** for full global key capture:
```
Right-click → "Run as administrator"
```

---

### 🐧 Linux
May require elevated privileges:
```bash
sudo python3 keylogger.py
```

> - **X11** works more reliably.
> - **Wayland** may restrict input capture.

---

### 🍎 macOS
Grant Accessibility permission:
```
System Settings → Privacy & Security → Accessibility → Add Python interpreter
```

---

## 🚀 Installation

**Step 1 — Clone the repository:**
```bash
git clone https://github.com/sonuishere/keylogger.git
cd keylogger
```

**Step 2 — Create a virtual environment (Recommended):**
```bash
python -m venv venv
```

Activate it:

| Platform | Command |
|----------|---------|
| Windows | `venv\Scripts\activate` |
| Linux / macOS | `source venv/bin/activate` |

**Step 3 — Install dependencies:**
```bash
pip install -r requirements.txt
```

---

## ▶️ Usage

| Platform | Command |
|----------|---------|
| Windows | `python keylogger.py` |
| Linux / macOS | `python3 keylogger.py` |

- Press **`ESC`** to stop logging.
- Log output is saved to **`keylog.txt`** in the project directory.

---

## 📄 Sample Output

```
2026-02-15 11:00:00 - hello
2026-02-15 11:00:05 - [space]
2026-02-15 11:00:10 - world
2026-02-15 11:00:15 - [copy: world]
2026-02-15 11:00:20 - [paste: world]
2026-02-15 11:00:25 - [enter]
```

---

## ⚠️ Limitations

| Limitation | Details |
|------------|---------|
| Not stealth software | Visible in terminal and task manager |
| No mouse capture | Mouse-based clipboard actions not logged |
| No secure field capture | Password fields may be excluded |
| Plain text logs | No encryption applied |
| Antivirus flags | May be detected by security software |
| Platform restrictions | Wayland, macOS permissions may limit functionality |

---

## 🔒 Security & Ethics

> Building input capture tools without understanding **defensive detection** creates incomplete cybersecurity knowledge.

Complement this project by studying:

- 🛡️ EDR (Endpoint Detection & Response) mechanisms
- 📊 Behavioral monitoring
- 🔍 Process inspection
- 🚫 Anti-keylogging defenses

This project is **educational only** — it is not intended for surveillance.

---

## ✅ Responsible Use Guidelines

- ✅ Use only on **your own system**
- ✅ Delete logs after testing
- ❌ Do not deploy on third-party machines
- ❌ Do not distribute malicious builds
- ❌ Do not store sensitive personal information

---

## 🛠️ Possible Improvements

| Feature | Description |
|---------|-------------|
| Log Encryption | Protect stored data with encryption |
| Improved Backspace Logic | More accurate editing simulation |
| Log Rotation | Prevent unbounded log file growth |
| JSON Logging | Structured, machine-readable output |
| Defensive Detection Demo | Show how keyloggers can be detected |
| GUI Dashboard | Visual monitoring interface |

---

## 🤝 Contributing

Contributions are welcome!

1. **Fork** the repository
2. Make your changes on a new branch
3. Submit a **Pull Request**

**Focus areas:**
- Stability improvements
- Cross-platform refinement
- Defensive learning features

---

## 📜 License

This project is licensed under the **MIT License**.

> You must include a `LICENSE` file separately if not already present.

---

<div align="center">

### 🧠 Final Note

*This is a learning project, not production software.*
*Use responsibly. Understand both offensive and defensive perspectives. Act ethically.*

</div>
