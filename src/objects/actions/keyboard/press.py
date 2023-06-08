#---------- Package ----------#

from __future__ import annotations

#---------- Locals ----------#

import src.objects.actions.action as action

# Class ActionKeyboardPress
class ActionKeyboardPress(action.Action):
    # Constructeur Renseigné
    def __init__(self, handler, code: int = None) -> None:
        # Parent
        super().__init__(handler)

        # On enregistre
        self.code = code

    # On démarre l'action
    def start(self) -> bool:
        # Check des paramètres
        if(self.code == None): return False

        # Action => Press
        self._handler.keyboard_manager.press(self.code)

        # Succès
        return True

    # On arrête l'action
    def stop(self) -> bool:
        # Succès
        return True