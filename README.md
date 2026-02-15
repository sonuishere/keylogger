# Keylogger.py - Educational Python Keylogger

![Python](https://img.shields.io/badge/Python-3.6%2B-blue.svg) ![License](https://img.shields.io/badge/License-MIT-green.svg) ![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20Linux%20%7C%20macOS-orange.svg)

## 📝 Overview
This is a simple, educational Python-based keylogger designed to demonstrate keyboard event handling, clipboard monitoring, and logging mechanics. It captures keystrokes, groups them into words, handles special keys, and detects copy/cut/paste operations via keyboard shortcuts. **⚠️ Warning: This tool is for learning purposes only. Using it to monitor others without explicit consent is unethical, illegal in many jurisdictions, and could violate privacy laws (e.g., India's IT Act 2000). Always test on your own system and delete logs afterward.**

The script uses `pynput` for input listening and `tkinter` for clipboard access, making it cross-platform but with OS-specific setup needs.

## ✨ Features
- 🔤 **Keystroke Grouping**: Aggregates printable characters into words (e.g., "hello" instead of individual letters).
- 📋 **Clipboard Capture**: Detects and logs copy (Ctrl/Cmd+C), cut (Ctrl/Cmd+X), and paste (Ctrl/Cmd+V) with content (e.g., "[paste: some text]").
- ⏰ **Timestamped Logs**: Each entry includes a date-time stamp for tracking.
- 🔑 **Special Key Handling**: Logs keys like [space], [enter], [shift], etc., with basic backspace support.
- 🛑 **Graceful Exit**: Stops logging on Esc key press.
- 📂 **Append-Only Logging**: Writes to `keylog.txt` without overwriting existing data.
- 🧵 **Threaded Execution**: Handles Tkinter and listener in separate threads to avoid main thread errors.

## 🛠️ Requirements
- **Python**: 3.6 or higher (download from python.org).
- **Libraries**:
  - `pynput`: Install via `pip install pynput`.
  - `tkinter`: Usually bundled with Python; on Linux, install with `sudo apt install python3-tk` (or equivalent for your distro).
- **Permissions** (OS-specific):
  - Windows: Run as administrator for global capture (right-click Command Prompt > Run as administrator).
  - Linux: May need `sudo` for system-wide hooks; ensure X11/Wayland compatibility (e.g., on Ubuntu/Parrot OS, switch to X11 if issues).
  - macOS: Grant Accessibility permissions in System Settings > Privacy & Security > Accessibility (add Python or the script).
- **Hardware**: Standard keyboard; tested on desktops/laptops (e.g., Parrot OS on Raspberry Pi).

## 🚀 Installation
1. Clone or download the repository:
2. git clone https://github.com/sonuishere/keylogger.git
3. cd keylogger
2. Set up a virtual environment (recommended for all OS):
3. python -m venv venv  # Or python3 on Linux/macOS
4. - Activate:
  - Windows: `venv\Scripts\activate`
  - Linux/macOS: `source venv/bin/activate`
3. Install dependencies:
pip install -r requirements.txt
- **Windows-Specific**: If tkinter is missing (rare), ensure Python installation includes it (check via `python -m tkinter`).
- **Linux-Specific**: Install tkinter if needed: `sudo apt update && sudo apt install python3-tk` (for Debian-based like Ubuntu/Parrot OS) or `sudo dnf install python3-tkinter` (Fedora).
- **macOS-Specific**: tkinter is usually included; if not, reinstall Python via Homebrew (`brew install python-tk`).

## 📖 Usage
1. Run the script (from the repo directory):
- **Windows**: Open Command Prompt, navigate to folder, run `python keylogger.py` (or right-click > Run as administrator for full capture).
- **Linux**: Open Terminal, run `python3 keylogger.py` (use `sudo python3 keylogger.py` for global capture; e.g., on Parrot OS).
- **macOS**: Open Terminal, run `python3 keylogger.py` (ensure Accessibility granted first).
2. Type, copy/paste, etc., in any window—the script captures while running.
3. Press **Esc** to stop.
4. View logs in `keylog.txt` (appends new sessions; located in the same directory).

**Example Log Output:**
2026-02-15 11:00:00 - hello
2026-02-15 11:00:05 - [space]
2026-02-15 11:00:10 - world
2026-02-15 11:00:15 - [copy: world]
2026-02-15 11:00:20 - [paste: world]
2026-02-15 11:00:25 - [enter]
## ⚙️ How It Works
- **Event Listening**: Uses `pynput.keyboard.Listener` to hook key presses/releases.
- **Buffering**: Accumulates chars into a word buffer, flushed on special keys.
- **Clipboard Integration**: Detects modifiers + C/V/X, reads clipboard via Tkinter (thread-safe).
- **Error Handling**: Catches exceptions; debug prints for issues.

## ⚠️ Limitations and Warnings
- **Not Stealthy**: Visible in task manager/terminal; not hidden or persistent.
- **Incomplete Capture**: Misses mouse-based copy/paste, secure fields (e.g., passwords), or non-keyboard inputs.
- **Platform Quirks**: On Linux (e.g., Parrot OS), may need tweaks for Wayland; clipboard delays could vary. On Windows/macOS, admin/accessibility required for full functionality.
- **Ethical Concerns**: This isn't a production tool—it's educational. I challenge the assumption that building keyloggers is harmless; it can lead to misuse. Use responsibly, or better yet, explore ethical alternatives like input simulators for testing.
- **Security Risks**: Antivirus may flag it; running could expose your own data if mishandled.
- **No Encryption**: Logs are plain text—add your own if needed.

## 🤝 Contributing
Feel free to fork and submit PRs for improvements (e.g., better backspace handling). Keep it educational!

## 📄 License
MIT License - See [LICENSE](LICENSE) file for details. (Note: You'll need to add a LICENSE file separately if desired.)
