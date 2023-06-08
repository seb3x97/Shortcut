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
        self.command: Command.Command = None

    # On sauvegarde les arguments
    def set_args(self, command: Command.Command) -> bool:
        # On enregistre
        self.command = command

        # Succès
        return True

    # On éxécute les sous-tâches du mode
    def exec(self) -> bool:
        # Check si il n'y a pas de commande
        if self.command is None: return False

        print(f"Start action {self.__class__.__name__}")

        # On boucle les actions pour les démarrer
        for action in self.command.actions:
            action.start()

        print(f"End action {self.__class__.__name__}")

        # Succès
        return True


    #---------- Events ----------#

    # Event raccourci
    def on_shortcut(self, codes: list[int], new: bool):
        # On récupére le code unique
        code: tuple = tuple(codes)

        # Si le raccourci éxiste dans la liste des commandes on charge l'action
        if new and (code in self._commands): self.load_action(code)