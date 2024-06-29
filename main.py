import os
import time
import pyautogui
import win32clipboard
from io import BytesIO
from PIL import Image

def capture_screenshot():
    # Capture the screenshot
    screenshot = pyautogui.screenshot()
    return screenshot

def save_screenshot(screenshot, directory):
    # Create the directory if it doesn't exist
    if not os.path.exists(directory):
        os.makedirs(directory)

    # Generate a unique filename based on the current timestamp
    timestamp = time.strftime("%Y%m%d-%H%M%S")
    filename = f"screenshot_{timestamp}.png"
    filepath = os.path.join(directory, filename)

    # Save the screenshot to the specified directory
    screenshot.save(filepath)
    print(f"Screenshot saved: {filepath}")

def copy_to_clipboard(screenshot):
    # Convert the screenshot to a format suitable for the clipboard
    output = BytesIO()
    screenshot.convert("RGB").save(output, "BMP")
    data = output.getvalue()[14:]  # Remove the BMP header
    output.close()

    # Copy the screenshot to the clipboard
    win32clipboard.OpenClipboard()
    win32clipboard.EmptyClipboard()
    win32clipboard.SetClipboardData(win32clipboard.CF_DIB, data)
    win32clipboard.CloseClipboard()
    print("Screenshot copied to clipboard")

def main():
    # Specify the directory to save screenshots
    save_directory = r"C:\Screenshots"

    # Capture the screenshot
    screenshot = capture_screenshot()

    # Save the screenshot to the directory
    save_screenshot(screenshot, save_directory)

    # Copy the screenshot to the clipboard
    copy_to_clipboard(screenshot)

if __name__ == "__main__":
    main()