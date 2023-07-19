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
print("1. Click the position for 'Middle Tile' - Up Key")
print("2. Click the position for 'Left Arrow' - Left Key")
print("3. Click the position for 'Down Arrow' - Down Key")
print("4. Click the position for 'Right Arrow' - Right Key")
print("5. Click the position for 'Store Block' - Spacebar")
print("6. Click the position for 'Drop Block' - Left Shift")
print("TIP: You can adjust the keys yourself check the code!")

# Variables to store the six positions and associated actions
positions = [None] * 6
actions = [None] * 6
current_position = 0

def on_click(x, y, button, pressed):
    global current_position

    if pressed:
        if current_position < 6:
            positions[current_position] = (x, y)
            print(f'Position {current_position+1} set: {positions[current_position]}')
            current_position += 1

def on_arrow_key_press(key):
    if key == keyboard.Key.up: #You can adjust the from key.up to key.down ( example ) 
        pyautogui.moveTo(*positions[0])
        pyautogui.click()
    elif key == keyboard.Key.left: #You can adjust the from key.up to key.down ( example ) 
        pyautogui.moveTo(*positions[1])
        pyautogui.click()
    elif key == keyboard.Key.down: #You can adjust the from key.up to key.down ( example ) 
        pyautogui.moveTo(*positions[2])
        pyautogui.click()
    elif key == keyboard.Key.right: #You can adjust the from key.up to key.down ( example ) 
        pyautogui.moveTo(*positions[3])
        pyautogui.click()

    if key == keyboard.Key.shift_l: #You can adjust the from key.up to key.down ( example ) 
        pyautogui.moveTo(*positions[5])
        pyautogui.click()
    elif key == keyboard.Key.space: #You can adjust the from key.up to key.down ( example ) 
        pyautogui.moveTo(*positions[4])
        pyautogui.click()

# Register mouse click event handler
listener = mouse.Listener(on_click=on_click)
listener.start()

# Register arrow key press event handler
with keyboard.Listener(on_press=on_arrow_key_press) as key_listener:
    key_listener.join()

listener.join()
