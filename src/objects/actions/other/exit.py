#---------- Package ----------#

from __future__ import annotations

#---------- Locals ----------#

import src.objects.actions.action as action

# Class ActionOtherExit
class ActionOtherExit(action.Action):
    # Constructeur Renseigné
    def __init__(self, handler) -> None:
        # Parent
        super().__init__(handler)

    # On démarre l'action
    def start(self) -> bool:
        # Check si le mode est défini
        if self._handler.mode is None: return False

        # On stop le programme
        self._handler.stop()

        # Succès
        return True

    # On arrête l'action
    def stop(self) -> bool:
        # Succès
        return True