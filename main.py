import pytesseract
from PIL import ImageGrab
import pyperclip
import tkinter as tk
import shutil
import os
from pynput import keyboard as pynput_keyboard

# --- Configure Tesseract path ---
def configure_tesseract():
    custom_path = r'C:/Program Files/Tesseract-OCR/tesseract.exe'

    if custom_path:
        pytesseract.pytesseract.tesseract_cmd = custom_path
    else:
        found = shutil.which("tesseract")
        if found:
            pytesseract.pytesseract.tesseract_cmd = found
        else:
            raise RuntimeError(
                "Tesseract not found. Install it or set TESSERACT_PATH."
            )

configure_tesseract()

def on_activate():
    recognize_text(auto_copy=True)

def get_text_from_clipboard_image():
    try:
        image = ImageGrab.grabclipboard()
    except Exception as e:
        return None

    if image is None:
        return None

    try:
        text = pytesseract.image_to_string(image, lang='eng')
        return " ".join(text.split())
    except Exception as e:
        return None


def recognize_text(auto_copy=True):
    text = get_text_from_clipboard_image()
    if text:
        if auto_copy:
            pyperclip.copy(text)


def copy_text():
    current_text = status_label.cget("text")
    if current_text and not current_text.startswith(("⚠️", "🎯", "✅")):
        pyperclip.copy(current_text)


def toggle_pin():
    current_state = root.attributes("-topmost")
    new_state = not current_state
    root.wm_attributes("-topmost", new_state)
    pin_button.config(text="📌 Unpin" if new_state else "📍 Pin")

def start_hotkey_listener():
    hotkey = pynput_keyboard.HotKey(
        pynput_keyboard.HotKey.parse('<ctrl>+<shift>+v'),
        on_activate
    )

    def on_press(key):
        hotkey.press(listener.canonical(key))

    def on_release(key):
        hotkey.release(listener.canonical(key))

    global listener
    listener = pynput_keyboard.Listener(
        on_press=on_press,
        on_release=on_release
    )
    listener.start()

# --- GUI Setup ---
root = tk.Tk()
root.title("Clipboard image text extractor")
root.geometry("180x240")
#root.resizable(False, False)
root.configure(bg="#f9f9fb")

# Keep window always on top
root.wm_attributes("-topmost", False)

# --- Widgets ---
title_label = tk.Label(
    root,
    text="📋 Clipboard OCR Tool",
    font=("Segoe UI", 10, "bold"),
    bg="#f9f9fb"
)
title_label.pack(pady=(5, 5))

status_label = tk.Label(
    root,
    text="🎯 Press Ctrl+Shift+V\nto OCR from clipboard",
    wraplength=440,
    bg="#f9f9fb",
    justify="center",
    fg="#333",
    font=("Segoe UI", 10)
)
status_label.pack(pady=5)

btn_frame = tk.Frame(root, bg="#f9f9fb")
btn_frame.pack(pady=5)

recognize_button = tk.Button(
    btn_frame,
    text="Get from Clipboard",
    command=lambda: recognize_text(auto_copy=True),
    height=2,
    width=22,
    relief="groove",
    font=("Segoe UI", 10)
)
recognize_button.grid(row=0, column=0, padx=5)

copy_button = tk.Button(
    btn_frame,
    text="📄 Copy Text",
    command=copy_text,
    height=2,
    width=12,
    relief="groove",
    font=("Segoe UI", 10)
)
copy_button.grid(row=1, column=0, padx=5)

pin_button = tk.Button(
    btn_frame,
    text="📌 Pin",
    command=toggle_pin,
    height=2,
    width=10,
    relief="groove",
    font=("Segoe UI", 10)
)
pin_button.grid(row=2, column=0, padx=5)

# Start the global hotkey listener
start_hotkey_listener()

root.mainloop()
