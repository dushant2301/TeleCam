import pystray
from PIL import Image, ImageDraw
from threading import Event

stopped = Event()
icon = None

def create_icon(color="green"):
    image = Image.new("RGB", (64, 64), "white")
    draw = ImageDraw.Draw(image)
    draw.ellipse((12, 12, 52, 52), fill=color)
    draw.ellipse((24, 24, 40, 40), fill="white")
    return image

def exit_application(icon_ref, item):
    stopped.set()
    icon_ref.stop()

def set_camera_state(is_active):
    """Changes the tray icon color based on camera status"""
    if icon:
        color = "red" if is_active else "green"
        icon.icon = create_icon(color)
        icon.title = "LaptopWebcam - ACTIVE" if is_active else "LaptopWebcam - Idle"

def run_tray():
    global icon
    
    menu = pystray.Menu(
        pystray.MenuItem("Exit", exit_application)
    )

    icon = pystray.Icon(
        "LaptopWebcam",
        create_icon("green"),
        "LaptopWebcam - Idle",
        menu
    )

    icon.run()