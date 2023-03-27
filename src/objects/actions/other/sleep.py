#---------- Package ----------#

import time

#---------- Locals ----------#

from src.objects.actions.action import Action

# Class ActionOtherSleep
class ActionOtherSleep(Action):
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
        self._handler.mode.thread.wait(self.secs)

        # Succès
        return True

    # On arrête l'action
    def stop(self) -> bool:
        # Succès
        return True