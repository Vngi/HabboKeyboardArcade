# Mouse Control with Arrow Keys
This script allows you to define screen positions by clicking on them and perform mouse clicks based on arrow key presses. It is compatible with both Windows and Mac.
This Python script allows you to associate arrow keys with specific positions on the screen and perform double-click actions at those positions when the corresponding key is pressed. It utilizes the `pyautogui` and `pynput` libraries to control the mouse and listen for keyboard events.

## Installation

1. Make sure you have Python installed on your system. It can be found here: https://www.python.org/downloads/
2. Clone this repository or download the script file (`Snake.py and Snake.bat`) to your local machine.
3. Place both them on your desktop, or you'll need to edit the snake.bat file! ( remove them from the folder ) place both files on the desktop.
4. This depends on the verison you download WASD or Arrowkeys, however it's the same process!

## Dependencies

The following Python packages are required:
- these are auto installed for you when you run the .bat
- `pyautogui`: Used for controlling the mouse and performing double-click actions.
- `pynput`: Used for listening to keyboard events.

You can install the dependencies by running the following command:

## Mac Instatlion: 

Open a terminal and run the command python3 --version to check if Python is installed. If Python is not installed, you can download and install it from the official Python website (https://www.python.org/downloads/).

## Prerequisites

- Python 3 installed
- Required packages: pyautogui, pynput

## Installation

1. Clone the repository to your local machine:

2. Install the required packages. Open a terminal and run the following commands:

python3 -m pip install pyautogui
python3 -m pip install pynput

run in terminal python3 script.py ( make sure to put the right directory )

```shell
Run the Snake.bat
Click on the desired areas of the screen in the following order:

Click the position for 'UP'
Click the position for 'LEFT'
Click the position for 'Down'
Click the position for 'Right'
Once the positions are set, you can use the corresponding letter keys ('up', 'left', 'down', 'right') to perform double-click actions at the associated positions on the screen.

To exit the script, simply close the terminal or press Ctrl+C.
