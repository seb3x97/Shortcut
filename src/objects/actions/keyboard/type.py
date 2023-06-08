#---------- Package ----------#

from __future__ import annotations

#---------- Locals ----------#

import src.objects.actions.action as action

# Class ActionKeyboardType
class ActionKeyboardType(action.Action):
    # Constructeur Renseigné
    def __init__(self, handler, text: str = None) -> None:
        # Parent
        super().__init__(handler)

        # On enregistre
        self.text = text

    # On démarre l'action
    def start(self) -> bool:
        # Check des paramètres
        if(self.text == None): return False

        # Action => Type
        self._handler.keyboard_manager.type(self.text)

        # Succès
        return True

    # On arrête l'action
    def stop(self) -> bool:
        # Succès
        return True