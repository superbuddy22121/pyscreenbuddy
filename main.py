import os
import time
import tkinter as tk
from PIL import Image, ImageGrab, ImageTk
import win32clipboard
from io import BytesIO
import keyboard
import sys

# Global variables
screenshot_dir = "screenshots"
root = None
canvas = None
rect = None
start_x = start_y = 0
curX = curY = 0
running = True

# Ensure the screenshot directory exists
if not os.path.exists(screenshot_dir):
    os.makedirs(screenshot_dir)

def start_capture(e):
    global root, canvas, rect, start_x, start_y
    start_x = e.x
    start_y = e.y
    rect = canvas.create_rectangle(e.x, e.y, e.x, e.y, outline='red', width=2)

def drag(e):
    global canvas, rect, curX, curY
    curX, curY = e.x, e.y
    canvas.coords(rect, start_x, start_y, curX, curY)

def capture_screenshot(e):
    global root, start_x, start_y, curX, curY
    x1 = min(start_x, curX)
    y1 = min(start_y, curY)
    x2 = max(start_x, curX)
    y2 = max(start_y, curY)
    
    root.withdraw()  # Hide the window temporarily
    time.sleep(0.1)  # Small delay to ensure the window is hidden
    
    screenshot = ImageGrab.grab(bbox=(x1, y1, x2, y2))
    
    # Save to file
    timestamp = time.strftime("%Y%m%d-%H%M%S")
    filename = os.path.join(screenshot_dir, f"screenshot_{timestamp}.png")
    screenshot.save(filename)
    print(f"Screenshot saved: {filename}")

    # Copy to clipboard
    output = BytesIO()
    screenshot.convert("RGB").save(output, "BMP")
    data = output.getvalue()[14:]
    output.close()

    win32clipboard.OpenClipboard()
    win32clipboard.EmptyClipboard()
    win32clipboard.SetClipboardData(win32clipboard.CF_DIB, data)
    win32clipboard.CloseClipboard()

    print("Screenshot copied to clipboard")
    root.quit()

def start_screenshot_mode():
    global root, canvas
    
    root = tk.Tk()
    root.attributes('-fullscreen', True)
    root.attributes('-alpha', 0.3)
    root.configure(cursor="cross")

    canvas = tk.Canvas(root, cursor="cross")
    canvas.pack(fill=tk.BOTH, expand=True)

    root.bind('<ButtonPress-1>', start_capture)
    root.bind('<B1-Motion>', drag)
    root.bind('<ButtonRelease-1>', capture_screenshot)

    root.mainloop()

print("Press PrintScreen to start capturing...")

try:
    while True:
        keyboard.wait('print_screen')
        start_screenshot_mode()
        print("Press PrintScreen to capture again.")
except KeyboardInterrupt:
    print("\nProgram terminated by user.")
finally:
    keyboard.unhook_all()