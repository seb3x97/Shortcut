#---------- Package ----------#

from __future__ import annotations

#---------- Locals ----------#

import src.objects.actions.action as action

# Class ActionMouseMoveTo
class ActionMouseMoveTo(action.Action):
    # Constructeur Renseigné
    def __init__(self, handler, x: int = None, y: int = None) -> None:
        # Parent
        super().__init__(handler)

        # On enregistre
        self.x: int = x
        self.y: int = y

    # On démarre l'action
    def start(self) -> bool:
        # Check des paramètres
        if(self.x == None or self.y == None): return False

        print(str(self.x) + " " + str(self.y))

        # Action => MoveTo
        self._handler.mouse_manager.move_to(self.x, self.y)

        # Succès
        return True

    # On arrête l'action
    def stop(self) -> bool:
        # Succès
        return True