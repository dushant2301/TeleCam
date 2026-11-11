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

