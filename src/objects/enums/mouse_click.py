#---------- Package ----------#

import enum
import pynput.mouse as py_mouse

# Class ActionMouseClick
class ActionMouseClick(enum.Enum):
    LEFT = py_mouse.Button.left
    RIGHT = py_mouse.Button.right