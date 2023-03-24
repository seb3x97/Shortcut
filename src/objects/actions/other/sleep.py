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

        # If no kill signal is set, sleep for the interval,
        # If kill signal comes in while sleeping, immediately
        # wake up and handle
        time.sleep(self.secs)
        print("end waiting")

        # Succès
        return True

    # On arrête l'action
    def stop(self) -> bool:
        # Succès
        return True