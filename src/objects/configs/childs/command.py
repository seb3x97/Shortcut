#---------- Locals ----------#

from src.objects.configs.childs.action import ConfigChildAction

class ConfigChildCommand:
    name: str
    shortcut: tuple
    actions: list[ConfigChildAction]

    def __init__(self, name: str, shortcut: list, actions: list) -> None:
        self.name = name
        self.shortcut = tuple(shortcut)
        self.actions = list(map((lambda action: ConfigChildAction(**action)), actions))