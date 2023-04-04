#---------- Package ----------#

from __future__ import annotations
import pynput.mouse as py_mouse

#---------- Locals ----------#

import src.objects.actions.action as action

# Class ActionMouseClick
class ActionMouseClick(action.Action):
    # Constructeur Renseigné
    def __init__(self, handler, btn_value: tuple = (), count: int = 1) -> None:
        # Parent
        super().__init__(handler)

        # On enregistre
        self.button: py_mouse.Button    = py_mouse.Button.left
        self.count: int                 = count

    # On démarre l'action
    def start(self) -> bool:
        # Action => click
        self._handler.mouse_manager.click(self.button, self.count)
        
        # Succès
        return True

    # On arrête l'action
    def stop(self) -> bool:
        # Succès
        return True