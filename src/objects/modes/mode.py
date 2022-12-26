#---------- Package ----------#

from pynput import mouse

# Class Mode
class Mode():
    # Default Constructor
    def __init__(self, startup) -> None:
        from src.startup import Startup

        # On enregistre
        self._startup: Startup = startup

    # On démarre le mode
    def start(self) -> bool: raise NotImplementedError()

    # On arrête le mode
    def stop(self) -> bool: raise NotImplementedError()

    # Events du clavier
    def on_press(self, code: int, new: bool): pass
    def on_release(self, code: int): pass
    def on_shortcut(self, codes: list[int], new: bool): pass

    # Events de la souris
    def on_move(self, x: int, y: int): pass
    def on_click(self, x: int, y: int, button: mouse.Button, pressed: bool): pass
    def on_scroll(self, x: int, y: int, dx: int, dy: int): pass