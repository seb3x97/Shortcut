#---------- Package ----------#

from __future__ import annotations

#---------- Locals ----------#

import src.objects.actions.action as action

# Class ActionOtherSleep
class ActionOtherSleep(action.Action):
    # Constructeur Renseigné
    def __init__(self, handler) -> None:
        # Parent
        super().__init__(handler)

        # Default
        self.secs: int = 0

    # On démarre l'action
    def start(self) -> bool:
        # On mets en pause le thread pendant "x" (secs) secondes
        # Si un signal arrive pendant la pause, on ne fini pas la pause et on continue le code
        print("we")
        self._handler.mode.thread.wait(self.secs)
        print("end")

        # Succès
        return True

    # On arrête l'action
    def stop(self) -> bool:
        # Succès
        return True