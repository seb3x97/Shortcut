#---------- Package ----------#

from pynput import mouse

#---------- Locals ----------#

from src.objects.actions.action import Action

# Class ActionMouseClick
class ActionMouseClick(Action):
    # Constructeur Renseigné
    def __init__(self, startup, btn_value: tuple = (), count: int = 1) -> None:
        # Parent
        super().__init__(startup)

        # On enregistre
        self.button: mouse.Button   = mouse.Button.left
        self.count: int             = count

    # On démarre l'action
    def start(self) -> bool:
        # Action => click
        self._startup.mouse_manager.click(self.button, self.count)
        
        # Succès
        return True

    # On arrête l'action
    def stop(self) -> bool:
        # Succès
        return True