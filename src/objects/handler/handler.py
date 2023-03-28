#---------- Package ----------#

from __future__ import annotations

#---------- Locals ----------#

# Managers
from src.objects.managers.keyboard import ManagerKeyboard
from src.objects.managers.mouse import ManagerMouse

# Command
from src.objects.command.command import Command

# Modes
from src.objects.modes.mode import Mode
from src.objects.enums.mode_type import ModeType, MODES

# Class Handler
class Handler():
    # Default Constructor
    def __init__(self) -> None:
        # -- Default -- #
        self.keyboard_manager: ManagerKeyboard = ManagerKeyboard()          # Manager du clavier
        self.mouse_manager: ManagerMouse = ManagerMouse()                   # Manager de la souris
        #
        self.__modes: dict[ModeType, Mode] = {}                             # Dictionnaire de tous les modes
        self.mode: Mode = None                                              # Mode actuel

    # On initialise la classe
    def init(self) -> bool:
        # On enregistre les modes
        self.__modes = {key: MODES[key](self) for key in MODES}

        # On essaye de lire les données et mettre le mode par défaut
        if not self.set_mode(ModeType.NORMAL): return False

        # Succès
        return True

    # On démarre
    def start(self) -> bool:
        # On essaye de faire démarrer les managers
        if not self.keyboard_manager.start(): return False
        if not self.mouse_manager.start(): return False
        if not self.mode.start(): return False

        # Succès
        return True

    # On arrête
    def stop(self) -> bool:
        self.keyboard_manager.stop()
        self.mouse_manager.stop()
        self.mode.stop()

        # Succès
        return True

    # On enregistre le mode (en le démarrant)
    def start_mode(self, mode_type: ModeType = ModeType.NORMAL, args: tuple = ()) -> bool:
        # On essaye d'initialiser le mode
        if not self.set_mode(mode_type, args): return False

        # On essaye de démarrer le mode
        if not self.mode.start(): return False

        # Succès
        return True

    # On enregistre le mode (sans le démarrer)
    def set_mode(self, mode_type: ModeType, args: tuple = ()) -> bool:
        # On stop l'ancien mode
        if not self.mode is None: self.mode.stop()

        # On essaye d'enregistrer le nouveau mode et de l'initialiser
        self.mode = self.__modes.get(mode_type, None)
        if self.mode is None: return False
        if not self.mode.init(*args): return False

        # Events du clavier
        self.keyboard_manager.on_press = self.mode.on_press
        self.keyboard_manager.on_release = self.mode.on_release
        self.keyboard_manager.on_shortcut = self.mode.on_shortcut

        # Events de la souris
        self.mouse_manager.on_move = self.mode.on_move
        self.mouse_manager.on_click = self.mode.on_click
        self.mouse_manager.on_scroll = self.mode.on_scroll

        # Succès
        return True