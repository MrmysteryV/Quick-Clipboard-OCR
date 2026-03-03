# Quick-Clipboard-OCR
A lightweight python program that extracts text from images stored in your clipboard using Tesseract OCR using a shortcut or the simple GUI.

# Compatibility

## Operating Systems

| OS      | Supported | Notes                                                          |
| ------- | --------- | -------------------------------------------------------------- |
| Windows | ✅ Yes     | Fully supported                                                |
| macOS   | ✅ Yes     | Requires Tesseract installed via Homebrew                      |
| Linux   | ⚠ Partial | Clipboard image support may depend on your desktop environment |

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

## 3. Create a Virtual Environment (Recommended but not necessary)

### Windows

```bash
python -version(e.g 3.12) -m venv venv
venv\Scripts\activate
```

### macOS / Linux

```bash
python3 -version(e.g 3.12) -m venv venv
source venv/bin/activate
```

---

## 4. Install Python Dependencies

```bash
pip install -r requirements.txt
```

### Windows

```bash
py -version(e.g 3.12) -m pip install -r requirements.txt
```

---

## 5. (Optional) Specify Custom Tesseract Path

If Tesseract is not in your system `PATH`, set an environment variable:

### Windows

```bash
set TESSERACT_PATH=C:\Path\To\tesseract.exe
```

### macOS / Linux

```bash
export TESSERACT_PATH=/usr/local/bin/tesseract
```

---

# How to Use

## Start the Application

```bash
python main.py
```
You could also make a .bat file (on windows) in the same directory and create a shortcut to that file for easy access:
```bash
@echo off
call venv\Scripts\activate
set SCRIPT=main.py

if exist "%~dp0%SCRIPT%" (
    py -version(e.g 3.12) "%~dp0%SCRIPT%"
) else (
    echo "%SCRIPT%" not found in this directory.
)

pause
```
```bash
**Or a macOS / Linux shell script (.sh)**

SCRIPT="main.py"

if [ -d "venv" ]; then
    source venv/bin/activate
else
    echo "⚠️ Virtual environment not found. Create it first with:"
    echo "   python3 -m venv venv"
    exit 1
fi

if [ -f "$SCRIPT" ]; then
    # Run with Python from the virtual environment
    python "$SCRIPT"
else
    echo "⚠️ '$SCRIPT' not found in this directory."
fi
```
---

## Extract Text from Clipboard

1. Copy or screenshot an image containing text.
2. Press:

```
Ctrl + Shift + V
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

---

If you encounter issues or would like to contribute improvements, feel free to open a pull request or issue.

