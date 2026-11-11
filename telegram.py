
import requests
from dotenv import load_dotenv
import os

load_dotenv("config/.env")

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")


def send_photo(image_path):
    if not TOKEN or not CHAT_ID:
        print("Telegram credentials missing!")
        return False

    url = f"https://api.telegram.org/bot{TOKEN}/sendPhoto"

    try:
        with open(image_path, "rb") as image:
            response = requests.post(
                url,
                data={
                    "chat_id": CHAT_ID,
                    "caption": "Laptop Webcam Monitor - Approved Capture"
                },
                files={"photo": image},
                timeout=30
            )

        response.raise_for_status()

        result = response.json()

        if result.get("ok"):
            print("Image successfully sent to Telegram!")
            return True

        print("Telegram error:", result)
        return False

    except Exception as error:
        print("Error:", error)
        return False
