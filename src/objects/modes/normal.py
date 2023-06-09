#---------- Package ----------#

from __future__ import annotations

#---------- Locals ----------#

import src.utils.paths as Paths
import src.objects.modes.mode as mode

# Class ModeNormal
class ModeNormal(mode.Mode):
    # Default Constructor
    def __init__(self, handler):
        # Parent
        super().__init__(handler)

        # Default
        self.path_config = [Paths.FILE_CONFIG_MODE_NORMAL, Paths.FILE_CONFIG_CUSTOM]  # todo : 

    # On sauvegarde les arguments
    def set_args(self) -> bool:
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
        if new and (code in self._commands): self.load_action(code)