#---------- Locals ----------#

from src.objects.handler.handler import Handler

# Class Startup
class Startup():
    # Default Constructor
    def __init__(self) -> None:
        # -- Default -- #
        self.handler: Handler = Handler()               # Gestionnaire du programme

    # On initialise la classe
    def init(self) -> bool:
        # On essaye d'initialiser le handler
        if not self.handler.init(): return False

        # Succès
        return True

    # On démarre
    def start(self) -> bool:
        # On essaye de démarrer le handler
        if not self.handler.start(): return False

        # Succès
        return True

    # On arrête
    def stop(self) -> bool:
        # On essaye de stopper le handler
        if not self.handler.stop(): return False

        # Succès
        return True