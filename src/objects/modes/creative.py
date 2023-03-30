#---------- Package ----------#

from __future__ import annotations
import pynput.mouse as py_mouse

#---------- Locals ----------#

import src.utils.paths as Paths
import src.objects.modes.mode as Mode

# Class ModeCreative
class ModeCreative(Mode.Mode):
    # Default Constructor
    def __init__(self, handler):
        # Parent
        super().__init__(handler)

        # Default
        self.path_config = Paths.FILE_CONFIG_MODE_CREATIVE

    # On initialise les variables
    def init(self) -> bool:
        # Succès
        return True
    
    # On éxécute les sous-tâches du mode
    def exec(self) -> bool:
        # Succès
        return True
    
    # Events du clavier
    def on_press(self, code: int, new: bool): pass
    def on_release(self, code: int): pass
    def on_shortcut(self, codes: list[int], new: bool): pass

    # Events de la souris
    def on_move(self, x: int, y: int): pass
    def on_click(self, x: int, y: int, button: py_mouse.Button, pressed: bool): pass
    def on_scroll(self, x: int, y: int, dx: int, dy: int): pass