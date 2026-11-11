# 🎥 TeleCam

<div align="center">

### Your Personal, Secure, Cloud-Connected Webcam

![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)
![Platform](https://img.shields.io/badge/Platform-Windows-0078D6.svg)
![Telegram](https://img.shields.io/badge/Telegram-Bot%20API-2CA5E0.svg)
![OpenCV](https://img.shields.io/badge/OpenCV-Computer%20Vision-green.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

**TeleCam** is a lightweight Python-based Windows webcam automation application that captures images during an explicitly authorized camera session and delivers them directly to your personal Telegram account.

</div>

---

## ✨ Features

- 🛡️ **Consent-First Architecture:** Camera access starts only after explicit user authorization.
- 🖥️ **System Tray Integration:** Runs unobtrusively in the Windows system tray without an unnecessary application window.
- 📸 **Automated Scheduling:** Automatically captures and sends images at configurable intervals (default: 10 seconds) during an authorized session.
- 🌐 **Smart Network Monitor:** Detects internet connectivity and waits for the connection to return before attempting delivery.
- 🔒 **Secure Credentials:** Uses environment variables and `.env` files to protect Telegram API credentials.
- 🔴 **Visual Status Indicator:** Tray icon changes color to communicate the camera's active or inactive state.
- 🚀 **Windows Auto-Start:** Includes a custom `.vbs` launcher for starting the application when Windows boots.
- 🧹 **Safe Shutdown:** Releases the webcam and terminates background tasks when the application exits.

---

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python 3 | Core application |
| OpenCV | Webcam access and image capture |
| Telegram Bot API | Image delivery |
| Requests | HTTP communication |
| python-dotenv | Environment configuration |
| pystray | Windows system tray |
| Pillow | Tray icon generation |
| Tkinter | Consent interface |
| Threading | Background execution |

---

## 🚀 Installation & Setup

### 1. Prerequisites

- Windows 10 or Windows 11
- Python 3.10 or higher
- A working webcam
- An active internet connection
- A Telegram account

### 2. Clone the Repository

Open PowerShell or the VS Code terminal:

```bash
git clone https://github.com/dushant2301/TeleCam.git
```

Navigate into the project directory:

```bash
cd TeleCam
```

### 3. Install Dependencies

Install all required Python packages:

```bash
pip install -r requirements.txt
```

---

## 🤖 Telegram Bot Integration

To receive captured images, you need to create a Telegram bot and configure your Chat ID.

### Step A: Create a Telegram Bot

1. Open Telegram.
2. Search for [BotFather](https://t.me/BotFather).
3. Send the command `/newbot`.
4. Enter a name for your bot, such as `My TeleCam`.
5. Choose a username ending in `bot`, such as `MyTeleCam_bot`.
6. BotFather will generate an HTTP API token.
7. Copy and securely store this token.

### Step B: Get Your Telegram Chat ID

1. Search for [userinfobot](https://t.me/userinfobot) on Telegram.
2. Start a conversation with the bot.
3. It will display your Telegram user ID.
4. Copy the ID.
5. Open your newly created Telegram bot and press **Start**.

### Step C: Configure Environment Variables

Navigate to the `config/` directory.

Create a file named `.env` or rename `.env.example` to `.env`.

Add your credentials:

```env
TELEGRAM_BOT_TOKEN=YOUR_BOT_TOKEN
TELEGRAM_CHAT_ID=YOUR_CHAT_ID
```

Replace the placeholders with your actual credentials.

> ⚠️ **Security Warning:** Never upload your `.env` file to GitHub. Keep it excluded through `.gitignore`. If your bot token is accidentally exposed, regenerate it using BotFather.

---

## 💻 Usage

### Manual Application Launch

Open the project directory in your terminal and execute:

```bash
python main.py
```

Application workflow:

1. The application starts.
2. A consent window requests permission to activate the webcam session.
3. After authorization, the application runs in the system tray.
4. The tray icon indicates the camera status.
5. During the authorized session, images are captured at the configured interval.
6. Captured images are delivered to your configured Telegram account.
7. Right-click the tray icon and select **Exit** to close the application.

### Start Automatically on Windows Boot

TeleCam includes a `startup.vbs` script for Windows startup integration.

Follow these steps:

1. Open `startup.vbs` in a text editor.
2. Update the Python executable path.
3. Update the project directory path.
4. Press `Win + R`.
5. Enter:

```text
shell:startup
```

6. Press Enter.
7. Place a shortcut to `startup.vbs` inside the Startup folder.

The application will launch automatically when Windows starts. Camera access still requires the application's explicit authorization.

---

## 📁 Project Structure

```text
TeleCam/
│
├── config/
│   ├── .env
│   └── .env.example
│
├── captures/
│
├── main.py
├── tray.py
├── camera.py
├── webcam.py
├── telegram.py
├── network_monitor.py
├── scheduler.py
│
├── startup.vbs
├── requirements.txt
├── .gitignore
├── LICENSE
└── README.md
```

### File Responsibilities

| File | Responsibility |
|---|---|
| `main.py` | Main application entry point and threading coordinator |
| `tray.py` | Windows system tray interface and Exit functionality |
| `camera.py` | Webcam initialization, image capture and image saving |
| `webcam.py` | Webcam-related functionality and testing |
| `telegram.py` | Telegram Bot API integration and image delivery |
| `network_monitor.py` | Internet connectivity detection |
| `scheduler.py` | Configurable automatic capture scheduling |
| `startup.vbs` | Windows startup launcher |
| `config/.env` | Private Telegram credentials |
| `requirements.txt` | Python dependencies |
| `.gitignore` | Excludes sensitive and temporary files |

---

## ⚙️ Configuration

The capture interval can be customized according to your requirements.

Default interval:

```python
CAPTURE_INTERVAL = 10
```

The interval is measured in seconds.

For example:

```python
CAPTURE_INTERVAL = 30
```

This changes the interval to 30 seconds.

---

## 🔐 Privacy & Security

TeleCam is designed around user consent and responsible webcam access.

- Camera access requires explicit authorization.
- Camera activity must remain apparent to the laptop user.
- Captured images should only be sent to the configured, authorized Telegram recipient.
- Telegram credentials must remain private.
- The webcam must be released when the application exits.
- Users should not use the application to photograph people without their knowledge or permission.

---

## 🧪 Testing

Before using the application regularly, verify the following:

- [ ] Python dependencies install successfully.
- [ ] Webcam is detected correctly.
- [ ] Consent interface works.
- [ ] Tray icon appears.
- [ ] Camera status indicator updates correctly.
- [ ] Manual image capture works.
- [ ] Telegram image delivery works.
- [ ] Internet disconnection is handled.
- [ ] Automatic scheduling works during an authorized session.
- [ ] Exit closes the application and releases the webcam.
- [ ] Windows startup integration works.

---

## 🛣️ Future Improvements

- [ ] Improved camera status notifications.
- [ ] Configurable capture intervals through a settings interface.
- [ ] Improved retry and delivery handling.
- [ ] Capture history and delivery logs.
- [ ] Image compression for faster Telegram delivery.
- [ ] Better application startup and shutdown management.
- [ ] Packaging as a standalone Windows executable.

---

## 📜 License

This project is distributed under the MIT License.

See the [LICENSE](LICENSE) file for more information.

---

<div align="center">

### Built with ❤️ using Python

**TeleCam — Simple. Secure. Automated.**

</div>