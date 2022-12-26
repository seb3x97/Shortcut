import time

"""
from src.listeners.keyboard import ListenerKeyboard
listener = ListenerKeyboard()
def press(x, t):
    #print((x, y, button, pressed))
    pass
listener.on_press = press
listener.start()
"""

from src.listeners.mouse import ListenerMouse
listener = ListenerMouse()
def press(x, y, btn, press):
    print((x, y, btn, press))
    #print((x, y, button, pressed))
    pass
listener.on_click = press
listener.start()


while True:
    time.sleep(1)