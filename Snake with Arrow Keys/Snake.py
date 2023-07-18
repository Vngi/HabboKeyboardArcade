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
print("1. Click the position for 'up'")
print("2. Click the position for 'left'")
print("3. Click the position for 'down'")
print("4. Click the position for 'right'")

# Variables to store the four positions and arrow key actions
positions = [None] * 4
arrow_actions = [None] * 4
current_position = 0

def on_click(x, y, button, pressed):
    global current_position

    if pressed:
        if current_position < 4:
            positions[current_position] = (x, y)
            print(f'Position {current_position+1} set: {positions[current_position]}')
            current_position += 1

def on_arrow_key_press(key):
    if key == keyboard.Key.up:
        arrow_actions[0] = pyautogui.click(*positions[0])
    elif key == keyboard.Key.left:
        arrow_actions[1] = pyautogui.click(*positions[1])
    elif key == keyboard.Key.down:
        arrow_actions[2] = pyautogui.click(*positions[2])
    elif key == keyboard.Key.right:
        arrow_actions[3] = pyautogui.click(*positions[3])

# Register mouse click event handler
listener = mouse.Listener(on_click=on_click)
listener.start()

# Register arrow key press event handler
with keyboard.Listener(on_press=on_arrow_key_press) as key_listener:
    key_listener.join()

listener.join()
