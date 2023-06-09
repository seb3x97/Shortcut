#---------- Locals ----------#

from src.objects.configs.childs.command import ConfigChildCommand

# ConfigCustom
class ConfigCustom:
    name: str
    commands: list[ConfigChildCommand]

    def __init__(self, name: str, commands: list) -> None:
        # todo : check si les variables sont cohérentes dans toutes les configs et childs
        self.name = name
        self.commands = list(map((lambda command: ConfigChildCommand(**command)), commands))