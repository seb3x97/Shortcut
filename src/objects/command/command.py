#---------- Locals ----------#

from src.objects.actions.action import Action

# Class Command
class Command():
    # Default Constructor
    def __init__(self, name: str, shortcut: tuple, actions: list[Action]) -> None:
        # On enregistre
        self.name: str = name
        self.shortcut: tuple = shortcut
        self.actions: list[Action] = actions