#---------- Package ----------#

from __future__ import annotations
import pynput.mouse as py_mouse

#---------- Locals ----------#

import src.objects.actions.action as action

# Class ActionMouseClick
class ActionMouseClick(action.Action):
    # Constructeur Renseigné
    def __init__(self, handler, button: int = None, count: int = None) -> None:
        # Parent
        super().__init__(handler)

        # On enregistre
        self.button: button
        self.count: count

    # On démarre l'action
    def start(self) -> bool:
        # Check des paramètres
        if(self.button == None or self.count == None): return False

        # Action => click
        self._handler.mouse_manager.click(self.button, self.count)
        
        # Succès
        return True

    # On arrête l'action
    def stop(self) -> bool:
        # Succès
        return True