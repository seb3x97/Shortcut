#---------- Package ----------#

from __future__ import annotations

#---------- Locals ----------#

import src.objects.actions.action as Action

# Class Command
class Command():
    # Default Constructor
    def __init__(self, name: str, shortcut: tuple, actions: list[Action.Action]) -> None:
        # On enregistre
        self.name: str = name
        self.shortcut: tuple = shortcut
        self.actions: list[Action.Action] = actions