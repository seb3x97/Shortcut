#---------- Package ----------#

from __future__ import annotations

# Class Manager
class Manager():
    # Default Constructor
    def __init__(self) -> None:
        pass

    # On démarre le manager
    def start(self) -> None: raise NotImplementedError()

    # On arrête le manager
    def stop(self) -> None: raise NotImplementedError()

    # On join le manager
    def stop(self) -> None: raise NotImplementedError()