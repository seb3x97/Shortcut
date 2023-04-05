#---------- Package ----------#

from __future__ import annotations

#---------- Locals ----------#

# Managers
import src.objects.managers.keyboard as keyboard
import src.objects.managers.mouse as mouse

# Modes
import src.objects.modes.mode as mode
import src.objects.enums.mode_type as mode_type

# Class Handler
class Handler():
    # Default Constructor
    def __init__(self) -> None:
        # -- Default -- #
        self.keyboard_manager: keyboard.ManagerKeyboard = keyboard.ManagerKeyboard()        # Manager du clavier
        self.mouse_manager: mouse.ManagerMouse = mouse.ManagerMouse()                       # Manager de la souris
        #
        self.__modes: dict[mode_type.ModeType, mode.Mode] = {}                              # Dictionnaire de tous les modes
        self.mode: mode.Mode = None                                                         # Mode actuel

    # On initialise la classe
    def init(self) -> bool:
        # On enregistre les modes
        self.__modes = {key: item(self) for key, item in mode_type.MODES.items()}

        # On récupére la liste des modes
        for key, item in mode_type.MODES.items():
            # On essaye de charger le mode
            instance: mode.Mode = item(self)
            if not instance.init():
                print(f"Une erreure est survenue l'hors du chargement du mode '{item.__class__.__name__}'")
                break

            # On enregistre le mode
            self.__modes[key] = instance

        # On essaye de lire les données et mettre le mode par défaut
        if not self.set_mode(mode_type.ModeType.NORMAL): return False

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

    # On enregistre le mode (sans le démarrer)
    def set_mode(self, mode_type: mode_type.ModeType, args: tuple = ()) -> bool:
        # On stop l'ancien mode
        if not self.mode is None: self.mode.stop()

        # On essaye d'enregistrer le nouveau mode et de l'initialiser
        self.mode = self.__modes.get(mode_type, None)
        if self.mode is None: return False
        if not self.mode.set_args(*args): return False

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
    
    # On enregistre le mode (en le démarrant)
    def start_mode(self, mode_type: mode_type.ModeType = mode_type.ModeType.NORMAL, args: tuple = ()) -> bool:
        # On essaye d'initialiser le mode
        if not self.set_mode(mode_type, args): return False

        # On essaye de démarrer le mode
        if not self.mode.start(): return False

        # Succès
        return True