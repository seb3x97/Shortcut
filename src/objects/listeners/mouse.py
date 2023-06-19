#---------- Package ----------#

from __future__ import annotations
import pynput.mouse as py_mouse

#---------- Locals ----------#

import src.objects.listeners.listener as Listener

# Class ListenerMouse
class ListenerMouse(Listener.Listener):
    # Default Constructor
    def __init__(self) -> None:
        # Parent
        super().__init__()

        # Events
        self.on_move: function = None                   # Evenement => movement de la souris
        self.on_click: function = None                  # Evenement => Clique de la souris
        self.on_scroll: function = None                 # Evenement => Scroll de la souris

        # Controller
        self.__controller: py_mouse.Controller = py_mouse.Controller()

        # Listener
        self.__listener: py_mouse.Listener = py_mouse.Listener(
            on_move=self.__on_move,
            on_click=self.__on_click,
            on_scroll=self.__on_scroll)


    #---------- Herited ----------#

    # On démarre le listener
    def start(self) -> bool:
        self.__listener.start()

        # Succès
        return True

    # On arrête le listener
    def stop(self) -> bool:
        self.__listener.stop()

        # Succès
        return True
    
    # On join le listener
    def join(self) -> bool:
        self.__listener.join()

        # Succès
        return True


    #---------- Functions ----------#

    # -- Action -- #

    # On bouge la souris (delta)
    def move(self, dx: int, dy: int):
        self.__controller.move(dx=dx, dy=dy)

    # On bouge la souris (position)
    def move_to(self, x: int, y: int):
        self.__controller.position = (x, y)

    # On click avec la souris
    def click(self, button: py_mouse.Button, count: int = 1):
        self.__controller.click(button=button, count=count)

    # On scroll avec la souris
    def scroll(self, dx: int, dy: int):
        self.__controller.scroll(dx=dx, dy=dy)

    # -- Get -- #

    # On récupére la position de la souris
    def get_mouse_pos(self) -> tuple:
        return self.__controller.position


    #---------- Events ----------#

    # Event quand on bouge la souris
    def __on_move(self, x: int, y: int):
        # On trigger l'event move
        if not self.on_move is None: self.on_move(x, y)

    # Event quand on clique avec la souris
    def __on_click(self, x: int, y: int, button: py_mouse.Button, pressed: bool):
        # On trigger l'event click
        if not self.on_click is None: self.on_click(x, y, button, pressed)

    # Event quand on scroll avec la souris
    def __on_scroll(self, x: int, y: int, dx: int, dy: int):
        # On trigger l'event scroll
        if not self.on_scroll is None: self.on_scroll(x, y, dx, dy)