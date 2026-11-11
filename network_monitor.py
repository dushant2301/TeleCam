import requests
import time

def wait_for_internet(stop_event):
    print("Waiting for internet connection...")

    while not stop_event.is_set():
        try:
            response = requests.get(
                "https://www.google.com/generate_204",
                timeout=5
            )

            if response.status_code == 204:
                print("Internet connection available!")
                return True

        except requests.RequestException:
            pass

        # Wait 5 seconds, but check if we should stop every 0.5s
        if stop_event.wait(timeout=5):
            return False
            
    return False