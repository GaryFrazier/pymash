from pyinput import pyinput, pyinputkeycodes
import sys

if len(sys.argv) != 5:
    print("Usage: python pymash.py WindowName KeyCode NumPresses Interval(in seconds)")
    print("Keycodes (must convert from hex to decimal) can be found here http://www.kbdedit.com/manual/low_level_vk_list.html")
    exit(1)

window_name  =  sys.argv[1]
keycode  =  int(sys.argv[2])
numpresses = int(sys.argv[3])  # Number of times to press the button
interval = float(sys.argv[4])  # Interval between button presses in seconds
hwnd  =  pyinput.get_handle(window_name) # Gets the handle
print(hwnd)

for _ in range(numpresses):
    print("hit")
    pyinput.press_key(hwnd, keycode, interval, False) # Sends W key for 2 seconds, but doesnt force foreground
