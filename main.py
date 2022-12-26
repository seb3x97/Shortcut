#---------- Locals ----------#

# Class Shortcut
class Shortcut:
    # Default Constructor
    def __init__(self) -> None:
        from src.startup import Startup
        # -- Default -- #
        self.startup: Startup = Startup()

    # On initialise le programme
    def init(self) -> bool:
        print("Init programm")
        return self.startup.init()

    # On démarre le programme
    def start(self) -> bool:
        print("Starting programm")
        return self.startup.start()

    # On arrête le programme
    def stop(self) -> bool:
        print("Stopping programm")
        return self.startup.stop()


# On essaye de démarrer le programme
if __name__ == "__main__":
    shortcut = Shortcut()
    if not shortcut.init() or not shortcut.start(): shortcut.stop()

    # todo : enlever
    import time
    while True:
        time.sleep(1)