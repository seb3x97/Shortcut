#---------- Locals ----------#

from src.objects.actions.action import Action

# Class ActionKeyboardRelease
class ActionKeyboardRelease(Action):
    # Constructeur Renseigné
    def __init__(self, startup) -> None:
        # Parent
        super().__init__(startup)

    # On démarre l'action
    def start(self) -> bool:
        # Succès
        return True

    # On arrête l'action
    def stop(self) -> bool:
        # Succès
        return True