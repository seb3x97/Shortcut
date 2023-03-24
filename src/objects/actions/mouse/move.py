#---------- Locals ----------#

from src.objects.actions.action import Action

# Class ActionMouseMove
class ActionMouseMove(Action):
    # Constructeur Renseigné
    def __init__(self, handler, dx: int = 0, dy: int = 0) -> None:
        # Parent
        super().__init__(handler)

        # On enregistre
        self.dx: int = dx
        self.dy: int = dy

    # On démarre l'action
    def start(self) -> bool:
        # Action => Move
        self._handler.mouse_manager.move(self.dx, self.dy)

        # Succès
        return True

    # On arrête l'action
    def stop(self) -> bool:
        # Succès
        return True