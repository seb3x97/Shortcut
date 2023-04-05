#---------- Package ----------#

from __future__ import annotations

#---------- Locals ----------#

import src.utils.paths as Paths
import src.objects.modes.mode as Mode
import src.objects.command.command as Command

# Class ModeAction
class ModeAction(Mode.Mode):
    # Default Constructor
    def __init__(self, handler):
        # Parent
        super().__init__(handler)

        # Default
        self.path_config = Paths.FILE_CONFIG_MODE_ACTION
        self.__command: Command.Command = None

    # On sauvegarde les arguments
    def set_args(self, command: Command.Command) -> bool:
        # On enregistre
        self.__command = command

        # Succès
        return True

    # On éxécute les sous-tâches du mode
    def exec(self) -> bool:
        # Check si il n'y a pas de commande
        if self.__command is None: return False

        # On boucle les actions pour les démarrer
        for action in self.__command.actions:
            action.start()

        # On recharge le mode normal
        if not self._handler.start_mode(): return False

        # Succès
        return True


    #---------- Events ----------#

    # Event raccourci
    def on_shortcut(self, codes: list[int], new: bool):
        # On récupére le code unique
        code: tuple = tuple(codes)

        default_actions = {
            (27,): self._handler.start_mode
        }

        if code in default_actions: default_actions.get(code)()