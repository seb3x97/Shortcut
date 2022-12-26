#---------- Locals ----------#

from src.objects.actions.action import Action

# Class ActionMouseMove
class ActionMouseMove(Action):
    # Constructeur Renseigné
    def __init__(self, startup, dx: int = 0, dy: int = 0) -> None:
        # Parent
        super().__init__(startup)

        # On enregistre
        self.dx: int = dx
        self.dy: int = dy

    # On démarre l'action
    def start(self) -> bool:
        # Action => Move
        self._startup.mouse_manager.move(self.dx, self.dy)

        # Succès
        return True

    # On arrête l'action
    def stop(self) -> bool:
        # Succès
        return True