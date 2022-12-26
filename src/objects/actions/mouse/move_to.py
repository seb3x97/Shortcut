#---------- Locals ----------#

from src.objects.actions.action import Action

# Class ActionMouseMoveTo
class ActionMouseMoveTo(Action):
    # Constructeur Renseigné
    def __init__(self, startup, x: int = 0, y: int = 0) -> None:
        # Parent
        super().__init__(startup)

        # On enregistre
        self.x: int = x
        self.y: int = y

    # On démarre l'action
    def start(self) -> bool:
        # Action => MoveTo
        self._startup.mouse_manager.move_to(self.x, self.y)

        # Succès
        return True

    # On arrête l'action
    def stop(self) -> bool:
        # Succès
        return True