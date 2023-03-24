#---------- Locals ----------#

from src.objects.actions.action import Action

# Class ActionKeyboardPress
class ActionKeyboardPress(Action):
    # Constructeur Renseigné
    def __init__(self, handler) -> None:
        # Parent
        super().__init__(handler)

    # On démarre l'action
    def start(self) -> bool:
        # Succès
        return True

    # On arrête l'action
    def stop(self) -> bool:
        # Succès
        return True