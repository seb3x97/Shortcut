#---------- Locals ----------#

from src.objects.configs.childs.command import ConfigChildCommand

# Class ConfigChildMode
class ConfigChildMode:
    name: str
    commands: list[ConfigChildCommand]

    def __init__(self, name: str, commands: list) -> None:
        self.name = name
        self.commands = list(map((lambda command: ConfigChildCommand(**command)), commands))