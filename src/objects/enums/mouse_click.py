#---------- Package ----------#

from enum import Enum
from pynput import mouse

# Class ActionMouseClick
class ActionMouseClick(Enum):
    LEFT = mouse.Button.left
    RIGHT = mouse.Button.right