#---------- Package ----------#

from __future__ import annotations

import sys
sys.dont_write_bytecode = True

#---------- Locals ----------#

# Imports
import src.objects.handler.handler as handler

# Class Shortcut
class Shortcut:
    # Default Constructor
    def __init__(self) -> None:
        # -- Default -- #
        self.handler: handler.Handler = handler.Handler()

    # On initialise le programme
    def init(self) -> bool:
        print("Init programm")
        return self.handler.init()

    # On démarre le programme
    def start(self) -> bool:
        print("Starting programm")
        return self.handler.start()

    # On arrête le programme
    def stop(self) -> bool:
        print("Stopping programm")
        return self.handler.stop()


# On essaye de démarrer le programme
if __name__ == "__main__":
    shortcut = Shortcut()
    if not shortcut.init() or not shortcut.start(): shortcut.stop()

    # todo : enlever
    import time
    while True:
        time.sleep(1)