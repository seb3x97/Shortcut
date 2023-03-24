#---------- Locals ----------#

from src.objects.modes.mode import Mode

# Class ModeCreative
class ModeCreative(Mode):
    # Default Constructor
    def __init__(self, handler):
        # Parent
        super().__init__(handler)

    # On initialise les variables
    def init(self) -> bool:
        # Succès
        return True

    # On démarre le mode
    def start(self) -> bool:
        return True

    # On arrête le mode
    def stop(self) -> bool:
        return True