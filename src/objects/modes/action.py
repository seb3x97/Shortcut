#---------- Locals ----------#

from src.objects.modes.mode import Mode
from src.objects.command.command import Command

# Class ModeAction
class ModeAction(Mode):
    # Default Constructor
    def __init__(self, handler):
        # Parent
        super().__init__(handler)

        self.__command: Command = None

    # On initialise les variables
    def init(self, command: Command) -> bool:
        # On enregistre
        self.__command = command

        # Succès
        return True

    # On éxécute les actions d'une commande
    def exec(self) -> bool:
        # Check si il n'y a pas de commande
        if self.__command is None: return False

        # On boucle les actions pour les démarrer
        for action in self.__command.actions:
            action.start()

        # On recharge le mode normal
        from src.objects.enums.mode_type import ModeType
        if not self._handler.start_mode(ModeType.NORMAL): return False

        # Succès
        return True


    #---------- Events ----------#

    # Event raccourci
    def on_shortcut(self, codes: list[int], new: bool):
        # On récupére le code unique
        code: tuple = tuple(codes)

        print("action mode " + str(code))

        default_actions = {
            (27,): self.stop
        }

        if code in default_actions: default_actions.get(code)()