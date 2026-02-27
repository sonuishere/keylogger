# Keylogger
Educational Python Keyboard Event Logger

Python 3.6+ | MIT License | Windows | Linux | macOS

------------------------------------------------------------

1. PROJECT OVERVIEW

Keylogger.py is an educational Python project designed to demonstrate:

- Keyboard event listening
- Keystroke buffering and grouping
- Clipboard interaction
- Timestamped logging
- Multithreaded execution handling

This project is strictly for learning purposes in controlled environments.

IMPORTANT LEGAL NOTICE:
Monitoring someone without explicit consent is illegal in many jurisdictions and may violate privacy laws (including India's IT Act 2000). Use only on systems you own or have written permission to test. Delete logs after experimentation.

------------------------------------------------------------

2. EDUCATIONAL OBJECTIVES

This project demonstrates:

- How global keyboard hooks work
- Event-driven programming in Python
- Buffer management logic
- Thread separation for stability
- File logging techniques

If you are studying cybersecurity, you should analyze both:
- How such tools operate
- How they are detected and prevented

------------------------------------------------------------

3. FEATURES

3.1 Keystroke Grouping
Printable characters are grouped into words.
Example:
Instead of logging: h e l l o
It logs:
hello

3.2 Clipboard Capture
Detects keyboard-based:
- Ctrl/Cmd + C (Copy)
- Ctrl/Cmd + X (Cut)
- Ctrl/Cmd + V (Paste)

Logs in format:
[paste: copied_text]

Note: Mouse-based copy/paste is not captured.

3.3 Timestamped Logs
Each log entry includes:
YYYY-MM-DD HH:MM:SS - data

3.4 Special Key Handling
Logs keys like:
[space]
[enter]
[shift]
[backspace]

Basic backspace support is implemented.

3.5 Append-Only Logging
Writes to keylog.txt
Does not overwrite previous data.

3.6 Graceful Exit
Press ESC to stop the logger.

3.7 Threaded Execution
Keyboard listener and clipboard access run in separate threads to prevent crashes.

------------------------------------------------------------

4. TECHNICAL STRUCTURE

Keyboard Listening:
Uses pynput.keyboard.Listener to capture key events.

Buffer System:
Characters accumulate in a buffer.
Buffer flushes on special keys or clipboard events.

Clipboard Access:
Uses tkinter for clipboard interaction.

Error Handling:
Exceptions are caught to prevent program termination.

------------------------------------------------------------

5. REQUIREMENTS

Python:
Version 3.6 or higher

Required Library:
pip install pynput

Tkinter:
Usually bundled with Python.
On Debian-based Linux:
sudo apt install python3-tk

------------------------------------------------------------

6. OPERATING SYSTEM SETUP

Windows:
Run Command Prompt as Administrator for full global capture.

Linux:
May require:
sudo python3 keylogger.py

Wayland may restrict input capture.
X11 works more reliably.

macOS:
Grant Accessibility permission:
System Settings → Privacy & Security → Accessibility
Add Python interpreter.

------------------------------------------------------------

7. INSTALLATION

Step 1:
git clone https://github.com/sonuishere/keylogger.git
cd keylogger

Step 2 (Recommended):
Create virtual environment:
python -m venv venv

Activate:
Windows:
venv\Scripts\activate

Linux/macOS:
source venv/bin/activate

Step 3:
pip install -r requirements.txt

------------------------------------------------------------

8. USAGE

Windows:
python keylogger.py

Linux/macOS:
python3 keylogger.py

Press ESC to stop logging.

Log file:
keylog.txt (located in project directory)

------------------------------------------------------------

9. SAMPLE OUTPUT

2026-02-15 11:00:00 - hello
2026-02-15 11:00:05 - [space]
2026-02-15 11:00:10 - world
2026-02-15 11:00:15 - [copy: world]
2026-02-15 11:00:20 - [paste: world]
2026-02-15 11:00:25 - [enter]

------------------------------------------------------------

10. LIMITATIONS

- Not stealth software
- Visible in terminal and task manager
- Does not capture mouse-based clipboard actions
- Does not capture secure fields
- Logs are plain text (no encryption)
- May be flagged by antivirus software
- Platform restrictions may apply

------------------------------------------------------------

11. SECURITY & ETHICS

Building input capture tools without understanding defensive detection creates incomplete knowledge.

Study:
- EDR detection mechanisms
- Behavioral monitoring
- Process inspection
- Anti-keylogging defenses

This project is educational only. It is not intended for surveillance.

------------------------------------------------------------

12. RESPONSIBLE USE GUIDELINES

- Use only on your own system
- Do not deploy on third-party machines
- Do not distribute malicious builds
- Delete logs after testing
- Avoid storing sensitive personal information

------------------------------------------------------------

13. POSSIBLE IMPROVEMENTS

- Log encryption
- Improved backspace logic
- Log rotation
- Structured JSON logging
- Defensive detection demo
- GUI monitoring dashboard

------------------------------------------------------------

14. CONTRIBUTING

Fork the repository and submit pull requests.

Focus on:
- Stability improvements
- Cross-platform refinement
- Defensive learning features

------------------------------------------------------------

15. LICENSE

MIT License

You must include a LICENSE file separately if not already present.

------------------------------------------------------------

FINAL NOTE

This is a learning project, not production software.
Use responsibly.
Understand both offensive and defensive perspectives.
Act ethically.
