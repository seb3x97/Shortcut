#---------- Package ----------#

import enum
import pynput.mouse as py_mouse

# Enum ActionMouseClick
class ActionMouseClick(enum.Enum):
    LEFT = py_mouse.Button.left
    RIGHT = py_mouse.Button.right