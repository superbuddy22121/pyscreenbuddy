import tkinter as tk
import keyboard
from PIL import ImageGrab, ImageTk, Image
import win32clipboard
import io
import os
from datetime import datetime

def send_to_clipboard(clip_type, data):
    win32clipboard.OpenClipboard()
    win32clipboard.EmptyClipboard()
    win32clipboard.SetClipboardData(clip_type, data)
    win32clipboard.CloseClipboard()

def start_screenshot_mode():
    global root
    root = tk.Tk()
    root.attributes('-alpha', 0.3)
    root.attributes('-fullscreen', True)
    root.attributes('-topmost', True)
    root.configure(cursor="cross")

    # Bring the window to the foreground
    root.lift()
    root.focus_force()

    canvas = tk.Canvas(root, cursor="cross")
    canvas.pack(fill=tk.BOTH, expand=True)

    start_x = start_y = 0
    rect = None

    def start_capture(event):
        nonlocal start_x, start_y, rect
        start_x = event.x
        start_y = event.y
        if rect:
            canvas.delete(rect)
        rect = canvas.create_rectangle(start_x, start_y, start_x, start_y, outline='red', width=2)

    def drag(event):
        nonlocal rect
        canvas.coords(rect, start_x, start_y, event.x, event.y)

    def capture_screenshot(event):
        x1 = min(start_x, event.x)
        y1 = min(start_y, event.y)
        x2 = max(start_x, event.x)
        y2 = max(start_y, event.y)
        root.withdraw()
        
        # Ensure the rectangle has a minimum size
        if x2 - x1 < 5 or y2 - y1 < 5:
            print("Selected area too small. Please try again.")
            root.quit()
            return

        # Capture the screenshot
        screenshot = ImageGrab.grab(bbox=(x1, y1, x2, y2))
        
        # Create screenshots directory if it doesn't exist
        screenshot_dir = os.path.join(os.getcwd(), "screenshots")
        os.makedirs(screenshot_dir, exist_ok=True)
        
        # Save the screenshot with a timestamp
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"screenshot_{timestamp}.png"
        filepath = os.path.join(screenshot_dir, filename)
        screenshot.save(filepath)
        print(f"Screenshot saved as {filepath}")

        # Copy to clipboard
        output = io.BytesIO()
        screenshot.convert('RGB').save(output, 'BMP')
        data = output.getvalue()[14:]
        output.close()
        send_to_clipboard(win32clipboard.CF_DIB, data)
        print("Screenshot copied to clipboard")

        root.quit()

    root.bind('<ButtonPress-1>', start_capture)
    root.bind('<B1-Motion>', drag)
    root.bind('<ButtonRelease-1>', capture_screenshot)
    root.bind('<Escape>', lambda e: root.quit())  # Add Escape key to exit

    root.mainloop()

def on_print_screen():
    start_screenshot_mode()
    print("Press PrintScreen to capture again, or Ctrl+C to exit.")

print("Press PrintScreen to start capturing...")

try:
    keyboard.add_hotkey('print_screen', on_print_screen)
    keyboard.wait()
except KeyboardInterrupt:
    print("\nProgram terminated by user.")
finally:
    keyboard.unhook_all()