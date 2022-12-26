#---------- Locals ----------#

from src.objects.modes.mode import Mode

# Class ModeNormal
class ModeNormal(Mode):
    # Default Constructor
    def __init__(self, handler):
        # Parent
        super().__init__(handler)

    # On démarre le mode
    def start(self) -> bool:
        return True

    # On arrête le mode
    def stop(self) -> bool:
        return True


    #---------- Events ----------#

    # Event raccourci
    def on_shortcut(self, codes: list[int], new: bool):
        # On récupére le code unique
        code: tuple = tuple(codes)

        # Si le raccourci éxiste dans la liste des commandes on charge l'action
        if new and (code in self._startup.commands): self.load_action(code)


    #---------- Functions ----------#

    # On essaye de charger une action
    def load_action(self, code: tuple) -> bool:
        from src.objects.enums.mode_type import ModeType
        # On essaye de mettre le mode action
        if not self._startup.set_mode(ModeType.ACTION, [self._startup.commands[code]]):
            print("Impossible de changer de mode")
            return False

        # Succès
        return True