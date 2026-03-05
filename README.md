# Quick-Clipboard-OCR
A lightweight python program that extracts text from images stored in your clipboard using Tesseract OCR using a shortcut or the simple GUI.

# Compatibility

## Operating Systems

| OS      | Supported | Notes                                                          |
| ------- | --------- | -------------------------------------------------------------- |
| Windows | ✅ Yes     | Fully supported                                                |
| macOS   | ⚠ Partial    | Not tested, couldnt get to work yet                     |
| Linux   | ⚠ Partial | Not tested, couldnt get to work yet |

MacOS :
System Settings → Privacy & Security → Accessibility → Allow Terminal / Python to monitor keyboard input.

Linux:
Should work well on X11, but may not work on Wayland (depends on distro/security policy).

## Python Version

* Tested with: **Python 3.12**

---

# Installation & Setup

## 1. Install Tesseract OCR

Tesseract must be installed separately.

### Windows

1. Download and install Tesseract OCR from ```https://github.com/UB-Mannheim/tesseract/wiki``` and read the warning
2. Ensure it is added to your system `PATH`.

### macOS

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
brew install tesseract
```

### Ubuntu / Debian

```bash
sudo apt install tesseract-ocr
```

---

## 2. Clone the Repository

```bash
git clone https://github.com/MrmysteryV/Quick-Clipboard-OCR.git
cd Quick-Clipboard-OCR
```

---

## 3. Install Python Dependencies

```bash
python3.12 -m pip install -r requirements.txt
```

### Windows

```bash
py -version(e.g 3.12) -m pip install -r requirements.txt
```

---

## 4. Specify Custom Tesseract Path

Go into **main.py** and replace the default tesseract path with your one (on windows the default should be C:/Program Files/Tesseract-OCR/tesseract.exe):
```python
custom_path = r'C:/Program Files/Tesseract-OCR/tesseract.exe'
```
---

# How to Use

## Start the Application

**MacOS / Linux**
```bash
python3.12 main.py
```
**Windows**
```bash
py -version(e.g 3.12) main.py
```
You could also make a .bat file (on windows) in the same directory and create a shortcut to that file for easy access:
```bash
@echo off
set SCRIPT=main.py

if exist "%~dp0%SCRIPT%" (
    py -version(e.g 3.12) "%~dp0%SCRIPT%"
) else (
    echo "%SCRIPT%" not found in this directory.
)

pause
```
**Or a macOS / Linux shell script (.sh)**
```bash
SCRIPT="main.py"

if [ -f "$SCRIPT" ]; then
    python3.12 "$SCRIPT"
else
    echo "⚠️ '$SCRIPT' not found in this directory."
fi
```
---

## Extract Text from Clipboard

1. Copy or screenshot an image containing text.
2. Press:

```
Ctrl + Shift + V (you will probably need to press it multiple times before it pastes the text)
```

**OR**

Click the **"Get from Clipboard"** button.

The recognized text will automatically be copied to your clipboard.

---

## Additional Controls

* 📄 **Copy Text** – Copies the last recognized text manually
* 📌 **Pin** – Toggle always-on-top mode

---

# Notes

* The clipboard must contain an image (not text).
* Accuracy depends on image quality and language.
* Currently configured for English (`eng`) recognition.
