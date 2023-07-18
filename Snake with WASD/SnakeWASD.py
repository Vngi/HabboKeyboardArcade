import subprocess
import sys

# Check if required packages are installed, and install them if necessary
def install_packages():
    required_packages = ['pyautogui', 'pynput']

    for package in required_packages:
        try:
            __import__(package)
        except ImportError:
            subprocess.check_call([sys.executable, "-m", "pip", "install", package])

# Install required packages
install_packages()

import pyautogui
from pynput import mouse, keyboard

print("Click on the desired areas of the screen in the following order:")
print("1. Click the position for 'W'")
print("2. Click the position for 'A'")
print("3. Click the position for 'S'")
print("4. Click the position for 'D'")

# Variables to store the four positions and letter key actions
positions = [None] * 4
letter_actions = [None] * 4
current_position = 0

def on_click(x, y, button, pressed):
    global current_position

    if pressed:
        if current_position < 4:
            positions[current_position] = (x, y)
            print(f'Position {current_position+1} set: {positions[current_position]}')
            current_position += 1

def on_letter_key_press(key):
    if hasattr(key, 'char'):
        if key.char == 'w':
            letter_actions[0] = pyautogui.doubleClick(*positions[0])
        elif key.char == 'a':
            letter_actions[1] = pyautogui.doubleClick(*positions[1])
        elif key.char == 's':
            letter_actions[2] = pyautogui.doubleClick(*positions[2])
        elif key.char == 'd':
            letter_actions[3] = pyautogui.doubleClick(*positions[3])

# Register mouse click event handler
listener = mouse.Listener(on_click=on_click)
listener.start()

# Register letter key press event handler
with keyboard.Listener(on_press=on_letter_key_press) as key_listener:
    key_listener.join()

listener.join()
