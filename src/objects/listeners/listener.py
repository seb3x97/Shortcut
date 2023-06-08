#---------- Package ----------#

from __future__ import annotations

# Class Listener
class Listener():
    # Default Constructor
    def __init__(self) -> None:
        pass

    # On démarre le listener
    def start(self) -> None: raise NotImplementedError()

    # On arrête le listener
    def stop(self) -> None: raise NotImplementedError()

    # On join le listener
    def join(self) -> None: raise NotImplementedError()