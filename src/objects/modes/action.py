#---------- Package ----------#

import multiprocessing

#---------- Locals ----------#

from src.objects.modes.mode import Mode
#
from src.objects.command.command import Command
from src.objects.actions.action import Action

# Class ModeAction
class ModeAction(Mode):
    # Default Constructor
    def __init__(self, handler):
        # Parent
        super().__init__(handler)

        # Private
        self.__process: multiprocessing.Process = None

    # On démarre le processus
    def start(self, command: Command) -> bool:
        # Check si il n'y a pas de processus en court
        if not self.__process is None and self.__process.is_alive(): return False

        # On démarre le processus
        #self.exec_actions(command.actions)
        self.__process: multiprocessing.Process = multiprocessing.Process(target=self.exec_actions, args=(command.actions,))
        self.__process.start()

        # Succès
        return True

    # On arrête le mode
    def stop(self) -> bool:
        # Check si il y a un processus en court
        if self.__process is None or not self.__process.is_alive(): return False

        # On termine le processus
        #self.__process.terminate()

        # Succès
        return True

    # On éxécute les actions
    def exec_actions(self, actions: list[Action]):
        # On boucle les actions pour les démarrer
        for action in actions:
            action.start()

        # On recharge le mode normal
        from src.objects.enums.mode_type import ModeType
        self._startup.set_mode(ModeType.NORMAL)