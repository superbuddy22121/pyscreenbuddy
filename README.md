# Multi-Monitor Screenshot Tool

This tool allows users to capture screenshots across multiple monitors with ease. It provides a simple, intuitive interface for selecting the area to be captured and automatically saves the screenshot while also copying it to the clipboard.

## Features

- Capture screenshots across multiple monitors
- Interactive selection of capture area
- Automatic saving of screenshots with timestamps
- Clipboard integration for quick pasting
- Hotkey support for easy activation

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/yourusername/multi-monitor-screenshot-tool.git
   ```

2. Navigate to the project directory:
   ```
   cd multi-monitor-screenshot-tool
   ```

3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

Run the script:

```
python screenshot_tool.py
```

- Press the 'Print Screen' key to start the capture mode.
- Click and drag to select the area you want to capture.
- Release the mouse button to capture the screenshot.
- The screenshot will be saved in a 'screenshots' folder and copied to your clipboard.
- Press 'Esc' to cancel the capture.
- Use Ctrl+C in the terminal to exit the program.

## Dependencies

This project uses the following third-party libraries:

- keyboard
- Pillow (PIL)
- pywin32
- screeninfo
- mss

Please see the NOTICE file for more information about these libraries and their licenses.

## License

This project is licensed under the Apache License 2.0. See the LICENSE file for details.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Acknowledgements

Special thanks to the developers of the third-party libraries used in this project. Their work has been instrumental in creating this tool.