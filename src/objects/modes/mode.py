#---------- Package ----------#

from pynput import mouse

#---------- Locals ----------#

from src.utils.abortable_thread import AbortableThread

# Class Mode
class Mode():
    # Default Constructor
    def __init__(self, handler) -> None:
        # Default
        self.thread: AbortableThread = None

        # On enregistre
        self._handler = handler

    # On démarre le mode
    def start(self) -> bool:
        # Check si il n'y a pas de processus en court
        if not self.thread is None and self.thread.is_alive(): return False

        # On démarre le thread
        self.thread = AbortableThread(target=self.exec, args=())
        self.thread.start()

        # Succès
        return True

    # On arrête le mode
    def stop(self) -> bool:
        # Check si il y a un processus en court
        if self.thread is None or not self.thread.is_alive(): return False

        # On termine le thread
        self.thread.stop()

        # Succès
        return True
    
    # -- Abstract Function -- #

    # Execution du code
    def init(): raise NotImplementedError()
    def exec(): raise NotImplementedError()

    # Events du clavier
    def on_press(self, code: int, new: bool): pass
    def on_release(self, code: int): pass
    def on_shortcut(self, codes: list[int], new: bool): pass

    # Events de la souris
    def on_move(self, x: int, y: int): pass
    def on_click(self, x: int, y: int, button: mouse.Button, pressed: bool): pass
    def on_scroll(self, x: int, y: int, dx: int, dy: int): pass