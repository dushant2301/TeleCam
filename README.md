<div align="center">

# 🎥 TeleCam 

**Your Personal, Secure, Cloud-Connected Webcam.**

[![Python 3.10+](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![Windows](https://img.shields.io/badge/Platform-Windows-0078D6.svg)](https://www.microsoft.com/windows)
[![Telegram API](https://img.shields.io/badge/Telegram-Bot%20API-2CA5E0.svg)](https://core.telegram.org/bots/api)
[![OpenCV](https://img.shields.io/badge/OpenCV-Computer%20Vision-green.svg)](https://opencv.org/)

TeleCam is a lightweight Windows automation tool that silently captures images from your laptop's webcam at regular intervals and securely delivers them directly to your Telegram account. 

</div>

---

## ✨ Features

*   🛡️ **Consent-First Architecture:** The application will never access your camera without explicit user authorization via a startup popup.
*   🕵️ **Stealth Background Mode:** Runs completely silently in the Windows System Tray. No annoying console windows.
*   📸 **Automated Scheduling:** Captures and sends an image every 10 seconds (configurable).
*   🌐 **Smart Network Monitor:** If your internet drops, TeleCam waits safely and resumes automatically once connection is restored.
*   🔒 **Secure Credentials:** Uses `.env` files to ensure API keys and Chat IDs are never hardcoded or exposed on GitHub.
*   🔴 **Visual Status Indicator:** The tray icon changes color (Red/Green) so you always know when the camera is active.
*   🚀 **Auto-Start:** Includes a custom `.vbs` script to launch the app seamlessly on Windows login.

---

## 🛠️ Tech Stack

*   **Core:** Python 3
*   **Computer Vision:** OpenCV (`cv2`)
*   **UI / Tray:** `pystray`, `Pillow`, `tkinter`
*   **Network:** `requests`
*   **Security:** `python-dotenv`

---

## 🚀 Installation & Setup

### 1. Prerequisites
*   Windows OS
*   Python 3.10 or higher installed.

### 2. Clone the Repository
```bash
git clone https://github.com/dushant2301/TeleCam.git
cd TeleCam

3. Install Dependencies
bash
pip install -r requirements.txt
🤖 Telegram Bot Integration (Crucial Step)
To receive the images, you need to create a Telegram Bot and get your Chat ID.

Step A: Create the Bot & Get Token
Open Telegram and search for BotFather.

Send the command /newbot.

Give your bot a name (e.g., My TeleCam) and a username (must end in bot, e.g., MyTeleCam_bot).

BotFather will give you an HTTP API Token. It looks like 123456789:ABCdefGHIjklMNOpqrSTUvwxYZ. Copy this.

Step B: Get your Chat ID
Search for userinfobot on Telegram and start a chat.

It will instantly reply with your Id (e.g., 123456789). Copy this.

Important: Go to your newly created bot and click Start so it has permission to message you.

Step C: Configure .env
Navigate to the config/ folder in this project.

Rename the file .env.example to .env.

Open .env and paste your credentials:

env
TELEGRAM_BOT_TOKEN=123456789:ABCdefGHIjklMNOpqrSTUvwxYZ
TELEGRAM_CHAT_ID=123456789
⚠️ SECURITY WARNING: Never commit your .env file to GitHub. It is already listed in .gitignore to protect you.

💻 Usage
Manual Run (For Testing)
Open a terminal and run:

bash
python main.py
A consent window will pop up. Click Yes.

Check your system tray (bottom right of Windows). You will see a green icon.

The icon will turn Red, capture an image, send it to Telegram, and turn Green again.

To stop the application, right-click the tray icon and select Exit.

Start on Windows Boot (Silent Mode)
To make TeleCam run automatically when you turn on your PC:

Open startup.vbs in a text editor.

Update the pythonPath and projectFolder to match your exact PC paths.

Press Win + R, type shell:startup, and press Enter.

Create a shortcut of startup.vbs and paste it into this Startup folder.

📁 Project Structure
File	Responsibility
main.py	Main entry point, consent UI, and threading coordinator.
tray.py	Handles the Windows System Tray icon and Exit menu.
camera.py	Opens the webcam, captures the frame, and saves it.
telegram.py	Handles the Telegram sendPhoto API request.
network_monitor.py	Pings Google to verify internet availability.
startup.vbs	Silent launcher for Windows boot.
config/.env	Stores your private Telegram Tokens (Ignored by Git).
📜 License
Distributed under the MIT License. See LICENSE for more information.

<div align="center"> <i>Built with ❤️ for privacy and automation.</i> </div> ```