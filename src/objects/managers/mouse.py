#---------- Package ----------#

from pynput import mouse

#---------- Locals ----------#

from src.objects.managers.manager import Manager
from src.objects.listeners.mouse import ListenerMouse

# Class ManagerMouse
class ManagerMouse(Manager):
    # Default Constructor
    def __init__(self):
        # Parent
        super().__init__()

        # -- Default -- #
        self.__enable_events: bool = True               # active/désactive les évenements

        # Events
        self.on_move: function = None                   # Evenement => movement de la souris
        self.on_click: function = None                  # Evenement => Clique de la souris
        self.on_scroll: function = None                 # Evenement => Scroll de la souris

        # Listener + ajout des events
        self.__mouse_listener: ListenerMouse = ListenerMouse()
        self.__mouse_listener.on_move = self.__on_move
        self.__mouse_listener.on_click = self.__on_click
        self.__mouse_listener.on_scroll = self.__on_scroll


    #---------- Herited ----------#

    # On démarre le listener
    def start(self) -> bool:
        return self.__mouse_listener.start()

    # On arrête le listener
    def stop(self) -> bool:
        return self.__mouse_listener.stop()


    #---------- Functions ----------#


    # -- Action -- #

    # On bouge la souris (delta)
    def move(self, dx: int, dy: int):
        self.__enable_events = False
        self.__mouse_listener.move(dx=dx, dy=dy)
        self.__enable_events = True

    # On bouge la souris (position)
    def move_to(self, x: int, y: int):
        self.__enable_events = False
        self.__mouse_listener.move_to(x, y)
        self.__enable_events = True

    # On click avec la souris
    def click(self, button: mouse.Button, count: int = 1):
        self.__enable_events = False
        self.__mouse_listener.click(button=button, count=count)
        self.__enable_events = True

    # On scroll avec la souris
    def scroll(self, dx: int, dy: int):
        self.__enable_events = False
        self.__mouse_listener.scroll(dx=dx, dy=dy)
        self.__enable_events = True


    # -- Get -- #

    # On récupére la position de la souris
    def get_mouse_pos(self) -> tuple:
        return self.__mouse_listener.get_mouse_pos()


    #---------- Events ----------#

    # Event quand on bouge la souris
    def __on_move(self, x: int, y: int):
        # Check si les evenements sont activés
        if not self.__enable_events: return

        # On trigger l'event move
        if not self.on_move is None: self.on_move(x, y)

    # Event quand on clique avec la souris
    def __on_click(self, x: int, y: int, button: mouse.Button, pressed: bool):
        # Check si les evenements sont activés
        if not self.__enable_events: return

        # On trigger l'event click
        if not self.on_click is None: self.on_click(x, y, button, pressed)

    # Event quand on scroll avec la souris
    def __on_scroll(self, x: int, y: int, dx: int, dy: int):
        # Check si les evenements sont activés
        if not self.__enable_events: return

        # On trigger l'event scroll
        if not self.on_scroll is None: self.on_scroll(x, y, dx, dy)