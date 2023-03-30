#---------- Package ----------#

from __future__ import annotations

#---------- Locals ----------#

import src.utils.paths as Paths
import src.objects.modes.mode as Mode

# Class ModeNormal
class ModeNormal(Mode.Mode):
    # Default Constructor
    def __init__(self, handler):
        # Parent
        super().__init__(handler)

        # Default
        self.path_config = Paths.FILE_CONFIG_MODE_NORMAL

    # On initialise les variables
    def init(self) -> bool:
        # Succès
        return True
    
    # On éxécute les sous-tâches du mode
    def exec(self) -> bool:
        # Succès
        return True


    #---------- Events ----------#

    # Event raccourci
    def on_shortcut(self, codes: list[int], new: bool):
        # On récupére le code unique
        code: tuple = tuple(codes)

        # Si le raccourci éxiste dans la liste des commandes on charge l'action
        if new and (code in self.commands): self.load_action(code)


    #---------- Functions ----------#

    # On essaye de charger une action
    def load_action(self, code: tuple) -> bool:
        from src.objects.enums.mode_type import ModeType
        # On essaye de mettre le mode action
        if not self._handler.start_mode(ModeType.ACTION, [self.commands[code]]):
            print("Impossible de changer de mode")
            return False

        # Succès
        return True